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
        freeplay build-image test-image run-image deploy-lambda smoketest \
        terraform-apply terraform-apply-ecr terraform-destroy check-vars \
        deploy-to-testsliderule deploy-to-slideruleearth \
        destroy-testsliderule destroy-slideruleearth \
        update-testsliderule update-slideruleearth \
        update-infra-testsliderule update-infra-slideruleearth \
        smoketest-testsliderule smoketest-slideruleearth \
        logs logs-testsliderule logs-slideruleearth

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
	docker buildx build --load --platform linux/arm64 -f server/Dockerfile -t docsearch:dev .

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

# ---- Per-environment wrappers ---------------------------------------------------------------------

deploy-to-testsliderule: ## First-time deploy: ECR → image push → full stack at search.testsliderule.org
	make terraform-apply-ecr DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org && \
	make deploy-lambda       DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org && \
	make terraform-apply     DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

update-testsliderule: ## Routine update: rebuild image + update Lambda at search.testsliderule.org
	make deploy-lambda DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

update-infra-testsliderule: ## Terraform-only update at search.testsliderule.org (WAF, DNS, CloudFront, etc. — no Lambda rebuild)
	make terraform-apply DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

destroy-testsliderule: ## Tear down search.testsliderule.org infrastructure
	make terraform-destroy DOMAIN=search.testsliderule.org DOMAIN_APEX=testsliderule.org

smoketest-testsliderule: ## Smoketest against search.testsliderule.org
	make smoketest DOMAIN=search.testsliderule.org

logs-testsliderule: ## Tail CloudWatch logs for search.testsliderule.org
	make logs DOMAIN=search.testsliderule.org

deploy-to-slideruleearth: ## First-time deploy: ECR → image push → full stack at search.slideruleearth.io
	make terraform-apply-ecr DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io && \
	make deploy-lambda       DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io && \
	make terraform-apply     DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

update-slideruleearth: ## Routine update: rebuild image + update Lambda at search.slideruleearth.io
	make deploy-lambda DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

update-infra-slideruleearth: ## Terraform-only update at search.slideruleearth.io (WAF, DNS, CloudFront, etc. — no Lambda rebuild)
	make terraform-apply DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

destroy-slideruleearth: ## Tear down search.slideruleearth.io infrastructure
	make terraform-destroy DOMAIN=search.slideruleearth.io DOMAIN_APEX=slideruleearth.io

smoketest-slideruleearth: ## Smoketest against search.slideruleearth.io
	make smoketest DOMAIN=search.slideruleearth.io

logs-slideruleearth: ## Tail CloudWatch logs for search.slideruleearth.io
	make logs DOMAIN=search.slideruleearth.io

# ---- Validation -----------------------------------------------------------------------------------

check-vars:
	@test -n "$(DOMAIN)"          || (echo "❌ DOMAIN is not set"; exit 1)
	@test -n "$(DOMAIN_APEX)"     || (echo "❌ DOMAIN_APEX is not set"; exit 1)
	@test -n "$(DISTRIBUTION_ID)" || (echo "❌ DISTRIBUTION_ID could not be resolved for DOMAIN=$(DOMAIN)"; exit 1)
	@echo "✅ All required variables are set:"
	@echo "   DOMAIN          = $(DOMAIN)"
	@echo "   DOMAIN_APEX     = $(DOMAIN_APEX)"
	@echo "   DISTRIBUTION_ID = $(DISTRIBUTION_ID)"
