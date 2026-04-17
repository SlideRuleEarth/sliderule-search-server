# tools/

Scripts that produce the content under [`generated/`](../generated/). These
scripts require network access **at build time**. They are not part of the
serving path — the deployed distribution is pure static JSON, with no
server-side compute.

## `build_docsearch_corpus.py`

Crawls [docs.slideruleearth.io](https://docs.slideruleearth.io/), chunks the
pages by heading, embeds every chunk with
`sentence-transformers/all-MiniLM-L6-v2`, and writes
[`generated/docsearch/corpus.json`](../generated/docsearch/) +
`meta.json`.

```bash
pip install -r tools/requirements.txt
python tools/build_docsearch_corpus.py
```

Optional flags:

- `--output-dir PATH` — default `generated/docsearch/`
- `--max-pages N` — default `200`

### First run

The first invocation downloads the ~80 MB `all-MiniLM-L6-v2` model from
HuggingFace and caches it under `~/.cache/huggingface/`. Subsequent runs
are offline-capable for the embedding step (the crawl still needs the
network).

### Determinism

Builds are deterministic given the same source site: chunks are sorted by
URL then by in-page section order, embeddings are rounded to 6 decimal
places, and `built_at` lives only in `meta.json` (never in `corpus.json`).
Running the script twice back-to-back on an unchanged site should produce
byte-identical `corpus.json` output.
