####################################################################################################
#
# SlideRule Search Server — serves /docsearch/search over CloudFront + Lambda.
#
# Architecture: one Lambda container image (sentence-transformers model + corpus.json
# baked in) fronted by CloudFront via OAC. No S3 artifact hosting, no meta.json
# polling — a corpus rebuild is just a new image push.
#
# Skills are packaged separately via scripts/package_skill.sh.
#
####################################################################################################

SHELL := /bin/bash
ROOT  = $(shell pwd)

# DOMAIN / DOMAIN_APEX are supplied by wrapper targets (or the environment).
# DOMAIN_ROOT is the *middle* label — the environment differentiator — so
# search.testsliderule.org -> testsliderule and search.slideruleearth.io ->
# slideruleearth. (The first label is "search" in both envs, which would
# collapse the Project cost-attribution tag to a single value.)
DOMAIN          ?=
DOMAIN_ROOT     = $(word 2,$(subst ., ,$(DOMAIN)))
DOMAIN_APEX     ?= $(DOMAIN)
DISTRIBUTION_ID = $(shell aws cloudfront list-distributions --query "DistributionList.Items[?Aliases.Items[0]=='$(DOMAIN)'].Id" --output text 2>/dev/null)

# Reject DOMAIN=localhost — almost always an unrelated shell export
# leaking in (e.g. from ~/.zshrc) rather than an intentional override.
# Without this guard, targets like `make logs` / `make smoketest` /
# `make deploy-lambda` pass their `test -n "$(DOMAIN)"` checks and
# silently target the wrong thing. Wrapper targets (update-testsliderule
# etc.) supply real FQDNs; bare invocations should leave DOMAIN unset.
ifeq ($(DOMAIN),localhost)
$(error DOMAIN=localhost is almost certainly a stray shell export, not intent. `unset DOMAIN` (or remove the export from ~/.zshrc) and re-run, or pass an explicit DOMAIN= on the command line. For a real environment use a wrapper like `make update-testsliderule`)
endif

SRC_DIR      = $(ROOT)/generated
CORPUS_FILE  = $(SRC_DIR)/docsearch/corpus.json

# Prefer the repo-local .venv when it exists so `make freeplay` and
# `make rebuild-corpus-*` Just Work without requiring the user to
# `source .venv/bin/activate` first. Falls back to whatever python3 is
# on PATH — if that shell's python doesn't have the deps, the
# per-target import-check below prints a clear install hint instead
# of a raw ModuleNotFoundError traceback.
PYTHON := $(shell test -x $(ROOT)/.venv/bin/python && echo $(ROOT)/.venv/bin/python || echo python3)

.PHONY: help clean verify rebuild-corpus-docsearch rebuild-corpus-nsidc \
        build-corpus-image \
        package-skill-docsearch package-skill-nsidc package-skills \
        freeplay build-image test-image run-image deploy-lambda smoketest query \
        terraform-apply terraform-apply-ecr terraform-destroy check-vars \
        bootstrap-deploy-to-testsliderule bootstrap-deploy-to-slideruleearth \
        deploy-to-testsliderule deploy-to-slideruleearth \
        destroy-testsliderule destroy-slideruleearth \
        update-testsliderule update-slideruleearth \
        update-infra-testsliderule update-infra-slideruleearth \
        smoketest-testsliderule smoketest-slideruleearth \
        query-testsliderule query-slideruleearth \
        logs logs-testsliderule logs-slideruleearth \
        errors errors-testsliderule errors-slideruleearth \
        error-count error-count-testsliderule error-count-slideruleearth \
        invocations invocations-testsliderule invocations-slideruleearth \
        requests requests-testsliderule requests-slideruleearth \
        cost-estimate cost-estimate-testsliderule cost-estimate-slideruleearth

# ---- Corpus builder container (x86_64) -----------------------------------------------------------

# Builder image name. Tagged :latest; the `build-corpus-image` target
# rebuilds it on demand, and docker's layer cache keeps subsequent runs
# instant unless tools/requirements.txt changed.
CORPUS_BUILDER_IMAGE = docsearch-corpus-builder:latest

# Corpus rebuilds run inside an x86_64 container so the embedding arch
# matches what Lambda runs. See tools/Dockerfile.builder for rationale.
# On an M-series Mac this first-time build is Rosetta-emulated (slower
# than native arm64 but cached after).
build-corpus-image: ## Build the x86_64 container used for corpus rebuilds
	docker buildx build --load --platform linux/amd64 \
		-f $(ROOT)/tools/Dockerfile.builder \
		-t $(CORPUS_BUILDER_IMAGE) \
		$(ROOT)

help: ## That's me!
	@printf "\033[37m%-40s\033[0m %s\n" "#-----------------------------------------------------------------------------------------"
	@printf "\033[37m%-40s\033[0m %s\n" "# Makefile Help"
	@printf "\033[37m%-40s\033[0m %s\n" "#-----------------------------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_-].+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo DOMAIN:          $(DOMAIN)
	@echo DOMAIN_ROOT:     $(DOMAIN_ROOT)
	@echo DOMAIN_APEX:     $(DOMAIN_APEX)
	@echo DISTRIBUTION_ID: $(DISTRIBUTION_ID)

# ---- Local CI (mirrors .github/workflows/ci.yml) --------------------------------------------------

# `make verify` is the one-stop contributor check: py syntax + tf fmt +
# corpora parse + skills package. The same four steps run in CI as the
# `verify` job gated by branch protection. If this passes locally, the
# PR should pass CI.
#
# Deliberately *excludes* `make build-image` — the Dockerfile bake pulls
# torch CPU wheels and downloads the MiniLM model (~1 GB image, several
# minutes). That path is exercised at deploy time via `make update-<env>`.
verify: ## Run local CI checks: py syntax, tf fmt, corpora parse, skills package
	@python3 -m compileall -q server tools skills
	@terraform fmt -check -recursive terraform/
	@python3 -c "import json; json.load(open('generated/docsearch/corpus.json'))"
	@python3 -c "import json; json.load(open('generated/nsidc/corpus.json'))"
	@$(MAKE) --no-print-directory package-skill-docsearch > /dev/null
	@$(MAKE) --no-print-directory package-skill-nsidc > /dev/null
	@echo "✅ make verify OK"

# ---- Corpus + dev iteration -----------------------------------------------------------------------

rebuild-corpus-docsearch: build-corpus-image ## Re-crawl docs.slideruleearth.io and regenerate generated/docsearch/
	docker run --rm --platform linux/amd64 \
		-v $(ROOT):/app -w /app \
		$(CORPUS_BUILDER_IMAGE) \
		python tools/build_docsearch_corpus.py

rebuild-corpus-nsidc: build-corpus-image ## Download NSIDC + ORNL references and regenerate generated/nsidc/
	docker run --rm --platform linux/amd64 \
		-v $(ROOT):/app -w /app \
		$(CORPUS_BUILDER_IMAGE) \
		python tools/build_nsidc_corpus.py

freeplay: ## Interactive search REPL against the committed corpus (no deploy involved)
	@test -f $(CORPUS_FILE) || { \
	  echo "❌ $(CORPUS_FILE) is missing. Run 'make rebuild-corpus-docsearch' first."; \
	  exit 1; \
	}
	@$(PYTHON) -c "import onnxruntime, tokenizers, numpy, fastapi, pydantic" 2>/dev/null || { \
	  echo "❌ server dependencies missing in $(PYTHON)."; \
	  echo "   Install them one of two ways:"; \
	  echo "     (a) Repo-local venv (picked up automatically next run):"; \
	  echo "         python3 -m venv .venv \\"; \
	  echo "           && .venv/bin/pip install -r server/requirements.txt"; \
	  echo "     (b) Your active Python environment:"; \
	  echo "         pip install -r server/requirements.txt"; \
	  exit 1; \
	}
	@cd $(ROOT) && $(PYTHON) -m server.freeplay --corpus-file $(CORPUS_FILE)

package-skill-docsearch: ## Package skills/sliderule-docsearch/ into a .skill zip
	@bash $(ROOT)/scripts/package_skill.sh sliderule-docsearch

package-skill-nsidc: ## Package skills/nsidc-reference/ into a .skill zip
	@bash $(ROOT)/scripts/package_skill.sh nsidc-reference

package-skills: package-skill-docsearch package-skill-nsidc ## Package both skills

# ---- Lambda image build + deploy ------------------------------------------------------------------

# `build-image` is a local sanity check; it doesn't push. `deploy-lambda` is the real thing —
# it builds, pushes to ECR, and (if the Lambda already exists) updates its image_uri in place.
build-image: ## Locally build the Lambda container image (sanity check; no push)
	@test -f $(CORPUS_FILE) || { \
	  echo "❌ $(CORPUS_FILE) is missing. Run 'make rebuild-corpus-docsearch' first."; \
	  exit 1; \
	}
	docker buildx build --load --platform linux/amd64 -f server/Dockerfile -t docsearch:dev .

test-image: ## Build + run the image locally via the AWS Lambda RIE and exercise all routes
	@bash $(ROOT)/scripts/test_image.sh

run-image: build-image ## Build the image and run it interactively on :9000 (Ctrl-C to stop)
	@echo
	@echo "Lambda RIE listening on http://localhost:9000"
	@echo "Invoke endpoint:"
	@echo "  POST http://localhost:9000/2015-03-31/functions/function/invocations"
	@echo "Payload: a Lambda Function URL v2 event. See scripts/test_image.sh for examples."
	@echo
	docker run --rm -p 9000:8080 docsearch:dev

deploy-lambda: ## Build + push image to ECR, update Lambda (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@bash $(ROOT)/scripts/deploy_lambda.sh $(DOMAIN)

# ---- Terraform (infrastructure lifecycle) ---------------------------------------------------------

# First-time deploy is two-phase because Lambda won't create without an image already in ECR:
#   1. terraform-apply-ecr   (creates just the ECR repo)
#   2. deploy-lambda         (pushes the initial image to :latest)
#   3. terraform-apply       (creates Lambda + CloudFront + Route53 using :latest)
#
# Subsequent routine updates are just `make deploy-lambda`.
terraform-apply-ecr: ## First-phase: create only the ECR repo so the image can be pushed
	mkdir -p terraform/ && cd terraform/ && terraform init && \
	(terraform workspace select $(DOMAIN)-search-server || terraform workspace new $(DOMAIN)-search-server) && \
	terraform apply \
		-target=module.cloudfront.aws_ecr_repository.docsearch \
		-target=module.cloudfront.aws_ecr_lifecycle_policy.docsearch \
		-var domainName=$(DOMAIN) \
		-var domainApex=$(DOMAIN_APEX) \
		-var domain_root=$(DOMAIN_ROOT)

terraform-apply: ## Create/update the full stack (ECR already must exist)
	mkdir -p terraform/ && cd terraform/ && terraform init && \
	(terraform workspace select $(DOMAIN)-search-server || terraform workspace new $(DOMAIN)-search-server) && \
	terraform validate && \
	terraform apply \
		-var domainName=$(DOMAIN) \
		-var domainApex=$(DOMAIN_APEX) \
		-var domain_root=$(DOMAIN_ROOT)

terraform-destroy: ## Tear down Lambda + CloudFront + ECR + DNS
	cd terraform/ && terraform init && \
	(terraform workspace select $(DOMAIN)-search-server || terraform workspace new $(DOMAIN)-search-server) && \
	terraform destroy \
		-var domainName=$(DOMAIN) \
		-var domainApex=$(DOMAIN_APEX) \
		-var domain_root=$(DOMAIN_ROOT)

# ---- Smoke tests ----------------------------------------------------------------------------------

smoketest: ## curl the deployed endpoints and verify status + CORS + consistency
	@DOMAIN=$(DOMAIN) bash $(ROOT)/scripts/smoketest.sh

# ---- Ad-hoc query ---------------------------------------------------------------------------------

# Hit /docsearch/search on the deployed endpoint with a single query and
# pretty-print the JSON response. Quick spot-checks ("does this phrase
# match what I think it matches?") without spinning up freeplay or
# editing scripts/smoketest.sh.
#
# CloudFront's OAC SigV4-signs origin requests but doesn't buffer the
# body to hash it, so viewers must send `x-amz-content-sha256` with the
# body's SHA256 or Lambda URL returns 403. Same pattern as
# scripts/smoketest.sh's signed_post(). `jq --arg` escapes QUERY so
# quotes and special chars can't break the JSON body. sha256sum is
# GNU coreutils; macOS uses shasum -a 256 — one or the other is always
# present.
query: ## Ad-hoc search query against deployed /docsearch/search (requires DOMAIN and QUERY)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@test -n "$(QUERY)"  || (echo "❌ QUERY is not set"; exit 1)
	@BODY=$$(jq -cn --arg q "$(QUERY)" '{query: $$q}'); \
	if command -v sha256sum >/dev/null 2>&1; then \
		HASH=$$(printf '%s' "$$BODY" | sha256sum | awk '{print $$1}'); \
	else \
		HASH=$$(printf '%s' "$$BODY" | shasum -a 256 | awk '{print $$1}'); \
	fi; \
	curl -s "https://$(DOMAIN)/docsearch/search" \
		-H 'content-type: application/json' \
		-H "x-amz-content-sha256: $$HASH" \
		-d "$$BODY" | jq .

# ---- CloudWatch logs ------------------------------------------------------------------------------

# `aws logs tail` pulls its region from the CLI default, which is
# probably not us-east-1 on your workstation (the Lambda lives in
# us-east-1, but your ~/.aws/config default may be elsewhere). Baking
# --region into the target means you never need to remember.
# --since 10m seeds with recent activity immediately (so you can see
# the most recent EventBridge warmup tick without waiting for the next
# one), then --follow streams new events until Ctrl-C.
logs: ## Tail Lambda CloudWatch logs (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	aws logs tail "/aws/lambda/docsearch-$(subst .,-,$(DOMAIN))" \
		--region us-east-1 \
		--since 10m \
		--follow \
		--format short

# `errors` is a one-shot filtered scan — `logs` with --follow is useful
# for watching live activity, but when something goes wrong you don't
# want to scroll through thousands of successful warmer ticks to find
# the one error line. The filter patterns target the concrete strings
# the Lambda runtime emits on a failure:
#
#   "Status: timeout"       — INIT_REPORT / invoke timeout
#   "Status: error"         — explicit error status on INIT_REPORT / REPORT
#   "Error Type:"           — Lambda runtime reports error class
#   "Runtime.ExitError"     — container crashed during init or invoke
#   "Traceback"             — unhandled Python exception in handler
errors: ## Show Lambda error events in CloudWatch logs for the last hour (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	aws logs tail "/aws/lambda/docsearch-$(subst .,-,$(DOMAIN))" \
		--region us-east-1 \
		--since 1h \
		--format short \
		--filter-pattern '?"Status: timeout" ?"Status: error" ?"Error Type:" ?"Runtime.ExitError" ?"Traceback"'

# `error-count` hits the Lambda Errors metric rather than the log
# stream — useful for "how many errors per hour over the last day"
# without paging through output.
#
# Window + bucket size match `invocations` and `requests` (24h / 1h)
# so the three outputs are apples-to-apples: line up the same hour
# across all three and you see invocations vs. real requests vs.
# errors at a glance. The Sum column is the Error count per bucket;
# a bucket with Sum=0 means zero errors that hour (which is most of
# them when things are healthy).
error-count: ## Show Lambda error count (CloudWatch metric, 1-hour buckets, last 24h) (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@aws cloudwatch get-metric-statistics \
		--region us-east-1 \
		--namespace AWS/Lambda \
		--metric-name Errors \
		--dimensions Name=FunctionName,Value="docsearch-$(subst .,-,$(DOMAIN))" \
		--start-time "$$(date -u -v-24H +%Y-%m-%dT%H:%M:%S)" \
		--end-time "$$(date -u +%Y-%m-%dT%H:%M:%S)" \
		--period 3600 \
		--statistics Sum \
		--output text \
		--query 'sort_by(Datapoints,&Timestamp)[].[Timestamp,Sum]' \
		| python3 $(ROOT)/scripts/utc_to_local.py

# `invocations` is the count of EVERY Lambda invocation over the last
# 24h, bucketed by hour. Includes:
#   - EventBridge warmer (rate(5 minutes) -> ~12/hr baseline)
#   - Post-deploy `aws lambda invoke` warmups from deploy_lambda.sh
#   - Real user traffic via CloudFront
# For *just* real external traffic use `make requests` instead (hits
# CloudFront metrics, which don't see the warmer or direct invokes).
invocations: ## Show Lambda invocation count (CloudWatch metric, 1-hour buckets, last 24h) (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@aws cloudwatch get-metric-statistics \
		--region us-east-1 \
		--namespace AWS/Lambda \
		--metric-name Invocations \
		--dimensions Name=FunctionName,Value="docsearch-$(subst .,-,$(DOMAIN))" \
		--start-time "$$(date -u -v-24H +%Y-%m-%dT%H:%M:%S)" \
		--end-time "$$(date -u +%Y-%m-%dT%H:%M:%S)" \
		--period 3600 \
		--statistics Sum \
		--output text \
		--query 'sort_by(Datapoints,&Timestamp)[].[Timestamp,Sum]' \
		| python3 $(ROOT)/scripts/utc_to_local.py

# `requests` hits CloudFront's Requests metric instead of Lambda's —
# so it counts only traffic that entered through the edge (real users,
# smoketest curls, etc.) and excludes warmer ticks and direct
# `aws lambda invoke` warmups that bypass CloudFront. This is the
# more meaningful "how many real queries have we served" number.
#
# CloudFront metrics are published per-distribution+Region=Global, so
# we have to resolve the distribution ID by domain alias. That lookup
# eats a CLI call per invocation of this target; the DOMAIN-scoped
# `DISTRIBUTION_ID` at the top of the Makefile does the same thing
# but only kicks in after DOMAIN is set by the wrappers — so for the
# base target we do the lookup inline.
requests: ## Show CloudFront request count (CloudWatch metric, 1-hour buckets, last 24h) (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@DIST_ID=$$(aws cloudfront list-distributions --query "DistributionList.Items[?Aliases.Items[0]=='$(DOMAIN)'].Id" --output text 2>/dev/null); \
	test -n "$$DIST_ID" || { echo "❌ No CloudFront distribution found for $(DOMAIN)"; exit 1; }; \
	aws cloudwatch get-metric-statistics \
		--region us-east-1 \
		--namespace AWS/CloudFront \
		--metric-name Requests \
		--dimensions Name=DistributionId,Value=$$DIST_ID Name=Region,Value=Global \
		--start-time "$$(date -u -v-24H +%Y-%m-%dT%H:%M:%S)" \
		--end-time "$$(date -u +%Y-%m-%dT%H:%M:%S)" \
		--period 3600 \
		--statistics Sum \
		--output text \
		--query 'sort_by(Datapoints,&Timestamp)[].[Timestamp,Sum]' \
		| python3 $(ROOT)/scripts/utc_to_local.py

# `cost-estimate` joins Lambda's Invocations and Duration metrics by
# timestamp and applies public Lambda pricing to estimate compute +
# request cost per hourly bucket over the last 24h. Architecture
# (x86_64) and memory (2 GB) are hardcoded in scripts/cost_estimate.py
# to match terraform/modules/lambda.tf; bump there if terraform
# changes. Covers Lambda compute + request fees only — doesn't include
# data transfer, CloudFront, ECR. Compute dominates our bill in
# practice, so this tracks the real AWS invoice closely.
#
# For penny-exact actuals use `aws ce get-cost-and-usage` (24h lag)
# filtered by the `Project` tag.
cost-estimate: ## Estimate Lambda cost by hour for the last 24h (requires DOMAIN)
	@test -n "$(DOMAIN)" || (echo "❌ DOMAIN is not set"; exit 1)
	@python3 $(ROOT)/scripts/cost_estimate.py "docsearch-$(subst .,-,$(DOMAIN))" \
		| python3 $(ROOT)/scripts/utc_to_local.py

# ---- Per-environment wrappers ---------------------------------------------------------------------

bootstrap-deploy-to-testsliderule: ## First-time deploy from a clean slate: ECR → image push → full stack at search.testsliderule.org
	make terraform-apply-ecr DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org && \
	make deploy-lambda       DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org && \
	make terraform-apply     DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

# Combined deploy for the case where both terraform config and Lambda
# code changed — e.g. bumping memory_size in a config apply alongside a
# code update, or today's arch switch (terraform flips to x86_64, then
# the new image replaces :latest). Terraform runs first so that any
# schema-incompatible infra change (arch, memory, env vars) is already
# live before the new image is pushed and update-function-code runs.
# For infra-only or code-only iteration, use update-infra-<env> or
# update-<env> directly.
deploy-to-testsliderule: ## Combined infra + code deploy at search.testsliderule.org (terraform first, then image)
	make update-infra-testsliderule && \
	make update-testsliderule

update-testsliderule: ## Code-only update: rebuild image + update Lambda at search.testsliderule.org
	make deploy-lambda DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

update-infra-testsliderule: ## Terraform-only update at search.testsliderule.org (WAF, DNS, CloudFront, etc. — no Lambda rebuild)
	make terraform-apply DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

destroy-testsliderule: ## Tear down search.testsliderule.org infrastructure
	make terraform-destroy DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

smoketest-testsliderule: ## Smoketest against search.testsliderule.org
	make smoketest DOMAIN=search.testsliderule.org

query-testsliderule: ## Ad-hoc query against search.testsliderule.org (requires QUERY)
	make query DOMAIN=search.testsliderule.org QUERY="$(QUERY)"

logs-testsliderule: ## Tail CloudWatch logs for search.testsliderule.org
	make logs DOMAIN=search.testsliderule.org

errors-testsliderule: ## Show Lambda error events for search.testsliderule.org (last 1h)
	make errors DOMAIN=search.testsliderule.org

error-count-testsliderule: ## Show Lambda error count for search.testsliderule.org (last 24h)
	make error-count DOMAIN=search.testsliderule.org

invocations-testsliderule: ## Show Lambda invocation count for search.testsliderule.org (last 24h)
	make invocations DOMAIN=search.testsliderule.org

requests-testsliderule: ## Show CloudFront request count for search.testsliderule.org (last 24h)
	make requests DOMAIN=search.testsliderule.org

cost-estimate-testsliderule: ## Estimate Lambda cost for search.testsliderule.org (last 24h)
	make cost-estimate DOMAIN=search.testsliderule.org

bootstrap-deploy-to-slideruleearth: ## First-time deploy from a clean slate: ECR → image push → full stack at search.slideruleearth.io
	make terraform-apply-ecr DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io && \
	make deploy-lambda       DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io && \
	make terraform-apply     DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

deploy-to-slideruleearth: ## Combined infra + code deploy at search.slideruleearth.io (terraform first, then image)
	make update-infra-slideruleearth && \
	make update-slideruleearth

update-slideruleearth: ## Code-only update: rebuild image + update Lambda at search.slideruleearth.io
	make deploy-lambda DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

update-infra-slideruleearth: ## Terraform-only update at search.slideruleearth.io (WAF, DNS, CloudFront, etc. — no Lambda rebuild)
	make terraform-apply DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

destroy-slideruleearth: ## Tear down search.slideruleearth.io infrastructure
	make terraform-destroy DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

smoketest-slideruleearth: ## Smoketest against search.slideruleearth.io
	make smoketest DOMAIN=search.slideruleearth.io

query-slideruleearth: ## Ad-hoc query against search.slideruleearth.io (requires QUERY)
	make query DOMAIN=search.slideruleearth.io QUERY="$(QUERY)"

logs-slideruleearth: ## Tail CloudWatch logs for search.slideruleearth.io
	make logs DOMAIN=search.slideruleearth.io

errors-slideruleearth: ## Show Lambda error events for search.slideruleearth.io (last 1h)
	make errors DOMAIN=search.slideruleearth.io

error-count-slideruleearth: ## Show Lambda error count for search.slideruleearth.io (last 24h)
	make error-count DOMAIN=search.slideruleearth.io

invocations-slideruleearth: ## Show Lambda invocation count for search.slideruleearth.io (last 24h)
	make invocations DOMAIN=search.slideruleearth.io

requests-slideruleearth: ## Show CloudFront request count for search.slideruleearth.io (last 24h)
	make requests DOMAIN=search.slideruleearth.io

cost-estimate-slideruleearth: ## Estimate Lambda cost for search.slideruleearth.io (last 24h)
	make cost-estimate DOMAIN=search.slideruleearth.io

# ---- Validation -----------------------------------------------------------------------------------

check-vars:
	@test -n "$(DOMAIN)"          || (echo "❌ DOMAIN is not set"; exit 1)
	@test -n "$(DOMAIN_APEX)"     || (echo "❌ DOMAIN_APEX is not set"; exit 1)
	@test -n "$(DISTRIBUTION_ID)" || (echo "❌ DISTRIBUTION_ID could not be resolved for DOMAIN=$(DOMAIN)"; exit 1)
	@echo "✅ All required variables are set:"
	@echo "   DOMAIN          = $(DOMAIN)"
	@echo "   DOMAIN_APEX     = $(DOMAIN_APEX)"
	@echo "   DISTRIBUTION_ID = $(DISTRIBUTION_ID)"
