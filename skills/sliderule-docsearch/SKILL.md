---
name: sliderule-docsearch
description: Semantic search over the SlideRule Earth documentation (docs.slideruleearth.io). Use this skill whenever the user asks about SlideRule concepts, parameters, APIs, data products, configuration options, Python client usage, endpoints, examples, or any 'how do I...' question about SlideRule. Retrieval is cosine similarity between the query embedding and pre-computed chunk embeddings from a static corpus hosted at search.testsliderule.org. First invocation downloads the all-MiniLM-L6-v2 sentence-transformer model (~80 MB) from HuggingFace.
---

# sliderule-docsearch

Semantic search over the SlideRule Earth documentation at
[docs.slideruleearth.io](https://docs.slideruleearth.io/).

## Architecture

- A pre-computed corpus of documentation chunks and their embeddings is
  hosted as static JSON at
  `https://search.testsliderule.org/docsearch/corpus.json`, with a
  small companion `meta.json` at the same base.
- At query time the skill fetches `meta.json` (tiny, ~300 bytes) on
  every invocation, then reuses its local corpus cache as long as
  `meta.json`'s `corpus_sha256` matches what's already cached. A new
  release flips the sha, and the skill transparently downloads the
  fresh corpus — cache invalidation is immediate, not a 24-hour lag.
- The skill embeds the user's query with the same sentence-transformer
  model (`sentence-transformers/all-MiniLM-L6-v2`), scores all chunks
  with a single cosine-similarity matmul, and fuses that ranking with
  an IDF-weighted lexical-overlap ranking via reciprocal rank fusion
  (RRF). The fusion rescues queries where the user's intent hinges on
  a specific identifier — e.g. `"atl03x"` vs `"atl03"` — that pure
  semantic similarity can't reliably distinguish.
- No Anthropic API calls. No server-side compute. Retrieval runs
  locally in pure Python.

## Invocation

```bash
python scripts/search.py "<query>" [--top-k 5]
```

Flags:

- `--top-k N` — number of results to return (default 5).
- `--corpus-url URL` — override the default corpus URL.
- `--meta-url URL` — override the default meta URL.
- `--corpus-file PATH` — read corpus from a local file instead of
  fetching (useful for local testing before the server is up).
- `--force-refresh` — re-download the corpus even if a cached copy
  exists for the current sha256.
- `--disable-lexical` — skip the lexical rank-fusion step; results
  become pure cosine similarity. Mainly for A/B comparison.
- `--repl` — drop into an interactive search loop instead of
  one-shot. Loads the embedder once (~3s) and then processes
  queries from stdin until Ctrl-D. Inside the REPL: `:k N` changes
  top-k, `:lex on|off` toggles fusion, `:help` lists commands. For
  local iteration, `make freeplay` is the canonical entry point.

The environment variable `SLIDERULE_SEARCH_BASE` (if set) selects a
different base URL — the skill appends `/docsearch/corpus.json` and
`/docsearch/meta.json`.

The local cache lives under `$TMPDIR/sliderule_docsearch/` as
`corpus_<sha256>.json`, one file per distinct corpus version.

## Output

The skill prints JSON to stdout:

```json
{
  "query": "what is the X-Series API",
  "results": [
    {
      "score": 0.742,
      "url": "https://docs.slideruleearth.io/...",
      "title": "X-Series APIs",
      "section": "Overview",
      "text": "...",
      "matched_tokens": ["atl03x"]
    }
  ],
  "corpus_meta": {
    "chunk_count": 1465,
    "embedder": "sentence-transformers/all-MiniLM-L6-v2",
    "embedding_dim": 384,
    "built_at": "2026-04-17T14:23:11Z",
    "corpus_sha256": "d69ac48ec5184c985f6c30760e953c124cc964e2f2eb9761096eede4db7f03b6",
    "pages_crawled": 133,
    "source_host": "docs.slideruleearth.io"
  }
}
```

## Agent instructions

1. Invoke `python scripts/search.py "<user's question>"` with a concise,
   information-rich query. If the user asked a verbose question, trim it
   to the key nouns and concepts — this typically lifts retrieval
   quality.
2. Parse the JSON response. Each `results[i]` has a `score` (cosine
   similarity, higher is better), `url`, `title`, `section`, and `text`.
   When present, `matched_tokens` lists which of the user's query tokens
   appeared literally in the chunk — a useful signal for confirming
   that an identifier-heavy query (e.g. `"atl03x"`) hit the right
   variant. Note: ranking reflects RRF-fused semantic + lexical scores,
   so `score` (which is cosine only) doesn't always monotonically
   decrease down the list.
3. Synthesize an answer from the top results. Cite the specific URLs
   you used — users rely on those links to go read the authoritative
   docs themselves.
4. If the top `score` is low (< 0.3) or the results look off-topic,
   tell the user the docs don't seem to cover their question and
   suggest rephrasing or pointing them at a specific doc section.

## First-run cost

The first invocation downloads the ~80 MB `all-MiniLM-L6-v2` model from
HuggingFace and caches it under `~/.cache/huggingface/`. Subsequent
invocations are fast and offline-capable for the embedding step (the
corpus fetch still needs the network unless `--corpus-file` is used).

## Not covered

For authoritative ICESat-2 / GEDI science (photon classification,
algorithm details, HDF5 structure, quality flags), use the
`nsidc-reference` skill instead — that's sourced from NSIDC user guides
and ATBDs rather than SlideRule's own docs.
