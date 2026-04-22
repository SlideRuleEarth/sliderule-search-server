#!/usr/bin/env python3
"""Regenerate generated/shared/{model.onnx, tokenizer.json} from the canonical
Hugging Face model `sentence-transformers/all-MiniLM-L6-v2`.

This is a *deliberate* build step. Run it only when you intend to change the
embedding model — a new MiniLM-L6-v2 revision, a different sentence encoder,
a fine-tuned variant, etc. Changing the model invalidates every committed
corpus; you must follow this with:

    make rebuild-corpus-docsearch
    make rebuild-corpus-nsidc

and then deploy the image, because the pre-computed chunk embeddings in the
committed corpora must be recomputed with the new model for query ranking
to make any sense.

Why the ONNX files live in generated/shared/ (and not tools/.cache/):
we want the *exact* bytes of model.onnx + tokenizer.json to travel with the
repo, so the server's inference code and the corpus builders' embedding
code are guaranteed to produce identical outputs. If this were cached and
regenerated per-machine, a future HF re-publish of the source model
(uncommon but possible) would silently produce drifted embeddings on the
next corpus rebuild.

Dependencies: `optimum-onnx` (brings torch + transformers transitively).
Those aren't in tools/requirements.txt by default because regenerating
happens rarely; install on demand:

    .venv/bin/pip install 'sentence-transformers[onnx]'

Usage:

    .venv/bin/python tools/export_minilm_onnx.py
"""

from __future__ import annotations

import pathlib
import shutil
import sys

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
REPO = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "generated" / "shared"

# Files we keep in the committed directory. Anything else optimum emits
# (config.json, vocab.txt, special_tokens_map.json) is redundant with the
# tokenizer.json for our inference path, so drop it to keep the committed
# footprint minimal.
KEEP = ("model.onnx", "tokenizer.json")


def main() -> int:
    try:
        from optimum.exporters.onnx import main_export
    except ImportError:
        print(
            "optimum.exporters.onnx not installed. Install with:\n"
            "    .venv/bin/pip install 'sentence-transformers[onnx]'",
            file=sys.stderr,
        )
        return 2

    staging = REPO / "tools" / ".cache" / "onnx_export_staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)

    print(f"exporting {MODEL_ID} to {staging} ...")
    main_export(
        model_name_or_path=MODEL_ID,
        output=str(staging),
        task="feature-extraction",
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name in KEEP:
        src = staging / name
        if not src.exists():
            print(f"expected output missing: {src}", file=sys.stderr)
            return 1
        shutil.copyfile(src, OUT_DIR / name)
        size_mb = src.stat().st_size / (1024 * 1024)
        print(f"  wrote {OUT_DIR / name}  ({size_mb:.1f} MB)")

    print(
        f"\ndone. Commit {OUT_DIR}/ and run corpus rebuilds:\n"
        "  make rebuild-corpus-docsearch\n"
        "  make rebuild-corpus-nsidc\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
