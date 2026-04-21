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
# `make rebuild-corpus` Just Work without requiring the user to
# `source .venv/bin/activate` first. Falls back to whatever python3 is
# on PATH — if that shell's python doesn't have the deps, the
# per-target import-check below prints a clear install hint instead
# of a raw ModuleNotFoundError traceback.
PYTHON := $(shell test -x $(ROOT)/.venv/bin/python && echo $(ROOT)/.venv/bin/python || echo python3)

.PHONY: help clean rebuild-corpus package-skill \
        freeplay build-image test-image run-image deploy-lambda smoketest \
        terraform-apply terraform-apply-ecr terraform-destroy check-vars \
        deploy-to-testsliderule deploy-to-slideruleearth \
        destroy-testsliderule destroy-slideruleearth \
        update-testsliderule update-slideruleearth \
        update-infra-testsliderule update-infra-slideruleearth \
        smoketest-testsliderule smoketest-slideruleearth

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

# ---- Corpus + dev iteration -----------------------------------------------------------------------

rebuild-corpus: ## Re-crawl docs.slideruleearth.io and regenerate generated/docsearch/
	@$(PYTHON) -c "import sentence_transformers, bs4, requests" 2>/dev/null || { \
	  echo "❌ builder dependencies missing in $(PYTHON)."; \
	  echo "   Install them one of two ways:"; \
	  echo "     (a) Repo-local venv (picked up automatically next run):"; \
	  echo "         python3 -m venv .venv \\"; \
	  echo "           && .venv/bin/pip install -r tools/requirements.txt"; \
	  echo "     (b) Your active Python environment:"; \
	  echo "         pip install -r tools/requirements.txt"; \
	  exit 1; \
	}
	$(PYTHON) $(ROOT)/tools/build_docsearch_corpus.py

freeplay: ## Interactive search REPL against the committed corpus (no deploy involved)
	@test -f $(CORPUS_FILE) || { \
	  echo "❌ $(CORPUS_FILE) is missing. Run 'make rebuild-corpus' first."; \
	  exit 1; \
	}
	@$(PYTHON) -c "import sentence_transformers, numpy, fastapi, pydantic" 2>/dev/null || { \
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

package-skill: ## Package skills/sliderule-docsearch/ into a .skill zip
	@bash $(ROOT)/scripts/package_skill.sh sliderule-docsearch

# ---- Lambda image build + deploy ------------------------------------------------------------------

# `build-image` is a local sanity check; it doesn't push. `deploy-lambda` is the real thing —
# it builds, pushes to ECR, and (if the Lambda already exists) updates its image_uri in place.
build-image: ## Locally build the Lambda container image (sanity check; no push)
	@test -f $(CORPUS_FILE) || { \
	  echo "❌ $(CORPUS_FILE) is missing. Run 'make rebuild-corpus' first."; \
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

# ---- Validation -----------------------------------------------------------------------------------

check-vars:
	@test -n "$(DOMAIN)"          || (echo "❌ DOMAIN is not set"; exit 1)
	@test -n "$(DOMAIN_APEX)"     || (echo "❌ DOMAIN_APEX is not set"; exit 1)
	@test -n "$(DISTRIBUTION_ID)" || (echo "❌ DISTRIBUTION_ID could not be resolved for DOMAIN=$(DOMAIN)"; exit 1)
	@echo "✅ All required variables are set:"
	@echo "   DOMAIN          = $(DOMAIN)"
	@echo "   DOMAIN_APEX     = $(DOMAIN_APEX)"
	@echo "   DISTRIBUTION_ID = $(DISTRIBUTION_ID)"
