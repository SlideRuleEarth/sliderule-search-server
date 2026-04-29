"""Parse filled-out review markdown files and emit evals/human_review.json.

Reads every .md file in evals/review/, extracts:
  - per-result verdicts (correct / partial / wrong) for both corpora
  - the overall query verdict
  - the cross-corpus routing decision
  - human-truth overrides (urls / sections / pages / notes / corpus)

Records that haven't been touched (every blank still empty) are tagged
`incomplete` and excluded from the aggregate. This lets the user review
incrementally — re-run this script anytime, the JSON updates.

Usage
-----
    python tools/ingest_review.py [--review-dir evals/review]

Output
------
    evals/human_review.json  — JSON object with one entry per filled file
                              + a summary block of counts.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_REVIEW_DIR = REPO_ROOT / "evals" / "review"
DEFAULT_OUTPUT_PATH = REPO_ROOT / "evals" / "human_review.json"
GOLDEN_SET_PATH = REPO_ROOT / "evals" / "golden_set.jsonl"

VALID_VERDICTS = {"correct", "partial", "wrong"}
VALID_ROUTING = {
    "keep", "redirect-to-docsearch", "redirect-to-nsidc", "both-corpora",
}
VALID_OVERALL = VALID_VERDICTS  # same vocabulary


# Regex anchors. The form is just markdown, so we use simple patterns
# tied to the section headers and bullet labels generate_review.py emits.

ROW_HEADER_RE = re.compile(r"^# Row (\d+) review", re.MULTILINE)
QUERY_RE = re.compile(r"^\*\*Query:\*\* `(.+?)`", re.MULTILINE)
LABELED_CORPUS_RE = re.compile(r"^\*\*Labeled corpus:\*\* `(\w+)`", re.MULTILINE)


def _extract_section(content: str, header: str, until_headers: list[str]) -> str:
    """Slice the content between `header` and the next of `until_headers`."""
    start = content.find(header)
    if start < 0:
        return ""
    start += len(header)
    end = len(content)
    for nxt in until_headers:
        idx = content.find(nxt, start)
        if 0 < idx < end:
            end = idx
    return content[start:end]


def _parse_verdicts(block: str) -> dict[str, str]:
    """Pull `r1: correct` style lines from a verdicts block.

    The character class `[ \\t]*` (not `\\s*`) is critical: \\s would also
    match newlines, causing the regex to slurp the next line's "- r2:"
    into r1's value.
    """
    out: dict[str, str] = {}
    for m in re.finditer(r"^- (r\d+):[ \t]*([^\n]*)", block, re.MULTILINE):
        rank_label = m.group(1)
        value = m.group(2).strip().lower()
        if not value:
            continue
        if value not in VALID_VERDICTS:
            # tolerate but flag — the harness can decide what to do
            value = f"INVALID:{value}"
        out[rank_label] = value
    return out


def _parse_truth_field_lines(block: str, field_names: list[str]) -> dict[str, list[str]]:
    """Each `- field: value` line in `block` becomes one entry under `field`.
    Multiple lines with the same field name accumulate into a list.

    Same `[ \\t]*` rule as _parse_verdicts — never let `\\s` consume newlines.
    """
    out: dict[str, list[str]] = {f: [] for f in field_names}
    for line in block.splitlines():
        m = re.match(r"^- (\w+):[ \t]*(.*)$", line)
        if not m:
            continue
        field = m.group(1).strip().lower()
        value = m.group(2).strip()
        if not value or field not in field_names:
            continue
        out[field].append(value)
    return out


def split_url_fragments(urls: list[str]) -> tuple[list[str], list[str]]:
    """Split `url#fragment` into bare URL + the fragment as a section hint.

    Pasted URLs from the docs site often carry anchor fragments
    (e.g. `https://docs.slideruleearth.io/user_guide/icesat2.html#atl06-atl06x`).
    Chunk URLs in the corpus are page-level (no fragments), so a fragment-
    bearing URL would never URL-match anything as written. Strip the
    fragment so the URL matches and surface the fragment as a section
    substring — anchor IDs on the docs site are derived from heading text,
    so they generally substring-match the chunk's `section` field.

    Returns (clean_urls, fragments_as_sections). Both are lists; either
    can be empty.
    """
    clean_urls: list[str] = []
    fragments: list[str] = []
    for u in urls:
        if "#" in u:
            base, _, frag = u.partition("#")
            clean_urls.append(base)
            if frag.strip():
                # Anchor IDs are usually hyphenated (atl06-atl06x). Keep as-is
                # for substring matching on chunk.section.lower().
                fragments.append(frag.strip())
        else:
            clean_urls.append(u)
    return clean_urls, fragments


def parse_pages(values: list[str]) -> list[list[int]]:
    """Accept page values like `25`, `25-30`, `[[25, 30]]`, `25,30` and
    normalize to a list of `[start, end]` ranges."""
    ranges: list[list[int]] = []
    for v in values:
        v = v.strip()
        # Try literal JSON first (e.g. `[[20, 50], [60, 70]]`)
        if v.startswith("[") and v.endswith("]"):
            try:
                parsed = json.loads(v)
                if isinstance(parsed, list):
                    if all(isinstance(x, list) and len(x) == 2 for x in parsed):
                        ranges.extend([[int(a), int(b)] for a, b in parsed])
                        continue
                    if all(isinstance(x, int) for x in parsed):
                        ranges.extend([[x, x] for x in parsed])
                        continue
            except (json.JSONDecodeError, ValueError, TypeError):
                pass
        # `25-30` or `25–30` (en-dash)
        m = re.match(r"^(\d+)\s*[\-–]\s*(\d+)$", v)
        if m:
            ranges.append([int(m.group(1)), int(m.group(2))])
            continue
        # `25, 30, 31`
        if "," in v:
            try:
                pages = [int(x.strip()) for x in v.split(",") if x.strip()]
                ranges.extend([[p, p] for p in pages])
                continue
            except ValueError:
                pass
        # Single integer
        try:
            p = int(v)
            ranges.append([p, p])
            continue
        except ValueError:
            pass
        # Unparseable — preserve as a string note in a side channel
        # by skipping silently here; the file's "notes" field can carry it.
    return ranges


def parse_review_file(path: Path) -> dict | None:
    """Parse one filled review markdown file. Returns None if the file
    isn't a review form at all (no `# Row N:` header)."""
    content = path.read_text()

    row_m = ROW_HEADER_RE.search(content)
    if not row_m:
        return None

    row_index = int(row_m.group(1))
    query_m = QUERY_RE.search(content)
    query = query_m.group(1) if query_m else None
    labeled_corpus_m = LABELED_CORPUS_RE.search(content)
    labeled_corpus = labeled_corpus_m.group(1) if labeled_corpus_m else None

    # Verdicts blocks live under "**docsearch:**" and "**nsidc:**" within
    # the "Per-result verdicts" section. Section headings are level-2
    # (##) in the companion-file -review.md form.
    verdicts_section = _extract_section(
        content, "## Per-result verdicts", ["## Overall verdict"]
    )
    ds_block = _extract_section(verdicts_section, "**docsearch:**", ["**nsidc:**"])
    ns_block = _extract_section(verdicts_section, "**nsidc:**", ["## "])
    docsearch_verdicts = _parse_verdicts(ds_block)
    nsidc_verdicts = _parse_verdicts(ns_block)

    # Overall verdict
    overall_block = _extract_section(
        content, "## Overall verdict", ["## Cross-corpus routing"]
    )
    overall_m = re.search(r"^- overall:[ \t]*([^\n]*)", overall_block, re.MULTILINE)
    overall = (overall_m.group(1).strip().lower() if overall_m else "") or None
    if overall and overall not in VALID_OVERALL:
        overall = f"INVALID:{overall}"

    # Cross-corpus routing
    routing_block = _extract_section(
        content, "## Cross-corpus routing", ["## Human truth"]
    )
    routing_m = re.search(r"^- routing:[ \t]*([^\n]*)", routing_block, re.MULTILINE)
    routing = (routing_m.group(1).strip().lower() if routing_m else "") or None
    if routing and routing not in VALID_ROUTING:
        routing = f"INVALID:{routing}"

    # Human truth — last section in the file, so just read until EOF.
    truth_block = _extract_section(content, "## Human truth", [])
    truth_fields = _parse_truth_field_lines(
        truth_block,
        field_names=["corpus", "url", "section", "pages", "notes"],
    )
    # Split URL fragments off the URLs and fold them into sections.
    # E.g. user pastes `https://docs.../icesat2.html#atl06-atl06x` — we want
    # the bare page URL on `urls` and `atl06-atl06x` appended to `sections`.
    # Anchor names usually map directly to chunk-section substrings (the
    # docs site's TOC anchors are derived from heading text).
    cleaned_urls, fragment_sections = split_url_fragments(truth_fields["url"])
    sections = list(truth_fields["section"]) + fragment_sections

    human_truth = {
        "corpus": truth_fields["corpus"][0] if truth_fields["corpus"] else None,
        "urls": cleaned_urls,
        "sections": sections,
        "pages": parse_pages(truth_fields["pages"]),
        "notes": " ".join(truth_fields["notes"]) if truth_fields["notes"] else None,
    }

    # Empty-record check: did the user actually fill anything in?
    is_empty = (
        not docsearch_verdicts
        and not nsidc_verdicts
        and not overall
        and not routing
        and not any(human_truth[k] for k in ("urls", "sections", "pages", "notes", "corpus"))
    )

    return {
        "row_index": row_index,
        "query": query,
        "labeled_corpus": labeled_corpus,
        "review_file": str(path.relative_to(REPO_ROOT)),
        "incomplete": is_empty,
        "verdicts": {
            "docsearch": docsearch_verdicts,
            "nsidc": nsidc_verdicts,
        },
        "overall_verdict": overall,
        "routing": routing,
        "human_truth": human_truth,
    }


def summarize(records: list[dict]) -> dict:
    """High-level counts to surface in human_review.json — useful for
    quick sanity checks without parsing the per-row entries."""
    completed = [r for r in records if not r["incomplete"]]
    overall_counts: dict[str, int] = {}
    routing_counts: dict[str, int] = {}
    for r in completed:
        overall = r["overall_verdict"] or "(blank)"
        overall_counts[overall] = overall_counts.get(overall, 0) + 1
        routing = r["routing"] or "(blank)"
        routing_counts[routing] = routing_counts.get(routing, 0) + 1
    return {
        "total_files": len(records),
        "completed": len(completed),
        "incomplete": len(records) - len(completed),
        "overall_verdicts": overall_counts,
        "routing_decisions": routing_counts,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--review-dir", default=str(DEFAULT_REVIEW_DIR),
                   help="Directory of filled-out review .md files.")
    p.add_argument("--output", default=str(DEFAULT_OUTPUT_PATH),
                   help="Where to write the aggregated JSON.")
    args = p.parse_args()

    review_dir = Path(args.review_dir)
    if not review_dir.exists():
        print(f"ERROR: {review_dir} does not exist", file=sys.stderr)
        return 2

    # Glob only -review.md (editable form). The companion -results.md
    # files are read-only auto-generated and have no verdicts to parse.
    files = sorted(review_dir.glob("*-review.md"))
    if not files:
        print(f"WARNING: no *-review.md files found in {review_dir}", file=sys.stderr)

    records: list[dict] = []
    for path in files:
        rec = parse_review_file(path)
        if rec is None:
            print(f"  skip {path.name}: doesn't look like a review form",
                  file=sys.stderr)
            continue
        records.append(rec)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "summary": summarize(records),
        "records": records,
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")

    summary = output["summary"]
    print(
        f"ingested {summary['total_files']} review file(s): "
        f"{summary['completed']} completed, {summary['incomplete']} incomplete\n"
        f"wrote {out_path.relative_to(REPO_ROOT)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
