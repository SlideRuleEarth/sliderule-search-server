#!/usr/bin/env bash
#
# Stage the publishable content into build/.
#
# No content shaping happens here — generated/ is the source of truth.
# We just copy it verbatim and drop an inlined errors/not-found.json.
#
# Before copying, we validate the artifact contract the client depends
# on: meta.json must exist, be valid JSON, have a corpus_sha256 field,
# and that hash must match the actual bytes of corpus.json. If any of
# that fails, the build aborts so we don't stage (and eventually
# deploy) a corpus/meta pair that would hard-fail at client load time.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

CORPUS_FILE="$ROOT/generated/docsearch/corpus.json"
META_FILE="$ROOT/generated/docsearch/meta.json"

# Wipe any previous build/ before validating. If validation fails, we
# want a clean slate rather than leaving stale bytes from a prior
# successful build — otherwise a distracted operator running
# 'make upload' next could push last-known-good over broken content.
rm -rf "$ROOT/build"

echo "Validating corpus/meta invariant..."
# Run as one python invocation so we get rich error messages + a single
# exit code. On success, writes the declared sha to a tmp file so the
# bash script below can read it for the content-addressed rename.
SHA_FILE="$(mktemp -t build_sha.XXXXXX)"
trap 'rm -f "$SHA_FILE"' EXIT

python3 - "$CORPUS_FILE" "$META_FILE" "$SHA_FILE" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

corpus_path = Path(sys.argv[1])
meta_path   = Path(sys.argv[2])
sha_out     = Path(sys.argv[3])

def fail(msg: str) -> None:
    # Uniform error format — always mention the fix so a sleep-deprived
    # operator at deploy time doesn't have to go spelunking.
    sys.stderr.write(f"❌ {msg}\n")
    sys.stderr.write("   Fix: run 'make rebuild-corpus' to regenerate\n")
    sys.stderr.write("   corpus.json + meta.json atomically, then retry.\n")
    sys.exit(1)

if not corpus_path.exists():
    fail(f"{corpus_path} is missing")
if not meta_path.exists():
    fail(f"{meta_path} is missing — meta.json is now part of the "
         f"build contract, not just a sidecar")

try:
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
except json.JSONDecodeError as e:
    fail(f"{meta_path} is not valid JSON: {e}")

declared = meta.get("corpus_sha256")
if not declared:
    fail(f"{meta_path} has no 'corpus_sha256' field. Older meta.json "
         f"files from before the content-addressed-cache change lack "
         f"this — a rebuild writes it.")

# Stream-hash corpus.json so we don't load ~10 MB into memory.
h = hashlib.sha256()
with open(corpus_path, "rb") as f:
    for block in iter(lambda: f.read(1 << 16), b""):
        h.update(block)
actual = h.hexdigest()

if actual != declared:
    fail(f"corpus_sha256 mismatch:\n"
         f"     meta.json declares {declared}\n"
         f"     corpus.json hashes {actual}\n"
         f"   The two files are out of sync; the skill client would "
         f"   hard-fail on this mismatch at runtime.")

# Pass the sha back to the bash script for the rename step.
sha_out.write_text(declared)
print(f"  OK  corpus_sha256={declared[:12]}... matches corpus.json")
PY

SHA="$(cat "$SHA_FILE")"

echo "Staging generated/ -> build/..."
mkdir -p "$ROOT/build/errors"

# Copy the content tree
cp -R "$ROOT/generated/"* "$ROOT/build/"

# Content-addressed corpus URL: what lives on disk as docsearch/corpus.json
# (one stable path for clean git diffs) gets PUBLISHED as
# docsearch/corpus_<sha>.json (unique path per content). This is what
# makes deploys race-free — the URL embeds the sha, so fetching it
# cannot return mismatched bytes. The client derives this path from
# meta.corpus_sha256 at fetch time.
mv "$ROOT/build/docsearch/corpus.json" "$ROOT/build/docsearch/corpus_${SHA}.json"

# 404 body for CloudFront's custom_error_response
cat > "$ROOT/build/errors/not-found.json" <<'JSON'
{"error": "not yet generated"}
JSON

echo
echo "Build tree:"
find "$ROOT/build" -type f | sed "s|^$ROOT/build/||" | sort | sed 's/^/  /'
