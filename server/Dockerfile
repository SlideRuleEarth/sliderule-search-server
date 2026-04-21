# syntax=docker/dockerfile:1.6
#
# Lambda container image for sliderule-search-server. Serves multiple
# corpora (docsearch + nsidc) out of one Lambda; see server/app.py's
# CORPORA dict for how they're routed.
#
# Three "heavy" items are baked in at build time so cold starts never
# reach the network:
#
#   1. sentence-transformers/all-MiniLM-L6-v2 (~90 MB) — pre-downloaded
#      into HF_HOME=/opt/hf-cache. HF_HUB_OFFLINE=1 at runtime enforces
#      no Hub call. One model instance serves every corpus.
#
#   2. generated/docsearch/corpus.json + meta.json — copied verbatim
#      into /var/task. The Lambda hashes corpus.json at cold start to
#      compute corpus_sha256.
#
#   3. generated/nsidc/corpus.json + meta.json — same deal, laid down
#      with `nsidc_` filename prefixes so both corpora coexist at the
#      task root. Environment variables in app.py (NSIDC_CORPUS_PATH,
#      DOCSEARCH_CORPUS_PATH) let local dev override without
#      rebuilding the image.
#
# Build from the repo root so the COPY paths resolve:
#
#   docker buildx build --platform linux/arm64 -f server/Dockerfile \
#     -t <ecr-url>:<tag> .

FROM public.ecr.aws/lambda/python:3.12

ENV HF_HOME=/opt/hf-cache \
    TRANSFORMERS_VERBOSITY=error \
    HF_HUB_VERBOSITY=error \
    TRANSFORMERS_OFFLINE=1 \
    HF_HUB_OFFLINE=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY server/requirements.txt ${LAMBDA_TASK_ROOT}/

# Install PyTorch CPU-only wheels FIRST. The default PyPI torch wheel
# ships ~2.5 GB of CUDA kernels we never use in Lambda (Lambda has no
# GPU). The CPU-only wheels are ~180 MB. Bypass the regular PyPI
# index for torch; install sentence-transformers afterwards and it
# will see torch is already satisfied and not re-install.
#
# Net effect on image size: ~5 GB → ~1 GB. Cold-start pulls + ECR
# storage + `docker push` time all improve proportionally.
RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch
RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Pre-download the sentence-transformer weights into HF_HOME. Bypass
# the offline flags for this single RUN so the Hub call succeeds; the
# rest of the image (and the runtime) stay offline.
RUN TRANSFORMERS_OFFLINE=0 HF_HUB_OFFLINE=0 python -c "\
from sentence_transformers import SentenceTransformer; \
SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

# Corpora + metadata. Both sets of files are committed in git; the
# image carries the exact bytes of the most recent
# `make rebuild-corpus-docsearch` / `make rebuild-corpus-nsidc` runs.
COPY generated/docsearch/corpus.json ${LAMBDA_TASK_ROOT}/corpus.json
COPY generated/docsearch/meta.json   ${LAMBDA_TASK_ROOT}/meta.json
COPY generated/nsidc/corpus.json     ${LAMBDA_TASK_ROOT}/nsidc_corpus.json
COPY generated/nsidc/meta.json       ${LAMBDA_TASK_ROOT}/nsidc_meta.json

# Application code. `server/__init__.py` is committed (empty) so
# `from server import …` works without a post-copy touch step.
COPY server/ ${LAMBDA_TASK_ROOT}/server/

CMD ["server.handler.lambda_handler"]
