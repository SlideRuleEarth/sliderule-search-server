#!/usr/bin/env bash
#
# Atomic deploy of a staged build/ tree to S3.
# Usage: scripts/upload.sh <build_dir> <bucket>
#
# Deploy is race-free because corpus URLs are content-addressed:
# /docsearch/corpus_<sha>.json. Each rebuild publishes a new path;
# previous versions stay live until the lifecycle rule reaps them
# (see bucket.tf — tag-based, only touches superseded objects).
#
# Three S3 ops + one tagging op, in strict order:
#
#   1. sync everything EXCEPT versioned corpora + meta.json. This runs
#      with --delete, so stale non-corpus files (errors/, etc.) get
#      cleaned up. Versioned corpora are preserved for in-flight
#      clients that still hold the old meta.
#
#   2. cp the new versioned corpus. Purely additive — no existing
#      path is modified. Cache-control is immutable (1y) because the
#      URL embeds the content hash; the object at that key can't
#      change.
#
#   3. cp the new meta.json. Atomic pointer flip at the edge. After
#      this step, new clients derive the URL for the new corpus,
#      which is already on S3.
#
# Then:
#
#   4. Tag the previously-live corpus as state=stale, which is what
#      the S3 lifecycle rule in terraform/modules/bucket.tf filters
#      on. Only tagged objects can be expired, so the currently-live
#      corpus is always safe from cleanup — even if you don't deploy
#      for a year.

set -euo pipefail

BUILD_DIR="${1:?usage: upload.sh <build_dir> <bucket>}"
BUCKET="${2:?usage: upload.sh <build_dir> <bucket>}"

# Capture the previously-live corpus sha BEFORE step 3 overwrites
# meta.json. On a first deploy there is no previous meta; we treat
# that as "nothing to tag" and move on.
echo "[capture] Fetching previously-live meta.json..."
OLD_SHA="$(
  aws s3 cp "s3://$BUCKET/docsearch/meta.json" - 2>/dev/null \
    | python3 -c "import json,sys; print(json.load(sys.stdin).get('corpus_sha256',''))" \
    2>/dev/null || true
)"
if [[ -n "$OLD_SHA" ]]; then
  echo "  previously-live sha: $OLD_SHA"
else
  echo "  (no previous meta.json — treating as first deploy)"
fi

echo "[1/3] Syncing non-corpus files -> s3://$BUCKET/ (preserving old versioned corpora)"
aws s3 sync "$BUILD_DIR/" "s3://$BUCKET/" \
  --delete \
  --cache-control "max-age=60" \
  --exclude "docsearch/corpus_*.json" \
  --exclude "docsearch/meta.json"

echo "[2/3] Publishing new versioned corpus (additive, immutable cache)"
for f in "$BUILD_DIR"/docsearch/corpus_*.json; do
  aws s3 cp "$f" "s3://$BUCKET/docsearch/$(basename "$f")" \
    --cache-control "max-age=31536000,immutable"
done

echo "[3/3] Flipping meta.json pointer -> s3://$BUCKET/docsearch/meta.json"
aws s3 cp "$BUILD_DIR/docsearch/meta.json" \
  "s3://$BUCKET/docsearch/meta.json" \
  --cache-control "max-age=60"

# Tag the superseded corpus so the S3 lifecycle rule knows it's
# eligible for expiration. Skip when there's no previous deploy or
# we're re-deploying the same sha (idempotency — tagging the current
# corpus stale would be self-defeating).
NEW_SHA="$(
  python3 -c "import json; print(json.load(open('$BUILD_DIR/docsearch/meta.json'))['corpus_sha256'])"
)"
if [[ -n "$OLD_SHA" && "$OLD_SHA" != "$NEW_SHA" ]]; then
  echo "[post] Tagging previously-live corpus_${OLD_SHA:0:12}... as state=stale"
  aws s3api put-object-tagging \
    --bucket "$BUCKET" \
    --key "docsearch/corpus_${OLD_SHA}.json" \
    --tagging 'TagSet=[{Key=state,Value=stale}]'
  echo "  (eligible for S3 lifecycle expiration ~30 days after its upload)"
else
  echo "[post] No previous corpus to tag (first deploy, or same sha as new)"
fi

echo "Done."
