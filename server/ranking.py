"""Pure ranking functions — cosine + IDF lexical + RRF fusion.

Lifted verbatim from the original client-side search.py. Keeping these
as pure functions (no I/O, no HTTP, no argparse) means both the Lambda
handler and the local freeplay REPL import the same implementation.

Any change to scoring semantics must happen here, not in the caller.
"""

from __future__ import annotations

import math
import re
import sys

import numpy as np

EXPECTED_EMBEDDER = "sentence-transformers/all-MiniLM-L6-v2"

# Minimal English stopwords. Intentionally small: we keep technical-looking
# tokens (atl03x, phoreal, etc.) through and only drop grammatical filler
# that would otherwise dilute IDF.
STOPWORDS = frozenset({
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "what", "which", "who", "when", "where", "why", "how",
    "and", "or", "but", "if", "then", "else", "of", "in", "on", "at",
    "to", "for", "with", "by", "as", "that", "this", "these", "those",
    "do", "does", "did", "can", "could", "should", "would",
    "i", "you", "he", "she", "it", "we", "they",
    "my", "your", "his", "her", "its", "our", "their",
    "me", "us", "them", "him",
})

# Identifier-friendly tokenizer: splits on non-alphanumeric, preserves
# underscores, lowercases. Keeps things like "atl03x" and "phoreal_18"
# as single tokens.
TOKEN_RE = re.compile(r"[a-z0-9_]+")

# Reciprocal rank fusion constant. k=60 is the value from the original
# RRF paper (Cormack et al. 2009); it damps the contribution of low-
# ranked items so the top few dominate without a single ranker winning
# everything.
RRF_K = 60


def tokenize(text: str) -> list[str]:
    """Lowercase + split on non-alphanumeric, drop length-1 tokens and
    grammatical stopwords."""
    return [
        t for t in TOKEN_RE.findall(text.lower())
        if len(t) > 1 and t not in STOPWORDS
    ]


def validate_corpus(corpus: dict) -> None:
    """Embeddings from a different model are not comparable to the
    query embedding we'll compute. Fail loudly instead of producing
    nonsense similarity scores."""
    found = corpus.get("embedder")
    if found != EXPECTED_EMBEDDER:
        print(
            f"ERROR: corpus was built with embedder '{found}', but this "
            f"server uses '{EXPECTED_EMBEDDER}'. Cosine similarity "
            f"between mismatched embedders is meaningless. Rebuild the "
            f"corpus or update the code.",
            file=sys.stderr,
        )
        sys.exit(2)


def lexical_signals(
    q_tokens: set[str],
    per_chunk_tokens: list[set[str]],
) -> tuple[list[int], list[list[str]]]:
    """Compute IDF-weighted lexical ranks per chunk.

    Returns (ranks, matched_tokens_per_chunk). ranks[i] is the chunk's
    1-based rank by lexical score (1 = best). matched_tokens_per_chunk[i]
    lists the query tokens that appeared in chunks[i].

    IDF formula: log((N+1) / (df+1)). A token in 1 of 1500 chunks
    contributes ~7.3 per match; a token in 1000 of 1500 contributes
    ~0.4. This is what rescues queries like "atl03x" — the rare token's
    IDF outweighs any shared prose.

    Unlike the original client-side helper, per_chunk_tokens is passed
    in precomputed; a Lambda tokenizes every chunk once at cold start
    and reuses the sets across requests.
    """
    n_chunks = len(per_chunk_tokens)

    if not q_tokens or n_chunks == 0:
        # No lexical signal available — flat ranking so RRF falls
        # through to pure semantic.
        return [n_chunks] * n_chunks, [[] for _ in per_chunk_tokens]

    idf: dict[str, float] = {}
    for t in q_tokens:
        df = sum(1 for toks in per_chunk_tokens if t in toks)
        idf[t] = math.log((n_chunks + 1) / (df + 1))

    matched_per_chunk = [sorted(q_tokens & toks) for toks in per_chunk_tokens]
    scores = [sum(idf[t] for t in m) for m in matched_per_chunk]

    order = sorted(range(n_chunks), key=lambda i: (-scores[i], i))
    ranks = [0] * n_chunks
    for rank, idx in enumerate(order, start=1):
        ranks[idx] = rank
    return ranks, matched_per_chunk


def fuse_rrf(semantic_ranks: list[int], lexical_ranks: list[int]) -> list[float]:
    """Reciprocal rank fusion. score[i] = 1/(k+sem_rank) + 1/(k+lex_rank).

    Independently low ranks on both sides → tiny contribution; a top
    rank on either side → meaningful contribution. Symmetric weighting
    means neither signal can win a tied situation on its own.
    """
    return [
        1.0 / (RRF_K + s) + 1.0 / (RRF_K + lex)
        for s, lex in zip(semantic_ranks, lexical_ranks)
    ]


def _build_result_row(chunk: dict, cosine_score: float) -> dict:
    """Build one entry of the `results` array. Shared by fused and
    disable-lexical paths so they can't drift apart."""
    row = {
        "score": round(float(cosine_score), 4),
        "url": chunk.get("url", ""),
        "title": chunk.get("title", ""),
        "section": chunk.get("section", ""),
        "text": chunk.get("text", ""),
    }
    category = chunk.get("category")
    if category:
        row["category"] = category
    return row


def rank(
    chunks: list[dict],
    matrix,  # numpy ndarray, shape (n_chunks, 384), L2-normalized
    per_chunk_tokens: list[set[str]],
    query: str,
    query_vec,  # numpy ndarray, shape (384,), L2-normalized
    k: int,
    disable_lexical: bool = False,
) -> list[dict]:
    """Rank chunks by fused semantic + lexical signals, return top K.

    Caller owns the preprocessing: chunks + matrix + per_chunk_tokens
    are computed once at cold start; query + query_vec are per request.

    Ranking reflects RRF-fused ranks; the `score` on each result is
    cosine (display-friendly 0–1). So results[0].score > results[1].score
    isn't guaranteed — documented in SKILL.md.
    """
    if not chunks:
        return []

    cosine_scores = matrix @ query_vec

    if disable_lexical:
        # Preserve the pre-fusion behavior exactly for A/B comparison.
        idx_sorted = np.argsort(-cosine_scores)[:k]
        return [
            _build_result_row(chunks[int(i)], cosine_scores[int(i)])
            for i in idx_sorted
        ]

    sem_order = np.argsort(-cosine_scores)
    sem_ranks = np.empty(len(chunks), dtype=int)
    sem_ranks[sem_order] = np.arange(1, len(chunks) + 1)

    q_tokens = set(tokenize(query))
    lex_ranks, matched_per_chunk = lexical_signals(q_tokens, per_chunk_tokens)
    fused = fuse_rrf(sem_ranks.tolist(), lex_ranks)

    idx_sorted = sorted(range(len(chunks)), key=lambda i: (-fused[i], i))[:k]

    results = []
    for i in idx_sorted:
        row = _build_result_row(chunks[i], cosine_scores[i])
        if matched_per_chunk[i]:
            row["matched_tokens"] = matched_per_chunk[i]
        results.append(row)
    return results
