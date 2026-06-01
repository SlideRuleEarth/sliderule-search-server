"""Parse filled-out review markdown files and emit evals/human_review.json.

Reads every .md file in evals/review/, extracts:
  - per-result verdicts (correct / partial / wrong) for both corpora
  - the overall query verdict
  - the cross-corpus routing decision
  - human-truth overrides (urls / sections / pages / notes / corpus)

Records that haven't been touched (every blank still empty) are tagged
`incomplete` and excluded from the aggregate. This lets the user review
incrementally — re-run this script anytime, the JSON updates.

Each record also carries a `panel_status` from the staleness guard:
`current` (verdicts scored against the panel still in the corpus),
`stale` (corpus rechunked since scoring — the rank-keyed verdicts would
now attach to chunks the reviewer never saw), or `unverifiable` (a
pre-guard form with no panel signature). Only `current` records are
`usable`; the eval harness grades the human metric over those alone.

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
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

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
# Panel signature stamped into both companion files by generate_review.py.
# The one in -review.md is frozen at authoring time; the one in -results.md
# tracks the current corpus. A mismatch means the panel was rechunked since
# the verdicts were scored. Pre-guard forms have no signature line.
PANEL_SIG_RE = re.compile(r"^\*\*Panel signature:\*\* `([0-9a-f]+)`", re.MULTILINE)


def parse_panel_sig(text: str) -> str | None:
    """Pull the `**Panel signature:** \`<hex>\`` value, or None if absent
    (e.g. a review form generated before the staleness guard existed)."""
    m = PANEL_SIG_RE.search(text)
    return m.group(1) if m else None


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


RESULTS_CORPUS_HEADER_RE = re.compile(
    r"^## .*(docsearch|nsidc).*results.*$", re.MULTILINE | re.IGNORECASE
)
RESULTS_RANK_RE = re.compile(r"^#### r(\d+)", re.MULTILINE)
RESULTS_URL_RE = re.compile(r"^- \*\*url:\*\*\s+(.+)$", re.MULTILINE)
RESULTS_SECTION_RE = re.compile(r"^- \*\*section:\*\*\s+(.+)$", re.MULTILINE)
# Match the fenced code block right after `**Full text:**`. Non-greedy on
# the body so we stop at the first closing fence.
RESULTS_FULLTEXT_RE = re.compile(
    r"\*\*Full text:\*\*\s*\n+```\n(.*?)\n```",
    re.DOTALL,
)


def _content_sig(text: str) -> str:
    """First 12 hex chars of sha1(text). Long sections sometimes split
    into multiple chunks that share path + section; the text content is
    what makes them distinct. 12 hex chars = 48 bits, more than enough
    for our corpus of <2K chunks per index."""
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def chunk_key(url: str, section: str, text: str) -> str:
    """Stable per-chunk identifier: path + section + content signature.

    Path-only URL (host-stripped) so a verdict keyed off slideruleearth.io
    chunks transfers to a testsliderule.org rebuild. The content
    signature disambiguates multiple chunks that inherit the same
    (path, section) — common when CHUNK_CHAR_CAP splits a long section
    into 2+ pieces."""
    path = urlparse(url).path
    return f"{path}||{section.strip()}||{_content_sig(text)}"


def parse_results_chunks(results_path: Path) -> dict[str, dict[int, str]]:
    """Parse the companion -results.md file and return a per-corpus map
    `{corpus: {rank: chunk_key}}` for ranks 1..5.

    Used by the ingest to translate rank-keyed verdicts into chunk-keyed
    verdicts, so that reranking levers can be evaluated against the
    same chunk-level human judgments without re-reviewing."""
    if not results_path.exists():
        return {}
    text = results_path.read_text()
    out: dict[str, dict[int, str]] = {}

    parts = RESULTS_CORPUS_HEADER_RE.split(text)
    # parts: [pre, 'docsearch', body, 'nsidc', body]
    for i in range(1, len(parts), 2):
        corpus = parts[i].lower()
        body = parts[i + 1]
        chunks: dict[int, str] = {}
        # Each chunk block starts with #### r<N>
        for blk in re.split(r"(?=^#### r\d+)", body, flags=re.MULTILINE):
            rm = RESULTS_RANK_RE.match(blk)
            if not rm:
                continue
            rank = int(rm.group(1))
            url_m = RESULTS_URL_RE.search(blk)
            sec_m = RESULTS_SECTION_RE.search(blk)
            text_m = RESULTS_FULLTEXT_RE.search(blk)
            if url_m and sec_m and text_m:
                chunks[rank] = chunk_key(
                    url_m.group(1).strip(),
                    sec_m.group(1),
                    text_m.group(1),
                )
        out[corpus] = chunks
    return out


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

    # Translate rank-keyed verdicts to chunk-keyed verdicts so the
    # `--metric=human` mode survives reranking levers. Reads the matching
    # *-results.md and pairs each rank's chunk identity with the verdict
    # the user wrote at that rank.
    results_path = path.parent / path.name.replace("-review.md", "-results.md")
    chunk_ids = parse_results_chunks(results_path)

    # Staleness guard: compare the panel signature frozen in this form
    # (the panel the verdicts were scored against) to the one in the
    # freshly-regenerated -results.md (the current corpus). Reranking is
    # safe — same chunks, reordered — but a rechunk shifts chunk identities,
    # so the rank-keyed verdicts above would be re-pasted onto chunks the
    # reviewer never saw. Three states:
    #   current      — signatures match; verdicts apply to the live panel
    #   stale        — signatures differ; corpus rechunked since scoring
    #   unverifiable — no signature in the form (pre-guard) or no -results.md
    review_sig = parse_panel_sig(content)
    results_sig = (
        parse_panel_sig(results_path.read_text()) if results_path.exists() else None
    )
    if review_sig is None or results_sig is None:
        panel_status = "unverifiable"
    elif review_sig == results_sig:
        panel_status = "current"
    else:
        panel_status = "stale"
    verdicts_by_chunk: dict[str, dict[str, str]] = {"docsearch": {}, "nsidc": {}}
    for corpus, rank_verdicts in (
        ("docsearch", docsearch_verdicts),
        ("nsidc", nsidc_verdicts),
    ):
        rank_to_key = chunk_ids.get(corpus, {})
        for rank_label, verdict in rank_verdicts.items():
            try:
                rank = int(rank_label[1:])  # 'r1' -> 1
            except ValueError:
                continue
            key = rank_to_key.get(rank)
            if key:
                verdicts_by_chunk[corpus][key] = verdict

    # A record is usable by the human metric only if it's both filled in
    # AND scored against the panel that's still in the corpus. The eval
    # harness keys off this so stale/unverifiable verdicts never silently
    # inflate or deflate the metric.
    usable = (not is_empty) and panel_status == "current"

    return {
        "row_index": row_index,
        "query": query,
        "labeled_corpus": labeled_corpus,
        "review_file": str(path.relative_to(REPO_ROOT)),
        "incomplete": is_empty,
        "panel_status": panel_status,
        "panel_sig": review_sig,
        "current_panel_sig": results_sig,
        "usable": usable,
        "verdicts": {
            "docsearch": docsearch_verdicts,
            "nsidc": nsidc_verdicts,
        },
        "verdicts_by_chunk": verdicts_by_chunk,
        "overall_verdict": overall,
        "routing": routing,
        "human_truth": human_truth,
    }


def summarize(records: list[dict]) -> dict:
    """High-level counts to surface in human_review.json — useful for
    quick sanity checks without parsing the per-row entries.

    The buckets partition every file exactly once:
        total_files = incomplete + usable + stale + unverifiable
    where stale/unverifiable are counted only among *completed* forms
    (an incomplete form has no verdicts to be stale about). `usable` is
    the count the human metric actually grades over — completed AND
    scored against the current panel."""
    completed = [r for r in records if not r["incomplete"]]
    overall_counts: dict[str, int] = {}
    routing_counts: dict[str, int] = {}
    stale = unverifiable = usable = 0
    for r in completed:
        overall = r["overall_verdict"] or "(blank)"
        overall_counts[overall] = overall_counts.get(overall, 0) + 1
        routing = r["routing"] or "(blank)"
        routing_counts[routing] = routing_counts.get(routing, 0) + 1
        status = r.get("panel_status")
        if status == "current":
            usable += 1
        elif status == "stale":
            stale += 1
        else:
            unverifiable += 1
    return {
        "total_files": len(records),
        "completed": len(completed),
        "incomplete": len(records) - len(completed),
        # staleness buckets (among completed forms)
        "usable": usable,
        "stale": stale,
        "unverifiable": unverifiable,
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
        f"  of completed: {summary['usable']} usable, "
        f"{summary['stale']} stale (panel rechunked since scoring), "
        f"{summary['unverifiable']} unverifiable (no panel signature)\n"
        f"wrote {out_path.relative_to(REPO_ROOT)}",
        file=sys.stderr,
    )
    if summary["stale"] or summary["unverifiable"]:
        print(
            "  NOTE: stale/unverifiable rows are excluded from the human "
            "metric. Re-score them against the regenerated -results.md "
            "(generate_review.py --overwrite) and re-run this ingest.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
