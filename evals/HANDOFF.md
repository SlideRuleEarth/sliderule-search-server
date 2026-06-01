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

**Current state**: all three auto-metrics below bar (see [diagnosis.md](diagnosis.md)
for the breakdown). A 100-query golden set + offline harness exists, with
both auto and human (+ graded) grading modes. The human-review tool's
forms are currently blank — they were reset for re-scoring (see the
2026-06-01 update below). The corpus is built from the live
`docs.slideruleearth.io` site as of the 2026-05-29 rebaseline (was a
frozen `docs.testsliderule.org` mirror before then).

The next concrete step is **Phase 2** — re-score the human reviews, then
start pulling levers (the harness work is done). See "What's next" below.

## Update 2026-06-01 — metric work landed; reviews reset for re-scoring

Merged in PR #41 (this is why Phase 2 Step 1 below is marked done):

- **`--metric=human` + graded metrics** are live in
  [tools/eval_retrieval.py](../tools/eval_retrieval.py). The human metric
  grades over *completed reviews only* (reviewed_n / coverage reported
  explicitly), plus a graded family — nDCG@5, graded MRR, strict
  success@5, partial-or-better success@5 (`correct`=1.0/`partial`=0.5/
  `wrong`=0.0).
- **Panel-staleness guard.** `generate_review.py` stamps a panel
  signature (hash of the panel's chunk identities) into both companion
  files; `ingest_review.py` flags each row `current` / `stale` (corpus
  rechunked since scoring) / `unverifiable` (pre-guard form). Only
  `current` rows count; stale/unverifiable are excluded so a rechunk can
  no longer silently re-paste old verdicts onto chunks the reviewer never
  saw. This replaces the old `*-results.pre-rebaseline.md` forensic
  approach described under "Drift after rebaseline".

**The immediate task is re-scoring.** The pre-rebaseline (April) verdicts
were all `unverifiable` against the live-docs corpus, so on 2026-06-01 the
review forms were reset (`generate_review.py --overwrite`): all 100
`*-review.md` are now **blank** and carry current panel signatures, so
once filled they ingest as `usable`. Re-score, then `ingest_review.py` +
`eval_retrieval.py` to bring the human + graded metrics back.

A helper to speed re-scoring (delete once re-scoring is done):
- [prior_verdicts_reference.md](prior_verdicts_reference.md) — your April
  verdicts shown next to the *current* panels, per rank, as a memory aid
  (not ground truth — rank slots shifted with the rechunk).

The raw April `*-review.md` forms are recoverable from git history at the
commit just before the reset (the blank-forms commit's parent), e.g.
`git show <parent>:evals/review/01-...-review.md`.

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
  verdicts, with each row tagged `usable` / `stale` / `unverifiable` by
  the panel-staleness guard. Currently all forms are blank (reset
  2026-06-01), so this holds no verdicts until re-scoring is done.
- [evals/review/](review/) — 100 per-row markdown form pairs. The
  `*-review.md` files are the hand-filled scoresheets (each carries a
  frozen panel signature); the `*-results.md` files are auto-regenerated,
  show what an agent actually sees, and carry the current panel signature.
  Ingest compares the two to detect stale verdicts.

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

Currently all 100 forms are blank — the pre-rebaseline verdicts were
reset on 2026-06-01 (see the update near the top) because they were
unverifiable against the live-docs corpus. Re-scoring is the immediate
task; use [prior_verdicts_reference.md](prior_verdicts_reference.md) as a
memory aid.

The verdict scale and how to fill these in is documented in the
header of any `*-review.md` file plus under "Verdict scale" below.

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

### Step 0: re-score the reviews (the immediate task)

All 100 `evals/review/*-review.md` forms are blank (reset 2026-06-01) and
carry current panel signatures, so once filled they ingest as `usable`.
Re-score all 100 — order doesn't matter, do them in any sequence. While
scoring, glance at [prior_verdicts_reference.md](prior_verdicts_reference.md)
for your April call on each row (a memory aid, not ground truth — the
rechunk shifted rank slots).

Once a batch has verdicts, run `tools/ingest_review.py` then
`tools/eval_retrieval.py` — the human + graded metrics come back scoped to
what you've completed. Proceed to Step 2 when coverage is adequate.

### Step 1: `--metric=human` mode — DONE (PR #41)

The harness now grades against `evals/human_review.json` verdicts
(`correct`/`partial`/`wrong`) in addition to the auto-labels, plus a
graded family (nDCG@5, graded MRR, strict/partial success@5), and the
panel-staleness guard. See the 2026-06-01 update near the top for details.
`tools/eval_retrieval.py --metric={auto,human,both}`.

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

### Drift after rebaseline — handled by the staleness guard
When the corpus is rechunked, per-result verdicts (tied to specific
chunks) can silently become invalid. This is now caught automatically:
`generate_review.py` stamps a panel signature into both companion files
and `ingest_review.py` flags any row whose form signature no longer
matches the regenerated `-results.md` as `stale`, excluding it from the
human metric. So a rechunk no longer corrupts the metric — it just drops
the affected rows until they're re-scored. (Overall verdict, routing, and
human truth are mostly chunk-independent, but the guard excludes the whole
row to be safe.) Re-score flagged rows, then re-ingest.

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
