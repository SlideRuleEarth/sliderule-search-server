"""Offline retrieval-quality harness for the POC golden set.

Loads both corpora locally, runs each query in evals/golden_set.jsonl
through server.ranking.rank() (bypassing Lambda, HTTP, and the cache),
computes recall@5 / hit@1 / MRR, and writes a markdown report.

Two grading modes:
  --metric=auto  (default) grades against `expected_urls`/`expected_sections`/
                 `expected_pages` in golden_set.jsonl (cheap, can be wrong)
  --metric=human grades against per-result verdicts in human_review.json
                 (trustworthy ground truth, only as good as the reviewer)
  --metric=both  (recommended for Phase 2 reconciliation) emits both side-by-side

Usage
-----
    python tools/eval_retrieval.py [--metric={auto,human,both}]

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

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

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
HUMAN_REVIEW_PATH = REPO_ROOT / "evals" / "human_review.json"
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


def _url_path(url: str) -> str:
    """Path component of a URL, host-stripped. Lets the golden set keep
    canonical `docs.slideruleearth.io/...` URLs while we chunk against
    a mirror like `docs.testsliderule.org/...` — path is what's stable."""
    return urlparse(url).path


def chunk_full_match(
    r: dict,
    expected_paths: set[str],
    expected_sections: list[str] | None,
    expected_pages: list[list[int]] | None,
) -> bool:
    """Does this chunk satisfy URL + (section OR page if narrowing fields are set)?

    URL match is required (path-only — host is ignored). If neither
    narrowing field is provided, URL is sufficient. If either is
    provided, the chunk must also match at least one of them
    (OR-combined — see plan)."""
    if _url_path(r["url"]) not in expected_paths:
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
    expected_paths = {_url_path(u) for u in expected_urls}
    for rank_, r in enumerate(results, start=1):
        if chunk_full_match(r, expected_paths, expected_sections, expected_pages):
            return rank_
    return None


def load_human_review() -> dict[int, dict]:
    """Returns row_index → record from evals/human_review.json. Empty
    dict if the file doesn't exist yet (first run before any reviews
    have been ingested). Only completed records are included."""
    if not HUMAN_REVIEW_PATH.exists():
        return {}
    data = json.loads(HUMAN_REVIEW_PATH.read_bytes())
    return {
        r["row_index"]: r
        for r in data.get("records", [])
        if not r.get("incomplete")
    }


def first_human_rank(verdicts: dict | None) -> int | None:
    """1-based rank of the first chunk with a `correct` verdict in r1..r5.
    Returns None if no `correct` verdict in top-5. Strict-mode only —
    `partial` chunks don't count as hits. The reviewer only saw the top-5,
    so ranks 6-50 are necessarily None even if the chunk would be correct."""
    if not verdicts:
        return None
    for rank in range(1, 6):
        if verdicts.get(f"r{rank}") == "correct":
            return rank
    return None


AUDIT_TOP_N = 5
AUDIT_TEXT_CHARS = 400


def evaluate(rows: list[dict], corpora: dict, model, human_records: dict[int, dict] | None = None) -> list[dict]:
    """Run every query, return per-row records with rank + metrics +
    enough chunk detail for the audit report.

    If `human_records` is provided (row_index → human review record),
    each record also gets `human_first_rank` populated from the per-result
    verdicts on the row's labeled corpus."""
    human_records = human_records or {}
    records = []
    for idx, row in enumerate(rows, start=1):
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
        expected_path_set = {_url_path(u) for u in row["expected_urls"]}
        has_narrowing = bool(expected_sections or expected_pages)

        # Pull the human verdicts for this row's labeled corpus, if any.
        # Verdicts at ranks 1-5 only — that's all the reviewer was shown.
        human_rec = human_records.get(idx)
        human_verdicts = None
        if human_rec:
            human_verdicts = (human_rec.get("verdicts") or {}).get(row["corpus"])
        human_rank = first_human_rank(human_verdicts)

        top_results = []
        for i, r in enumerate(results[:AUDIT_TOP_N], start=1):
            url_match = _url_path(r["url"]) in expected_path_set
            full_match = chunk_full_match(
                r, expected_path_set, expected_sections, expected_pages
            )
            human_verdict = (human_verdicts or {}).get(f"r{i}") if human_verdicts else None
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
                "human_verdict": human_verdict,  # correct/partial/wrong/None
            })
        records.append({
            "row_index": idx,
            "corpus": row["corpus"],
            "type": row.get("type", "unknown"),
            "query": row["query"],
            "expected_urls": row["expected_urls"],
            "expected_sections": expected_sections,
            "expected_pages": expected_pages,
            "has_narrowing": has_narrowing,
            "first_rank": rank_,
            "human_first_rank": human_rank,
            "human_available": human_verdicts is not None,
            "top_urls": [r["url"] for r in results[:5]],
            "top_results": top_results,
            "notes": row.get("notes", ""),
        })
    return records


def aggregate(records: list[dict], rank_field: str = "first_rank") -> dict:
    """Compute recall@5, hit@1, MRR over a list of per-query records.

    `rank_field` selects which rank column to grade against:
      - 'first_rank'        (auto-metric — golden_set.jsonl labels)
      - 'human_first_rank'  (human-metric — per-result verdicts)

    Records where the rank field is None contribute 0 to all three metrics.
    For the human metric, that includes rows with no completed review."""
    n = len(records)
    if n == 0:
        return {"n": 0, "recall_at_5": 0.0, "hit_at_1": 0.0, "mrr": 0.0}
    recall5 = sum(1 for r in records if r.get(rank_field) is not None and r[rank_field] <= K_RECALL) / n
    hit1 = sum(1 for r in records if r.get(rank_field) == 1) / n
    mrr = sum(1.0 / r[rank_field] if r.get(rank_field) else 0.0 for r in records) / n
    return {"n": n, "recall_at_5": recall5, "hit_at_1": hit1, "mrr": mrr}


BAR = {"recall_at_5": 0.70, "hit_at_1": 0.50, "mrr": 0.55}


def _mark(value: float, bar: float) -> str:
    return "✓" if value >= bar else "✗"


def _verdict_section(label: str, summary: dict) -> list[str]:
    """Emit verdict + bar table for a single metric mode."""
    overall = summary["overall"]
    lines = [
        f"## Verdict — {label}",
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
            "**All three metrics clear the bar.**",
            "",
        ]
    else:
        failing = [k for k, v in BAR.items() if overall[k] < v]
        lines += [
            f"**Below bar on: {', '.join(failing)}.**",
            "",
        ]
    return lines


def _breakdown_section(label: str, summary: dict) -> list[str]:
    """Emit per-corpus and per-type tables for one metric mode."""
    lines = [
        f"## Per corpus — {label}",
        "",
        "| corpus | n | recall@5 | hit@1 | MRR |",
        "| --- | --- | --- | --- | --- |",
    ]
    for corpus_name, m in summary["by_corpus"].items():
        lines.append(f"| {corpus_name} | {m['n']} | {m['recall_at_5']:.3f} | {m['hit_at_1']:.3f} | {m['mrr']:.3f} |")
    lines += [
        "",
        f"## Per query type — {label}",
        "",
        "| corpus | type | n | recall@5 | hit@1 | MRR |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for (corpus_name, type_), m in sorted(summary["by_type"].items()):
        lines.append(f"| {corpus_name} | {type_} | {m['n']} | {m['recall_at_5']:.3f} | {m['hit_at_1']:.3f} | {m['mrr']:.3f} |")
    lines.append("")
    return lines


def _disagreement_section(records: list[dict]) -> list[str]:
    """List rows where auto and human disagree on hit-vs-miss in top-5.
    Only emitted when both metrics are available."""
    auto_human = [r for r in records if r.get("human_available")]
    if not auto_human:
        return []

    auto_hit = lambda r: r["first_rank"] is not None and r["first_rank"] <= K_RECALL
    human_hit = lambda r: r["human_first_rank"] is not None  # already capped at top-5

    auto_only = [r for r in auto_human if auto_hit(r) and not human_hit(r)]
    human_only = [r for r in auto_human if human_hit(r) and not auto_hit(r)]

    lines = [
        "## Auto vs human disagreements",
        "",
        f"Out of {len(auto_human)} rows with completed human review:",
        f"- **{len(auto_only)} rows where auto says hit, human says miss** (auto-label likely too generous)",
        f"- **{len(human_only)} rows where auto says miss, human says hit** (auto-label likely too narrow)",
        "",
        "The disagreements are the work for the auto-vs-human reconciliation step (Phase 2 step 3).",
        "",
    ]
    if auto_only:
        lines.append("### Auto says hit, human says miss")
        lines.append("")
        for r in auto_only:
            verdicts = [tr.get("human_verdict") or "_" for tr in r["top_results"]]
            lines.append(f"- **row {r['row_index']} [{r['corpus']}/{r['type']}]** `{r['query']}`")
            lines.append(f"  - auto first_rank: {r['first_rank']}; human verdicts r1..r5: {' '.join(verdicts)}")
        lines.append("")
    if human_only:
        lines.append("### Auto says miss, human says hit")
        lines.append("")
        for r in human_only:
            verdicts = [tr.get("human_verdict") or "_" for tr in r["top_results"]]
            lines.append(f"- **row {r['row_index']} [{r['corpus']}/{r['type']}]** `{r['query']}`")
            lines.append(f"  - auto first_rank: {r['first_rank']}; human verdicts r1..r5: {' '.join(verdicts)}; human first `correct` rank: {r['human_first_rank']}")
        lines.append("")
    return lines


def write_report(
    records: list[dict],
    auto_summary: dict | None,
    human_summary: dict | None,
) -> None:
    """Dump a human-readable breakdown to evals/report.md.

    Pass either or both summary dicts. When both are present, the report
    shows them side-by-side and includes an auto-vs-human disagreement
    section."""
    lines = [
        "# Retrieval POC — Baseline Report",
        "",
        "Generated by `tools/eval_retrieval.py`. Offline run against local",
        "corpora + `server.ranking.rank()` (no Lambda, no HTTP, no cache).",
        "",
    ]

    if auto_summary:
        lines += _verdict_section("auto-metric", auto_summary)
    if human_summary:
        lines += _verdict_section("human-metric", human_summary)

    if auto_summary and human_summary:
        a, h = auto_summary["overall"], human_summary["overall"]
        delta = lambda k: h[k] - a[k]
        sign = lambda x: f"+{x:.3f}" if x >= 0 else f"{x:.3f}"
        lines += [
            "## Auto vs human delta (overall)",
            "",
            "Positive delta = human-metric is higher (auto-labels too strict).",
            "Negative delta = human-metric is lower (auto-labels too generous).",
            "",
            "| Metric | auto | human | delta |",
            "| --- | --- | --- | --- |",
            f"| recall@5 | {a['recall_at_5']:.3f} | {h['recall_at_5']:.3f} | {sign(delta('recall_at_5'))} |",
            f"| hit@1    | {a['hit_at_1']:.3f} | {h['hit_at_1']:.3f} | {sign(delta('hit_at_1'))} |",
            f"| MRR      | {a['mrr']:.3f} | {h['mrr']:.3f} | {sign(delta('mrr'))} |",
            "",
        ]

    if auto_summary:
        lines += _breakdown_section("auto-metric", auto_summary)
    if human_summary:
        lines += _breakdown_section("human-metric", human_summary)

    if auto_summary and human_summary:
        lines += _disagreement_section(records)

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


def _build_summary(records: list[dict], rank_field: str) -> dict:
    """Aggregate at overall / per-corpus / per-type granularity for a given rank field."""
    return {
        "overall": aggregate(records, rank_field),
        "by_corpus": {
            c: aggregate([r for r in records if r["corpus"] == c], rank_field)
            for c in CORPUS_PATHS
        },
        "by_type": {
            (c, t): aggregate([r for r in records if r["corpus"] == c and r["type"] == t], rank_field)
            for c, t in sorted({(r["corpus"], r["type"]) for r in records})
        },
    }


def _summary_for_json(summary: dict) -> dict:
    return {
        "overall": summary["overall"],
        "by_corpus": summary["by_corpus"],
        "by_type": {f"{c}/{t}": m for (c, t), m in summary["by_type"].items()},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--metric",
        choices=("auto", "human", "both"),
        default="both",
        help="Grade against golden_set.jsonl labels (auto), human_review.json verdicts (human), or both (default).",
    )
    args = parser.parse_args()

    rows = [json.loads(l) for l in GOLDEN_SET_PATH.read_text().splitlines() if l.strip()]
    print(f"loaded {len(rows)} golden-set rows", file=sys.stderr)

    human_records = load_human_review() if args.metric in ("human", "both") else {}
    if human_records:
        print(f"loaded {len(human_records)} human-review records", file=sys.stderr)
    elif args.metric in ("human", "both"):
        print(f"warning: no human reviews available at {HUMAN_REVIEW_PATH}", file=sys.stderr)

    corpora = {name: load_corpus_state(path) for name, path in CORPUS_PATHS.items()}
    for name, s in corpora.items():
        print(f"loaded {name}: {len(s['chunks'])} chunks", file=sys.stderr)

    model = MiniLMEmbedder(MODEL_PATH, TOKENIZER_PATH)
    print("loaded embedder", file=sys.stderr)

    records = evaluate(rows, corpora, model, human_records=human_records)

    auto_summary = _build_summary(records, "first_rank") if args.metric in ("auto", "both") else None
    human_summary = _build_summary(records, "human_first_rank") if args.metric in ("human", "both") and human_records else None

    summary_out: dict = {}
    if auto_summary:
        summary_out["auto"] = _summary_for_json(auto_summary)
    if human_summary:
        summary_out["human"] = _summary_for_json(human_summary)
    print(json.dumps(summary_out, indent=2))

    write_report(records, auto_summary, human_summary)
    print(f"wrote {REPORT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    write_audit(records)
    print(f"wrote {AUDIT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
