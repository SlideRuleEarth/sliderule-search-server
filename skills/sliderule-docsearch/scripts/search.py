#!/usr/bin/env python3
"""Semantic search over the SlideRule docs corpus.

Two modes of operation:

  * --corpus-file PATH    read corpus from disk (no network; used in
                          development before the server is up).

  * remote (default)      fetch meta.json on every invocation, look up
                          a local corpus cache keyed by meta's
                          corpus_sha256 fingerprint, and only re-download
                          corpus.json when the fingerprint changes.

The meta.json-driven cache is the key design point. meta.json is tiny
(~300 bytes) and checking it every invocation is essentially free; the
corpus itself is ~11 MB but only changes when the upstream server is
released (at most weekly). So we fetch meta every time and the corpus
almost never, and cache invalidation is immediate instead of lagging
behind a wall-clock TTL.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import requests

EXPECTED_EMBEDDER = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_BASE_URL = "https://search.testsliderule.org"
DEFAULT_CORPUS_PATH = "/docsearch/corpus.json"
DEFAULT_META_PATH = "/docsearch/meta.json"

# Per-user cache root. We drop corpus files here keyed by their sha256
# so switching bases (test/prod) or picking up a freshly-released
# corpus doesn't collide with a stale cached copy.
CACHE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "sliderule_docsearch"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def resolve_urls(args: argparse.Namespace) -> tuple[str, str]:
    """Return (corpus_url, meta_url) based on flags + env + defaults.

    Precedence: explicit --corpus-url / --meta-url > SLIDERULE_SEARCH_BASE
    env var > built-in default. The two URLs are independent so a dev can
    point at a local file server for the corpus while still hitting prod
    meta, etc.
    """
    base = os.environ.get("SLIDERULE_SEARCH_BASE", DEFAULT_BASE_URL).rstrip("/")
    corpus_url = args.corpus_url or f"{base}{DEFAULT_CORPUS_PATH}"
    meta_url = args.meta_url or f"{base}{DEFAULT_META_PATH}"
    return corpus_url, meta_url


def cache_path_for(sha: str) -> Path:
    """Content-addressed cache filename.

    Using the corpus's own sha256 as the filename means: (a) concurrent
    versions can coexist on disk without overwriting each other, and
    (b) the existence of the file is itself a correctness check — a
    file at cache_path_for(X) is known to have hash X.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR / f"corpus_{sha}.json"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def fetch_meta(url: str) -> dict:
    """Pull the current meta.json from the distribution."""
    log(f"Fetching meta from {url}")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.json()


def load_corpus_from_url(
    corpus_url: str, meta: dict, force_refresh: bool
) -> tuple[dict, Path]:
    """Fetch corpus.json if our cache doesn't already have the sha'd copy.

    Also verifies the downloaded bytes actually hash to what meta said
    they would — a mismatch means either meta.json on the server is
    stale relative to corpus.json, or something tampered with the
    response in flight. Either way, refuse to load it.
    """
    sha = meta.get("corpus_sha256")
    if not sha:
        print(
            "ERROR: meta.json has no corpus_sha256 field. The server was "
            "built with an older tools/build_docsearch_corpus.py that "
            "doesn't emit this. Rebuild the corpus.",
            file=sys.stderr,
        )
        sys.exit(2)

    cache_path = cache_path_for(sha)

    if cache_path.exists() and not force_refresh:
        log(f"Using cached corpus at {cache_path}")
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f), cache_path

    log(f"Fetching corpus from {corpus_url}  (sha={sha[:12]}...)")
    resp = requests.get(corpus_url, timeout=120)
    resp.raise_for_status()

    actual = hashlib.sha256(resp.content).hexdigest()
    if actual != sha:
        print(
            f"ERROR: downloaded corpus hash {actual[:12]}... does not "
            f"match meta.json's corpus_sha256 {sha[:12]}.... Server "
            f"artifacts are in an inconsistent state; refusing to "
            f"proceed.",
            file=sys.stderr,
        )
        sys.exit(2)

    # Atomic write: stage under a tmp name then rename, so a Ctrl-C
    # mid-write never leaves a half-written file at cache_path_for(sha).
    tmp = cache_path.with_suffix(".json.partial")
    tmp.write_bytes(resp.content)
    tmp.replace(cache_path)
    return json.loads(resp.content), cache_path


def load_corpus(args: argparse.Namespace) -> tuple[dict, dict | None]:
    """Return (corpus, meta) — meta is None only in --corpus-file mode
    if there's no sibling meta.json on disk."""
    if args.corpus_file:
        with open(args.corpus_file, "r", encoding="utf-8") as f:
            corpus = json.load(f)
        # Opportunistically pick up a sibling meta.json for built_at.
        meta_path = Path(args.corpus_file).parent / "meta.json"
        meta = None
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
            except (OSError, json.JSONDecodeError):
                meta = None
        return corpus, meta

    corpus_url, meta_url = resolve_urls(args)
    meta = fetch_meta(meta_url)
    corpus, _cache_path = load_corpus_from_url(
        corpus_url, meta, force_refresh=args.force_refresh
    )
    return corpus, meta


def validate_corpus(corpus: dict) -> None:
    """Embeddings from a different model are not comparable to the
    query embedding we'll compute. Fail loudly instead of producing
    nonsense similarity scores."""
    found = corpus.get("embedder")
    if found != EXPECTED_EMBEDDER:
        print(
            f"ERROR: corpus was built with embedder '{found}', but this "
            f"script uses '{EXPECTED_EMBEDDER}'. Cosine similarity "
            f"between mismatched embedders is meaningless. Rebuild the "
            f"corpus or update the script.",
            file=sys.stderr,
        )
        sys.exit(2)


def embed_query(query: str):
    """Turn the query string into a unit-length 384-dim vector, ready
    to dot-product against the pre-computed chunk matrix."""
    import numpy as np
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(EXPECTED_EMBEDDER)
    vec = model.encode([query], convert_to_numpy=True)[0]
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec


def top_k(corpus: dict, query_vec, k: int):
    """Cosine similarity between query_vec and every chunk's embedding,
    then take the top K. The matrix is tiny (1400ish × 384 floats) so
    this is a single numpy matmul, microseconds in practice."""
    import numpy as np

    chunks = corpus.get("chunks", [])
    if not chunks:
        return []

    matrix = np.asarray([c["embedding"] for c in chunks], dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1)
    norms[norms == 0] = 1.0
    matrix = matrix / norms[:, None]

    scores = matrix @ query_vec
    idx_sorted = np.argsort(-scores)[:k]
    results = []
    for i in idx_sorted:
        c = chunks[int(i)]
        results.append(
            {
                "score": round(float(scores[int(i)]), 4),
                "url": c.get("url", ""),
                "title": c.get("title", ""),
                "section": c.get("section", ""),
                "text": c.get("text", ""),
            }
        )
    return results


def corpus_meta_summary(corpus: dict, meta: dict | None) -> dict:
    """Compact metadata block that goes into the search output. Always
    includes corpus-derived fields (embedder, chunk_count), and
    augments with built_at / corpus_sha256 / built-time signals from
    meta.json when available."""
    summary: dict = {
        "chunk_count": len(corpus.get("chunks", [])),
        "embedder": corpus.get("embedder"),
        "embedding_dim": corpus.get("embedding_dim"),
    }
    if meta:
        for key in ("built_at", "corpus_sha256", "pages_crawled", "source_host"):
            if key in meta:
                summary[key] = meta[key]
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="The search query.")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--corpus-url", default=None,
                        help="Override corpus URL (otherwise derived from base).")
    parser.add_argument("--meta-url", default=None,
                        help="Override meta URL (otherwise derived from base).")
    parser.add_argument("--corpus-file", default=None,
                        help="Read corpus from local path; skip remote fetch.")
    parser.add_argument("--force-refresh", action="store_true",
                        help="Re-download corpus even if a cached copy exists.")
    args = parser.parse_args()

    corpus, meta = load_corpus(args)
    validate_corpus(corpus)

    query_vec = embed_query(args.query)
    results = top_k(corpus, query_vec, args.top_k)

    output = {
        "query": args.query,
        "results": results,
        "corpus_meta": corpus_meta_summary(corpus, meta),
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
