"""FastAPI app for sliderule-search-server.

Loads one or more corpora + the shared embedder at module import
(cold-start) and serves:

  POST /<corpus>/search     run the ranking pipeline, return top K
  GET  /<corpus>/meta       return precomputed corpus metadata
  GET  /healthz             liveness probe
  * (catch-all)             JSON 404

Today `<corpus>` is just `docsearch`; `nsidc` lands in a follow-up
commit. The per-corpus state lives in the `CORPORA` dict keyed by
corpus name, so adding a second corpus is a registration + route
pair, not a module-level refactor.

Each corpus is baked into the Lambda image by the Dockerfile (the
skill-server publishes static artifacts, not live S3 reads), so
cold-start load is a `Path.read_bytes()` and a numpy matmul setup.
A corpus rebuild means a new image, which means a new container,
which means fresh in-memory state and a fresh corpus_sha256.
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

# Per-corpus source paths. Each corpus contributes two files: corpus.json
# (chunks + embeddings) and meta.json (build-time metadata). Env-var
# overrides let local dev point at generated/<corpus>/ directly; the Lambda
# image COPYs flat files into /var/task/ with a name prefix per corpus
# (see server/Dockerfile).
DOCSEARCH_CORPUS_PATH = Path(
    os.environ.get("DOCSEARCH_CORPUS_PATH", TASK_ROOT / "corpus.json")
)
DOCSEARCH_META_PATH = Path(
    os.environ.get("DOCSEARCH_META_PATH", TASK_ROOT / "meta.json")
)
NSIDC_CORPUS_PATH = Path(
    os.environ.get("NSIDC_CORPUS_PATH", TASK_ROOT / "nsidc_corpus.json")
)
NSIDC_META_PATH = Path(
    os.environ.get("NSIDC_META_PATH", TASK_ROOT / "nsidc_meta.json")
)

# Shared embedder artifacts. Env-var overrides let local dev point at
# generated/shared/ directly instead of /var/task/. Same model file +
# tokenizer the corpus builders use.
EMBEDDER_MODEL_PATH = Path(
    os.environ.get("EMBEDDER_MODEL_PATH", TASK_ROOT / "model.onnx")
)
EMBEDDER_TOKENIZER_PATH = Path(
    os.environ.get("EMBEDDER_TOKENIZER_PATH", TASK_ROOT / "tokenizer.json")
)


# -- Cold-start load ---------------------------------------------------------

def _load_corpus_state(corpus_path: Path, meta_path: Path) -> dict:
    """Load a corpus from disk and return its runtime state dict.

    Returned keys:
      corpus             the raw dict as loaded from JSON
      corpus_sha         hex sha256 of the corpus.json bytes
      chunks             corpus["chunks"] (reference, not a copy)
      matrix             (N, D) L2-normalized np.float32 embedding matrix
      per_chunk_tokens   list[set[str]] for lexical-overlap lookup
      corpus_meta        the dict served by /<corpus>/meta

    Failing here kills the Lambda init — which is exactly what we want
    if the image is malformed, so the function never serves broken
    traffic. CloudWatch captures the traceback.
    """
    t0 = time.time()

    raw = corpus_path.read_bytes()
    corpus_sha = hashlib.sha256(raw).hexdigest()
    corpus = json.loads(raw)
    ranking.validate_corpus(corpus)

    chunks = corpus.get("chunks", [])
    if not chunks:
        raise RuntimeError(f"corpus at {corpus_path} has no chunks")

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
    # comes from meta.json (generated alongside corpus.json by the
    # corpus builder) if present.
    meta_summary: dict = {
        "chunk_count": len(chunks),
        "embedder": corpus.get("embedder"),
        "embedding_dim": corpus.get("embedding_dim"),
        "corpus_sha256": corpus_sha,
    }
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_bytes())
            for key in ("built_at", "pages_crawled", "source_host"):
                if key in meta:
                    meta_summary[key] = meta[key]
        except (OSError, json.JSONDecodeError) as e:
            log.warning("failed to read meta.json at %s: %s", meta_path, e)

    log.info(
        "corpus %s loaded: %d chunks, sha=%s..., %.2fs",
        corpus_path.name, len(chunks), corpus_sha[:12], time.time() - t0,
    )
    return {
        "corpus": corpus,
        "corpus_sha": corpus_sha,
        "chunks": chunks,
        "matrix": matrix,
        "per_chunk_tokens": per_chunk_tokens,
        "corpus_meta": meta_summary,
    }


def _load_embedder():
    """Load the MiniLM ONNX session + tokenizer once at cold start.

    The model.onnx and tokenizer.json are baked into the Docker image
    at build time (copied from generated/shared/). No network call at
    runtime — onnxruntime just reads the local .onnx file. One embedder
    instance serves every corpus registered in CORPORA.
    """
    t0 = time.time()
    # Deferred import so --help-style tooling doesn't pay the cost.
    from server.embedder import MiniLMEmbedder

    model = MiniLMEmbedder(EMBEDDER_MODEL_PATH, EMBEDDER_TOKENIZER_PATH)
    log.info(
        "embedder loaded: %s in %.2fs",
        ranking.EXPECTED_EMBEDDER,
        time.time() - t0,
    )
    return model


# -- Module-level state ------------------------------------------------------

# Per-corpus state, keyed by corpus name. Each value is the dict returned
# by _load_corpus_state(). The two corpora share the embedder (MODEL
# below) and the LRU cache, but have independent chunks, matrix, sha,
# and meta.
CORPORA: dict[str, dict] = {
    "docsearch": _load_corpus_state(DOCSEARCH_CORPUS_PATH, DOCSEARCH_META_PATH),
    "nsidc": _load_corpus_state(NSIDC_CORPUS_PATH, NSIDC_META_PATH),
}

# Shared across all corpora. Both rely on a single model instance (saves
# ~80 MB of RAM per additional corpus) and a single result cache keyed
# by (corpus_name, query, ...) so cross-corpus entries can't collide.
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

app = FastAPI(title="sliderule-search-server", version="1.0.0")

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


# -- Per-corpus handler implementations --------------------------------------

def _search_impl(corpus_name: str, req: SearchRequest) -> dict:
    """Run the ranking pipeline for `corpus_name` against `req`.

    Shared by every /<corpus>/search route. Pulls per-corpus state out of
    CORPORA[corpus_name]; the MODEL and CACHE are shared module-level.
    """
    state = CORPORA[corpus_name]
    chunks = state["chunks"]
    matrix = state["matrix"]
    per_chunk_tokens = state["per_chunk_tokens"]
    corpus_sha = state["corpus_sha"]
    corpus_meta = state["corpus_meta"]

    # `None` means "no filter"; `[]` is explicit "zero matching categories" and
    # legitimately returns no results. Distinguish with `is not None`.
    cats_key = tuple(sorted(req.categories)) if req.categories is not None else None
    # corpus_name goes into the cache key for readability; corpus_sha
    # alone already uniquely identifies a corpus, so this is belt-and-
    # suspenders against future refactors that might drop the sha
    # dimension.
    cache_key = (corpus_name, req.query, req.top_k, req.disable_lexical, cats_key, corpus_sha)

    cached = CACHE.get(cache_key)
    if cached is not None:
        return cached

    if req.categories is not None:
        cat_set = set(req.categories)
        mask = np.array(
            [c.get("category") in cat_set for c in chunks],
            dtype=bool,
        )
        sub_chunks = [c for c, keep in zip(chunks, mask) if keep]
        sub_matrix = matrix[mask]
        sub_tokens = [t for t, keep in zip(per_chunk_tokens, mask) if keep]
    else:
        sub_chunks = chunks
        sub_matrix = matrix
        sub_tokens = per_chunk_tokens

    if not sub_chunks:
        response = {"query": req.query, "results": [], "corpus_meta": corpus_meta}
        CACHE.set(cache_key, response)
        return response

    # MiniLMEmbedder always returns (N, 384) float32 already-L2-normalized,
    # so no post-normalization step here (we used to re-normalize because
    # sentence-transformers' default didn't normalize).
    vec = MODEL.encode([req.query])[0]

    results = ranking.rank(
        sub_chunks, sub_matrix, sub_tokens,
        req.query, vec, req.top_k,
        disable_lexical=req.disable_lexical,
    )

    response = {
        "query": req.query,
        "results": results,
        "corpus_meta": corpus_meta,
    }
    CACHE.set(cache_key, response)
    return response


def _meta_impl(corpus_name: str) -> dict:
    """Return the /<corpus>/meta payload.

    Values come straight from cold-start state; the cache block is a
    runtime stat for operators poking at the endpoint.
    """
    return {**CORPORA[corpus_name]["corpus_meta"], "cache": CACHE.stats()}


# -- Routes ------------------------------------------------------------------

@app.post("/docsearch/search", response_model=SearchResponse)
def docsearch_search(req: SearchRequest) -> dict:
    return _search_impl("docsearch", req)


@app.get("/docsearch/meta")
def docsearch_meta() -> dict:
    return _meta_impl("docsearch")


@app.post("/nsidc/search", response_model=SearchResponse)
def nsidc_search(req: SearchRequest) -> dict:
    return _search_impl("nsidc", req)


@app.get("/nsidc/meta")
def nsidc_meta() -> dict:
    return _meta_impl("nsidc")


@app.get("/healthz")
def healthz() -> dict:
    # Response shape intentionally superset of the single-corpus era:
    # the top-level `corpus_sha256` field is preserved (pointing at the
    # docsearch corpus) so existing clients don't break; the new
    # `corpora` block enumerates every registered corpus. Add, don't
    # rename.
    return {
        "status": "ok",
        "corpus_sha256": CORPORA["docsearch"]["corpus_sha"],
        "corpora": {
            name: state["corpus_sha"]
            for name, state in CORPORA.items()
        },
    }


@app.api_route(
    "/{_path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
)
def _catch_all(_path: str) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"error": "not_found", "path": f"/{_path}"},
    )
