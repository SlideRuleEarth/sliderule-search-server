# syntax=docker/dockerfile:1.6
#
# Lambda container image for sliderule-search-server. Serves multiple
# corpora (docsearch + nsidc) out of one Lambda; see server/app.py's
# CORPORA dict for how they're routed.
#
# Build-time inputs baked into the image (so cold starts never reach
# the network):
#
#   1. generated/shared/model.onnx + tokenizer.json — the MiniLM-L6-v2
#      weights exported to ONNX plus the matching WordPiece tokenizer
#      config. Loaded via onnxruntime + the `tokenizers` Rust library.
#
#   2. generated/docsearch/corpus.json + meta.json — copied verbatim
#      into /var/task. The Lambda hashes corpus.json at cold start to
#      compute corpus_sha256.
#
#   3. generated/nsidc/corpus.json + meta.json — same deal, laid down
#      with `nsidc_` filename prefixes so both corpora coexist at the
#      task root. Environment variables in app.py (NSIDC_CORPUS_PATH,
#      DOCSEARCH_CORPUS_PATH, EMBEDDER_MODEL_PATH, etc.) let local dev
#      override paths without rebuilding the image.
#
# Build from the repo root so the COPY paths resolve:
#
#   docker buildx build --platform linux/amd64 -f server/Dockerfile \
#     -t <ecr-url>:<tag> .
#
# Platform is linux/amd64 to match the x86_64 Lambda architecture
# (terraform/modules/lambda.tf). arm64 Lambda was abandoned after
# onnxruntime's bundled cpuinfo failed to parse Lambda arm64's
# restricted /sys/devices/system/cpu/*, terminating the container
# during init. x86_64 Lambda exposes a normal /sys, and cpuinfo works.

FROM public.ecr.aws/lambda/python:3.13

ENV PYTHONDONTWRITEBYTECODE=1

COPY server/requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Shared embedder artifacts. One model file + one tokenizer, same bytes
# the corpus builders used to produce the committed embeddings. Keeping
# these byte-equal across builder and server is the whole reason we ship
# them in the repo instead of re-downloading from Hugging Face — see
# server/embedder.py for the full rationale.
COPY generated/shared/model.onnx     ${LAMBDA_TASK_ROOT}/model.onnx
COPY generated/shared/tokenizer.json ${LAMBDA_TASK_ROOT}/tokenizer.json

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
