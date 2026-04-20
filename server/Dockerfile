# syntax=docker/dockerfile:1.6
#
# Lambda container image for sliderule-docsearch.
#
# Two "heavy" items are baked in at build time so cold starts never reach
# the network:
#
#   1. sentence-transformers/all-MiniLM-L6-v2 (~90 MB) — pre-downloaded
#      into HF_HOME=/opt/hf-cache. HF_HUB_OFFLINE=1 at runtime enforces
#      no Hub call.
#
#   2. generated/docsearch/corpus.json + meta.json — copied verbatim
#      into /var/task. The Lambda hashes corpus.json at cold start to
#      compute corpus_sha256.
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
RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Pre-download the sentence-transformer weights into HF_HOME. Bypass
# the offline flags for this single RUN so the Hub call succeeds; the
# rest of the image (and the runtime) stay offline.
RUN TRANSFORMERS_OFFLINE=0 HF_HUB_OFFLINE=0 python -c "\
from sentence_transformers import SentenceTransformer; \
SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

# Corpus + metadata. Both committed in git; the image carries the
# exact bytes of the most recent `make rebuild-corpus` run.
COPY generated/docsearch/corpus.json ${LAMBDA_TASK_ROOT}/corpus.json
COPY generated/docsearch/meta.json   ${LAMBDA_TASK_ROOT}/meta.json

# Application code. `server/__init__.py` is committed (empty) so
# `from server import …` works without a post-copy touch step.
COPY server/ ${LAMBDA_TASK_ROOT}/server/

CMD ["server.handler.lambda_handler"]
