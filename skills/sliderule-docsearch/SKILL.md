---
name: sliderule-docsearch
description: Semantic search over the SlideRule Earth documentation (docs.slideruleearth.io). Use this skill whenever the user asks about SlideRule concepts, parameters, APIs, data products, configuration options, Python client usage, endpoints, examples, or any 'how do I...' question about SlideRule. Retrieval runs server-side at search.testsliderule.org — semantic cosine similarity fused with IDF-weighted lexical overlap via reciprocal rank fusion. The skill itself is a thin HTTP client.
---

# sliderule-docsearch

Semantic search over the SlideRule Earth documentation at
[docs.slideruleearth.io](https://docs.slideruleearth.io/).

## Architecture

- Retrieval runs on a Lambda behind CloudFront at
  `https://search.testsliderule.org/docsearch/search`. The Lambda image
  bakes in the corpus and the `all-MiniLM-L6-v2` sentence-transformer
  model, so there's no network fetch at query time beyond the single
  POST.
- The skill client is a thin HTTP wrapper: it POSTs the query (plus
  `top_k`, `disable_lexical`, and an optional `categories` allowlist)
  and prints the server's JSON response to stdout.
- The server embeds the query, scores all chunks with cosine
  similarity, fuses that ranking with IDF-weighted lexical overlap via
  reciprocal rank fusion (RRF), and returns the top K. The fusion
  rescues queries where the user's intent hinges on a specific
  identifier — e.g. `"atl03x"` vs `"atl03"` — that pure semantic
  similarity can't reliably distinguish.
- Results for the same `(query, top_k, disable_lexical, categories)`
  tuple are cached in the Lambda's LRU so repeat queries return in
  single-digit milliseconds.

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

The skill requires network access (a single HTTPS POST per query).
There is no offline mode.

### Direct HTTPS callers (curl, browsers, anything other than `scripts/search.py`)

The endpoint is fronted by CloudFront + Lambda Function URL with OAC,
so every POST body must carry an `x-amz-content-sha256` header whose
value is the hex-encoded SHA-256 of the request body. CloudFront uses
this to SigV4-sign the origin request; without it the Lambda URL
rejects the call with 403. `scripts/search.py` computes and adds the
header automatically; direct callers must do it themselves:

```bash
body='{"query":"atl03x","top_k":3}'
curl -sS https://search.testsliderule.org/docsearch/search \
  -H "Content-Type: application/json" \
  -H "x-amz-content-sha256: $(printf %s "$body" | sha256sum | awk '{print $1}')" \
  -d "$body"
```

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
2. Parse the JSON response. Each `results[i]` has a `score` (cosine
   similarity, higher is better), `url`, `title`, `section`, `category`,
   and `text`. When present, `matched_tokens` lists which of the user's
   query tokens appeared literally in the chunk — a useful signal for
   confirming that an identifier-heavy query (e.g. `"atl03x"`) hit the
   right variant. Note: ranking reflects RRF-fused semantic + lexical
   scores, so `score` (which is cosine only) doesn't always
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
5. If the top `score` is low (< 0.3) or the results look off-topic,
   tell the user the docs don't seem to cover their question and
   suggest rephrasing or pointing them at a specific doc section.

## Not covered

For authoritative ICESat-2 / GEDI science (photon classification,
algorithm details, HDF5 structure, quality flags), use the
`nsidc-reference` skill instead — that's sourced from NSIDC user guides
and ATBDs rather than SlideRule's own docs.
