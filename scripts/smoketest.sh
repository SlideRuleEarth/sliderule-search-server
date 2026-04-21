#!/usr/bin/env bash
#
# Smoke-test the deployed sliderule-search-server distribution.
# Usage: DOMAIN=search.testsliderule.org ./scripts/smoketest.sh
#
# Exercises both corpora and the domain-wide plumbing:
#   GET     /healthz                     liveness + enumerates corpora
#   GET     /docsearch/meta              static corpus metadata (per-corpus)
#   GET     /nsidc/meta
#   OPTIONS /docsearch/search            CORS preflight (domain-wide concern,
#                                        tested once against docsearch)
#   POST    /docsearch/search            happy-path + validation failures
#   POST    /nsidc/search                happy-path + sha consistency
#   consistency: corpus_sha256 in POST response matches GET /meta (per-corpus)
#
# Every POST must include `x-amz-content-sha256: <body-hash>`. CloudFront
# SigV4-signs origin requests using OAC and doesn't buffer the body to
# hash it itself — it copies whatever the viewer sent. Without this header
# Lambda URL returns 403. See scripts/smoketest.sh notes below and
# skills/sliderule-docsearch/scripts/search.py.

set -uo pipefail

DOMAIN="${DOMAIN:-search.testsliderule.org}"
BASE="https://$DOMAIN"

pass=0
fail=0

# Trap-managed tmpfiles — initialize empty up front so the EXIT trap
# never sees an unbound variable even if the script exits before
# assignment. Without this, `set -u` turns a smoketest failure into
# an error from the trap itself that masks the underlying cause.
preflight_headers=""
tmpfile=""
trap 'rm -f "$preflight_headers" "$tmpfile"' EXIT

status_of() { curl -sS -o /dev/null -w '%{http_code}' "$@"; }

check_status() {
  local name="$1"; shift
  local want="$1"; shift
  local got
  got="$(status_of "$@")"
  if [[ "$got" == "$want" ]]; then
    echo "  PASS  $name  ($got)"
    pass=$((pass+1))
  else
    echo "  FAIL  $name  got=$got want=$want"
    fail=$((fail+1))
  fi
}

# sha256 helper; GNU coreutils has sha256sum, macOS has shasum -a 256.
# Both output "<hex>  <name>"; we want just the hex.
sha256_hex() {
  if command -v sha256sum >/dev/null 2>&1; then
    printf '%s' "$1" | sha256sum | awk '{print $1}'
  else
    printf '%s' "$1" | shasum -a 256 | awk '{print $1}'
  fi
}

# POST helper that attaches the required x-amz-content-sha256 header
# with the body's hash. Writes the response body to the caller's file
# and echoes the status code to stdout.
#
# Args: 1=body-json-string  2=out-file-path  [extra curl args ...]
signed_post() {
  local body="$1"; shift
  local out_file="$1"; shift
  local body_sha
  body_sha="$(sha256_hex "$body")"
  curl -sS -o "$out_file" -w '%{http_code}' \
    -H "Content-Type: application/json" \
    -H "x-amz-content-sha256: $body_sha" \
    -d "$body" \
    "$@"
}

echo "Smoke-testing $BASE"
echo

# --- Liveness --------------------------------------------------------------
check_status "GET /healthz" 200 "$BASE/healthz"

# --- Static corpus metadata ------------------------------------------------
check_status "GET /docsearch/meta" 200 "$BASE/docsearch/meta"

if command -v jq >/dev/null 2>&1; then
  echo
  echo "  /docsearch/meta body:"
  curl -sS "$BASE/docsearch/meta" \
    | jq -c '{corpus_sha256, chunk_count, embedder, embedding_dim, built_at}' \
    | sed 's/^/    /' \
    || fail=$((fail+1))
fi

# --- CORS preflight --------------------------------------------------------
# Preflight MUST return 2xx for real browsers to send the follow-up POST,
# and MUST include POST in Access-Control-Allow-Methods. CloudFront's CORS
# response headers policy adds ACAM unconditionally (even to 4xx from the
# origin), so a header-only check would miss the status problem. Check
# status *first*.
echo
echo "  OPTIONS /docsearch/search (preflight):"
preflight_headers="$(mktemp)"

preflight_status="$(
  curl -sS -o /dev/null -D "$preflight_headers" -w '%{http_code}' \
    -X OPTIONS \
    -H "Origin: https://example.com" \
    -H "Access-Control-Request-Method: POST" \
    -H "Access-Control-Request-Headers: content-type" \
    "$BASE/docsearch/search"
)"

if [[ "$preflight_status" =~ ^2[0-9][0-9]$ ]]; then
  echo "    PASS  preflight status=$preflight_status"
  pass=$((pass+1))
else
  echo "    FAIL  preflight status=$preflight_status (real browsers will reject the preflight)"
  fail=$((fail+1))
fi

allow_methods="$(
  awk 'BEGIN{IGNORECASE=1} /^access-control-allow-methods:/{sub(/^[^:]*:[ ]*/,""); print}' \
    "$preflight_headers" | tr -d '\r'
)"
if [[ "$allow_methods" == *POST* ]]; then
  echo "    PASS  Allow-Methods includes POST: '$allow_methods'"
  pass=$((pass+1))
else
  echo "    FAIL  Allow-Methods missing POST: '$allow_methods'"
  fail=$((fail+1))
fi

acao="$(
  awk 'BEGIN{IGNORECASE=1} /^access-control-allow-origin:/{sub(/^[^:]*:[ ]*/,""); print}' \
    "$preflight_headers" | tr -d '\r'
)"
if [[ "$acao" == "*" ]]; then
  echo "    PASS  Allow-Origin: *"
  pass=$((pass+1))
else
  echo "    FAIL  Allow-Origin: '$acao' (expected '*')"
  fail=$((fail+1))
fi

# --- Happy-path POST -------------------------------------------------------
echo
echo "  POST /docsearch/search (happy path):"
tmpfile="$(mktemp)"
status="$(signed_post '{"query":"how do I use atl03x","top_k":3}' "$tmpfile" "$BASE/docsearch/search")"
if [[ "$status" == "200" ]]; then
  echo "    PASS  POST returned 200"
  pass=$((pass+1))
  if command -v jq >/dev/null 2>&1; then
    keys="$(jq -c 'keys' "$tmpfile")"
    result_count="$(jq '.results | length' "$tmpfile")"
    if [[ "$keys" == '["corpus_meta","query","results"]' ]]; then
      echo "    PASS  response keys: $keys"
      pass=$((pass+1))
    else
      echo "    FAIL  unexpected response keys: $keys"
      fail=$((fail+1))
    fi
    echo "    info  results: $result_count"
  fi
else
  echo "    FAIL  POST returned $status"
  echo "          body: $(head -c 500 "$tmpfile")"
  fail=$((fail+1))
fi

# --- Validation failures ---------------------------------------------------
# Body bytes still need a matching x-amz-content-sha256 or the request
# will 403 before FastAPI ever sees it. We're testing 422, not 403.
echo
missing_body='{"top_k":3}'
missing_sha="$(sha256_hex "$missing_body")"
check_status "POST /docsearch/search (missing query) -> 422" 422 \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-amz-content-sha256: $missing_sha" \
  -d "$missing_body" \
  "$BASE/docsearch/search"

zero_body='{"query":"x","top_k":0}'
zero_sha="$(sha256_hex "$zero_body")"
check_status "POST /docsearch/search (top_k=0) -> 422" 422 \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-amz-content-sha256: $zero_sha" \
  -d "$zero_body" \
  "$BASE/docsearch/search"

# --- Consistency: corpus_sha256 matches /meta and POST response -----------
#
# Run per-corpus: both /docsearch and /nsidc must have a meta endpoint
# returning 200 JSON, a search endpoint that serves a happy-path POST,
# and `corpus_meta.corpus_sha256` in the POST response must equal what
# /<corpus>/meta advertises. Catches both "new corpus wasn't wired up"
# and "meta/corpus got out of sync at build time."
check_corpus_consistency() {
  local corpus="$1"
  local sample_query="$2"

  echo
  echo "  === corpus: $corpus ==="

  check_status "GET /$corpus/meta" 200 "$BASE/$corpus/meta"

  if ! command -v jq >/dev/null 2>&1; then
    return
  fi

  local body sha meta_sha post_sha
  body="{\"query\":\"${sample_query}\",\"top_k\":1}"
  sha="$(sha256_hex "$body")"

  meta_sha="$(curl -sS "$BASE/$corpus/meta" | jq -r '.corpus_sha256')"
  post_sha="$(
    curl -sS \
      -H "Content-Type: application/json" \
      -H "x-amz-content-sha256: $sha" \
      -d "$body" \
      "$BASE/$corpus/search" \
      | jq -r '.corpus_meta.corpus_sha256'
  )"

  if [[ -n "$meta_sha" && "$meta_sha" == "$post_sha" ]]; then
    echo "    PASS  sha matches: ${meta_sha:0:12}..."
    pass=$((pass+1))
  else
    echo "    FAIL  sha mismatch: /meta=$meta_sha  POST=$post_sha"
    fail=$((fail+1))
  fi
}

check_corpus_consistency docsearch "ok"
check_corpus_consistency nsidc     "icesat2"

# --- healthz reports both corpora ------------------------------------------
if command -v jq >/dev/null 2>&1; then
  echo
  echo "  healthz /corpora block:"
  corpora_keys="$(curl -sS "$BASE/healthz" | jq -c '.corpora | keys')"
  if [[ "$corpora_keys" == '["docsearch","nsidc"]' ]]; then
    echo "    PASS  /healthz reports both corpora: $corpora_keys"
    pass=$((pass+1))
  else
    echo "    FAIL  /healthz corpora unexpected: $corpora_keys"
    fail=$((fail+1))
  fi
fi

echo
echo "Summary: $pass passed, $fail failed."
exit $(( fail > 0 ? 1 : 0 ))
