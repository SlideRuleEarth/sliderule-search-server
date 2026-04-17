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

check "docsearch/corpus.json"          "$BASE/docsearch/corpus.json"          200 "application/json"
check "docsearch/meta.json"            "$BASE/docsearch/meta.json"            200 "application/json"

# Unpublished corpora should 404 with the JSON error body.
check "nonexistent/corpus.json (404)"  "$BASE/nonexistent-corpus/corpus.json" 404 "application/json"

# Body sanity check on meta.json (requires jq; non-fatal if missing).
if command -v jq >/dev/null 2>&1; then
  echo
  echo "Body sanity checks:"
  echo "  docsearch/meta.json:"
  curl -sS "$BASE/docsearch/meta.json" \
    | jq -c '{built_at, chunk_count, embedder, pages_crawled}' \
    || fail=$((fail+1))
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
