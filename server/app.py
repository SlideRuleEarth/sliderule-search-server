"""FastAPI app for /docsearch/search.

Loads the corpus + model at module import (cold-start) and serves:

  POST /docsearch/search     run the ranking pipeline, return top K
  GET  /docsearch/meta       return precomputed corpus metadata
  GET  /healthz              liveness probe
  * (catch-all)              JSON 404

The corpus is baked into the Lambda image at /var/task/corpus.json
(committed from generated/docsearch/corpus.json by the Dockerfile),
so there's no S3 round-trip and no freshness polling — a corpus
rebuild means a new image, which means a new container, which means
a fresh in-memory corpus and CORPUS_SHA.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from pathlib import Path

import numpy as np
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from server import ranking
from server.cache import LRUCache

log = logging.getLogger("docsearch")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")

# -- Paths --------------------------------------------------------------------

# /var/task is the Lambda container working dir; overridable for local dev
# where the repo layout differs.
TASK_ROOT = Path(os.environ.get("LAMBDA_TASK_ROOT", "/var/task"))
CORPUS_PATH = Path(os.environ.get("DOCSEARCH_CORPUS_PATH", TASK_ROOT / "corpus.json"))
META_PATH = Path(os.environ.get("DOCSEARCH_META_PATH", TASK_ROOT / "meta.json"))


# -- Cold-start load ---------------------------------------------------------

def _load_corpus_and_matrix() -> tuple[dict, str, "np.ndarray", list[set[str]], dict]:
    """Read corpus.json (+ optional meta.json) once at import, return the
    parsed corpus, its sha256, the L2-normalized embedding matrix, the
    tokenized-per-chunk lookup, and the static corpus_meta block.

    Failing here kills the Lambda init — which is exactly what we want
    if the image is malformed, so the function never serves broken
    traffic. CloudWatch captures the traceback.
    """
    t0 = time.time()

    raw = CORPUS_PATH.read_bytes()
    corpus_sha = hashlib.sha256(raw).hexdigest()
    corpus = json.loads(raw)
    ranking.validate_corpus(corpus)

    chunks = corpus.get("chunks", [])
    if not chunks:
        raise RuntimeError(f"corpus at {CORPUS_PATH} has no chunks")

    matrix = np.asarray([c["embedding"] for c in chunks], dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1)
    norms[norms == 0] = 1.0
    matrix = matrix / norms[:, None]

    # Tokenize each chunk once — lexical signals reuse this on every
    # request. Section included because headings carry distinctive
    # tokens (matches the original search.py behavior).
    per_chunk_tokens = [
        set(ranking.tokenize(c.get("text", "") + " " + c.get("section", "")))
        for c in chunks
    ]

    # Corpus metadata: chunk_count / embedder / embedding_dim from the
    # corpus itself; corpus_sha256 is computed fresh above; built_at
    # comes from meta.json (generated alongside corpus.json by
    # tools/build_docsearch_corpus.py) if present.
    meta_summary: dict = {
        "chunk_count": len(chunks),
        "embedder": corpus.get("embedder"),
        "embedding_dim": corpus.get("embedding_dim"),
        "corpus_sha256": corpus_sha,
    }
    if META_PATH.exists():
        try:
            meta = json.loads(META_PATH.read_bytes())
            for key in ("built_at", "pages_crawled", "source_host"):
                if key in meta:
                    meta_summary[key] = meta[key]
        except (OSError, json.JSONDecodeError) as e:
            log.warning("failed to read meta.json: %s", e)

    log.info(
        "corpus loaded: %d chunks, sha=%s..., %.2fs",
        len(chunks), corpus_sha[:12], time.time() - t0,
    )
    return corpus, corpus_sha, matrix, per_chunk_tokens, meta_summary


def _load_embedder():
    """Load the sentence-transformer model once at cold start.

    The model is pre-downloaded into the Docker image via a RUN step,
    and HF_HOME is set so sentence-transformers reads from there. With
    HF_HUB_OFFLINE=1 we guarantee no network call at runtime.
    """
    t0 = time.time()
    # Deferred import so --help-style tooling doesn't pay the cost.
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(ranking.EXPECTED_EMBEDDER)
    log.info("embedder loaded: %s in %.2fs", ranking.EXPECTED_EMBEDDER, time.time() - t0)
    return model


CORPUS, CORPUS_SHA, MATRIX, PER_CHUNK_TOKENS, CORPUS_META = _load_corpus_and_matrix()
CHUNKS: list[dict] = CORPUS["chunks"]
MODEL = _load_embedder()
CACHE = LRUCache(maxsize=1024)


# -- Request / response models -----------------------------------------------

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=2000)
    top_k: int = Field(5, ge=1, le=50)
    disable_lexical: bool = False
    categories: list[str] | None = None


class SearchResponse(BaseModel):
    query: str
    results: list[dict]
    corpus_meta: dict


# -- FastAPI app -------------------------------------------------------------

app = FastAPI(title="sliderule-docsearch", version="1.0.0")

# CORSMiddleware primarily exists to short-circuit OPTIONS preflights with a
# 2xx status. The response CORS headers it emits are then overridden by
# CloudFront's response-headers policy (origin_override=true) — which is
# fine; what matters is that preflight returns 2xx so real browsers actually
# send the follow-up POST. Without this, OPTIONS falls through to the
# catch-all 404 below and browsers reject the preflight.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    max_age=86400,
)


@app.exception_handler(RequestValidationError)
async def _validation_error(_request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "validation_error", "detail": exc.errors()},
    )


@app.post("/docsearch/search", response_model=SearchResponse)
def search(req: SearchRequest) -> dict:
    # `None` means "no filter"; `[]` is explicit "zero matching categories" and
    # legitimately returns no results. Distinguish with `is not None`.
    cats_key = tuple(sorted(req.categories)) if req.categories is not None else None
    cache_key = (req.query, req.top_k, req.disable_lexical, cats_key, CORPUS_SHA)

    cached = CACHE.get(cache_key)
    if cached is not None:
        return cached

    if req.categories is not None:
        cat_set = set(req.categories)
        mask = np.array(
            [c.get("category") in cat_set for c in CHUNKS],
            dtype=bool,
        )
        sub_chunks = [c for c, keep in zip(CHUNKS, mask) if keep]
        sub_matrix = MATRIX[mask]
        sub_tokens = [t for t, keep in zip(PER_CHUNK_TOKENS, mask) if keep]
    else:
        sub_chunks = CHUNKS
        sub_matrix = MATRIX
        sub_tokens = PER_CHUNK_TOKENS

    if not sub_chunks:
        response = {"query": req.query, "results": [], "corpus_meta": CORPUS_META}
        CACHE.set(cache_key, response)
        return response

    vec = MODEL.encode([req.query], convert_to_numpy=True)[0]
    norm = float(np.linalg.norm(vec))
    if norm > 0:
        vec = vec / norm

    results = ranking.rank(
        sub_chunks, sub_matrix, sub_tokens,
        req.query, vec, req.top_k,
        disable_lexical=req.disable_lexical,
    )

    response = {
        "query": req.query,
        "results": results,
        "corpus_meta": CORPUS_META,
    }
    CACHE.set(cache_key, response)
    return response


@app.get("/docsearch/meta")
def meta() -> dict:
    # Add a small cache block for operators poking at the endpoint; the
    # values themselves come straight from cold-start state.
    return {**CORPUS_META, "cache": CACHE.stats()}


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "corpus_sha256": CORPUS_SHA}


@app.api_route(
    "/{_path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
)
def _catch_all(_path: str) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"error": "not_found", "path": f"/{_path}"},
    )
