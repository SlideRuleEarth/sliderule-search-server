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
  `https://search.testsliderule.org/docsearch/corpus.json` (built by the
  `sliderule-search-server` repo).
- At query time the skill fetches that corpus (cached locally for 24
  hours), embeds the user's query with the same sentence-transformer
  model (`sentence-transformers/all-MiniLM-L6-v2`), and returns the
  top-K chunks by cosine similarity.
- No Anthropic API calls. No server-side compute. Retrieval runs
  locally in pure Python.

## Invocation

```bash
python scripts/search.py "<query>" [--top-k 5]
```

Flags:

- `--top-k N` — number of results to return (default 5).
- `--corpus-url URL` — override the default corpus URL.
- `--corpus-file PATH` — read corpus from a local file instead of
  fetching (useful for local testing before the server is up).
- `--force-refresh` — bypass the 24-hour local cache.

The environment variable `SLIDERULE_SEARCH_BASE` (if set) selects a
different base URL — the skill appends `/docsearch/corpus.json`.

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
      "text": "..."
    }
  ],
  "corpus_meta": {
    "built_at": "2026-04-17T14:23:11Z",
    "chunk_count": 735,
    "embedder": "sentence-transformers/all-MiniLM-L6-v2"
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
