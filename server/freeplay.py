"""Local REPL for iterating on ranking against a committed corpus file.

Replaces the --repl mode that lived in the old search.py. Same behavior
(interactive search loop, :k / :lex / :help), but importing server.ranking
directly so local iteration and the deployed Lambda share exactly one
ranking implementation.

Usage:
  python -m server.freeplay --corpus-file generated/docsearch/corpus.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path



def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def print_human_table(results: list[dict]) -> None:
    """Same compact per-hit format the old search.py REPL printed."""
    if not results:
        print("  (no results)")
        return
    for i, r in enumerate(results, 1):
        url = r.get("url", "")
        for prefix in ("https://docs.slideruleearth.io/", "https://", "http://"):
            if url.startswith(prefix):
                url = url[len(prefix):]
                break
        text = r.get("text", "")
        if len(text) > 80:
            text = text[:77] + "..."
        matched = r.get("matched_tokens")
        mt_str = f"  matched={matched}" if matched else ""
        category = r.get("category") or "-"
        print(
            f"  {i}. {r['score']:.3f}  "
            f"[{category:<15}]  {url[:55]:<55}  {text}{mt_str}"
        )


REPL_HELP = """\
Commands:
  :k N          change top-k (current: {k})
  :lex on|off   toggle lexical fusion (current: {lex})
  :cat user_guide,api_reference | :cat off   filter by category (current: {cat})
  :help         show this help
  Ctrl-D        exit
Anything else is treated as a search query."""


def handle_repl_command(line: str, state: dict) -> None:
    parts = line[1:].split()
    if not parts:
        return
    cmd = parts[0]
    if cmd in ("help", "h", "?"):
        print(REPL_HELP.format(
            k=state["top_k"],
            lex="off" if state["disable_lexical"] else "on",
            cat=",".join(state["categories"]) if state["categories"] else "off",
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
    elif cmd == "cat":
        if len(parts) < 2:
            print("usage: :cat user_guide,api_reference  |  :cat off")
            return
        if parts[1] == "off":
            state["categories"] = None
            print("categories=off")
        else:
            state["categories"] = [c.strip() for c in parts[1].split(",") if c.strip()]
            print(f"categories={state['categories']}")
    else:
        print(f"unknown command: :{cmd}  (try :help)")


def main() -> int:
    import numpy as np

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--corpus-file", required=True,
        help="Path to a local corpus.json (typically generated/docsearch/corpus.json).",
    )
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--disable-lexical", action="store_true")
    parser.add_argument(
        "--categories", default=None,
        help="Comma-separated category allowlist.",
    )
    args = parser.parse_args()

    corpus_path = Path(args.corpus_file)
    if not corpus_path.exists():
        print(f"ERROR: {corpus_path} does not exist.", file=sys.stderr)
        return 2

    # Delay the ranking import so `--help` stays fast.
    from server import ranking

    log(f"Loading corpus from {corpus_path}...")
    raw = corpus_path.read_bytes()
    corpus_sha = hashlib.sha256(raw).hexdigest()
    corpus = json.loads(raw)
    try:
        ranking.validate_corpus(corpus)
    except ranking.CorpusValidationError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    chunks = corpus.get("chunks", [])
    log(f"  {len(chunks)} chunks, sha={corpus_sha[:12]}")

    matrix = np.asarray([c["embedding"] for c in chunks], dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1)
    norms[norms == 0] = 1.0
    matrix = matrix / norms[:, None]
    per_chunk_tokens = [
        set(ranking.tokenize(c.get("text", "") + " " + c.get("section", "")))
        for c in chunks
    ]

    log("Loading embedder (one-time)...")
    t0 = time.time()
    try:
        from server.embedder import MiniLMEmbedder
    except ModuleNotFoundError as exc:
        print(
            f"ERROR: {exc}\n"
            "  Install:  pip install -r server/requirements.txt",
            file=sys.stderr,
        )
        return 2
    # Default to the committed generated/shared/ artifacts; allow override
    # via env var in case of alternate checkouts.
    repo_root = Path(__file__).resolve().parent.parent
    model_path = Path(os.environ.get("EMBEDDER_MODEL_PATH", repo_root / "generated" / "shared" / "model.onnx"))
    tok_path = Path(os.environ.get("EMBEDDER_TOKENIZER_PATH", repo_root / "generated" / "shared" / "tokenizer.json"))
    model = MiniLMEmbedder(model_path, tok_path)
    log(f"  loaded in {time.time() - t0:.2f}s")

    state = {
        "top_k": args.top_k,
        "disable_lexical": args.disable_lexical,
        "categories": (
            [c.strip() for c in args.categories.split(",") if c.strip()]
            if args.categories else None
        ),
    }

    print()
    print(f"Corpus: {len(chunks)} chunks, sha={corpus_sha[:12]}")
    print(f"top_k={state['top_k']}, "
          f"lexical={'off' if state['disable_lexical'] else 'on'}, "
          f"categories={state['categories'] or 'all'}")
    print("Commands: :k N   :lex on|off   :cat <list>|off   :help   (Ctrl-D to exit)")
    print()

    while True:
        try:
            line = input("search> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not line:
            continue
        if line.startswith(":"):
            handle_repl_command(line, state)
            continue

        if state["categories"]:
            cat_set = set(state["categories"])
            mask = np.array([c.get("category") in cat_set for c in chunks], dtype=bool)
            sub_chunks = [c for c, keep in zip(chunks, mask) if keep]
            sub_matrix = matrix[mask]
            sub_tokens = [t for t, keep in zip(per_chunk_tokens, mask) if keep]
        else:
            sub_chunks = chunks
            sub_matrix = matrix
            sub_tokens = per_chunk_tokens

        if not sub_chunks:
            print("  (no chunks match the category filter)")
            print()
            continue

        vec = model.encode([line])[0]
        n = np.linalg.norm(vec)
        if n > 0:
            vec = vec / n

        results = ranking.rank(
            sub_chunks, sub_matrix, sub_tokens,
            line, vec, state["top_k"],
            disable_lexical=state["disable_lexical"],
        )
        print_human_table(results)
        print()


if __name__ == "__main__":
    sys.exit(main())
