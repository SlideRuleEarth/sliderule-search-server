# Contributing

Thanks for your interest in sliderule-search-server. This repo is the
source tree, corpus pipeline, and deploy plumbing for the hosted
search at `search.slideruleearth.io` — a CloudFront → Lambda
(FastAPI + Mangum) service that backs the `sliderule-docsearch` and
`nsidc-reference` Claude skills.

## TL;DR workflow

```bash
git clone git@github.com:SlideRuleEarth/sliderule-search-server.git
cd sliderule-search-server

# Normal code edit (server/, terraform/, skills/):
make verify               # python syntax + tf fmt + corpora parse + skills package
git commit && git push
# open a PR into main — CI re-runs `make verify` on the PR

# Corpus refresh (heavy, not in CI):
make rebuild-corpus-docsearch        # or rebuild-corpus-nsidc
git add generated/
git commit -m "corpus: refresh docsearch from docs.slideruleearth.io"
```

That's the whole loop. The rest of this doc explains why each step
exists and what can go wrong.

## Setting up your environment

### Required

- **git**
- **Python 3.11+** — the server targets Python 3.12 in Lambda but
  3.11 is the CI floor for local development.
- **Terraform 1.14.9+** — `required_version` is pinned in
  [terraform/versions.tf](terraform/versions.tf).
- **Docker** — only for `make build-image` / `make test-image` /
  `make update-<env>`. Cloning and running `make verify` doesn't
  need Docker.
- **AWS CLI v2** — only for actual deploys. Read-only checks don't
  need credentials.

### Optional

- **gitleaks** — used in the pre-public-flip secret audit; run with
  `docker run --rm -v "$PWD:/repo" zricethezav/gitleaks:latest git /repo`.
- **jq** — nice for poking at JSON responses from the deployed
  search endpoint.

### Repo-local virtualenv

The Makefile prefers `.venv/bin/python` when it exists, so create
one and the corpus builders / REPL will Just Work:

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt   # for corpus rebuilds
.venv/bin/pip install -r server/requirements.txt  # for freeplay REPL
```

Fall back to your active Python if you prefer — the Makefile's
per-target import checks will print an install hint if deps are
missing.

## The three-layer content model

```
tools/        build_docsearch_corpus.py, build_nsidc_corpus.py  (builders)
generated/
  docsearch/corpus.json   committed artifact (docs.slideruleearth.io)
  nsidc/corpus.json       committed artifact (NSIDC + ORNL DAAC PDFs/HTML)
server/       FastAPI app, Mangum handler, ranking, Dockerfile  (runtime)
skills/
  sliderule-docsearch/    thin HTTP client (docs skill)
  nsidc-reference/        thin HTTP client (ATBD/user-guide skill)
```

- `tools/` crawls / downloads public documentation and emits
  corpus.json into `generated/`. Rebuilds are deliberate: the
  committed corpora are what gets baked into the Lambda image, so
  a rebuild is always paired with a deploy.
- `server/` reads the corpora from the image's working directory and
  exposes `/docsearch/{search,meta}` + `/nsidc/{search,meta}` +
  `/healthz`. Ranking is cosine similarity (MiniLM embeddings) + IDF
  lexical overlap fused via RRF.
- `skills/` are thin HTTP clients that POST to the hosted endpoint.
  `make package-skill-<name>` zips them into `.skill` archives.

## Pre-flight validations

`make verify` — run it before every commit. It does:

1. `python -m compileall -q server tools skills` — catches
   SyntaxError / indent bugs without executing the modules.
2. `terraform fmt -check -recursive terraform/` — formatting is
   enforced, not suggested.
3. JSON parse of both committed corpora — catches truncation /
   invalid escapes before Lambda image bake time.
4. `make package-skill-docsearch && make package-skill-nsidc` —
   confirms each skill directory is complete enough to zip.

CI re-runs the same four checks under the `verify` job. If it fails
on a PR, `make verify` locally will reproduce it.

## Running the test deploy

If you have AWS credentials with the right profile:

```bash
# First-time from a clean slate (creates ECR, pushes image, then full stack):
make bootstrap-deploy-to-testsliderule

# Combined infra + code update (terraform first, then image):
make deploy-to-testsliderule

# Routine code update (just rebuild image + update Lambda):
make update-testsliderule

# Infra-only update (WAF tweak, CloudFront setting, etc.):
make update-infra-testsliderule

# Verify the deploy:
make smoketest-testsliderule

# Tail CloudWatch logs (region baked in):
make logs-testsliderule
```

CloudFront distribution creation on a fresh stack takes a few
minutes; DNS propagation a few more. If smoketest fails right after
the first apply, wait 5–10 minutes and re-run.

## Reviewing a PR

Checklist for reviewers:

- [ ] CI's `verify` job is green
- [ ] If `server/` changed: does `make test-image` still pass
      locally? (CI doesn't run it — too slow)
- [ ] If `terraform/` changed: `terraform plan` diff reviewed
      against the actual change, not just the lock file
- [ ] If `generated/*/corpus.json` changed: diff the chunk count
      + a `jq .sha256` peek from the associated `meta.json`; large
      unexplained corpus deltas warrant a rebuild-reproduction
- [ ] If a new skill or route was added: SKILL.md's trigger
      description doesn't overlap with the other skill's triggers
- [ ] No new untracked files that should have been committed

## Style

- **JSON formatting:** `json.dump(..., indent=2)` for meta files,
  builder-choice for corpora (compactness wins — they're large).
- **Commit messages:** first line is a short summary (`area: what`).
  Body explains *why*, not *what* — the diff shows what. Reference
  issues or review feedback that prompted the change where
  applicable.
- **Python:** Python 3.11+ syntax is fine (`list[str]`, `X | None`,
  walrus). Keep the server modules readable — they're the kind of
  files future maintainers grep into, not just execute.
- **Terraform:** `terraform fmt -recursive terraform/` before
  committing; `make verify` will fail otherwise.

## Getting help

- Open a GitHub issue for bugs or proposed changes.
- Email **security@mail.slideruleearth.io** for security issues (see
  [SECURITY.md](SECURITY.md)).
- For SlideRule usage questions, try the `sliderule-docsearch` or
  `nsidc-reference` skills themselves — this repo's concern is the
  search service, not how to use SlideRule.
