"""Offline retrieval-quality harness for the POC golden set.

Loads both corpora locally, runs each query in evals/golden_set.jsonl
through server.ranking.rank() (bypassing Lambda, HTTP, and the cache),
computes recall@5 / hit@1 / MRR, and writes a markdown report.

Usage
-----
    python tools/eval_retrieval.py

Outputs
-------
    stdout       JSON summary (for machine consumption / CI diffing)
    evals/report.md  human-readable per-query breakdown + diagnosis

Determinism
-----------
Same corpus + same golden_set + same code = identical metrics run over run.
Numpy argsort and Python's sorted() both use stable ordering; rank()
tiebreaks on index ascending. If this ever emits different numbers on a
repeat run with unchanged inputs, something stateful leaked in.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from server import ranking
from server.embedder import MiniLMEmbedder

TOP_K = 50
K_RECALL = 5

CORPUS_PATHS = {
    "docsearch": REPO_ROOT / "generated" / "docsearch" / "corpus.json",
    "nsidc": REPO_ROOT / "generated" / "nsidc" / "corpus.json",
}
MODEL_PATH = REPO_ROOT / "generated" / "shared" / "model.onnx"
TOKENIZER_PATH = REPO_ROOT / "generated" / "shared" / "tokenizer.json"
GOLDEN_SET_PATH = REPO_ROOT / "evals" / "golden_set.jsonl"
REPORT_PATH = REPO_ROOT / "evals" / "report.md"
AUDIT_PATH = REPO_ROOT / "evals" / "audit.md"


def load_corpus_state(path: Path) -> dict:
    """Replicate the server's cold-start prep: load corpus, L2-normalize
    the embedding matrix, pre-tokenize each chunk (text + section). The
    exact shape ranking.rank() expects."""
    corpus = json.loads(path.read_bytes())
    ranking.validate_corpus(corpus)
    chunks = corpus["chunks"]

    matrix = np.asarray([c["embedding"] for c in chunks], dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1)
    norms[norms == 0] = 1.0
    matrix = matrix / norms[:, None]

    per_chunk_tokens = [
        set(ranking.tokenize(c.get("text", "") + " " + c.get("section", "")))
        for c in chunks
    ]
    return {"chunks": chunks, "matrix": matrix, "per_chunk_tokens": per_chunk_tokens}


def _section_match(section: str, expected_sections: list[str] | None) -> bool:
    """Case-insensitive substring match against the chunk's section."""
    if not expected_sections:
        return False
    s = (section or "").lower()
    return any(sub.lower() in s for sub in expected_sections)


def _page_match(page: int | None, expected_pages: list[list[int]] | None) -> bool:
    """Inclusive [start, end] range match against the chunk's source_page."""
    if not expected_pages or page is None:
        return False
    return any(start <= page <= end for start, end in expected_pages)


def chunk_full_match(
    r: dict,
    expected_urls_set: set[str],
    expected_sections: list[str] | None,
    expected_pages: list[list[int]] | None,
) -> bool:
    """Does this chunk satisfy URL + (section OR page if narrowing fields are set)?

    URL match is required. If neither narrowing field is provided, URL
    is sufficient. If either is provided, the chunk must also match at
    least one of them (OR-combined — see plan)."""
    if r["url"] not in expected_urls_set:
        return False
    if not expected_sections and not expected_pages:
        return True
    return _section_match(r.get("section", ""), expected_sections) or _page_match(
        r.get("source_page"), expected_pages
    )


def first_expected_rank(
    results: list[dict],
    expected_urls: list[str],
    expected_sections: list[str] | None = None,
    expected_pages: list[list[int]] | None = None,
) -> int | None:
    """1-based rank of the first result that fully matches the expected
    label (URL + section/page narrowing if provided), or None if no
    chunk in `results` qualifies."""
    expected_urls_set = set(expected_urls)
    for rank_, r in enumerate(results, start=1):
        if chunk_full_match(r, expected_urls_set, expected_sections, expected_pages):
            return rank_
    return None


AUDIT_TOP_N = 5
AUDIT_TEXT_CHARS = 400


def evaluate(rows: list[dict], corpora: dict, model) -> list[dict]:
    """Run every query, return per-row records with rank + metrics +
    enough chunk detail for the audit report."""
    records = []
    for row in rows:
        state = corpora[row["corpus"]]
        vec = model.encode([row["query"]])[0]
        results = ranking.rank(
            state["chunks"],
            state["matrix"],
            state["per_chunk_tokens"],
            row["query"],
            vec,
            TOP_K,
        )
        expected_sections = row.get("expected_sections")
        expected_pages = row.get("expected_pages")
        rank_ = first_expected_rank(
            results, row["expected_urls"], expected_sections, expected_pages
        )
        expected_set = set(row["expected_urls"])
        has_narrowing = bool(expected_sections or expected_pages)
        top_results = []
        for i, r in enumerate(results[:AUDIT_TOP_N], start=1):
            url_match = r["url"] in expected_set
            full_match = chunk_full_match(
                r, expected_set, expected_sections, expected_pages
            )
            top_results.append({
                "rank": i,
                "score": r["score"],
                "url": r["url"],
                "section": r.get("section", ""),
                "title": r.get("title", ""),
                "text": r.get("text", ""),
                "category": r.get("category"),
                "source_product": r.get("source_product"),
                "source_page": r.get("source_page"),
                "match": full_match,           # full-hit (URL + narrowing if any)
                "url_match": url_match,        # URL-only — useful for the audit's tiered flag
            })
        records.append({
            "corpus": row["corpus"],
            "type": row.get("type", "unknown"),
            "query": row["query"],
            "expected_urls": row["expected_urls"],
            "expected_sections": expected_sections,
            "expected_pages": expected_pages,
            "has_narrowing": has_narrowing,
            "first_rank": rank_,
            "top_urls": [r["url"] for r in results[:5]],
            "top_results": top_results,
            "notes": row.get("notes", ""),
        })
    return records


def aggregate(records: list[dict]) -> dict:
    """Compute recall@5, hit@1, MRR over a list of per-query records."""
    n = len(records)
    if n == 0:
        return {"n": 0, "recall_at_5": 0.0, "hit_at_1": 0.0, "mrr": 0.0}
    recall5 = sum(1 for r in records if r["first_rank"] is not None and r["first_rank"] <= K_RECALL) / n
    hit1 = sum(1 for r in records if r["first_rank"] == 1) / n
    mrr = sum(1.0 / r["first_rank"] if r["first_rank"] else 0.0 for r in records) / n
    return {"n": n, "recall_at_5": recall5, "hit_at_1": hit1, "mrr": mrr}


BAR = {"recall_at_5": 0.70, "hit_at_1": 0.50, "mrr": 0.55}


def _mark(value: float, bar: float) -> str:
    return "✓" if value >= bar else "✗"


def write_report(records: list[dict], summary: dict) -> None:
    """Dump a human-readable breakdown to evals/report.md."""
    overall = summary["overall"]
    lines = [
        "# Retrieval POC — Baseline Report",
        "",
        "Generated by `tools/eval_retrieval.py`. Offline run against local",
        "corpora + `server.ranking.rank()` (no Lambda, no HTTP, no cache).",
        "",
        "## Verdict",
        "",
        "| Metric | Value | Bar | Pass |",
        "| --- | --- | --- | --- |",
        f"| recall@5 | {overall['recall_at_5']:.3f} | ≥ 0.70 | {_mark(overall['recall_at_5'], BAR['recall_at_5'])} |",
        f"| hit@1 | {overall['hit_at_1']:.3f} | ≥ 0.50 | {_mark(overall['hit_at_1'], BAR['hit_at_1'])} |",
        f"| MRR | {overall['mrr']:.3f} | ≥ 0.55 | {_mark(overall['mrr'], BAR['mrr'])} |",
        "",
    ]

    all_pass = all(overall[k] >= v for k, v in BAR.items())
    if all_pass:
        lines += [
            "**All three metrics clear the bar.** The retrieval layer is working",
            "well enough on this golden set that the next investment is either",
            "Option C (architecture POC: latency / cost / reliability under load)",
            "or the cheap Tier-2 levers that tackle the specific misses below.",
            "",
        ]
    else:
        failing = [k for k, v in BAR.items() if overall[k] < v]
        lines += [
            f"**Below bar on: {', '.join(failing)}.** Investment priority is",
            "the Tier 1-2 / Tier 3 levers in LongTermIdeas.md whose failure modes",
            "match the diagnosis section below.",
            "",
        ]

    lines += [
        "## Per corpus",
        "",
        "| corpus | n | recall@5 | hit@1 | MRR |",
        "| --- | --- | --- | --- | --- |",
    ]
    for corpus_name, m in summary["by_corpus"].items():
        lines.append(f"| {corpus_name} | {m['n']} | {m['recall_at_5']:.3f} | {m['hit_at_1']:.3f} | {m['mrr']:.3f} |")

    lines += [
        "",
        "## Per query type",
        "",
        "Lowest-scoring buckets are the most informative for picking levers.",
        "",
        "| corpus | type | n | recall@5 | hit@1 | MRR |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for (corpus_name, type_), m in sorted(summary["by_type"].items()):
        lines.append(f"| {corpus_name} | {type_} | {m['n']} | {m['recall_at_5']:.3f} | {m['hit_at_1']:.3f} | {m['mrr']:.3f} |")

    # Below top-5 are the most diagnostic: expected URL existed in corpus but
    # ranked outside the user-visible top-5 window.
    below_5 = [r for r in records if r["first_rank"] is None or r["first_rank"] > 5]
    lines += [
        "",
        "## Queries below recall@5",
        "",
        f"{len(below_5)} / {len(records)} queries where no expected URL appeared in top 5.",
        "Each is a candidate for a specific lever — not a mislabel (the URL is",
        "in the corpus; if it were truly missing, it wouldn't appear in top 50",
        "either and would show in the Misses section at the end).",
        "",
    ]
    for r in sorted(below_5, key=lambda x: (x["corpus"], x["first_rank"] or 999)):
        rank_display = f"rank {r['first_rank']}" if r["first_rank"] else "not in top 50"
        lines.append(f"- **[{r['corpus']}/{r['type']}]** `{r['query']}` ({rank_display})")
        lines.append(f"  - expected: {r['expected_urls'][0]}")
        lines.append(f"  - top 3 returned:")
        for u in r["top_urls"][:3]:
            lines.append(f"    - {u}")

    lines += [
        "",
        "## Per-query results",
        "",
        "`rank` = 1-based rank of the first expected_url in top 50; `—` = not found.",
        "",
    ]
    for corpus_name in ("docsearch", "nsidc"):
        lines.append(f"### {corpus_name}")
        lines.append("")
        lines.append("| type | rank | query |")
        lines.append("| --- | --- | --- |")
        for r in records:
            if r["corpus"] != corpus_name:
                continue
            rank_str = str(r["first_rank"]) if r["first_rank"] is not None else "—"
            lines.append(f"| {r['type']} | {rank_str} | {r['query']} |")
        lines.append("")

    # Total misses (not in top 50 at all) is a different class — if this is
    # non-empty, the golden set is likely mislabeled or the corpus genuinely
    # doesn't contain the answer.
    misses = [r for r in records if r["first_rank"] is None]
    lines += [
        "## Misses",
        "",
        "Queries where no expected URL appeared in top 50. A non-empty list",
        "here indicates either (a) a mislabeled expected URL, (b) the answer",
        "is genuinely not in the corpus, or (c) a severe retrieval failure",
        "that no lever short of rechunking or an embedder swap will fix.",
        "",
    ]
    if not misses:
        lines.append("None.")
    else:
        for r in misses:
            lines.append(f"- **[{r['corpus']}/{r['type']}]** `{r['query']}`")
            lines.append(f"  - expected: {', '.join(r['expected_urls'])}")
            lines.append(f"  - top 5 returned: {', '.join(r['top_urls']) if r['top_urls'] else '(none)'}")
            if r["notes"]:
                lines.append(f"  - notes: {r['notes']}")

    lines.append("")
    REPORT_PATH.write_text("\n".join(lines))


def fmt_metrics_row(label: str, m: dict) -> str:
    return (
        f"- **{label}**: n={m['n']}, "
        f"recall@5={m['recall_at_5']:.3f}, "
        f"hit@1={m['hit_at_1']:.3f}, "
        f"MRR={m['mrr']:.3f}"
    )


def _truncate_text(text: str, limit: int = AUDIT_TEXT_CHARS) -> str:
    """Collapse whitespace + truncate at word boundary."""
    t = " ".join(text.split())
    if len(t) <= limit:
        return t
    cut = t[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def write_audit(records: list[dict]) -> None:
    """Per-query audit report: each golden-set row + its top-5 chunks with
    the actual text, so a human can judge whether expected_urls is a fair
    label and whether the returned chunks answer the query.

    Regenerates on every run. For auditing labels, not measuring quality
    — metrics live in report.md."""
    lines = [
        "# Retrieval POC — Label Audit",
        "",
        "Per-query view of what the retriever returned + the actual chunk",
        "text, so you can judge:",
        "",
        "- Does the chunk at an `expected_url` actually answer the query?",
        "- Are there chunks returned at top ranks that *also* legitimately",
        "  answer the query but aren't in `expected_urls`?",
        "",
        f"Top {AUDIT_TOP_N} results per query. Chunk text truncated to",
        f"~{AUDIT_TEXT_CHARS} characters for readability; full text is in the",
        "chunk's source URL.",
        "",
        "Legend:",
        "- `[✓✓]` — full hit (URL match AND, if narrowing fields are set, section/page match)",
        "- `[✓ ]` — URL match only (right doc, but section/page narrowing rejected this chunk)",
        "- `[  ]` — URL not in `expected_urls`",
        "",
        "For rows without `expected_sections` or `expected_pages`, URL match",
        "alone is sufficient and shows as `[✓✓]` (no narrowing applied).",
        "",
    ]

    for corpus_name in ("docsearch", "nsidc"):
        lines.append(f"## {corpus_name}")
        lines.append("")
        corpus_records = [r for r in records if r["corpus"] == corpus_name]
        for idx, r in enumerate(corpus_records, start=1):
            rank = r["first_rank"]
            rank_badge = f"rank {rank}" if rank else "not found"
            pass_mark = "✓" if rank and rank <= 5 else "✗"
            lines.append(
                f"### {corpus_name} #{idx} — `{r['type']}` — {pass_mark} {rank_badge}"
            )
            lines.append("")
            lines.append(f"**Query:** `{r['query']}`")
            lines.append("")
            lines.append(f"**Expected URL(s):**")
            for u in r["expected_urls"]:
                lines.append(f"- {u}")
            if r.get("expected_sections"):
                lines.append("")
                lines.append(f"**Expected sections** (case-insensitive substring on chunk.section):")
                for s in r["expected_sections"]:
                    lines.append(f"- `{s}`")
            if r.get("expected_pages"):
                lines.append("")
                lines.append(f"**Expected pages** (inclusive ranges on chunk.source_page):")
                for start, end in r["expected_pages"]:
                    lines.append(f"- {start}–{end}")
            if r.get("notes"):
                lines.append("")
                lines.append(f"**Author's note:** {r['notes']}")
            lines.append("")
            lines.append(f"**Top {AUDIT_TOP_N} returned:**")
            lines.append("")
            for tr in r["top_results"]:
                # tiered flag: full hit, URL-only, or no URL match
                if tr["match"]:
                    mark = "✓✓"
                elif tr.get("url_match"):
                    mark = "✓ "
                else:
                    mark = "  "
                meta_parts = []
                if tr.get("category"):
                    meta_parts.append(f"category=`{tr['category']}`")
                if tr.get("source_product"):
                    meta_parts.append(f"product=`{tr['source_product']}`")
                if tr.get("source_page"):
                    meta_parts.append(f"page {tr['source_page']}")
                meta_suffix = "  \n    " + " · ".join(meta_parts) if meta_parts else ""
                lines.append(
                    f"{tr['rank']}. [{mark}] **score {tr['score']:.3f}** — "
                    f"{tr['url']}  \n    "
                    f"*section:* **{tr['section'] or '(none)'}**"
                    f"{meta_suffix}"
                )
                lines.append("")
                lines.append(f"    > {_truncate_text(tr['text'])}")
                lines.append("")
            lines.append("---")
            lines.append("")

    AUDIT_PATH.write_text("\n".join(lines))


def main() -> int:
    rows = [json.loads(l) for l in GOLDEN_SET_PATH.read_text().splitlines() if l.strip()]
    print(f"loaded {len(rows)} golden-set rows", file=sys.stderr)

    corpora = {name: load_corpus_state(path) for name, path in CORPUS_PATHS.items()}
    for name, s in corpora.items():
        print(f"loaded {name}: {len(s['chunks'])} chunks", file=sys.stderr)

    model = MiniLMEmbedder(MODEL_PATH, TOKENIZER_PATH)
    print("loaded embedder", file=sys.stderr)

    records = evaluate(rows, corpora, model)

    summary = {
        "overall": aggregate(records),
        "by_corpus": {c: aggregate([r for r in records if r["corpus"] == c]) for c in CORPUS_PATHS},
        "by_type": {
            (c, t): aggregate([r for r in records if r["corpus"] == c and r["type"] == t])
            for c, t in sorted({(r["corpus"], r["type"]) for r in records})
        },
    }

    summary_out = {
        "overall": summary["overall"],
        "by_corpus": summary["by_corpus"],
        "by_type": {f"{c}/{t}": m for (c, t), m in summary["by_type"].items()},
    }
    print(json.dumps(summary_out, indent=2))

    write_report(records, summary)
    print(f"wrote {REPORT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    write_audit(records)
    print(f"wrote {AUDIT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
