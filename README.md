# sliderule-search-server

Hosts `POST /docsearch/search` — a semantic + lexical retrieval endpoint
over the SlideRule Earth documentation corpus. Consumed by the
[`sliderule-docsearch`](skills/sliderule-docsearch/) skill and any
other agent/tool that wants ranked chunks from docs.slideruleearth.io.

## Architecture

```
Client ── POST /docsearch/search ──▶ CloudFront (search.testsliderule.org)
                                     │  aliased via Route 53 + ACM
                                     ▼
                                     Lambda Function URL (OAC-signed)
                                     │
                                     ▼
                                     Lambda container image (arm64)
                                       ├── sentence-transformers/all-MiniLM-L6-v2 (baked in)
                                       ├── corpus.json + meta.json (baked in)
                                       ├── FastAPI + Mangum
                                       └── LRU cache (1024 entries)
```

Retrieval = cosine similarity over the pre-computed chunk embeddings,
fused with an IDF-weighted lexical overlap via reciprocal rank fusion
(RRF). All of it runs server-side; the client is a thin HTTP wrapper.

**One origin, one deploy unit.** The corpus is part of the Lambda image
— there is no separate S3 artifact host, no `meta.json` polling, no
content-addressed URL scheme. A corpus rebuild is a new image push;
everything else flows from that.

## Endpoints

| Path                    | Method   | What it does                                           |
| ----------------------- | -------- | ------------------------------------------------------ |
| `/docsearch/search`     | POST     | Run the ranking pipeline, return top K chunks as JSON. |
| `/docsearch/meta`       | GET      | Static corpus metadata (sha, chunk count, built_at).   |
| `/healthz`              | GET      | Liveness probe.                                        |
| anything else           | *        | JSON 404.                                              |

Request:

```json
{
  "query": "how do I apply geoid correction to get orthometric heights from atl03x",
  "top_k": 5,
  "disable_lexical": false,
  "categories": ["user_guide", "api_reference"]
}
```

Response: see [skills/sliderule-docsearch/SKILL.md](skills/sliderule-docsearch/SKILL.md#output).

CORS: `Access-Control-Allow-Origin: *`, methods `GET, HEAD, OPTIONS, POST`.

### Request signing

**POST bodies require an `x-amz-content-sha256` header** whose value is
the hex-encoded SHA-256 of the request body. CloudFront uses this to
SigV4-sign the origin request via OAC; without it, Lambda Function URL
rejects the call with 403. The `sliderule-docsearch` skill client
computes and adds this header automatically. Direct HTTPS callers
(`curl`, browser `fetch`, any client that isn't `scripts/search.py`)
need to compute and add it themselves:

```bash
body='{"query":"atl03x","top_k":3}'
curl -sS https://search.testsliderule.org/docsearch/search \
  -H "Content-Type: application/json" \
  -H "x-amz-content-sha256: $(printf %s "$body" | sha256sum | awk '{print $1}')" \
  -d "$body"
```

The hash must match the exact bytes of the request body (no
reformatting, no extra whitespace) since that's what CloudFront signs.

## Repository layout

```
server/                                   FastAPI + Lambda handler
├── app.py                                POST /docsearch/search + friends
├── ranking.py                            cosine + IDF + RRF (pure functions)
├── cache.py                              LRU for ranked responses
├── handler.py                            Mangum adapter (Lambda entrypoint)
├── freeplay.py                           local REPL against a corpus file
├── Dockerfile                            arm64 Lambda image (model + corpus baked in)
└── requirements.txt

generated/docsearch/
├── corpus.json                           chunks + embeddings (committed; baked into image)
└── meta.json                             build metadata (committed)

skills/sliderule-docsearch/               thin HTTP client skill
├── SKILL.md
├── requirements.txt                      just `requests`
└── scripts/search.py

tools/
└── build_docsearch_corpus.py             crawl + chunk + embed docs.slideruleearth.io

terraform/                                ECR + Lambda + CloudFront + Route 53 + ACM
scripts/
├── deploy_lambda.sh                      docker build → ECR push → update Lambda
├── test_image.sh                         build + run image via Lambda RIE locally
├── smoketest.sh                          curl the deployed endpoints
└── package_skill.sh                      zip a .skill archive
```

## Local iteration

```bash
python3 -m venv .venv
.venv/bin/pip install -r server/requirements.txt

# Interactive REPL against the committed corpus; no Lambda, no network.
make freeplay
```

The REPL imports `server.ranking` directly — same implementation the
deployed Lambda uses.

### Local Docker testing

To exercise the exact container image the Lambda will run — build +
AWS Lambda Runtime Interface Emulator + full assertion suite:

```bash
make test-image         # build + run + test + teardown
make run-image          # build + run interactively on :9000 for manual poking
```

`test-image` exercises 8 routes through the real Mangum → FastAPI →
ranking path, including OPTIONS preflight, validation 422s, the
`categories=[]` zero-results semantic, and the catch-all 404. Doesn't
exercise CloudFront, OAC, or the `x-amz-content-sha256` path — those
only show up under real AWS.

## Corpus rebuild

The server hosts two corpora, each rebuilt by a distinct target:

```bash
.venv/bin/pip install -r tools/requirements.txt   # first time only
make rebuild-corpus-docsearch   # crawls docs.slideruleearth.io
make rebuild-corpus-nsidc       # downloads NSIDC + ORNL PDFs and the GEDI HTML
# Review the generated/{docsearch,nsidc}/ diff (chunk counts,
# corpus_sha256 all shift). Commit the change:
git add generated/ && git commit -m "rebuild corpora for release X.Y.Z"
```

The corpus rebuild is **release-coupled**: regenerate when upstream
docs change. Both `corpus.json` and `meta.json` (per corpus) are
committed so a deploy from a given git sha ships deterministic
bytes — the Docker image's COPY step bakes in whatever is committed
at that moment.

Empty-corpus guard: the builder refuses to overwrite existing
artifacts unless it crawled at least `--min-pages` (default 20) pages
and produced at least `--min-chunks` (default 100) chunks.

## Deploy flow

### First-time setup (per domain)

Because Lambda won't create without an image already present in ECR,
the first deploy is three steps, driven by `bootstrap-deploy-to-<env>`:

```bash
make bootstrap-deploy-to-testsliderule    # runs all three below
```

which expands to:

1. `make terraform-apply-ecr` — create the ECR repo.
2. `make deploy-lambda` — build the image (x86_64) and push `:latest` + a content-tagged audit artifact.
3. `make terraform-apply` — create Lambda + Function URL + CloudFront + Route 53 + ACM, wiring everything together.

**IAM requirement:** step 3 creates an IAM role (`docsearch-lambda-<sanitized-domain>`),
so the running principal needs `iam:CreateRole` + `iam:AttachRolePolicy`.
Standard PowerUser/developer roles typically lack these; use admin-level
credentials for the initial apply. Routine `deploy-lambda` updates do
not need IAM permissions.

### Routine updates

Three shapes depending on what changed:

| Changed       | Target                            | What it does                                        |
|---------------|-----------------------------------|-----------------------------------------------------|
| Code only     | `make update-testsliderule`       | Rebuild image, push, `update-function-code`, warm.  |
| Infra only    | `make update-infra-testsliderule` | `terraform apply` — no Lambda rebuild.              |
| Both          | `make deploy-to-testsliderule`    | Terraform apply first, then image push + update.    |

Use the combined `deploy-to-<env>` when a single change touches both
`terraform/` and `server/` — e.g. bumping `memory_size` alongside a
code change, or an architecture switch where terraform must recreate
the Lambda before `update-function-code` can accept the new image.

Terraform has `lifecycle { ignore_changes = [image_uri] }` on the
Lambda so code-only `update-<env>` out-of-band deploys don't get
reverted by a subsequent `update-infra-<env>`.

### Verify

```bash
make smoketest DOMAIN=search.testsliderule.org
```

Checks `/healthz`, `/docsearch/meta`, OPTIONS preflight, happy-path
POST, two validation-failure POSTs, and the `corpus_sha256`
consistency between `/docsearch/meta` and the POST response.

## Environments

| Environment   | Domain                     | Lambda / ECR name                   |
| ------------- | -------------------------- | ----------------------------------- |
| test          | `search.testsliderule.org` | `docsearch-search-testsliderule-org` |
| prod (future) | `search.slideruleearth.io` | `docsearch-search-slideruleearth-io` |

Per-environment wrapper targets in the Makefile carry the `DOMAIN` /
`DOMAIN_APEX` variables. `DISTRIBUTION_ID` is auto-resolved from the
domain alias.

## Configuration

- `DOMAIN`, `DOMAIN_APEX` — set by wrappers or overrideable on the command line.
- `DOMAIN_ROOT` — derived from `DOMAIN`: the **middle** label (e.g. `testsliderule` for `search.testsliderule.org`). Used as the environment differentiator in the `Project` cost-attribution tag so test and prod don't collide.
- AWS resource names (Lambda function, ECR repo, log group) use the **full sanitized domain** (`docsearch-search-testsliderule-org`) — `DOMAIN_ROOT` alone wouldn't be distinctive enough for resource identity.
- `AWS_REGION` — defaults to `us-east-1`; same for Lambda, ECR, and CloudFront.
- `terraform/backend.tf` — state is `s3://sliderule/tf-states/search-server.tfstate` with per-domain workspaces.

## Skill packaging

```bash
make package-skill-docsearch    # → skills/sliderule-docsearch.skill
make package-skill-nsidc        # → skills/nsidc-reference.skill
make package-skills             # both
```

Each `.skill` archive is a zip with the skill directory at the root
(e.g. `sliderule-docsearch/…`). Packages are ~6 KB — no corpus or
model bytes bundled, just SKILL.md + the thin Python client.

The packages are environment-independent: the same `.skill` works
whether it's pointed at `search.testsliderule.org` (current default)
or `search.slideruleearth.io` (production once we cut over). The
host is a one-line constant in the skill's `scripts/search.py`.

## Operational notes

- **Cold start:** ~3 s model load + ~1 s corpus parse + ~500 ms matrix normalization. First request after a container boot pays this; warm requests run in 30–70 ms (uncached) or 1–5 ms (cached).
- **First-ever request after a fresh image push** carries an additional one-time cost while Lambda copies the image from ECR into its optimized runtime storage — up to ~60 s for this image. CloudFront's default `origin_read_timeout` is 30 s, so the first request of a fresh deploy will 504 once; subsequent requests hit the now-warmed container normally. Bumping `origin_read_timeout` to 60 s is a planned follow-up.
- **Cache:** in-memory LRU, keyed by `(query, top_k, disable_lexical, categories, corpus_sha256)`. Bounded at 1024 entries. Stats visible at `GET /docsearch/meta`.
- **Freshness:** no polling. A new corpus means a new image; a new image means a new Lambda container, which means fresh state. No stale-data window.
- **Logs:** CloudWatch log group `/aws/lambda/docsearch-<sanitized-domain>` (e.g. `/aws/lambda/docsearch-search-testsliderule-org`), 30-day retention.
