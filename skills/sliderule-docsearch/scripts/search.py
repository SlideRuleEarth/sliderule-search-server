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
import math
import os
import re
import sys
from pathlib import Path

# Quiet two known-benign HuggingFace banners that would otherwise print
# every time search.py runs. Set via env vars (rather than calling the
# libraries' logging APIs) so this works before 'import transformers'
# has happened — the first import is deep inside sentence_transformers.
# setdefault() means a user who explicitly overrides these in their
# shell keeps control.
#
#   TRANSFORMERS_VERBOSITY=error
#     Hides the BertModel LOAD REPORT with the
#     'embeddings.position_ids UNEXPECTED' line. That tensor is a
#     fixed arange(max_len) buffer that older transformers versions
#     registered and newer versions compute on the fly — the
#     mismatch is cosmetic, not functional.
#
#   HF_HUB_VERBOSITY=error
#     Hides the 'Warning: You are sending unauthenticated requests
#     to the HF Hub' message. Anonymous downloads are fine for our
#     volume; rate limits only bite if you're hammering the Hub.
#
# We intentionally do NOT set HF_HUB_DISABLE_PROGRESS_BARS — cold-start
# model downloads (~80 MB) show a progress bar, which is the useful
# feedback a user wants on a fresh install.
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
os.environ.setdefault("HF_HUB_VERBOSITY", "error")

import requests

EXPECTED_EMBEDDER = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_BASE_URL = "https://search.testsliderule.org"
DEFAULT_CORPUS_PATH = "/docsearch/corpus.json"
DEFAULT_META_PATH = "/docsearch/meta.json"

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


def tokenize(text: str) -> list[str]:
    """Lowercase + split on non-alphanumeric, drop length-1 tokens and
    grammatical stopwords. Preserves identifier-shaped tokens like
    'atl03x', 'phoreal', 'atl06_land_ice_height' intact."""
    return [
        t for t in TOKEN_RE.findall(text.lower())
        if len(t) > 1 and t not in STOPWORDS
    ]


def lexical_signals(
    query: str, chunks: list[dict]
) -> tuple[list[int], list[list[str]]]:
    """Compute IDF-weighted lexical scores per chunk, return (ranks,
    matched_tokens_per_chunk).

    ranks[i] is chunks[i]'s 1-based rank by lexical score (1 = best).
    matched_tokens_per_chunk[i] lists the query tokens that appeared
    in chunks[i] — surfaced in the output so agents can see *why* a
    result ranked high.

    IDF formula: log((N+1) / (df+1)). Rare terms dominate common ones.
    A token in 1 of 1500 chunks contributes ~7.3 per match; a token
    in 1000 of 1500 contributes ~0.4. That's what rescues queries
    like "atl03x" — the rare token's IDF outweighs any shared prose.
    """
    q_tokens = set(tokenize(query))
    n_chunks = len(chunks)

    if not q_tokens or n_chunks == 0:
        # No lexical signal available — report a flat ranking so the
        # caller's fusion just falls through to the semantic rank.
        return [n_chunks] * n_chunks, [[] for _ in chunks]

    # Tokenize each chunk once. Section is worth including because
    # headings often contain the most-distinctive tokens (e.g. an
    # "ATL03x" section heading is a stronger signal than a passing
    # mention in prose).
    per_chunk_tokens = [
        set(tokenize(c.get("text", "") + " " + c.get("section", "")))
        for c in chunks
    ]

    idf = {}
    for t in q_tokens:
        df = sum(1 for toks in per_chunk_tokens if t in toks)
        idf[t] = math.log((n_chunks + 1) / (df + 1))

    matched_per_chunk = [sorted(q_tokens & toks) for toks in per_chunk_tokens]
    scores = [sum(idf[t] for t in m) for m in matched_per_chunk]

    # Sort by score desc; ties broken by chunk index for stability.
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
        1.0 / (RRF_K + s) + 1.0 / (RRF_K + l)
        for s, l in zip(semantic_ranks, lexical_ranks)
    ]


def _build_result_row(chunk: dict, cosine_score: float) -> dict:
    """Build one entry of the `results` array.

    Shared by the fused and disable-lexical code paths so they can't
    drift apart. `score` is always cosine (the display-friendly 0-1
    value); the ordering of the caller's list is what reflects
    fusion vs pure cosine. `category` is emitted only when the chunk
    actually has one — older corpora built before the tagging change
    won't, and we shouldn't leak a spurious null.
    """
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


def top_k(
    corpus: dict,
    query: str,
    query_vec,
    k: int,
    disable_lexical: bool = False,
) -> list[dict]:
    """Rank chunks by fused semantic + lexical signals, return top K.

    Semantic side: cosine similarity between query_vec and every chunk's
    embedding — a single matmul, microseconds.

    Lexical side: IDF-weighted token-overlap between query and chunk
    text (see lexical_signals). Rescues queries where the user's
    intent is a specific identifier (e.g. 'atl03x' vs 'atl03') that
    the embedder can't reliably distinguish from near-neighbors.

    The two ranks are fused with RRF. If disable_lexical=True the
    lexical signal is skipped entirely and results are pure cosine —
    useful for A/B comparison or when the query contains no
    identifier-like tokens.
    """
    import numpy as np

    chunks = corpus.get("chunks", [])
    if not chunks:
        return []

    matrix = np.asarray([c["embedding"] for c in chunks], dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1)
    norms[norms == 0] = 1.0
    matrix = matrix / norms[:, None]

    cosine_scores = matrix @ query_vec

    if disable_lexical:
        # Preserve the pre-fusion behavior exactly for A/B testing.
        idx_sorted = np.argsort(-cosine_scores)[:k]
        results = []
        for i in idx_sorted:
            c = chunks[int(i)]
            results.append(_build_result_row(c, cosine_scores[int(i)]))
        return results

    # Semantic rank (1-based, via argsort inversion).
    sem_order = np.argsort(-cosine_scores)
    sem_ranks = np.empty(len(chunks), dtype=int)
    sem_ranks[sem_order] = np.arange(1, len(chunks) + 1)

    lex_ranks, matched_per_chunk = lexical_signals(query, chunks)
    fused = fuse_rrf(sem_ranks.tolist(), lex_ranks)

    # Sort by fused score desc; stable by chunk index for reproducibility.
    idx_sorted = sorted(range(len(chunks)), key=lambda i: (-fused[i], i))[:k]

    results = []
    for i in idx_sorted:
        row = _build_result_row(chunks[i], cosine_scores[i])
        if matched_per_chunk[i]:
            # Only emit when nonempty — keeps output tidy for pure
            # semantic matches that don't share any identifier tokens.
            row["matched_tokens"] = matched_per_chunk[i]
        results.append(row)
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


def print_human_table(results: list[dict]) -> None:
    """Render results as a compact per-line summary for the REPL.

    One line per hit: rank, cosine score (display-only; ordering uses
    the fused RRF score), short URL tail (host-stripped), first ~80
    chars of text, and matched_tokens if present. Much easier to scan
    than the JSON we emit in one-shot mode.
    """
    if not results:
        print("  (no results)")
        return
    for i, r in enumerate(results, 1):
        url = r.get("url", "")
        for prefix in ("https://docs.slideruleearth.io/",
                       "https://", "http://"):
            if url.startswith(prefix):
                url = url[len(prefix):]
                break
        text = r.get("text", "")
        if len(text) > 80:
            text = text[:77] + "..."
        matched = r.get("matched_tokens")
        mt_str = f"  matched={matched}" if matched else ""
        # Category shows up before the URL so you can eyeball at a
        # glance whether a hit is user_guide, release_notes, etc.
        # Fixed-width column keeps things aligned across rows; we
        # show a short dash for chunks without a category (older
        # corpora).
        category = r.get("category") or "-"
        # Pad columns so text aligns across rows regardless of
        # variable-length category/URL.
        print(
            f"  {i}. {r['score']:.3f}  "
            f"[{category:<15}]  {url[:55]:<55}  {text}{mt_str}"
        )


REPL_HELP = """\
Commands:
  :k N          change top-k (current: {k})
  :lex on|off   toggle lexical fusion (current: {lex})
  :help         show this help
  Ctrl-D        exit
Anything else is treated as a search query."""


def handle_repl_command(line: str, state: dict) -> None:
    """Parse and apply a ':command' entered in the REPL.

    Only state-mutating commands live here. Anything unrecognized
    just prints a hint — we never raise, because the user is sitting
    at a prompt and expects to keep typing.
    """
    parts = line[1:].split()
    if not parts:
        return
    cmd = parts[0]
    if cmd in ("help", "h", "?"):
        print(REPL_HELP.format(
            k=state["top_k"],
            lex="off" if state["disable_lexical"] else "on",
        ))
    elif cmd == "k":
        if len(parts) < 2 or not parts[1].isdigit() or int(parts[1]) < 1:
            print("usage: :k <N>  (positive integer)")
            return
        state["top_k"] = int(parts[1])
        print(f"top_k={state['top_k']}")
    elif cmd == "lex":
        if len(parts) < 2 or parts[1] not in ("on", "off"):
            print("usage: :lex on|off")
            return
        state["disable_lexical"] = (parts[1] == "off")
        print(f"lexical={'off' if state['disable_lexical'] else 'on'}")
    else:
        print(f"unknown command: :{cmd}  (try :help)")


def run_repl(corpus: dict, meta: dict | None, args: argparse.Namespace) -> int:
    """Interactive search loop.

    Loads the sentence-transformer model once (~3s) and then processes
    queries from stdin until EOF/Ctrl-D. Each subsequent query is
    <100ms, which makes this the right tool for iterating on wording,
    toggling lexical fusion on/off for comparison, and sanity-checking
    the corpus after a rebuild.
    """
    import numpy as np
    from sentence_transformers import SentenceTransformer

    log("Loading embedder (one-time, ~3s)...")
    model = SentenceTransformer(EXPECTED_EMBEDDER)

    # State mutated by :commands. Kept in a dict so handle_repl_command
    # can update it in place without passing a slew of out-parameters.
    state = {
        "top_k": args.top_k,
        "disable_lexical": args.disable_lexical,
    }

    built_at = meta.get("built_at", "unknown") if meta else "unknown"
    sha = (meta.get("corpus_sha256") or "")[:12] if meta else ""
    chunk_count = len(corpus.get("chunks", []))

    print()
    print(f"Corpus: {chunk_count} chunks, built_at {built_at}"
          + (f", sha={sha}" if sha else ""))
    print(f"top_k={state['top_k']}, "
          f"lexical={'off' if state['disable_lexical'] else 'on'}")
    print("Commands: :k N   :lex on|off   :help   (Ctrl-D to exit)")
    print()

    while True:
        try:
            line = input("search> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()  # trailing newline after ^D
            return 0

        if not line:
            continue

        if line.startswith(":"):
            handle_repl_command(line, state)
            continue

        # Normal query: embed, score, print. Uses the same top_k() as
        # the one-shot code path, so results match exactly.
        vec = model.encode([line], convert_to_numpy=True)[0]
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        results = top_k(
            corpus, line, vec, state["top_k"],
            disable_lexical=state["disable_lexical"],
        )
        print_human_table(results)
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    # query is optional so --repl can run without one. We validate
    # below that exactly one of (query, --repl) is provided.
    parser.add_argument("query", nargs="?", default=None,
                        help="The search query. Required unless --repl is set.")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--corpus-url", default=None,
                        help="Override corpus URL (otherwise derived from base).")
    parser.add_argument("--meta-url", default=None,
                        help="Override meta URL (otherwise derived from base).")
    parser.add_argument("--corpus-file", default=None,
                        help="Read corpus from local path; skip remote fetch.")
    parser.add_argument("--force-refresh", action="store_true",
                        help="Re-download corpus even if a cached copy exists.")
    parser.add_argument("--disable-lexical", action="store_true",
                        help=(
                            "Skip the lexical rank-fusion step. Results become "
                            "pure cosine similarity, matching the pre-fusion "
                            "behavior. Mainly for A/B comparison — leave off for "
                            "normal use, where the lexical boost helps identifier-"
                            "shaped queries (e.g. 'atl03x' vs 'atl03')."
                        ))
    parser.add_argument("--repl", action="store_true",
                        help=(
                            "Drop into an interactive search loop instead of "
                            "running one query and exiting. Loads the embedder "
                            "model once, then processes queries from stdin "
                            "until Ctrl-D. Use :help inside the REPL for "
                            "supported commands. See also: 'make freeplay'."
                        ))
    args = parser.parse_args()

    # query is required unless --repl is set; enforce here rather than
    # via argparse since the rule is "exactly one of the two."
    if not args.repl and not args.query:
        parser.error("query is required (or pass --repl for interactive mode)")
    if args.repl and args.query:
        parser.error("--repl is mutually exclusive with a positional query")

    corpus, meta = load_corpus(args)
    validate_corpus(corpus)

    if args.repl:
        return run_repl(corpus, meta, args)

    query_vec = embed_query(args.query)
    results = top_k(
        corpus, args.query, query_vec, args.top_k,
        disable_lexical=args.disable_lexical,
    )

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
