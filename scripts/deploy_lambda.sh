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
#
# Requires generated/docsearch/corpus.json + generated/nsidc/corpus.json
# to be present (image bakes both in). `make rebuild-corpus-docsearch`
# and `make rebuild-corpus-nsidc` refresh them.

set -euo pipefail

DOMAIN="${1:?usage: deploy_lambda.sh <domain>  (e.g. search.testsliderule.org)}"
AWS_REGION="${AWS_REGION:-us-east-1}"
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
  echo "[3/3] Updating Lambda $LAMBDA_NAME -> $ECR_URI:$TAG"
  aws lambda update-function-code \
    --function-name "$LAMBDA_NAME" \
    --image-uri "$ECR_URI:$TAG" \
    --region "$AWS_REGION" >/dev/null
  aws lambda wait function-updated \
    --function-name "$LAMBDA_NAME" \
    --region "$AWS_REGION"
  echo "  Lambda is live."
else
  echo "[3/3] Lambda $LAMBDA_NAME does not exist yet."
  echo "      Run 'make terraform-apply …' next to create it from :latest."
fi

echo "Done."
