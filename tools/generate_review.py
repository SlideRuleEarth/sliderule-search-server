"""Generate per-row markdown review forms for the golden set.

Walks evals/golden_set.jsonl and, for each row, runs the query against
BOTH corpora (docsearch + nsidc), captures the top-K full chunks, and
writes a markdown file at evals/review/<NN>-<slug>.md with a fillable
review form.

The point: present what an agent (Claude / ChatGPT / etc.) would actually
see in the search response — full chunk text, not truncated — so a
domain expert can score the results offline.

Usage
-----
    python tools/generate_review.py [--limit N] [--overwrite]

By default, files that already exist in evals/review/ are NOT overwritten,
so a partially-completed review survives a re-run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from server import ranking  # noqa: E402
from server.embedder import MiniLMEmbedder  # noqa: E402
from tools.eval_retrieval import (  # noqa: E402
    CORPUS_PATHS,
    GOLDEN_SET_PATH,
    MODEL_PATH,
    TOKENIZER_PATH,
    load_corpus_state,
)

REVIEW_DIR = REPO_ROOT / "evals" / "review"
TOP_K = 5  # how many chunks to surface per corpus in the review form


def slugify(text: str, max_len: int = 60) -> str:
    """ASCII-safe lowercase slug for filenames."""
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rsplit("-", 1)[0]
    return s


def format_chunk_block(rank: int, chunk: dict) -> list[str]:
    """One result block for the human-review form. Full chunk text — no
    truncation — because the form is supposed to show what the agent sees.
    """
    lines = []
    lines.append(f"#### r{rank} — score {chunk['score']:.3f}")
    lines.append("")
    lines.append(f"- **url:** {chunk.get('url', '')}")
    lines.append(f"- **title:** {chunk.get('title', '') or '(none)'}")
    lines.append(f"- **section:** {chunk.get('section', '') or '(none)'}")
    if chunk.get("category"):
        lines.append(f"- **category:** `{chunk['category']}`")
    if chunk.get("source_product"):
        lines.append(
            f"- **source_product:** `{chunk['source_product']}` · "
            f"**page:** {chunk.get('source_page', '?')}"
        )
    if chunk.get("matched_tokens"):
        lines.append(f"- **matched_tokens:** {chunk['matched_tokens']}")
    lines.append("")
    lines.append("**Full text:**")
    lines.append("")
    lines.append("```")
    lines.append(chunk.get("text", ""))
    lines.append("```")
    lines.append("")
    return lines


def render_results_md(
    idx: int,
    row: dict,
    results_by_corpus: dict[str, list[dict]],
    review_filename: str,
) -> str:
    """Compose the read-only `-results.md` companion: query header,
    auto-labels, and the two result panels with full chunk text.

    This file is regenerated on every run — do not edit it. Verdicts and
    feedback go in the matching `-review.md` file.
    """
    lines = [
        f"# Row {idx} results: {row['corpus']} / {row.get('type', '?')}",
        "",
        f"> Auto-generated. Open this file alongside `{review_filename}` —",
        f"> verdicts go there, this side is read-only.",
        "",
        f"**Query:** `{row['query']}`",
        "",
        "## Auto-labeled (current ground truth)",
        "",
        f"- **corpus:** `{row['corpus']}`",
        "- **expected_urls:**",
    ]
    for u in row["expected_urls"]:
        lines.append(f"  - {u}")
    if row.get("expected_sections"):
        lines.append("- **expected_sections:**")
        for s in row["expected_sections"]:
            lines.append(f"  - `{s}`")
    else:
        lines.append("- **expected_sections:** (none)")
    if row.get("expected_pages"):
        lines.append("- **expected_pages:**")
        for start, end in row["expected_pages"]:
            lines.append(f"  - {start}–{end}")
    else:
        lines.append("- **expected_pages:** (none)")
    if row.get("notes"):
        lines.append(f"- **notes:** {row['notes']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Two result panels — what an agent would see if it queried each corpus
    for corpus_label, panel_title in [
        ("docsearch", "📚 docsearch results"),
        ("nsidc", "📘 nsidc results"),
    ]:
        lines.append(f"## {panel_title} (top {TOP_K})")
        lines.append("")
        results = results_by_corpus[corpus_label]
        if not results:
            lines.append("_(no results)_")
            lines.append("")
            continue
        for rank, chunk in enumerate(results, start=1):
            lines.extend(format_chunk_block(rank, chunk))
        lines.append("---")
        lines.append("")

    return "\n".join(lines) + "\n"


def render_review_md(idx: int, row: dict, results_filename: str) -> str:
    """Compose the editable `-review.md` companion: short query header
    + the form with all blanks. This file is preserved across re-runs
    of generate_review.py unless --overwrite is set.

    Header includes row index + query so the parser can extract
    metadata directly from this file (no need to cross-read -results.md).
    """
    lines = [
        f"# Row {idx} review",
        "",
        f"> Companion to `{results_filename}`. Open both side-by-side;",
        f"> this file is your editable form.",
        "",
        f"**Query:** `{row['query']}`",
        f"**Labeled corpus:** `{row['corpus']}`",
        "",
        "---",
        "",
        "## Per-result verdicts",
        "",
        "Mark each result `correct`, `partial`, or `wrong`. Leave blank to skip.",
        "",
        "**docsearch:**",
        "",
        "- r1: ",
        "- r2: ",
        "- r3: ",
        "- r4: ",
        "- r5: ",
        "",
        "**nsidc:**",
        "",
        "- r1: ",
        "- r2: ",
        "- r3: ",
        "- r4: ",
        "- r5: ",
        "",
        "## Overall verdict",
        "",
        "One of: `correct` | `partial` | `wrong`",
        "",
        "- overall: ",
        "",
        "## Cross-corpus routing",
        "",
        "Should this query target a different corpus? One of:",
        "`keep` | `redirect-to-docsearch` | `redirect-to-nsidc` | `both-corpora`",
        "",
        "- routing: ",
        "",
        "## Human truth (the actual right answer)",
        "",
        "If the right answer was returned at some rank, you can leave these",
        "blank — the per-result verdicts above already capture that. Fill",
        "these in **only if** the correct answer is not in either result set,",
        "or if you want to override what's correct.",
        "",
        "Repeat any field on a new `- field: value` line for multiple values.",
        "",
        "- corpus: ",
        "- url: ",
        "- section: ",
        "- pages: ",
        "- notes: ",
        "",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--limit", type=int, default=None,
                   help="Only generate the first N rows (e.g. for a pilot).")
    p.add_argument("--overwrite", action="store_true",
                   help="Overwrite existing review files. Default: skip them.")
    args = p.parse_args()

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)

    rows = [
        json.loads(line)
        for line in GOLDEN_SET_PATH.read_text().splitlines()
        if line.strip()
    ]
    if args.limit is not None:
        rows = rows[: args.limit]
    print(f"loaded {len(rows)} golden-set rows", file=sys.stderr)

    corpora = {name: load_corpus_state(path) for name, path in CORPUS_PATHS.items()}
    for name, state in corpora.items():
        print(f"loaded {name}: {len(state['chunks'])} chunks", file=sys.stderr)

    model = MiniLMEmbedder(MODEL_PATH, TOKENIZER_PATH)
    print("loaded embedder", file=sys.stderr)

    results_written = 0
    review_written = 0
    review_preserved = 0
    for idx, row in enumerate(rows, start=1):
        slug = slugify(row["query"])
        results_path = REVIEW_DIR / f"{idx:02d}-{slug}-results.md"
        review_path = REVIEW_DIR / f"{idx:02d}-{slug}-review.md"

        # Always run retrieval — even if -review.md is preserved we want
        # a fresh -results.md reflecting current corpus + ranking code.
        results_by_corpus: dict[str, list[dict]] = {}
        for corpus_name, state in corpora.items():
            vec = model.encode([row["query"]])[0]
            results = ranking.rank(
                state["chunks"], state["matrix"], state["per_chunk_tokens"],
                row["query"], vec, TOP_K,
            )
            results_by_corpus[corpus_name] = results

        # `-results.md` is auto-generated and ALWAYS regenerated. The user
        # never edits it, so overwriting is safe.
        results_md = render_results_md(idx, row, results_by_corpus, review_path.name)
        results_path.write_text(results_md)
        results_written += 1
        print(f"  wrote {results_path.relative_to(REPO_ROOT)}", file=sys.stderr)

        # `-review.md` is the editable form. Skip if it exists already, so
        # in-progress feedback is never clobbered. --overwrite lets the user
        # explicitly reset.
        if review_path.exists() and not args.overwrite:
            review_preserved += 1
            print(
                f"  skip  {review_path.relative_to(REPO_ROOT)} (preserved)",
                file=sys.stderr,
            )
        else:
            review_md = render_review_md(idx, row, results_path.name)
            review_path.write_text(review_md)
            review_written += 1
            print(f"  wrote {review_path.relative_to(REPO_ROOT)}", file=sys.stderr)

    print(
        f"\ndone: results={results_written} (always refreshed), "
        f"review wrote={review_written}, preserved={review_preserved} "
        f"(use --overwrite to reset preserved review files)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
