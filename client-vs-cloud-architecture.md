# Client-side search vs cloud service: feasibility & token analysis

## Context

The search server today is a Lambda + CloudFront service exposing
`POST /docsearch/search` and `/nsidc/search`. It embeds the query with
`all-MiniLM-L6-v2` (ONNX) and ranks precomputed corpus embeddings with a
cosine + IDF-lexical RRF fusion. The skills (`sliderule-docsearch`,
`nsidc-reference`) are thin HTTP wrappers.

The question: **could the search run client-side inside a skill instead
of in the cloud, and would that be more or less token-efficient?** This
document answers feasibility (across both Claude Code local and
claude.ai sandbox environments), settles the token question, designs
lighter-weight client-side variants, and gives a focused head-to-head of
the Claude Code local full-semantic path against the current cloud
service. It is an analysis/decision document — **no code changes are
proposed for implementation yet.**

## The headline answer on tokens

**Token usage is essentially identical between the two architectures, and
client-side trends slightly *worse*.** Tokens are the wrong axis to
optimize on.

Why: LLM token cost for a search is dominated by the **results returned
into context**. For `top_k=5`, each result carries up to ~1500 chars of
text (~375 tokens) plus url/title/section/score ≈ **2.5–3k tokens per
response**. That payload is *identical* in both designs, because same
model + same corpus + same ranking ⇒ same top_k. Neither design puts the
query embedding or the 2,511 corpus vectors into LLM context — those are
pure local/remote compute.

What differs (all small, all favoring the cloud):

| Token source | Cloud service | Client-side |
|---|---|---|
| Results payload (dominant) | ~2.5–3k | ~2.5–3k (identical) |
| Tool-invocation command | 1 Bash call (signed POST) | 1 Bash call (local rank script) |
| Skill instructions loaded | small | slightly larger (setup/deps logic) |
| Cold-start / model-load stderr | none (remote) | ONNX load warnings can leak |
| First-run `pip install` output | none | potentially large if not suppressed |
| Failure-mode debug loops | simple HTTP 429/503/timeout | larger surface: missing deps, platform/arch, model load |

**Conclusion: client-side offers no token savings, and its extra failure
surface and cold-start noise make it marginally more expensive in
tokens.** The genuine trade-offs are latency, packaging size,
dependency availability, freshness, and reliability — not tokens.

## Feasibility by environment

To run the full semantic pipeline client-side you must ship and execute
locally: `model.onnx` (86 MB) + `tokenizer.json` (696 KB) + corpus JSON
(`docsearch` 5.7 MB + `nsidc` 14 MB) ≈ **107 MB**, plus `onnxruntime` +
`tokenizers` + `numpy`. The actual per-query compute is trivial (embed
one query + dot product over 2,511 vectors ≈ 30–70 ms once the model is
loaded); the cost is the **~3 s model cold-start** and the dependency
footprint.

- **Claude Code local — feasible.** Full Python, can `pip install
  onnxruntime numpy tokenizers`, persistent filesystem so the ~107 MB
  bundle and pip cache survive across a session. Model cold-start (~3 s)
  recurs per fresh process unless the script is structured to stay warm.
  This is the only environment where the full ONNX path is comfortable.

- **claude.ai web sandbox — likely NOT feasible for the ONNX path.**
  `onnxruntime` is a ~50 MB native wheel and `tokenizers` is Rust-backed;
  availability/installability in the sandbox is the blocker, plus
  ephemeral storage makes the 107 MB bundle and 3 s cold-start recur
  every invocation. This environment is what breaks the full client-side
  approach — and is exactly why the cloud service exists.

There's a structural reason you can't avoid shipping the model: queries
are arbitrary, so the query vector must be computed at request time — you
cannot precompute it. The 86 MB transformer forward pass is unavoidable
for the semantic half unless you change the retrieval method.

## Lighter client-side variants (design)

### Variant A — Pure-lexical client-side (no model, no onnxruntime)
Drop the semantic half entirely and run only the existing IDF-weighted
token-overlap ranking (`server/ranking.py` `lexical_signals`, lines
80–118) over the corpus *text* — no embeddings needed.
- **Ship:** corpus text only (strip the `embedding` arrays → corpus JSON
  shrinks dramatically, ~107 MB → a few MB).
- **Deps:** pure Python + stdlib (no onnxruntime, no numpy required).
- **Feasibility:** works in *both* environments, including the sandbox.
- **Cost:** retrieval quality drops — the eval shows hybrid matters
  (overall recall@5 0.676; lexical-only would regress, worst on `nsidc`
  where semantic recall carries more). Good for a fallback or a
  "keyword-ish" fast path, not a full replacement.

### Variant B — Remote query-embedding + local rank
Call a hosted embedding endpoint for *only the query vector* (tiny
request/response, ~1 KB) and do cosine + RRF locally over shipped corpus
embeddings.
- **Ship:** corpus + embeddings (~20 MB), no 86 MB model.
- **Deps:** numpy only; no onnxruntime.
- **Feasibility:** both environments, if outbound HTTP is allowed.
- **Cost:** still a network dependency (defeats much of the "no cloud"
  motivation) and adds an embedding-API contract; but removes the 86 MB
  model and the onnxruntime/arch headaches. Token cost unchanged.

### Variant C — Full ONNX client-side, Claude Code local only
The literal "run the whole service in the skill" option. Bundle all
~107 MB, `pip install` deps on first run, reuse `server/embedder.py` +
`server/ranking.py` as a local library invoked by a helper script.
- **Feasibility:** Claude Code local only; not the sandbox.
- **Cost:** largest bundle, 3 s cold-start, biggest dependency/failure
  surface, slightly higher tokens (cold-start + install noise). Highest
  fidelity (bit-identical to cloud) but the worst packaging story.

### Recommendation
Keep the cloud service as the primary path. **Tokens do not justify a
client-side move.** If a client-side capability is still wanted, the
most defensible is **Variant A (pure-lexical) as an offline/fallback
mode** plus a clean fallback-to-cloud, because it is the only option that
works in *both* target environments and adds near-zero dependency
weight — accepting the quality regression as the explicit trade.

## Reuse — existing code that a client-side variant would build on
- `server/embedder.py` `MiniLMEmbedder` — query embedding (Variant C).
- `server/ranking.py` — `tokenize`, `lexical_signals`, `fuse_rrf`,
  `rank`. Variant A uses `lexical_signals` only; Variant B/C use all.
- Corpus format produced by `tools/build_docsearch_corpus.py` /
  `tools/build_nsidc_corpus.py` (`generated/*/corpus.json`) — a
  lexical-only build would emit the same schema minus `embedding`.
- The skills already exist as HTTP wrappers — a client-side mode is an
  alternate branch in the same skill, not a new skill.

## Focused head-to-head: Claude Code local (full semantic) vs cloud

Scope: ignore the claude.ai sandbox. Compare **the current cloud service**
against **Variant C — full semantic search running inside a Claude Code
skill** (full 86 MB ONNX model + full corpus + identical RRF ranking).

**Decisive fact:** the model files (`model.onnx`, `tokenizer.json`) are
committed byte-for-byte and the corpus + ranking are identical, so the
two produce **bit-for-bit identical results**. There is zero
retrieval-quality difference. The comparison is entirely about latency,
distribution, freshness, dependencies, and ops — never quality, never
meaningfully tokens.

| Dimension | Cloud service (current) | Claude Code local, full semantic (Variant C) |
|---|---|---|
| Retrieval quality | baseline | identical (same committed model + corpus + RRF) |
| Tokens (steady state) | ~2.5–3k/response | identical — same top_k payload |
| Tokens (overhead) | none | slight: cold-start warnings, first-run `pip install` logs can leak |
| Warm latency | ~30–70 ms compute + network RTT ≈ 150–400 ms; cached 1–5 ms | ~30–70 ms, no network — *if the process stays warm* |
| Cold latency | ~4.5 s Lambda cold start (kept warm by EventBridge) | ~3–4 s model load per fresh Python process; + tens of seconds first-ever `pip install` |
| Latency catch | warm-keeping solved centrally | a skill spawning fresh Python per query reloads the 86 MB model every time (~3–4 s/query) unless a persistent local daemon is run — which re-implements the cloud service locally |
| Distribution | skill = tiny HTTP wrapper (KBs) | skill bundle balloons to ~107 MB, downloaded by every user |
| Freshness | one image push → all clients instantly current | corpus frozen at skill-install time; update = re-ship 107 MB to every client (reintroduces staleness the cloud design avoids) |
| Dependency fragility | x86_64 Lambda chosen to dodge onnxruntime arm64 cpuinfo regression | most Claude Code users are on Apple Silicon (arm64) — macOS arm64 wheels generally work but are a real fragility/support vector |
| Failure surface | HTTP 429/503/timeout, network down | dep install fail, model load fail, platform/arch mismatch, disk space |
| Offline / privacy | requires network; query hits your AWS | works offline; query never leaves the machine |
| Ops / cost | terraform + ECR + Lambda + CloudFront + SigV4 + warmup (real ops, small $) | no server infra, no per-call cost; but you own version-skew + distribution |

**The trade, stated plainly:** moving full semantic search into a Claude
Code skill buys **offline operation, no server infra, and no network
round-trip** — at the cost of a **~107 MB per-client bundle, reintroduced
corpus staleness, an arm64 dependency-fragility risk, and a latency
cliff** (model reloads per process unless you stand up a warm local
daemon, which rebuilds the very service you were deleting). It is **not a
token play** (tokens are identical); it is an *offline + no-infra* play
vs a *fresh + zero-client-footprint + centrally-operated* play. Given the
corpus is meant to be updated centrally and most local users are on
Apple Silicon, the cloud service remains the stronger default; the
local-full path wins only if **offline use or eliminating AWS infra**
becomes a hard requirement.

## Verification (if a prototype is later pursued)
This document is analysis only. Should a prototype be greenlit, the way
to turn the token estimates into measured numbers:
1. Build a lexical-only corpus (Variant A) by stripping `embedding`
   arrays from `generated/*/corpus.json`; confirm size + that
   `lexical_signals` ranks without numpy.
2. Run the existing eval harness (`tools/eval_retrieval.py`) with a
   `disable_lexical`-analogous "lexical-only" config to quantify the
   recall@5 / hit@1 / MRR regression vs the current hybrid baseline.
3. For token measurement: run the same 5–10 golden queries through (a)
   the cloud endpoint and (b) a local script, and compare actual context
   tokens consumed per query — expect parity on the results payload and a
   small client-side overhead on first run.
