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
The corpus is locked at a `docs.testsliderule.org` snapshot.

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
- [evals/golden_set.jsonl](golden_set.jsonl) — 68 queries (35 docsearch,
  33 nsidc) with `expected_urls` and optional `expected_sections` /
  `expected_pages` for narrowing. URLs use the canonical
  `https://docs.slideruleearth.io/...` host; harness path-matching
  ignores host so a `testsliderule.org`-hosted corpus still matches.
- [evals/human_review.json](human_review.json) — aggregated user
  verdicts. Currently sparse — only a few rows complete.
- [evals/review/](review/) — 68 per-row markdown form files
  (results + review pairs). The `*-review.md` files are the hand-filled
  scoresheets. The `*-results.md` files are auto-regenerated and show
  what an agent actually sees.

### Analysis docs
- [evals/diagnosis.md](diagnosis.md) — current metric state,
  per-bucket breakdown, recommendation for the first lever.
- [LongTermIdeas.md](../LongTermIdeas.md) — full Tier 1-4 lever
  catalog with file/line references.

## Current state

### Corpus (as of last commit)
- **docsearch**: built from `docs.testsliderule.org` (a frozen mirror
  of the live docs). 754 chunks across 92 pages. Locked — will not
  change unless we ask the developer to redeploy.
- **nsidc**: NASA + ORNL DAAC user guides and ATBDs. 1,757 chunks
  across 12 PDFs. Stable.

### Baseline numbers (auto-metric)
| | recall@5 | hit@1 | MRR |
| --- | --- | --- | --- |
| Overall (n=68) | 0.676 | 0.309 | 0.469 |
| docsearch (n=35) | 0.800 | 0.371 | 0.561 |
| nsidc (n=33) | 0.545 | 0.242 | 0.371 |

All three below bar. NSIDC is the weaker corpus; docsearch handles
identifier-style queries well but loses precision on multi-section
pages.

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
- Python 3.11+ in `.venv`. Install: `python -m venv .venv && .venv/bin/pip install -r tools/requirements.txt`.
- Re-export the embedder if `generated/shared/model.onnx` is missing:
  `.venv/bin/python tools/export_minilm_onnx.py`
- The corpus files are pre-built and committed; no network needed
  to run the harness.

### Common commands
```bash
# Re-chunk docsearch (default host = docs.slideruleearth.io live).
# Use DOCSEARCH_HOST to point elsewhere — currently testsliderule.org
# is the locked source.
DOCSEARCH_HOST=docs.testsliderule.org .venv/bin/python tools/build_docsearch_corpus.py

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

Rows flagged for re-review (after the testsliderule.org rebaseline):
- **Repurposed** (full re-review needed): rows 13, 14, 15, 16, 17, 25.
- **Drift-flagged** (top-5 changed, re-check existing verdicts):
  rows 2, 3, 4, 5, 6, 7, 23, 27, 30, 34, 38, 41, 48, 49, 53, 55, 56,
  57, 59. (Generated by the ad-hoc drift checker — see the rebaseline
  section in [diagnosis.md](diagnosis.md).)

Once all 68 rows have verdicts, run `tools/ingest_review.py` and
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

### testsliderule.org doesn't mirror everything
The locked snapshot is missing:
- All 7 `assets/*.html` example notebooks
- All 6 `user_guide/how_tos/*.html` pages
- 3 release-notes pages were renamed (paths don't match 4/20 docs)

Source notebooks for the missing examples ARE in
[SlideRuleEarth/sliderule-python](https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples)
but the docs build pipeline isn't currently rendering them onto
testsliderule.org. If we want them back in the corpus, the
developer needs to fix the build — we don't control that.

For the eval, we worked around it by repurposing 6 rows and
trimming `assets/*` URLs from 10 others. See the
"Current corpus baseline" section in [diagnosis.md](diagnosis.md).

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
