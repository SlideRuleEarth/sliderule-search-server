"""Offline retrieval-quality harness for the POC golden set.

Loads both corpora locally, runs each query in evals/golden_set.jsonl
through server.ranking.rank() (bypassing Lambda, HTTP, and the cache),
computes recall@5 / hit@1 / MRR, and writes a markdown report.

Two grading modes:
  --metric=auto  (default) grades against `expected_urls`/`expected_sections`/
                 `expected_pages` in golden_set.jsonl (cheap, can be wrong)
  --metric=human grades against per-result verdicts in human_review.json
                 (trustworthy ground truth, only as good as the reviewer).
                 Computed over completed reviews only — coverage against the
                 full golden set and the count of excluded incomplete forms
                 are reported alongside the metric, not folded into it.
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
import hashlib
import json
import math
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


def load_human_review() -> tuple[dict[int, dict], dict]:
    """Returns (row_index → record, meta) from evals/human_review.json.

    Only *usable* records land in the map — those that are both completed
    (not every-blank-empty) AND scored against the panel still in the
    corpus (`panel_status == "current"`). Incomplete, stale (corpus
    rechunked since scoring), and unverifiable (pre-guard, no panel
    signature) forms are excluded so they neither drag the metric toward
    zero nor — worse — attach a reviewer's verdict to a chunk they never
    saw. `meta` carries the ingest summary's coverage bookkeeping verbatim
    (incomplete / stale / unverifiable counts) so the report can state
    scope and excluded-reason explicitly.

    Records written before the staleness guard carry no `usable` flag; for
    those we fall back to the old completed-only rule so pre-guard
    human_review.json files keep working until re-ingested.

    Empty map + zeroed meta if the file doesn't exist yet (first run
    before any reviews have been ingested)."""
    if not HUMAN_REVIEW_PATH.exists():
        return {}, {"total_files": 0, "completed": 0, "incomplete": 0}
    data = json.loads(HUMAN_REVIEW_PATH.read_bytes())

    def _usable(r: dict) -> bool:
        flag = r.get("usable")
        if flag is None:  # pre-guard record: no staleness info to act on
            return not r.get("incomplete")
        return flag

    records_map = {
        r["row_index"]: r for r in data.get("records", []) if _usable(r)
    }
    return records_map, data.get("summary", {})


def _content_sig(text: str) -> str:
    """Mirror of ingest_review._content_sig — sha1[:12] of chunk text.
    Both producers must use the same hash so the chunk_key strings match."""
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def chunk_key_for_result(chunk: dict) -> str:
    """Build the chunk_key the way ingest_review.py does, so we can
    look up a chunk's human verdict regardless of its current rank.

    Survives reranking levers (cross-encoder, identifier boost, MMR,
    etc.) because the key is derived from chunk content + identity,
    not from rank position."""
    path = urlparse(chunk.get("url", "")).path
    section = (chunk.get("section") or "").strip()
    text = chunk.get("text", "")
    return f"{path}||{section}||{_content_sig(text)}"


def first_human_rank(
    results: list[dict],
    chunk_verdicts: dict[str, str] | None,
) -> int | None:
    """1-based rank of the first result whose chunk_key maps to verdict
    `correct` in `chunk_verdicts`. Returns None if no `correct` chunk in
    top-5 (the user only saw 5 chunks per panel; chunks they never saw
    have no verdict, so they count as no-hit).

    Robust to reranking — the verdict travels with the chunk, not with
    the rank slot it originally occupied."""
    if not chunk_verdicts:
        return None
    for rank, chunk in enumerate(results[:5], start=1):
        if chunk_verdicts.get(chunk_key_for_result(chunk)) == "correct":
            return rank
    return None


AUDIT_TOP_N = 5
AUDIT_TEXT_CHARS = 400

# Graded relevance scale for the human verdicts. Binary metrics treat
# only `correct` as a hit; the graded family below gives `partial` half
# credit, so a near-miss ranked highly scores better than a flat wrong.
GRADE = {"correct": 1.0, "partial": 0.5, "wrong": 0.0}


def _grade(verdict: str | None) -> float:
    """Map a verdict to its graded relevance. Unknown/None (a chunk the
    reviewer never saw, e.g. one a lever surfaced into top-5) scores 0 —
    same treatment as `wrong`, since we have no evidence it's relevant."""
    return GRADE.get(verdict or "", 0.0)


def _dcg(grades: list[float]) -> float:
    """Discounted cumulative gain with the standard log2(rank+1) discount
    (rank is 1-based, so rank 1 gets the full grade)."""
    return sum(g / math.log2(i + 1) for i, g in enumerate(grades, start=1))


def graded_metrics_at_5(
    top_verdicts: list[str | None],
    judged_grades: list[float],
) -> dict:
    """Graded relevance metrics over the retrieved top-5.

    `top_verdicts` are the verdicts at the current top-5 ranks (in order);
    `judged_grades` are the grades of *every* chunk the reviewer judged
    for this row — the pool the ideal ranking is drawn from, so a known-
    good chunk that a lever pushed out of top-5 still costs nDCG.

    Returns:
      - ndcg_at_5            DCG of the retrieved top-5 over the ideal DCG
      - graded_rr            grade of the first relevant (grade>0) result,
                             divided by its rank — the graded reciprocal
                             rank; aggregates to graded MRR. Binary MRR is
                             the special case where every hit grades 1.0.
      - strict_success_5     1.0 if any `correct` in top-5, else 0.0
      - partial_success_5    1.0 if any `partial`-or-better in top-5, else 0.0
    """
    retrieved = [_grade(v) for v in top_verdicts]
    idcg = _dcg(sorted(judged_grades, reverse=True)[:5])
    ndcg = _dcg(retrieved) / idcg if idcg > 0 else 0.0

    graded_rr = 0.0
    for rank, g in enumerate(retrieved, start=1):
        if g > 0:
            graded_rr = g / rank
            break

    return {
        "ndcg_at_5": ndcg,
        "graded_rr": graded_rr,
        "strict_success_5": 1.0 if any(g >= 1.0 for g in retrieved) else 0.0,
        "partial_success_5": 1.0 if any(g > 0 for g in retrieved) else 0.0,
    }


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

        # Pull the human chunk-keyed verdicts for this row's labeled
        # corpus, if any. Chunk-keyed (vs the older rank-keyed) so that
        # reranking levers don't invalidate the human-metric — the
        # verdict travels with the chunk, not the rank slot.
        human_rec = human_records.get(idx)
        chunk_verdicts = None
        if human_rec:
            chunk_verdicts = (human_rec.get("verdicts_by_chunk") or {}).get(row["corpus"])
        human_rank = first_human_rank(results, chunk_verdicts)

        top_results = []
        for i, r in enumerate(results[:AUDIT_TOP_N], start=1):
            url_match = _url_path(r["url"]) in expected_path_set
            full_match = chunk_full_match(
                r, expected_path_set, expected_sections, expected_pages
            )
            human_verdict = (
                chunk_verdicts.get(chunk_key_for_result(r))
                if chunk_verdicts
                else None
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
                "human_verdict": human_verdict,  # correct/partial/wrong/None
            })

        # Graded human metrics over the retrieved top-5. Only meaningful
        # when the row has verdicts; otherwise left None so the aggregate
        # can skip it (same gating as the binary human metric).
        graded = None
        if chunk_verdicts is not None:
            graded = graded_metrics_at_5(
                [tr["human_verdict"] for tr in top_results],
                [_grade(v) for v in chunk_verdicts.values()],
            )

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
            "human_available": chunk_verdicts is not None,
            "graded": graded,
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

    Records where the rank field is None contribute 0 to all three
    metrics. The caller controls the denominator by choosing which
    records to pass: the auto-metric grades over every golden-set row,
    while the human-metric is given only the reviewed subset so that
    unreviewed rows don't masquerade as retrieval misses."""
    n = len(records)
    if n == 0:
        return {"n": 0, "recall_at_5": 0.0, "hit_at_1": 0.0, "mrr": 0.0}
    recall5 = sum(1 for r in records if r.get(rank_field) is not None and r[rank_field] <= K_RECALL) / n
    hit1 = sum(1 for r in records if r.get(rank_field) == 1) / n
    mrr = sum(1.0 / r[rank_field] if r.get(rank_field) else 0.0 for r in records) / n
    return {"n": n, "recall_at_5": recall5, "hit_at_1": hit1, "mrr": mrr}


def aggregate_graded(records: list[dict]) -> dict:
    """Mean of the per-record graded metrics over `records`.

    Pass the reviewed subset (records carrying a non-None `graded`); any
    record without graded metrics contributes 0, matching the binary
    human metric's denominator convention. Reports nDCG@5, graded MRR,
    strict success@5 (any `correct` in top-5), and partial-or-better
    success@5 (any `partial`-or-better in top-5)."""
    n = len(records)
    keys = ("ndcg_at_5", "graded_rr", "strict_success_5", "partial_success_5")
    if n == 0:
        return {"n": 0, **{k: 0.0 for k in keys}}
    sums = {k: 0.0 for k in keys}
    for r in records:
        g = r.get("graded")
        if not g:
            continue
        for k in keys:
            sums[k] += g[k]
    out = {"n": n}
    # graded_rr aggregates to "graded MRR" — surface it under that name.
    out["ndcg_at_5"] = sums["ndcg_at_5"] / n
    out["graded_mrr"] = sums["graded_rr"] / n
    out["strict_success_at_5"] = sums["strict_success_5"] / n
    out["partial_success_at_5"] = sums["partial_success_5"] / n
    return out


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


def _coverage_note(cov: dict) -> list[str]:
    """Blockquote stating the human-metric's scope: it grades only the
    usable subset, so the denominator and every excluded reason must be
    spelled out or the numbers read as if they covered the whole set."""
    lines = [
        "> **Scope:** the human-metric is computed over *usable reviews only* —",
        "> completed AND scored against the panel still in the corpus. Unreviewed,",
        "> incomplete, stale, and unverifiable rows are excluded from the",
        "> denominator (rather than counted as misses).",
        ">",
        f"> - reviewed_n (usable): **{cov['reviewed_n']}** of {cov['total_rows']} golden-set rows",
        f"> - coverage: **{cov['coverage']:.1%}**",
        f"> - incomplete rows excluded: **{cov['incomplete_excluded']}**",
        f"> - stale rows excluded (corpus rechunked since scoring): **{cov.get('stale_excluded', 0)}**",
        f"> - unverifiable rows excluded (no panel signature): **{cov.get('unverifiable_excluded', 0)}**",
        "",
    ]
    return lines


def _human_suppressed_section(cov: dict) -> list[str]:
    """When completed reviews exist but none are usable, the human metric
    can't be computed — say so loudly and show the excluded breakdown,
    rather than letting the section silently disappear from the report."""
    return [
        "## Verdict — human-metric (suppressed)",
        "",
        "**No usable human reviews.** Completed verdicts exist but every one was",
        "excluded, so the human metric is not computed. Most often this means the",
        "corpus was rechunked since the reviews were scored (stale), or the review",
        "forms predate the panel-signature guard (unverifiable). Re-score against",
        "the regenerated `-results.md` panels and re-run `ingest_review.py`.",
        "",
        *_coverage_note(cov),
    ]


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


def _graded_verdict_section(summary: dict) -> list[str]:
    """Overall graded-relevance table. No pass/fail bars — these are
    diagnostic, the binary human-metric carries the bars."""
    o = summary["overall"]
    return [
        "## Verdict — human-metric (graded)",
        "",
        "Graded relevance: `correct`=1.0, `partial`=0.5, `wrong`=0.0.",
        "`strict success@5` counts a row a hit only on a `correct` in top-5;",
        "`partial-or-better success@5` also accepts a `partial`.",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| nDCG@5 | {o['ndcg_at_5']:.3f} |",
        f"| graded MRR | {o['graded_mrr']:.3f} |",
        f"| strict success@5 | {o['strict_success_at_5']:.3f} |",
        f"| partial-or-better success@5 | {o['partial_success_at_5']:.3f} |",
        "",
    ]


def _graded_breakdown_section(summary: dict) -> list[str]:
    """Per-corpus and per-type graded-metric tables."""
    header = "| nDCG@5 | gradedMRR | strict@5 | partial@5 |"
    sep = "| --- | --- | --- | --- |"
    fmt = lambda m: (
        f"{m['ndcg_at_5']:.3f} | {m['graded_mrr']:.3f} | "
        f"{m['strict_success_at_5']:.3f} | {m['partial_success_at_5']:.3f}"
    )
    lines = [
        "## Per corpus — human-metric (graded)",
        "",
        f"| corpus | n | {header[2:]}",
        f"| --- | --- | {sep[2:]}",
    ]
    for corpus_name, m in summary["by_corpus"].items():
        lines.append(f"| {corpus_name} | {m['n']} | {fmt(m)} |")
    lines += [
        "",
        "## Per query type — human-metric (graded)",
        "",
        f"| corpus | type | n | {header[2:]}",
        f"| --- | --- | --- | {sep[2:]}",
    ]
    for (corpus_name, type_), m in sorted(summary["by_type"].items()):
        lines.append(f"| {corpus_name} | {type_} | {m['n']} | {fmt(m)} |")
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
    human_coverage: dict | None = None,
    graded_summary: dict | None = None,
) -> None:
    """Dump a human-readable breakdown to evals/report.md.

    Pass either or both summary dicts. When both are present, the report
    shows them side-by-side and includes an auto-vs-human disagreement
    section. `human_coverage`, when given, is rendered as a scope note
    under the human-metric verdict (reviewed_n / coverage / excluded).
    `graded_summary`, when given, adds the graded-relevance verdict and
    breakdown tables; it shares the human-metric's reviewed-subset scope."""
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
        if human_coverage:
            lines += _coverage_note(human_coverage)
        if graded_summary:
            lines += _graded_verdict_section(graded_summary)
    elif human_coverage:
        lines += _human_suppressed_section(human_coverage)

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
    if graded_summary:
        lines += _graded_breakdown_section(graded_summary)

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


def _build_graded_summary(records: list[dict]) -> dict:
    """Same overall / per-corpus / per-type shape as _build_summary, but
    using the graded aggregator. Pass the reviewed subset."""
    return {
        "overall": aggregate_graded(records),
        "by_corpus": {
            c: aggregate_graded([r for r in records if r["corpus"] == c])
            for c in CORPUS_PATHS
        },
        "by_type": {
            (c, t): aggregate_graded([r for r in records if r["corpus"] == c and r["type"] == t])
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

    if args.metric in ("human", "both"):
        human_records, human_meta = load_human_review()
    else:
        human_records, human_meta = {}, {}
    if human_records:
        print(f"loaded {len(human_records)} usable human-review records", file=sys.stderr)
    elif args.metric in ("human", "both"):
        completed = human_meta.get("completed", 0)
        if completed:
            print(
                f"warning: {completed} completed review(s) exist but none are "
                f"usable ({human_meta.get('stale', 0)} stale, "
                f"{human_meta.get('unverifiable', 0)} unverifiable) — "
                f"human metric suppressed",
                file=sys.stderr,
            )
        else:
            print(f"warning: no human reviews available at {HUMAN_REVIEW_PATH}", file=sys.stderr)

    corpora = {name: load_corpus_state(path) for name, path in CORPUS_PATHS.items()}
    for name, s in corpora.items():
        print(f"loaded {name}: {len(s['chunks'])} chunks", file=sys.stderr)

    model = MiniLMEmbedder(MODEL_PATH, TOKENIZER_PATH)
    print("loaded embedder", file=sys.stderr)

    records = evaluate(rows, corpora, model, human_records=human_records)

    auto_summary = _build_summary(records, "first_rank") if args.metric in ("auto", "both") else None

    # The human-metric grades only the reviewed subset. Unreviewed rows
    # have human_first_rank=None; folding them into the denominator would
    # conflate "nobody reviewed this" with "retrieval missed it". Coverage
    # against the full golden set is reported separately, alongside the
    # count of incomplete forms the ingest dropped.
    human_summary = None
    human_coverage = None
    graded_summary = None
    # Build the coverage block whenever any review forms have been ingested
    # — even if none are usable — so a fully-stale/unverifiable corpus still
    # gets an explicit "metric suppressed, here's why" note rather than the
    # human section silently vanishing. The metric tables themselves are
    # built only when there's a usable subset to grade.
    if args.metric in ("human", "both") and (human_records or human_meta.get("completed")):
        reviewed_records = [r for r in records if r.get("human_available")]
        total_rows = len(records)
        reviewed_n = len(reviewed_records)
        human_coverage = {
            "reviewed_n": reviewed_n,
            "total_rows": total_rows,
            "coverage": reviewed_n / total_rows if total_rows else 0.0,
            "incomplete_excluded": human_meta.get("incomplete", 0),
            "stale_excluded": human_meta.get("stale", 0),
            "unverifiable_excluded": human_meta.get("unverifiable", 0),
        }
        if reviewed_records:
            human_summary = _build_summary(reviewed_records, "human_first_rank")
            graded_summary = _build_graded_summary(reviewed_records)
        print(
            f"human-metric scope: {reviewed_n}/{total_rows} rows usable "
            f"({human_coverage['coverage']:.1%} coverage); excluded "
            f"{human_coverage['incomplete_excluded']} incomplete, "
            f"{human_coverage['stale_excluded']} stale, "
            f"{human_coverage['unverifiable_excluded']} unverifiable",
            file=sys.stderr,
        )

    summary_out: dict = {}
    if auto_summary:
        summary_out["auto"] = _summary_for_json(auto_summary)
    if human_summary:
        human_out = _summary_for_json(human_summary)
        human_out["coverage"] = human_coverage
        summary_out["human"] = human_out
    elif human_coverage:
        # completed reviews exist but none usable — emit coverage + suppressed flag
        summary_out["human"] = {"suppressed": True, "coverage": human_coverage}
    if graded_summary:
        summary_out["human_graded"] = _summary_for_json(graded_summary)
    print(json.dumps(summary_out, indent=2))

    write_report(records, auto_summary, human_summary, human_coverage, graded_summary)
    print(f"wrote {REPORT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    write_audit(records)
    print(f"wrote {AUDIT_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
