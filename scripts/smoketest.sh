#!/usr/bin/env bash
#
# Smoke test the deployed search distribution.
# Usage: DOMAIN=search.testsliderule.org ./scripts/smoketest.sh

set -uo pipefail

DOMAIN="${DOMAIN:-search.testsliderule.org}"
BASE="https://$DOMAIN"

pass=0
fail=0

check() {
  local name="$1" url="$2" expect_status="$3" expect_ctype="$4"
  local status ctype
  read -r status ctype < <(
    curl -sS -o /dev/null -D - "$url" \
      | awk 'BEGIN{s="";c=""} /^HTTP\//{s=$2} tolower($1)=="content-type:"{c=$2} END{print s" "c}'
  )
  if [[ "$status" == "$expect_status" && "$ctype" == *"$expect_ctype"* ]]; then
    echo "  PASS  $name  ($status $ctype)  $url"
    pass=$((pass+1))
  else
    echo "  FAIL  $name  got='$status $ctype' want='$expect_status *$expect_ctype*'  $url"
    fail=$((fail+1))
  fi
}

echo "Smoke-testing $BASE"

# meta.json is always at the flat path — it's the one mutable thing in
# the tree and the skill client fetches it on every query.
check "docsearch/meta.json"            "$BASE/docsearch/meta.json"            200 "application/json"

# Legacy flat /docsearch/corpus.json must 404: the URL scheme moved to
# content-addressed /docsearch/corpus_<sha>.json. Asserting 404 here
# confirms the old scheme is actually retired, so we don't accidentally
# keep serving both and invite a race back in.
check "legacy flat corpus.json (404)"  "$BASE/docsearch/corpus.json"          404 "application/json"

# A totally unpublished path should 404 with the CORS'd JSON error body.
check "nonexistent/corpus.json (404)"  "$BASE/nonexistent-corpus/corpus.json" 404 "application/json"

# Body sanity check on meta.json (requires jq; non-fatal if missing).
if command -v jq >/dev/null 2>&1; then
  echo
  echo "Body sanity checks:"
  echo "  docsearch/meta.json:"
  curl -sS "$BASE/docsearch/meta.json" \
    | jq -c '{built_at, chunk_count, embedder, pages_crawled, corpus_sha256}' \
    || fail=$((fail+1))
fi

# Artifact-contract check, now against the versioned corpus URL.
# Fetches meta, reads corpus_sha256, verifies that the URL
# /docsearch/corpus_<sha>.json both (a) exists and (b) actually hashes
# to that sha. This catches:
#   - missing versioned upload (pass 2 of the 3-step rollout failed)
#   - S3/CDN serving corrupt content for a given key
#   - meta advertising a sha that's gone (e.g., garbage-collected too
#     early by an overly aggressive S3 lifecycle rule)
# Requires jq + shasum; both ship with macOS and with GitHub Actions.
if command -v jq >/dev/null 2>&1 && command -v shasum >/dev/null 2>&1; then
  echo
  echo "Artifact-contract check (versioned corpus exists + hash matches meta):"
  declared_sha="$(curl -sS "$BASE/docsearch/meta.json" | jq -r '.corpus_sha256')"
  if [[ -z "$declared_sha" || "$declared_sha" == "null" ]]; then
    echo "  FAIL  meta.json has no corpus_sha256 field"
    fail=$((fail+1))
  else
    versioned_url="$BASE/docsearch/corpus_${declared_sha}.json"
    # Verify HTTP status of the versioned URL before wasting time hashing.
    vstatus="$(curl -sS -o /dev/null -w '%{http_code}' "$versioned_url")"
    if [[ "$vstatus" != "200" ]]; then
      echo "  FAIL  versioned corpus URL returned $vstatus"
      echo "        $versioned_url"
      fail=$((fail+1))
    else
      actual_sha="$(curl -sS "$versioned_url" | shasum -a 256 | awk '{print $1}')"
      if [[ "$declared_sha" == "$actual_sha" ]]; then
        echo "  PASS  ${declared_sha:0:12}... matches bytes at $versioned_url"
        pass=$((pass+1))
      else
        echo "  FAIL  hash mismatch at $versioned_url"
        echo "        meta declares: $declared_sha"
        echo "        actual bytes : $actual_sha"
        fail=$((fail+1))
      fi
    fi
  fi
fi

# CORS response must carry Access-Control-Allow-Origin: *.
echo
echo "CORS check:"
acao="$(curl -sS -I -H "Origin: https://example.com" "$BASE/docsearch/meta.json" \
  | awk 'tolower($1)=="access-control-allow-origin:"{print $2}' | tr -d '\r')"
if [[ "$acao" == "*" ]]; then
  echo "  PASS  Access-Control-Allow-Origin: *"
  pass=$((pass+1))
else
  echo "  FAIL  Access-Control-Allow-Origin: '$acao' (expected '*')"
  fail=$((fail+1))
fi

echo
echo "Summary: $pass passed, $fail failed."
exit $(( fail > 0 ? 1 : 0 ))
