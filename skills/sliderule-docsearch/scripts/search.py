#!/usr/bin/env python3
"""Semantic search over the SlideRule docs corpus.

Fetches the static corpus (or reads it from --corpus-file), embeds the query
with the same sentence-transformer used at build time, and prints top-K
results as JSON to stdout.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

EXPECTED_EMBEDDER = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_CORPUS_URL = "https://search.testsliderule.org/docsearch/corpus.json"
CACHE_PATH = Path("/tmp/sliderule_docsearch_corpus.json")
CACHE_TTL_SECONDS = 24 * 60 * 60


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def resolve_corpus_url(args: argparse.Namespace) -> str:
    if args.corpus_url:
        return args.corpus_url
    base = os.environ.get("SLIDERULE_SEARCH_BASE")
    if base:
        return f"{base.rstrip('/')}/docsearch/corpus.json"
    return DEFAULT_CORPUS_URL


def load_corpus(args: argparse.Namespace) -> dict:
    if args.corpus_file:
        with open(args.corpus_file, "r", encoding="utf-8") as f:
            return json.load(f)

    url = resolve_corpus_url(args)
    cache_fresh = (
        CACHE_PATH.exists()
        and (time.time() - CACHE_PATH.stat().st_mtime) < CACHE_TTL_SECONDS
        and not args.force_refresh
    )
    if cache_fresh:
        log(f"Using cached corpus at {CACHE_PATH}")
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    log(f"Fetching corpus from {url}")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    CACHE_PATH.write_bytes(resp.content)
    return json.loads(resp.content)


def validate_corpus(corpus: dict) -> None:
    found = corpus.get("embedder")
    if found != EXPECTED_EMBEDDER:
        print(
            f"ERROR: corpus was built with embedder '{found}', but this script uses\n"
            f"'{EXPECTED_EMBEDDER}'. Cosine similarity between mismatched embedders is\n"
            f"meaningless. Rebuild the corpus or update the script.",
            file=sys.stderr,
        )
        sys.exit(2)


def embed_query(query: str):
    import numpy as np
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(EXPECTED_EMBEDDER)
    vec = model.encode([query], convert_to_numpy=True)[0]
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec


def top_k(corpus: dict, query_vec, k: int):
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


def corpus_meta_summary(corpus: dict, args: argparse.Namespace) -> dict:
    summary = {
        "chunk_count": len(corpus.get("chunks", [])),
        "embedder": corpus.get("embedder"),
        "embedding_dim": corpus.get("embedding_dim"),
    }
    meta_path = None
    if args.corpus_file:
        meta_path = Path(args.corpus_file).parent / "meta.json"
    if meta_path and meta_path.exists():
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            summary["built_at"] = meta.get("built_at")
        except (OSError, json.JSONDecodeError):
            pass
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="The search query.")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--corpus-url", default=None)
    parser.add_argument("--corpus-file", default=None)
    parser.add_argument("--force-refresh", action="store_true")
    args = parser.parse_args()

    corpus = load_corpus(args)
    validate_corpus(corpus)

    query_vec = embed_query(args.query)
    results = top_k(corpus, query_vec, args.top_k)

    output = {
        "query": args.query,
        "results": results,
        "corpus_meta": corpus_meta_summary(corpus, args),
    }
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
