#!/usr/bin/env bash
#
# End-to-end local test of the Lambda container image via the AWS RIE
# (Runtime Interface Emulator) that ships inside public.ecr.aws/lambda/*
# base images. Exercises the exact image a deploy would push — catches
# Dockerfile bugs, pip/arm64 resolution issues, Mangum adapter bugs,
# cold-start init failures, etc. Doesn't exercise CloudFront / OAC /
# x-amz-content-sha256, which only AWS can validate.
#
# Usage:
#   scripts/test_image.sh                 # build + run + test + teardown
#   scripts/test_image.sh --no-build      # reuse existing docsearch:dev
#
# The RIE exposes the Lambda Invoke API at:
#   http://localhost:9000/2015-03-31/functions/function/invocations
# Payload is a Lambda Function URL event (payload format v2), which is
# what the live Lambda will receive from CloudFront. See:
#   https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html

set -euo pipefail

IMAGE_TAG="docsearch:dev"
CONTAINER_NAME="docsearch-rie-test"
RIE_PORT=9000
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

do_build=1
if [[ "${1:-}" == "--no-build" ]]; then
  do_build=0
fi

cd "$REPO_ROOT"

pass=0
fail=0
cleanup() {
  docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
}
trap cleanup EXIT

if (( do_build )); then
  echo "[1/4] Building image ($IMAGE_TAG) for linux/arm64..."
  docker buildx build \
    --load \
    --platform linux/arm64 \
    -f server/Dockerfile \
    -t "$IMAGE_TAG" \
    .
else
  echo "[1/4] Skipping build (--no-build); assuming $IMAGE_TAG already exists."
fi

echo
echo "[2/4] Starting container (Lambda RIE on :$RIE_PORT)..."
docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
docker run -d --name "$CONTAINER_NAME" -p "$RIE_PORT:8080" "$IMAGE_TAG" >/dev/null

# Wait for RIE + cold-start init. Loading the sentence-transformer +
# reading corpus + building the matrix takes ~4–6s; poll /ping endpoint
# the RIE exposes, with a generous overall budget.
echo -n "       waiting for RIE ready"
ready=0
for i in $(seq 1 60); do
  if curl -sS -o /dev/null -w '%{http_code}' \
       "http://localhost:$RIE_PORT/2015-03-31/functions/function/invocations" \
       -d '{}' 2>/dev/null | grep -q '^2'; then
    ready=1
    echo "  ready after ${i}s"
    break
  fi
  echo -n "."
  sleep 1
done
if (( ! ready )); then
  echo
  echo "  RIE did not become ready in 60s. Container logs:"
  docker logs "$CONTAINER_NAME" | tail -40
  exit 1
fi

# Helper: POST a Lambda Function URL v2 event to the RIE, return the
# deserialized response body to stdout. All fields come from how
# CloudFront will actually frame the request (path, method, headers,
# stringified body, isBase64Encoded=false).
invoke() {
  local path="$1" method="$2" body="$3"
  local event
  # shellcheck disable=SC2016
  event="$(python3 -c '
import json, sys
path, method, body = sys.argv[1], sys.argv[2], sys.argv[3]
print(json.dumps({
  "version": "2.0",
  "routeKey": f"{method} {path}",
  "rawPath": path,
  "rawQueryString": "",
  "headers": {
    "content-type": "application/json",
    "host": "localhost",
  },
  "requestContext": {
    "http": {"method": method, "path": path, "sourceIp": "127.0.0.1"},
    "stage": "$default",
  },
  "body": body,
  "isBase64Encoded": False,
}))
' "$path" "$method" "$body")"
  curl -sS -XPOST "http://localhost:$RIE_PORT/2015-03-31/functions/function/invocations" \
    -H "Content-Type: application/json" \
    -d "$event"
}

check_json_status() {
  local name="$1" got="$2" want="$3"
  if [[ "$got" == "$want" ]]; then
    echo "  PASS  $name  ($got)"
    pass=$((pass+1))
  else
    echo "  FAIL  $name  got=$got want=$want"
    fail=$((fail+1))
  fi
}

echo
echo "[3/4] Exercising the container..."

# GET /healthz
resp="$(invoke /healthz GET '')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "GET /healthz" "$status" "200"

# GET /docsearch/meta
resp="$(invoke /docsearch/meta GET '')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "GET /docsearch/meta" "$status" "200"
if command -v jq >/dev/null 2>&1; then
  echo "  /docsearch/meta body:"
  echo "$resp" \
    | python3 -c 'import json,sys; print(json.load(sys.stdin)["body"])' \
    | jq -c '{corpus_sha256, chunk_count, embedder, built_at}' \
    | sed 's/^/    /'
fi

# POST /docsearch/search (happy path)
body='{"query":"how do I use atl03x","top_k":3}'
resp="$(invoke /docsearch/search POST "$body")"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "POST /docsearch/search (happy)" "$status" "200"
if [[ "$status" == "200" ]] && command -v jq >/dev/null 2>&1; then
  n_results="$(echo "$resp" \
    | python3 -c 'import json,sys; print(json.load(sys.stdin)["body"])' \
    | jq '.results | length')"
  echo "    info  results=$n_results"
fi

# POST /docsearch/search (missing query -> 422)
resp="$(invoke /docsearch/search POST '{"top_k":3}')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "POST /docsearch/search (missing query)" "$status" "422"

# POST /docsearch/search (top_k=0 -> 422)
resp="$(invoke /docsearch/search POST '{"query":"x","top_k":0}')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "POST /docsearch/search (top_k=0)" "$status" "422"

# POST /docsearch/search (categories=[])
# categories=[] must return an empty results array (explicit "zero
# categories match" semantic — distinct from categories=null which means
# "no filter"). Assertion uses python3 rather than jq so it runs
# unconditionally; otherwise on a machine without jq the test would
# false-pass on any 200, regardless of how many results came back.
resp="$(invoke /docsearch/search POST '{"query":"atl03x","top_k":3,"categories":[]}')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "POST /docsearch/search (categories=[])" "$status" "200"
if [[ "$status" == "200" ]]; then
  n_results="$(
    echo "$resp" \
      | python3 -c '
import json, sys
outer = json.load(sys.stdin)
inner = json.loads(outer["body"])
print(len(inner.get("results", [])))
'
  )"
  if [[ "$n_results" == "0" ]]; then
    echo "    PASS  categories=[] -> 0 results"
    pass=$((pass+1))
  else
    echo "    FAIL  categories=[] -> $n_results results (expected 0)"
    fail=$((fail+1))
  fi
fi

# Catch-all 404
resp="$(invoke /nope GET '')"
status="$(echo "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["statusCode"])')"
check_json_status "GET /nope (catch-all)" "$status" "404"

# EventBridge scheduled warmup event — exercises server/handler.py's
# branch that short-circuits before Mangum. In production this is
# driven by the rule defined in terraform/modules/warmer.tf; here we
# synthesize the canonical envelope AWS emits for rate(5 minutes).
# The handler returns {"warmup":"ok","corpora":[...]} directly (no
# Lambda-proxy-response shape), so we key assertions off the raw
# top-level "warmup" and "corpora" fields rather than statusCode.
echo
echo "  EventBridge warmup event (scheduled-invoke path):"
warmup_event='{"version":"0","id":"abcd-1234","detail-type":"Scheduled Event","source":"aws.events","account":"0","time":"2026-04-21T20:00:00Z","region":"us-east-1","resources":["arn:aws:events:us-east-1:0:rule/test"],"detail":{}}'
resp="$(curl -sS -XPOST "http://localhost:$RIE_PORT/2015-03-31/functions/function/invocations" \
  -H "Content-Type: application/json" \
  -d "$warmup_event")"
warmup_status="$(echo "$resp" | python3 -c '
import json, sys
try:
  print(json.load(sys.stdin).get("warmup", "<missing>"))
except Exception as e:
  print(f"<parse-error: {e}>")
')"
if [[ "$warmup_status" == "ok" ]]; then
  corpora_list="$(echo "$resp" | python3 -c '
import json, sys
print(",".join(json.load(sys.stdin).get("corpora", [])))
')"
  echo "    PASS  warmup returned ok; corpora=[$corpora_list]"
  pass=$((pass+1))
else
  echo "    FAIL  warmup event did not short-circuit"
  echo "          response: $(echo "$resp" | head -c 200)"
  fail=$((fail+1))
fi

echo
echo "[4/4] Container logs (tail):"
docker logs "$CONTAINER_NAME" 2>&1 | tail -10 | sed 's/^/    /'

echo
echo "Summary: $pass passed, $fail failed."
exit $(( fail > 0 ? 1 : 0 ))
