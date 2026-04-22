#!/usr/bin/env bash
#
# Zip a skill directory into a .skill archive with the folder at the zip root.
# Usage: scripts/package_skill.sh <skill-name>
#
# Output goes to tmp_skill_for_export/ (separate from the sources under
# skills/ so the build artifacts don't clutter the same directory the
# authored content lives in). The directory is .gitignored.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="${1:?usage: package_skill.sh <skill-name>}"
SKILL_DIR="$ROOT/skills/$SKILL_NAME"

[[ -d "$SKILL_DIR" ]] || { echo "skill dir not found: $SKILL_DIR"; exit 1; }

OUT_DIR="$ROOT/tmp_skill_for_export"
mkdir -p "$OUT_DIR"
OUT="$OUT_DIR/${SKILL_NAME}.skill"
rm -f "$OUT"

# Still cd into skills/ so the zip's internal layout has the skill folder
# at the archive root (every entry starts with $SKILL_NAME/). The output
# path is absolute, so the archive lands in tmp_skill_for_export/.
( cd "$ROOT/skills" && zip -r "$OUT" "$SKILL_NAME/" \
  --exclude "*.pyc" --exclude "*__pycache__*" --exclude "*.DS_Store" )

echo
echo "Packaged: $OUT"
echo
echo "Contents (every path must start with $SKILL_NAME/):"
unzip -l "$OUT"
