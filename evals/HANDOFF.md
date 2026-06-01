# Retrieval-quality POC handoff

> Read this first. It tells you where the work is, how to resume, and
> what to do next. Files referenced here are repo-relative.

## TL;DR

This repo runs a Lambda that does semantic+lexical retrieval over two
corpora: the SlideRule docs (`docsearch`) and the NASA/ORNL data
product references (`nsidc`). We're running a proof-of-concept
**offline retrieval-quality eval** to decide whether the current
ranker is good enough to ship behind agent skills, and if not, which
levers to pull.

The POC gates on three metrics:

| Metric | Bar |
| --- | --- |
| recall@5 | ≥ 0.70 |
| hit@1 | ≥ 0.50 |
| MRR | ≥ 0.55 |

**Current state**: all three metrics below bar (see [diagnosis.md](diagnosis.md)
for the breakdown). A 68-query golden set + offline harness exists. A
human-review tool exists and a small subset of reviews is filled in.
The corpus is built from the live `docs.slideruleearth.io` site as of
the 2026-05-29 rebaseline (was a frozen `docs.testsliderule.org` mirror
before then).

The next concrete step is **Phase 2** — finish the human reviews,
then add a `--metric=human` mode to the harness, then start pulling
levers. See "What's next" below.

## What exists today

### Code
- [tools/build_docsearch_corpus.py](../tools/build_docsearch_corpus.py)
  — crawls a docs site, chunks, embeds, writes
  `generated/docsearch/corpus.json` + `meta.json`. Reads `DOCSEARCH_HOST`
  env var (defaults to `docs.slideruleearth.io`).
- [tools/build_nsidc_corpus.py](../tools/build_nsidc_corpus.py) —
  same idea for NASA/ORNL PDFs. Output to `generated/nsidc/`.
- [tools/eval_retrieval.py](../tools/eval_retrieval.py) — offline
  harness. Loads both corpora, runs each `golden_set.jsonl` query
  through `server.ranking.rank()`, computes hit@1 / recall@5 / MRR,
  writes [evals/report.md](report.md) and [evals/audit.md](audit.md).
  Path-only URL matching so the golden set's canonical
  `slideruleearth.io` URLs match a `testsliderule.org`-hosted corpus.
- [tools/generate_review.py](../tools/generate_review.py) — for each
  golden-set row, runs the query against BOTH corpora and writes
  `evals/review/<NN>-<slug>-results.md` (auto-managed, regenerated
  every run) plus `<NN>-<slug>-review.md` (editable form, preserved
  unless `--overwrite`).
- [tools/ingest_review.py](../tools/ingest_review.py) — reads filled
  `*-review.md` files, parses verdicts and human-truth fields, writes
  `evals/human_review.json`. Idempotent — re-run any time.

### Data
- [evals/golden_set.jsonl](golden_set.jsonl) — 100 queries (60 docsearch,
  40 nsidc) with `expected_urls` and optional `expected_sections` /
  `expected_pages` for narrowing. Even type mix: docsearch 10 each across
  identifier/conceptual/example/version_history/api_lookup/paraphrased;
  nsidc 8 each across algorithm/variable_lookup/product_disambiguation/
  cross_product/instrument. URLs use the canonical
  `https://docs.slideruleearth.io/...` host; harness path-matching
  ignores host so a `testsliderule.org`-hosted corpus still matches.
  Narrowing is calibrated to where the answer actually lives in the live
  corpus (real section headings for docsearch; page ranges for nsidc
  PDFs, whose chunk sections are unreliable "Page N"). Author/validate
  rows with [tools/gs_audit.py](../tools/gs_audit.py).
- [evals/human_review.json](human_review.json) — aggregated user
  verdicts. 67 rows carried over from the 68-row set; 33 new rows need
  review (see below).
- [evals/review/](review/) — 100 per-row markdown form files
  (results + review pairs). The `*-review.md` files are the hand-filled
  scoresheets. The `*-results.md` files are auto-regenerated and show
  what an agent actually sees.

### Analysis docs
- [evals/diagnosis.md](diagnosis.md) — current metric state,
  per-bucket breakdown, recommendation for the first lever.
- [LongTermIdeas.md](../LongTermIdeas.md) — full Tier 1-4 lever
  catalog with file/line references.

## Current state

### Corpus (as of the 2026-05-29 rebaseline)
- **docsearch**: built from the live `docs.slideruleearth.io` site.
  756 chunks across 94 pages. The builder skips `/_static/` (the
  Redoc-rendered OpenAPI spec HTML) — without that filter those
  auto-generated pages were ~40% of the crawl and swamped ranking; see
  the `SKIP_PATH_PREFIXES` comment in `tools/build_docsearch_corpus.py`.
  The live site updates weekly, so a fresh rebuild can move metrics.
- **nsidc**: NASA + ORNL DAAC user guides and ATBDs. 1,757 chunks
  across 12 PDFs. Stable.

### Baseline numbers (auto-metric, 100-row set)
| | recall@5 | hit@1 | MRR |
| --- | --- | --- | --- |
| Overall (n=100) | 0.780 | 0.390 | 0.544 |
| docsearch (n=60) | 0.767 | 0.433 | 0.577 |
| nsidc (n=40) | 0.800 | 0.325 | 0.495 |

recall@5 now clears its 0.70 bar; hit@1 (0.39, bar 0.50) and MRR (0.544,
bar 0.55) are close but below. These numbers are not comparable to the
old 68-row baseline (different, larger, recalibrated set). Weakest
buckets and the levers they point to:
- **version_history** (recall@5 0.50, hit@1 0.10) — semantic search can't
  pinpoint *which release* introduced a feature; release notes are
  repetitive. Wants category/recency signals or exact-version matching.
- **nsidc/algorithm** (hit@1 0.00) — right ATBD, wrong chapter at #1; the
  classic section-precision miss the cross-encoder reranker targets.
- **nsidc/variable_lookup** (hit@1 0.25) — short user guides under-surface.
docsearch identifier/example are strong (recall@5 1.0 / 0.80, hit@1
0.70 / 0.60).

### Human reviews
A human-review tool walks each query and presents the top-5 chunks
from BOTH corpora (cross-corpus visibility — a row labeled `docsearch`
might be better answered by `nsidc`). The user fills in:
- Per-result verdicts (`correct` / `partial` / `wrong`) for each chunk
- Overall verdict for the row (would an agent give a good answer?)
- Cross-corpus routing decision (is the labeled corpus right?)
- Human truth (only if the answer wasn't returned)

Currently filled in: ~5 pilot rows + some in-progress. Most rows
need re-checking after the rebaseline (see "Drift after rebaseline"
below).

The verdict scale and how to fill these in is documented in the
header of any `*-review.md` file plus in the plan history (search
this file for "Verdict scale").

## How to run

### Environment
- Python 3.13 in `.venv` (pinned via `.python-version`). Install: `uv venv && uv pip sync requirements-dev.lock`. See [README.md](../README.md#dev-environment) for full setup.
- Re-export the embedder if `generated/shared/model.onnx` is missing:
  `.venv/bin/python tools/export_minilm_onnx.py`
- The corpus files are pre-built and committed; no network needed
  to run the harness.

### Common commands
```bash
# Re-chunk docsearch from the live site (default host). Prefer the
# Makefile target — it runs in the x86_64 builder so embeddings match
# the Lambda arch. Set DOCSEARCH_HOST=docs.testsliderule.org only to
# target the frozen mirror instead of live.
make rebuild-corpus-docsearch

# Run the offline harness (writes report.md + audit.md, also prints JSON to stdout)
.venv/bin/python tools/eval_retrieval.py

# (Re)generate review form pairs for all rows
.venv/bin/python tools/generate_review.py

# Generate just the first N (pilot mode)
.venv/bin/python tools/generate_review.py --limit 5

# Reset preserved -review.md files (DANGEROUS — wipes filled-in verdicts)
.venv/bin/python tools/generate_review.py --overwrite

# Aggregate filled-in reviews into human_review.json
.venv/bin/python tools/ingest_review.py
```

## What's next — the Phase 2 plan

### Step 0: finish reviews (in flight)

Reviews are filled in at `evals/review/*-review.md`. Most rows still
need verdicts. Order doesn't matter; do them in any sequence.

Rows needing review (after the live-docs rebaseline + expansion to 100):
- **New rows (33)**: rows 69-100 (the +25 docsearch / +7 nsidc additions)
  plus row 40 (query re-pointed to the ATL03 ATBD output table) have blank
  `-review.md` forms — fill these in.
- **Carried over (67)**: verdicts preserved from the 68-row set. Because
  the corpus was re-chunked from live docs, top-5 for many rows shifted;
  re-check the carried-over verdicts as you go (verdicts are chunk-keyed,
  so they travel with the chunk, but new chunks won't have one).

Once all 100 rows have verdicts, run `tools/ingest_review.py` and
proceed to Step 1.

### Step 1: add `--metric=human` mode to the harness

Currently `tools/eval_retrieval.py` grades against `expected_urls` /
`expected_sections` in `golden_set.jsonl`. Add a parallel grading
path that reads per-result verdicts from `evals/human_review.json`:
- `correct` verdict on a returned chunk → counts as a hit.
- `partial` → 0.5 in MRR-style metrics.
- `wrong` or missing → not a hit.

CLI: `--metric=auto` (default, current behavior) vs `--metric=human`
(new). Both modes write into [evals/report.md](report.md) for side-by-side
comparison.

Effort: ~30-45 minutes. Touch `evaluate()`, `aggregate()`,
`write_report()` in `tools/eval_retrieval.py`.

### Step 2: apply routing decisions

For rows where the user marked `redirect-to-docsearch` /
`redirect-to-nsidc` / `both-corpora` in their review, update the
golden set's `corpus` field accordingly. Recommendation: duplicate
rows for `both-corpora` rather than introducing a `corpus: both`
sentinel.

Write a small `tools/apply_human_routing.py` that reads
`human_review.json`, reads `golden_set.jsonl`, applies decisions,
writes `golden_set.jsonl.bak` + new `golden_set.jsonl`.

Effort: ~20 minutes.

### Step 3: reconcile auto vs human metrics

Run both metric modes. For each query where `auto` and `human`
disagree:
- **Auto says correct, human says wrong** → auto-label was too
  generous. Tighten `expected_sections` or remove an over-broad URL.
- **Auto says wrong, human says correct** → auto-label was too narrow.
  Add the chunk's URL or section to the golden-set row.

Update labels, re-run, repeat until agreement is high. The auto
metric should converge toward the human one.

Effort: 1-2 hours scanning + tweaks.

### Step 4: pull the first lever

From [diagnosis.md](diagnosis.md), the recommended first lever is a
**cross-encoder reranker on the top-20**. ms-marco-MiniLM-L-6-v2
or similar, ~80 MB ONNX-exported. After RRF fusion, rerank the top-20
with the cross-encoder, return the new top-K.

Run the harness against both metrics, append before/after to
[diagnosis.md](diagnosis.md). Keep the lever if it moves human-metric
hit@1 by ≥5 points; revert otherwise.

Effort: 1-2 days.

### Step 5: decide

If human-metric hit@1 ≥ 0.55 after the reranker, retrieval is
acceptable — move to architecture/load-test work (Option C in the
historical plan).

If hit@1 still well below 0.55, pull the next lever. Candidates from
[LongTermIdeas.md](../LongTermIdeas.md):
- `source_product` filter for nsidc (query mentions ATL08 → only ATL08 chunks)
- Category auto-filter for docsearch `version_history`
- Exact-identifier boost (`atl06p`, `cnf`, etc.)
- Synonym map (`cnf` ↔ `confidence`, `srt` ↔ `surface reference type`)

## Known gotchas

### The old `assets/*` and `user_guide/how_tos/*` pages are gone, not restored
The HANDOFF used to assume the live site still served the example
notebooks and how-to pages the testsliderule mirror lacked. It does not —
the live site 403s every `assets/*.html` and `user_guide/how_tos/*.html`
URL; that content was restructured into `user_guide/articles/*` (dated
articles) and the canonical endpoint docs now live in
`user_guide/icesat2.html` / `gedi.html`. The 2026-05-29 golden-set pass
recalibrated every affected row to its true live-docs location (verified
with `tools/gs_audit.py`) rather than pointing at pages that no longer
exist, so there is no longer a "degraded rows" backlog.

### nsidc PDF chunk sections are unreliable — narrow by page
Some nsidc PDFs extract real heading text (ATL03 ATBD, the user guides);
others are pure "Page N" (ATL06/ATL08 ATBDs, GEDI). So `expected_sections`
silently fails to match on the Page-N docs. For nsidc rows, narrow with
`expected_pages` (every chunk has `source_page`); reserve
`expected_sections` for docsearch, where headings are clean.

### Keep `/_static/` filtered
The live site renders the OpenAPI specs as HTML under
`/_static/openapi/*.html` (Redoc). Those are auto-generated,
keyword-dense API dumps — `sliderule.html` alone is ~320 chunks — and
without filtering they were ~40% of the crawl and swamped IDF-lexical
ranking (identifier recall@5 cratered 0.83 → 0.33 on a straight live
rebuild). `tools/build_docsearch_corpus.py` skips `/_static/` in
`SKIP_PATH_PREFIXES`; don't remove it. The testsliderule mirror never
served these pages, which is why the filter wasn't needed before.

### Drift after rebaseline
When the corpus changes, per-result verdicts (tied to specific chunks
at specific ranks) may become invalid. Overall verdict, routing, and
human truth are mostly chunk-independent and survive. The pre-
rebaseline snapshot of each `*-results.md` is in
`evals/review/*-results.pre-rebaseline.md` for forensic comparison;
delete those once Phase 2 step 1 is done.

### Don't run on both machines
Claude Code session JSONL is append-only. If you sync `~/.claude/`
between machines, never have Claude Code running on both at the
same time on the same session — file conflicts will look like
corrupted history.

### Determinism
Same corpus + same `golden_set.jsonl` + same code = identical
metrics every run. If you see the numbers move without changing
inputs, something stateful leaked in.

## Verdict scale (quick reference)

For each `r1..r5` line in each corpus panel of a `*-review.md`:

- **`correct`** — a user reading just this chunk gets what they asked
  for.
- **`partial`** — chunk is on-topic and helpful but doesn't fully
  answer.
- **`wrong`** — chunk is off-topic, unrelated, or actively misleading.

Score by content fit only. Do NOT mark a chunk `wrong` because it's
from the "other" corpus — corpus appropriateness lives in the
`routing` field.

Overall verdict is "would the agent give a good answer if handed
these 10 chunks?" — position-weighted (top-1/2 chunks dominate).

## Where to look for what

| Question | File |
| --- | --- |
| What's the goal? | This file (TL;DR) |
| Why are we below bar? Which lever first? | [diagnosis.md](diagnosis.md) |
| What's the lever catalog? | [LongTermIdeas.md](../LongTermIdeas.md) |
| What's the test set? | [golden_set.jsonl](golden_set.jsonl) |
| What did the human reviewer say? | [human_review.json](human_review.json) |
| What does the harness output look like? | [report.md](report.md) (auto), [audit.md](audit.md) (auto) |
| How is a chunk built / what fields does it have? | [tools/build_docsearch_corpus.py](../tools/build_docsearch_corpus.py) |
| How is a query ranked? | `server/ranking.py:rank()` |
| How does the server expose the endpoint? | [README.md](../README.md) |

## Resuming as a fresh Claude Code session

If you're picking this up cold:

1. `cd` into the repo, `git pull` the latest.
2. Read this file, then [diagnosis.md](diagnosis.md), then skim
   [LongTermIdeas.md](../LongTermIdeas.md).
3. Run the harness once to confirm your env reproduces the baseline
   numbers in this file: `.venv/bin/python tools/eval_retrieval.py`.
   If they don't match, something's drifted (corpus, code, embedder).
4. Pick up at "What's next" — most likely Step 0 (finish reviews) or
   Step 1 (`--metric=human`) depending on how much review work the
   previous person finished.
