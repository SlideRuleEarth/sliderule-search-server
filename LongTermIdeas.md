# Long Term Ideas

> **Work in progress — captured 2026-04-24.**
> Candidate levers for improving retrieval quality on the search server,
> not a committed roadmap. If this project graduates past proof-of-concept,
> this document is the starting point for picking what to actually ship.
> File and line references are current as of the capture date; re-verify
> before acting on any of them.

## Context

The search server is a Lambda-backed semantic + lexical retrieval service
over two corpora:

- **SlideRule docs** (docs.slideruleearth.io) — ~1,465 chunks, served via
  the `sliderule-docsearch` skill.
- **NSIDC + ORNL DAAC reference PDFs** (ICESat-2 + GEDI user guides and
  ATBDs) — ~1,757 chunks, served via the `nsidc-reference` skill.

Retrieval today: embed query with `all-MiniLM-L6-v2` (384d, ONNX), compute
cosine against a pre-embedded corpus, compute IDF-weighted lexical overlap
in parallel, fuse with RRF (k=60). Category filtering applied pre-ranking.
No reranker. No per-query logging. No offline eval harness.

Levers are grouped by cost to apply. Tier 4 is listed last because
it's the one most teams underinvest in — but it's effectively the
prerequisite for responsibly tuning anything in Tiers 1-3.

---

## Tier 1 — Config tweaks (redeploy, no corpus rebuild)

Each of these is a constant or a short block of code. Effort per item is
minutes to hours. Composable.

- **RRF_K tuning** — hardcoded at 60 in [server/ranking.py:42] from the
  original Cormack 2009 paper. Lower → top ranks matter more; higher →
  smoother mixing. Worth sweeping {10, 30, 60, 100} against a harness.
- **RRF weighting (α·sem + β·lex)** — today implicit 1:1 in
  [server/ranking.py:121-131]. Exposing α/β lets you tilt toward lexical
  for identifier-heavy queries or toward semantic for conceptual queries.
- **Stopwords / tokenizer** — [server/ranking.py:36,45-51]: 31 generic
  stopwords + `[a-z0-9_]+` regex + drop length-1 tokens. Domain-aware
  stopwords (e.g. "sliderule", "icesat", "icesat-2" in the SlideRule
  corpus) would raise signal-to-noise.
- **Score floor / min cosine** — none today. A minimum cosine cutoff
  would suppress the "top score 0.22, citation irrelevant" failure mode
  without forcing retries.
- **`disable_lexical` auto-heuristic** — today always fused unless the
  caller opts out. A simple heuristic (query contains `_` or a digit →
  keep lexical; pure English prose → semantic-only) may reduce noise.
- **`max_length=256` vs `CHUNK_CHAR_CAP=1500` mismatch** —
  [server/embedder.py:41,70] truncates at 256 tokens, but
  [tools/build_docsearch_corpus.py:30] and
  [tools/build_nsidc_corpus.py:67] emit 1,500-char chunks that routinely
  exceed 256 tokens at embed time. Either shrink chunks (Tier 3) or
  move to a long-context embedder (Tier 3) — Tier 1 version is to
  explicitly log or fail when truncation occurs so the silent loss
  becomes visible.

## Tier 2 — Small code changes (server-side, no corpus rebuild)

Each of these is a focused PR. Effort per item is hours to a day.

- **Real BM25 instead of IDF overlap** — today's "lexical" in
  [server/ranking.py:106-112] is IDF-weighted token overlap, not BM25.
  Adding doc-length normalization + k1/b parameters is small, well-trodden,
  and usually a 10-20% MRR lift on short queries.
- **Exact-identifier boost** — `atl03` and `atl03x` both get whatever IDF
  weight happens to land. A "query token exactly matches a chunk's
  identifier set" bonus removes the near-miss failure mode. (The
  identifier set itself is Tier 3 — build it at index time.)
- **Cross-encoder reranker on top-20** — e.g. `ms-marco-MiniLM-L-6-v2`,
  ~80 MB. Adds ~50 ms latency. At ~1,500-1,800 chunks total, reranking
  the top-20 is typically the single biggest quality lever at this
  corpus size.
- **Query expansion / HyDE** — Claude synthesizes a hypothetical answer,
  embed that, fuse with the original query embedding. Works well for
  conceptual queries where the user's phrasing doesn't match doc
  phrasing.
- **Domain synonym map** — hand-authored list (`atl03 ≡ atl-03`,
  `yapc ≡ photon classifier`, `x-series ≡ atl03x/atl06x/...`). Tiny
  file, real gain on realistic paraphrasing.
- **Heuristic category auto-filter** — classify query intent and
  auto-set `categories`. "When did X change" → `release_notes`;
  "how do I..." → `user_guide,api_reference,tutorial`. Today the
  caller must pick categories manually.
- **MMR / diversity in top-K** — [server/ranking.py:169-216] picks
  top-K purely by fused rank. If 3 top hits come from the same page,
  users see redundancy. Maximal Marginal Relevance against the top-10
  is ~20 lines.
- **`source_product` filter on nsidc** — [server/app.py:263-275]
  filters by category only. Accepting `source_product=ATL06` is a
  one-line addition that directly prevents cross-product contamination.
- **Title vs body lexical boost** — [server/app.py:117] folds
  `section` into lexical tokens with equal weight. A title-match
  multiplier is trivial and usually a free win.

## Tier 3 — Corpus rebuild required

Each of these requires re-embedding the corpus. Effort per item is
hours to days; iteration is slower because each A/B requires a rebuild.

- **Embedder swap** — [server/embedder.py:37] pins MiniLM-L6 (384d).
  `bge-small-en-v1.5` is a drop-in 384d replacement (~130 MB),
  materially better on technical text. `gte-base-en-v1.5` (768d,
  8,192-token context) eliminates the silent 256-token truncation.
- **Chunk overlap** — [tools/build_docsearch_corpus.py:307-332] and
  [tools/build_nsidc_corpus.py:243-281] produce chunks with zero
  overlap. 15-20% overlap recovers cross-boundary answers (common in
  PDFs where a definition ends one page and usage begins on the next).
- **Chunk size** — `CHUNK_CHAR_CAP=1500` is aggressive for MiniLM.
  600-900 chars with overlap is the current RAG consensus for small
  corpora: more chunks, each denser in signal.
- **Per-chunk `identifiers` array** — extract identifiers from
  headings, code spans, parameter tables, ATBD variable names. Feeds
  the Tier-2 exact-match boost and enables an identifier-only search
  mode.
- **`last_modified` on docsearch chunks** — allows recency weighting in
  fusion. Currently a stale tutorial can't be deprioritized.
- **SPLADE / learned-sparse retrieval** — lives between BM25 and dense;
  strong for identifier-heavy corpora like these. Bigger bet than BM25,
  smaller than a full embedder swap.
- **int8 embedding quantization** — frees Lambda memory so a bigger
  embedder model fits in the existing image size budget. Not a
  quality lever directly, but unlocks one.

## Tier 4 — Observability & process (the real bottleneck)

Tier 4 is the prerequisite for responsibly tuning anything above.
Without it, every Tier 1-3 change is a gut-feel decision.

### Per-query logging

Today: zero per-request logging. The `docsearch` logger at
[server/app.py:42] only captures cold-start events
[server/app.py:140-170].

What to capture per request (as structured JSON):
- timestamp, corpus, raw query, top_k, categories filter, disable_lexical
- latency breakdown: embed ms, rank ms, total ms
- top-K returned: chunk_id, url, cosine score, fused rank, matched_tokens
- cache hit/miss
- `corpus_sha256` at query time — ties results to a specific corpus version

Where: CloudWatch Logs is already wired. Pipe to Kinesis Firehose → S3
→ Athena if volume grows.

Privacy: queries will contain a long tail of whatever users type.
Decide retention (30-90 days) up front.

Effort: ~0.5 day.

### Golden set

Needed: a list of `(query, expected_correct_url(s))` pairs. Three sources,
combined:

1. **Author rubrics** (synthetic, ~15 examples). Each has a query + expected
   behavior; convert "must cite URL X" criteria into retrieval ground truth.
2. **Sampled real traffic** (after logging is on). Pick ~100 queries from
   logs; annotate by hand (~3-4 hrs). Catches failure modes you didn't
   imagine.
3. **LLM-generated + human-verified**. Pull random chunks; Claude writes
   the question each chunk answers. Fast but suffers "teach to the test"
   bias.

The golden set **grows** — every production retrieval failure gets added
with its expected answer. Over months it becomes a regression suite.

### Metrics

Retrieval:
- **Recall@K** (K=5, K=10) — is the right answer anywhere in top K?
- **MRR** — 1/rank of first correct answer. Penalizes "correct but
  ranked 8th."
- **hit@1** — top result correct? Strictest; useful for identifier queries.
- **nDCG@K** — if you grade relevance (1=exact, 0.5=related, 0=wrong).

Watch over time:
- Top-line MRR — one number; must go up or stay flat, or revert.
- **Per-category MRR** — catches "swap helped `release_notes`, hurt
  `user_guide`".
- **Per-query-type MRR** — identifier vs conceptual vs default-value.
  Different levers move different buckets; aggregates hide that.

Latency falls out of CloudWatch for free: p50/p95/p99, cold-start rate,
cache hit rate.

### Harness

Script at `tools/eval_retrieval.py`:
- Input: `golden_set.jsonl`, one line per query.
- For each query, call `ranking.rank()` directly against a locally-loaded
  corpus (no Lambda round-trip).
- Output: JSON report + human-readable markdown per-query breakdown.
- 300 queries × ~50 ms ≈ 15 seconds per full run.

Run in CI on every PR touching `server/` or `tools/`. Regression budget:
MRR can't drop more than X%.

Periodic online variant calls the deployed Lambda end-to-end to confirm
the deployed binary matches offline behavior.

Effort: ~1 day.

### Feedback loop

Once logging + harness exist, close the loop. Today the skill has no
way to tell the server "this result was useful." Add a tiny endpoint:

```
POST /feedback
{ query_id, cited_urls, outcome }
```

Each skill calls it after rendering an answer. Millions of implicit
relevance labels accrue automatically. Queries where the cited URL wasn't
in top-5 are retrieval bugs; queries re-asked with rewording are probable
first-retrieval misses. Both feed the golden set automatically.

Effort: ~0.5 day. Multiplies the value of logging.

### Rebuild cadence

[Makefile:67-71] is manual. Docs drift silently.

- **Scheduled** (weekly): EventBridge → Lambda → corpus build → ECR
  push → Lambda deploy. Simple, no docs-change awareness.
- **On-change**: fetch docs-site sitemap hash; rebuild if changed. More
  moving parts, feels better.

Start scheduled; upgrade if drift becomes a problem.

Effort: ~0.5 day.

### Provisioned concurrency (latency, not quality)

Documented 3-5 s cold start; clients carry a 60 s timeout to absorb
it. Provisioned concurrency eliminates cold starts at the cost of idle
burn. Measure usage patterns before committing.

### Tier 4 total effort

| Piece | Rough effort |
| --- | --- |
| Per-query structured logging | 0.5 day |
| Golden set v1 (from rubrics) | 0.25 day |
| `tools/eval_retrieval.py` + CI | 1 day |
| Scheduled rebuild | 0.5 day |
| Golden set v2 (annotated traffic) | 0.5 day (after ~1 week of logging) |
| `/feedback` endpoint | 0.5 day |
| **Total** | **~2-3 days** |

After this, every other lever becomes a PR with a before/after number
attached.

---

## Where to start

Sequencing — because pulling levers in parallel without measurement means
you can't attribute wins to causes:

1. **Tier 4 foundation first.** Instrument before tuning. Without logging
   + harness, every Tier 1-3 change is vibes.
2. **One structural baseline change early.** Embedder swap (MiniLM →
   bge-small). Otherwise you tune RRF_K / stopwords / BM25 on top of a
   weak embedder and have to redo it all when you upgrade.
3. **Then the cheap Tier 1-2 bundle, one at a time, measured.** BM25,
   exact-ID boost, score floor, RRF weighting, synonym map, category
   auto-filter, cross-encoder reranker. Each is a PR. Each gets scored
   against the harness. Keep what moves recall@5 or MRR; revert what
   doesn't.
4. **Revisit chunking only after the cheap stuff plateaus.** Overlap +
   smaller chunks + `identifiers` array. Bigger lift in theory but
   expensive to A/B because every iteration is a full rebuild.

## What this document is not

- **Not a roadmap.** No prioritization beyond the sequencing note above.
- **Not a spec.** No acceptance criteria, no API designs.
- **Not a design doc.** SKILL.md files and server source remain the
  authoritative description of current behavior.
- **Not exhaustive.** Flagged WIP so future additions don't feel like
  they're violating a completed document.
