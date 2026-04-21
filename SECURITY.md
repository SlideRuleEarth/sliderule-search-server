# Security policy

## Reporting a vulnerability

If you believe you've found a security issue in sliderule-search-server
— whether in the Lambda server, the CloudFront / WAF edge, the corpus
builders, the Terraform infrastructure, or either of the packaged
Claude skills — **please do not open a public GitHub issue**.

Instead, email **security@mail.slideruleearth.io** with:

- A short description of the issue
- Steps to reproduce
- The impact you believe it has
- (Optional) A suggested fix

We'll acknowledge within 5 business days and keep you updated as we
triage, fix, and disclose.

Credible reports that demonstrate exploitable impact will be
acknowledged in the release notes unless you prefer otherwise.

## Scope

### In scope

- The search endpoints at `https://search.testsliderule.org/` (test)
  and `https://search.slideruleearth.io/` (production), plus any
  future variants. These are CloudFront → Lambda (FastAPI + Mangum)
  with a WAFv2 rate limit in front.
- The Lambda container image (`server/`) and its request handling
  (`server/app.py`, `server/handler.py`, `server/ranking.py`).
- The corpus builders in [tools/](tools/) — `build_docsearch_corpus.py`
  and `build_nsidc_corpus.py`.
- The Terraform in [terraform/](terraform/) — CloudFront + OAC + WAF +
  Lambda + ECR + EventBridge warmer.
- Both Claude skills in [skills/sliderule-docsearch/](skills/sliderule-docsearch/)
  and [skills/nsidc-reference/](skills/nsidc-reference/).

### Out of scope

- Rate-limiting / denial-of-service. CloudFront + the WAF's
  rate-based rule (2000 req / 5 min per IP) are the documented
  controls; reports of "I can make it slow at volumes below that
  threshold" are expected behaviour.
- Issues in SlideRule itself — use the
  [sliderule repository](https://github.com/SlideRuleEarth/sliderule)
  instead.
- Issues in the underlying docs at docs.slideruleearth.io or the
  NSIDC / ORNL DAAC PDFs the corpora index from — those are upstream
  concerns for the respective publishers.

## What we protect

- **No secrets in the repo.** Git history is audited with gitleaks
  across every commit before each public push; if you spot something
  that looks like a leaked credential in the repo, please email
  rather than post publicly so we can rotate immediately.
- **OAC + SigV4 at the edge.** CloudFront signs requests to the
  private Lambda Function URL via Origin Access Control; the Lambda
  rejects unsigned traffic. There is no public Lambda URL.
- **Pinned infra.** `terraform/.terraform.lock.hcl` pins provider
  hashes for all four target platforms so fresh clones reproduce the
  same provider build on any workstation and on CI.
- **Public-doc corpora.** The committed corpora in `generated/` are
  extracted from public documentation (docs.slideruleearth.io, NSIDC
  user guides + ATBDs, ORNL DAAC product docs) — nothing proprietary
  is indexed. Commit diffs are PR-reviewable (chunk counts + sha256).
- **No static AWS credentials.** The ECR push path in
  [scripts/deploy_lambda.sh](scripts/deploy_lambda.sh) authenticates
  via the caller's configured AWS identity at runtime. CI has no
  AWS creds wired in; all production changes flow through a
  maintainer's local `make update-<env>` or `make terraform-apply`.
