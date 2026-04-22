# syntax=docker/dockerfile:1.6
#
# Corpus-builder container. Pinned to linux/amd64 because the Lambda
# server runs on x86_64 — keeping builder and server on the same arch
# guarantees the pre-computed chunk embeddings in the committed
# corpora agree bit-for-bit with the query embeddings the server
# computes at runtime. (The fp32 matmul implementations in
# onnxruntime differ slightly across architectures; we've sidestepped
# that by pinning both sides to the same one.)
#
# On an M-series Mac this image builds and runs via Rosetta 2 — a bit
# slower than native arm64 but well within the budget for
# once-a-while corpus rebuilds.
#
# Build once (cached thereafter by `make build-corpus-image`):
#   docker buildx build --load --platform linux/amd64 \
#     -f tools/Dockerfile.builder -t docsearch-corpus-builder:latest .
#
# Run a rebuild inside it (`make rebuild-corpus-docsearch` / `-nsidc`
# wrap this):
#   docker run --rm --platform linux/amd64 \
#     -v $PWD:/app -w /app docsearch-corpus-builder:latest \
#     python tools/build_docsearch_corpus.py

FROM python:3.13-slim

# zip is only used by tools/export_minilm_onnx.py's optimum path; the
# corpus builders themselves don't need it. git is unused at build time
# but helpful when debugging inside the container interactively.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Copy only requirements.txt at build time so the pip install layer is
# cached unless that file actually changes. The rest of the repo gets
# volume-mounted at run time.
COPY tools/requirements.txt /app/tools/requirements.txt
RUN pip install --no-cache-dir -r /app/tools/requirements.txt

# No ENTRYPOINT — the caller picks the builder script. Defaulting to a
# python version print makes `docker run <image>` with no args a
# harmless smoke check.
CMD ["python", "--version"]
