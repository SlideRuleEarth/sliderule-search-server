# sliderule-search-server

A dedicated static-content CloudFront distribution that serves pre-computed
search corpora for SlideRule-adjacent AI skills to consume. Sibling service
to [`sliderule-schema-server`](../sliderule-schema-server/) — same
infrastructure pattern (S3 + CloudFront + Route 53 + ACM), different
content, independent deploy cadence.

## What this is (and isn't)

- **What it is:** dumb static JSON over CloudFront. A tenant (e.g. the
  docsearch corpus) is a pair of files at a known path:
  `/<tenant>/corpus.json` + `/<tenant>/meta.json`. Skills download the
  corpus, compute cosine similarity locally, and return ranked results.
- **What it isn't:** there is no server-side compute, no Lambda, no API
  Gateway, no Anthropic API usage at build or serve time. CloudFront
  serves the bytes in S3 verbatim.

## URL / S3 / disk layout (all identical)

```
generated/                                        ← on disk in this repo
                                                  ← same keys in s3://sliderule-search-test/
                                                  ← same paths at https://search.testsliderule.org/
└── docsearch/
    ├── corpus.json                               (semantic search corpus of docs.slideruleearth.io)
    └── meta.json                                 (build metadata)
```

`generated/` is the source of truth for deployed content. There is no
authored/generated/merged split like in `sliderule-schema-server` —
the corpora here are produced end-to-end by build-time scripts.

[`scripts/build.sh`](scripts/build.sh) stages `generated/` verbatim into
`build/` and drops an inlined `errors/not-found.json` alongside.
`build/` is gitignored and produced on every deploy.

Anything not present in the source tree returns `HTTP 404` with body:

```json
{"error": "not yet generated"}
```

Configured via CloudFront `custom_error_response` pointing at
`/errors/not-found.json`.

## Source files: where they come from

| Published URL              | In-repo source                             | Origin                                                    |
| -------------------------- | ------------------------------------------ | --------------------------------------------------------- |
| `/docsearch/corpus.json`   | `generated/docsearch/corpus.json`          | [`tools/build_docsearch_corpus.py`](tools/build_docsearch_corpus.py) crawls `docs.slideruleearth.io` |
| `/docsearch/meta.json`     | `generated/docsearch/meta.json`            | Produced alongside `corpus.json` by the same script        |

### Release flow — when do we rebuild?

The corpus rebuild is **release-coupled**. It gets regenerated when the
SlideRule server is released, which coincides with a docs-site release.
Typical cadence is once a week or less. In between releases the corpus
is frozen.

That matters for two things:

1. **Tracked artifacts.** Both `corpus.json` and `meta.json` are
   committed to git. `make build` never auto-regenerates — it fails
   loudly if `corpus.json` is missing. Deploys from a given commit
   always ship the bytes committed at that commit.
2. **Meta-driven client cache.** The skill fetches `meta.json` on every
   query (tiny, ~300 bytes), then reuses its local corpus cache as long
   as `meta.json`'s `corpus_sha256` matches. Clients pick up a new
   corpus the moment it's released, with no wall-clock TTL.

### Regenerating the docsearch corpus

```bash
make rebuild-corpus
# Review the diff — chunk count, pages_crawled, corpus_sha256 should
# all shift in a way that matches what changed upstream.
git add generated/ && git commit -m "rebuild docsearch corpus for release X.Y.Z"
```

The first invocation downloads the ~80 MB `all-MiniLM-L6-v2`
sentence-transformer model from HuggingFace; subsequent runs are
offline-capable for the embedding step.

Empty-corpus guard: the builder refuses to overwrite existing artifacts
unless it crawled at least `--min-pages` (default 20) pages and
produced at least `--min-chunks` (default 100) chunks. Prevents a
transient docs outage from silently shipping a zero-chunk corpus.

Builds are deterministic given the same source site: chunks are sorted
by URL then in-page section order, embeddings are rounded to 6 decimal
places, and `built_at` lives only in `meta.json`. `corpus_sha256` in
`meta.json` fingerprints the corpus bytes and is the cache key the
skill uses.

## Skills

The `sliderule-docsearch` skill lives at
[`skills/sliderule-docsearch/`](skills/sliderule-docsearch/) during the
POC phase. It will move to its own repo once stable — co-located here
so corpus-format changes and skill-code changes land in one commit.

Package the skill into a distributable `.skill` zip:

```bash
bash scripts/package_skill.sh sliderule-docsearch
# → skills/sliderule-docsearch.skill
```

The resulting archive has `sliderule-docsearch/` as its root directory
(so `unzip` drops a folder, not loose files).

Test the skill against a local corpus before anything is uploaded:

```bash
pip install -r skills/sliderule-docsearch/requirements.txt
python skills/sliderule-docsearch/scripts/search.py \
    --corpus-file generated/docsearch/corpus.json \
    "what is phoreal" \
    --top-k 3
```

## Environments

| Environment   | Domain                     | S3 bucket               |
| ------------- | -------------------------- | ----------------------- |
| test          | `search.testsliderule.org` | `sliderule-search-test` |
| prod (future) | `search.slideruleearth.io` | `sliderule-search-prod` |

Per-environment wrapper targets in the Makefile
(`deploy-to-testsliderule`, `deploy-to-slideruleearth`, etc.) carry the
`DOMAIN` / `S3_BUCKET` / `DOMAIN_APEX` variables. `DISTRIBUTION_ID` is
auto-resolved from the domain alias via `aws cloudfront list-distributions`.

## Makefile targets

```
make build                       Stage generated/ into build/
make clean                       Remove build/
make rebuild-corpus              Re-crawl docs.slideruleearth.io and
                                 regenerate generated/docsearch/

make package-skill               Zip skills/sliderule-docsearch/ into a .skill

make live-update                 Build + aws s3 sync + invalidation
                                 (requires DOMAIN + S3_BUCKET + DOMAIN_APEX)
make deploy                      Alias for live-update

make terraform-apply             Create/update distribution + bucket + DNS
make terraform-destroy           Tear down the above

make smoketest                   curl the public endpoints and verify
                                 status + Content-Type + CORS

# Per-env wrappers (no variables needed):
make deploy-to-testsliderule     Infra + content at search.testsliderule.org
make live-update-testsliderule   Content only (assumes infra exists)
make destroy-testsliderule       Tear down the test env
```

## Distribution configuration

- **Origin:** private S3 bucket, fronted by an Origin Access Identity.
  Only CloudFront can read it.
- **Path mapping:** 1:1. CloudFront strips the leading `/` and looks up
  the exact key. No CloudFront Functions, no Lambda@Edge, no rewriting.
  URLs are flat from the root — `/docsearch/corpus.json`, not
  `/source/docsearch/corpus.json`.
- **Content-Type:** `aws s3 sync` auto-detects `application/json` from
  the `.json` extension.
- **CORS:** `Access-Control-Allow-Origin: *`, `Methods: GET, OPTIONS`,
  `Headers: *`. Applied via a CloudFront response headers policy so every
  response (including errors) carries the CORS headers.
- **Cache:** `Cache-Control: max-age=60` while iterating.
- **TLS:** ACM certificate for `search.<apex>`, DNS-validated against
  the existing Route 53 zone for the apex. TLS 1.2+.
- **Errors:** 403/404 from S3 → 404 from CloudFront with body
  `/errors/not-found.json`.

## First-time setup

1. Build the docsearch corpus locally:
   ```bash
   pip install -r tools/requirements.txt
   python tools/build_docsearch_corpus.py
   ```
   Commit the resulting `generated/docsearch/` diff.
2. Stand up infra + push content:
   ```bash
   make deploy-to-testsliderule
   ```
   - Terraform creates the bucket, distribution, ACM cert, and Route 53
     record.
   - The same wrapper then runs `live-update`, which stages, syncs, and
     invalidates.
3. Verify:
   ```bash
   make smoketest DOMAIN=search.testsliderule.org
   ```

CloudFront distribution creation takes a few minutes; DNS propagation can
take a few more. If `smoketest` fails immediately after the first apply,
give it 5–10 minutes and re-run.

## Re-deploy after changes

```bash
# After rebuilding generated/ content:
make live-update-testsliderule
make smoketest DOMAIN=search.testsliderule.org
```

## Configuration surface

- `DOMAIN`, `S3_BUCKET`, `DOMAIN_APEX` — set by the per-env wrapper
  targets, or overrideable on the command line for ad-hoc deploys.
- `DISTRIBUTION_ID` — looked up from the `DOMAIN` alias; no manual input.
- `terraform/backend.tf` — state is stored in
  `s3://sliderule/tf-states/search-server.tfstate` with per-domain
  workspaces, mirroring the schema-server backend layout.

## Relationship to sliderule-schema-server

Parallel sibling service. Same infrastructure pattern (S3 + CloudFront
+ Route 53 + ACM), same CORS + cache policy, same 404-to-JSON handling,
but independent S3 bucket, distribution, DNS record, and Terraform
state key (`search-server.tfstate` vs. `schema-server.tfstate`).
They deploy independently and evolve independently.

Terraform here is a self-contained copy-adapt of the schema-server
modules rather than a reference to shared modules. If a third sibling
service shows up, we can refactor to a shared module repo then.
