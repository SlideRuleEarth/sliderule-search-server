#!/usr/bin/env bash
#
# Stage the publishable content into build/.
#
# No content shaping happens here — generated/ is the source of truth.
# We just copy it verbatim and drop an inlined errors/not-found.json.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Staging generated/ -> build/..."
rm -rf "$ROOT/build"
mkdir -p "$ROOT/build/errors"

# Copy the content tree
cp -R "$ROOT/generated/"* "$ROOT/build/"

# 404 body for CloudFront's custom_error_response
cat > "$ROOT/build/errors/not-found.json" <<'JSON'
{"error": "not yet generated"}
JSON

echo
echo "Build tree:"
find "$ROOT/build" -type f | sed "s|^$ROOT/build/||" | sort | sed 's/^/  /'
