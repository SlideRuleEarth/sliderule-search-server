---
name: sliderule-docsearch
description: Search the SlideRule Earth documentation. Use for questions about SlideRule APIs, parameters, data products, the Python client, configuration, examples, version history, or any "how do I..." or "what is..." question specific to SlideRule or its ICESat-2/GEDI endpoints (atl03p, atl06p, atl08p, atl13p, atl24p, gedil4ap, etc.). Use `nsidc-reference` instead for ICESat-2/GEDI science theory, ATBDs, photon-classification algorithms, or HDF5 structure.
---

# sliderule-docsearch

Semantic search over the SlideRule Earth documentation at
[docs.slideruleearth.io](https://docs.slideruleearth.io/).

## Architecture

Hosted semantic + lexical search. One HTTPS POST per query to a
Lambda behind CloudFront; there's no offline mode. All retrieval
(embedding with `all-MiniLM-L6-v2`, cosine scoring, IDF-weighted
lexical overlap, reciprocal rank fusion) runs server-side. The
skill client is a thin transport wrapper.

## Invocation

```bash
python scripts/search.py "<query>" [--top-k 5] [--disable-lexical] [--categories ...]
```

Flags:

- `--top-k N` — number of results to return (default 5, max 50).
- `--disable-lexical` — ask the server to skip lexical rank-fusion; results become pure cosine similarity. Mainly for A/B comparison — leave off for normal use.
- `--categories LIST` — comma-separated category allowlist (e.g. `user_guide,api_reference`). Filter is applied server-side **before** ranking, so `top_k` reflects the filtered universe.
- `--search-url URL` — full override of the search endpoint (for staging/dev).
- `--timeout SECONDS` — HTTP timeout (default 60). The server is a Lambda; a cold start adds ~3–5 s to the first request after a period of idleness, so the timeout is set higher than a typical HTTP default.

`SLIDERULE_SEARCH_BASE` env var picks a different base URL — the skill
appends `/docsearch/search`.

## Output

The skill prints JSON to stdout, byte-for-byte the server response:

```json
{
  "query": "what is the X-Series API",
  "results": [
    {
      "score": 0.742,
      "category": "user_guide",
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
    "corpus_sha256": "d69ac48ec5184c985f6c30760e953c124cc964e2f2eb9761096eede4db7f03b6",
    "built_at": "2026-04-17T14:23:11Z",
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

   **Example of trimming a verbose user question:**
   - User: *"how do I set up confidence filtering for photons when
     I'm using the atl03x endpoint, I can't figure out the parameter
     name"*
   - Good search query: `"atl03x confidence filtering parameters"`
   - The retrieval is cosine + IDF; concise technical nouns beat
     natural language.
2. Parse the JSON response. Each `results[i]` has a `score` (cosine
   similarity, higher is better), `url`, `title`, `section`, `category`,
   and `text`. When present, `matched_tokens` lists which of the user's
   query tokens appeared literally in the chunk. For identifier-heavy
   queries this is the **primary disambiguator** — verify the exact
   identifier appears in `matched_tokens` on the top result. If only
   a related variant matched (e.g. user asked about `atl03x` but the
   top hit only matched `atl03`), either re-run with a more specific
   query or flag the mismatch to the user rather than citing a
   near-miss as an answer. Note: ranking reflects RRF-fused semantic
   + lexical scores, so `score` (which is cosine only) doesn't always
   monotonically decrease down the list.

3. **Use `category` to weigh content types against the user's intent.**
   Each chunk is tagged by URL-derived content type:

   | category          | what it is                               | prioritize when the user's question is... |
   | ----------------- | ---------------------------------------- | ------------------------------------------ |
   | `user_guide`      | curated concept + usage pages            | conceptual, "how do I...", "what is..."    |
   | `api_reference`   | function signatures + parameter tables   | API/parameter lookups                       |
   | `background`      | theory, data product descriptions        | background science, data interpretation     |
   | `getting_started` | quickstarts, first-request examples      | onboarding questions                        |
   | `tutorial`        | rendered notebooks with worked examples  | "show me an example of X"                   |
   | `developer_guide` | architecture, internals, build process   | contributing, internals                     |
   | `release_notes`   | per-version changelogs + known issues    | **only** version-keyed: "when was X added", "did Y change", "known bug in v?" |

   `release_notes` chunks often score high on conceptual queries
   because they name-drop the concept while reporting historical bugs.
   For a conceptual question, treat `release_notes` hits as caveats or
   ignore them — prefer `user_guide` / `api_reference` / `background`
   hits as the primary answer. You can also narrow with
   `--categories user_guide,api_reference` when you're confident about
   the target content type; the filter applies before ranking so
   `top_k` is exact.

4. Synthesize an answer from the top results. Cite the specific URLs
   you used — users rely on those links to go read the authoritative
   docs themselves.
5. If the top `score` is low (e.g., below ~0.3) or the results look
   off-topic, tell the user the docs don't seem to cover their
   question and suggest rephrasing or pointing them at a specific
   doc section.

## Not covered

For authoritative ICESat-2 / GEDI science (photon classification,
algorithm details, HDF5 structure, quality flags), use the
`nsidc-reference` skill instead — that's sourced from NSIDC + ORNL
DAAC user guides and ATBDs (ATL03, ATL06, ATL08, ATL13, ATL24, GEDI
L4A) rather than SlideRule's own docs.
