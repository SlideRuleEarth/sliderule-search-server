#!/usr/bin/env bash
#
# Build + push the docsearch Lambda container image, then (if the
# function already exists) update its image_uri in place.
#
# Usage: scripts/deploy_lambda.sh <domain>
#   e.g. scripts/deploy_lambda.sh search.testsliderule.org
#
# Deploy pipeline, in order:
#
#   1. ECR login (requires aws CLI credentials).
#   2. docker buildx build --platform linux/arm64 --push
#      Image is tagged BOTH as :latest (terraform references this for
#      the initial Lambda create) AND :corpus-<sha>-code-<sha> (an
#      immutable audit tag pinned to the actual corpus + code).
#   3. aws lambda update-function-code → aws lambda wait function-updated.
#      Skipped on first deploy when the Lambda doesn't exist yet —
#      terraform-apply creates it using :latest right after.
#   4. Direct `aws lambda invoke` with a warmup payload. Forces cold-
#      start of the new image RIGHT NOW (paid from the CLI invocation,
#      not from a user's real query). Best-effort; failures don't fail
#      the deploy. See comment block at the invoke call.
#
# Requires generated/docsearch/corpus.json + generated/nsidc/corpus.json
# to be present (image bakes both in). `make rebuild-corpus-docsearch`
# and `make rebuild-corpus-nsidc` refresh them.

set -euo pipefail

DOMAIN="${1:?usage: deploy_lambda.sh <domain>  (e.g. search.testsliderule.org)}"
# Hardcoded: CloudFront is a global service pinned to us-east-1 for our
# domains, and ECR + Lambda are co-located there by design. Respecting
# a shell-exported AWS_REGION would let unrelated daily AWS work (say
# `export AWS_REGION=us-west-2` for a different project) accidentally
# point this deploy at the wrong region, producing confusing
# ResourceNotFoundException errors. If we ever multi-region this
# service, promote back to a CLI arg.
AWS_REGION="us-east-1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Sanitize domain for AWS resource names (lambda/ecr disallow dots).
# Mirrors `local.name_suffix = replace(var.domainName, ".", "-")` in
# terraform/modules/lambda.tf — the two must stay in sync.
NAME_SUFFIX="${DOMAIN//./-}"

cd "$REPO_ROOT"

test -f generated/docsearch/corpus.json || {
  echo "❌ generated/docsearch/corpus.json is missing."
  echo "   Run 'make rebuild-corpus-docsearch' first."
  exit 1
}
test -f generated/docsearch/meta.json || {
  echo "❌ generated/docsearch/meta.json is missing."
  echo "   Run 'make rebuild-corpus-docsearch' first."
  exit 1
}

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
ECR_HOST="$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
ECR_REPO="docsearch-$NAME_SUFFIX"
ECR_URI="$ECR_HOST/$ECR_REPO"
LAMBDA_NAME="docsearch-$NAME_SUFFIX"

# Pre-flight: ECR repo must exist before we try to push. If this is the
# first-ever deploy, the user needs to run `make terraform-apply-ecr`
# first — emit a clear message instead of a misleading docker push error.
if ! aws ecr describe-repositories \
     --repository-names "$ECR_REPO" \
     --region "$AWS_REGION" >/dev/null 2>&1; then
  echo "❌ ECR repo '$ECR_REPO' does not exist yet."
  echo "   For a first-time deploy, run in order:"
  echo "     make terraform-apply-ecr DOMAIN=$DOMAIN DOMAIN_APEX=..."
  echo "     make deploy-lambda        DOMAIN=$DOMAIN DOMAIN_APEX=..."
  echo "     make terraform-apply      DOMAIN=$DOMAIN DOMAIN_APEX=..."
  exit 1
fi

# Auditability: warn if building from a dirty tree — the code-sha tag
# won't correspond to any committed state.
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
  echo "⚠️  Uncommitted changes in working tree; image will be tagged with"
  echo "   the HEAD sha but contain uncommitted bytes. Commit first for"
  echo "   a reproducible image."
fi

GIT_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
CORPUS_SHA="$(
  python3 -c "import hashlib; print(hashlib.sha256(open('generated/docsearch/corpus.json','rb').read()).hexdigest()[:12])"
)"
TAG="corpus-${CORPUS_SHA}-code-${GIT_SHA}"

echo "[1/3] Logging in to ECR ($ECR_HOST)..."
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login --username AWS --password-stdin "$ECR_HOST"

echo "[2/3] Building + pushing image (tags: $TAG, latest) for linux/arm64..."
docker buildx build \
  --platform linux/arm64 \
  -f server/Dockerfile \
  -t "$ECR_URI:$TAG" \
  -t "$ECR_URI:latest" \
  --push \
  .

if aws lambda get-function \
     --function-name "$LAMBDA_NAME" \
     --region "$AWS_REGION" >/dev/null 2>&1; then
  echo "[3/4] Updating Lambda $LAMBDA_NAME -> $ECR_URI:$TAG"
  aws lambda update-function-code \
    --function-name "$LAMBDA_NAME" \
    --image-uri "$ECR_URI:$TAG" \
    --region "$AWS_REGION" >/dev/null
  aws lambda wait function-updated \
    --function-name "$LAMBDA_NAME" \
    --region "$AWS_REGION"
  echo "  Lambda is live."

  # Post-update warmup. `update-function-code` replaces the image but
  # doesn't boot a container; the next invocation pays the full
  # cold-start cost (image pull + handler init, ~15s total). If that
  # next invocation happens to be a real user query through CloudFront,
  # CloudFront's 30s origin_read_timeout returns 503 to the viewer
  # before the container finishes coming up. The EventBridge warmer
  # (see terraform/modules/warmer.tf) closes this window eventually,
  # but its first tick isn't for ~5 minutes.
  #
  # Fix by paying the cold-start ourselves, right here, via a direct
  # `aws lambda invoke`. That path bypasses CloudFront entirely — only
  # the Lambda's own 30s timeout applies, which comfortably covers our
  # cold-start budget. Payload is the same EventBridge envelope shape
  # our handler.py recognizes, so the invocation is cheap (short-
  # circuits before Mangum, returns the warmup acknowledgment).
  #
  # Best-effort: a failed warmup doesn't fail the deploy, because the
  # scheduled rule will close the window within 5 minutes either way.
  # Prints a warning instead.
  echo "[4/4] Warming the new container (direct lambda invoke; bypasses CloudFront)..."
  WARMUP_PAYLOAD_FILE="$(mktemp -t docsearch_warmup_payload.XXXXXX)"
  WARMUP_OUTPUT_FILE="$(mktemp -t docsearch_warmup_output.XXXXXX)"
  trap 'rm -f "$WARMUP_PAYLOAD_FILE" "$WARMUP_OUTPUT_FILE"' EXIT
  cat >"$WARMUP_PAYLOAD_FILE" <<'WARMUP_JSON'
{"source":"aws.events","detail-type":"Scheduled Event","detail":{"origin":"deploy_lambda.sh post-update warmup"}}
WARMUP_JSON

  warmup_t0="$(date +%s)"
  if aws lambda invoke \
       --function-name "$LAMBDA_NAME" \
       --payload "fileb://$WARMUP_PAYLOAD_FILE" \
       --region "$AWS_REGION" \
       "$WARMUP_OUTPUT_FILE" >/dev/null 2>&1; then
    warmup_elapsed=$(( $(date +%s) - warmup_t0 ))
    # Parse the response as JSON rather than grepping; AWS's Lambda
    # serializer adds whitespace around `:` and `,` that a tight
    # regex would miss (false-negative cosmetic bug in an earlier
    # draft).
    if python3 -c "
import json, sys
d = json.load(open('$WARMUP_OUTPUT_FILE'))
sys.exit(0 if d.get('warmup') == 'ok' else 1)
" 2>/dev/null; then
      echo "  Warmup OK (${warmup_elapsed}s): $(cat "$WARMUP_OUTPUT_FILE")"
    else
      echo "  ⚠️  Unexpected warmup response (${warmup_elapsed}s):"
      echo "      $(cat "$WARMUP_OUTPUT_FILE")"
      echo "      Next real request may cold-start; EventBridge warmer will close the gap."
    fi
  else
    echo "  ⚠️  Warmup invocation failed; next real request may cold-start."
    echo "      EventBridge warmer (rate(5 minutes)) will close the gap."
  fi
else
  echo "[3/4] Lambda $LAMBDA_NAME does not exist yet."
  echo "      Run 'make terraform-apply …' next to create it from :latest."
fi

echo "Done."
