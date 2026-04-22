"""
Shared MiniLM embedder backed by onnxruntime + tokenizers.

Imported by both the server (for per-query embedding at request time) and
the corpus builders in tools/ (for chunk embedding at build time). One
code path, one model file, one tokenizer — so the bytes that compute
query embeddings in Lambda are the same bytes that computed the chunk
embeddings in the committed corpus. Cannot drift.

Replicates sentence-transformers' default pipeline for
sentence-transformers/all-MiniLM-L6-v2:

  1. WordPiece tokenize via the committed tokenizer.json, pad & truncate
     to max_length=256 (the model's configured max_seq_length).
  2. Run the transformer backbone via onnxruntime on CPU.
  3. Mean-pool token embeddings with attention_mask weighting.
  4. L2-normalize, producing unit vectors for cosine similarity.

Bit-for-bit parity with the torch path was verified against 100 random
chunks + 20 representative queries (pairwise cosine = 1.000000 across
all 120 samples; top-20 ranked results identical for every query).

The model.onnx + tokenizer.json files live in generated/shared/ and are
committed to the repo. `tools/export_minilm_onnx.py` regenerates them
if the model ever needs to change — but that's a deliberate act paired
with a corpus rebuild, not a routine thing.
"""

from __future__ import annotations

import pathlib

import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

# Matches the `max_seq_length` baked into sentence-transformers/all-MiniLM-L6-v2's
# config. Longer chunks get truncated (same as the torch path did). Exposed as a
# class arg so a future re-chunking experiment can pass a larger value without
# touching the default.
DEFAULT_MAX_LENGTH = 256

# MiniLM-L6-v2 dim. Exposed as a class attribute so callers (ranking code,
# tests) can assert on it without re-running inference.
EMBEDDING_DIM = 384


class MiniLMEmbedder:
    """Encode text into 384-dim unit vectors using MiniLM-L6-v2."""

    def __init__(
        self,
        model_path: str | pathlib.Path,
        tokenizer_path: str | pathlib.Path,
        max_length: int = DEFAULT_MAX_LENGTH,
    ):
        self.model_path = pathlib.Path(model_path)
        self.tokenizer_path = pathlib.Path(tokenizer_path)
        self.session = ort.InferenceSession(
            str(self.model_path),
            providers=["CPUExecutionProvider"],
        )
        self.tokenizer = Tokenizer.from_file(str(self.tokenizer_path))
        # BERT WordPiece pad/truncate. `[PAD]` is token id 0 for this tokenizer
        # but we look it up by name in case the tokenizer ever changes.
        pad_id = self.tokenizer.token_to_id("[PAD]")
        if pad_id is None:
            raise ValueError(f"tokenizer at {tokenizer_path} has no [PAD] token")
        self.tokenizer.enable_padding(pad_id=pad_id, pad_token="[PAD]")
        self.tokenizer.enable_truncation(max_length=max_length)
        self._wants_token_type_ids = any(
            i.name == "token_type_ids" for i in self.session.get_inputs()
        )

    def encode(
        self,
        texts: list[str],
        batch_size: int = 32,
        show_progress: bool = False,
    ) -> np.ndarray:
        """Encode a batch of strings to (N, 384) float32, L2-normalized.

        Empty list returns shape (0, 384). Single strings should be wrapped in
        a list by the caller so the return shape stays consistent.

        Batches of size `batch_size` (default 32, matching sentence-transformers'
        default) keep peak memory bounded — a 1000-chunk corpus with 256-token
        sequences would otherwise allocate ~380 MB of activations in one shot.
        """
        if not texts:
            return np.zeros((0, EMBEDDING_DIM), dtype=np.float32)

        iterator = range(0, len(texts), batch_size)
        if show_progress:
            # tqdm is a transitive dep of onnxruntime/tokenizers; absence
            # is unusual but not fatal.
            try:
                from tqdm import tqdm

                iterator = tqdm(iterator, desc="embedding", total=(len(texts) + batch_size - 1) // batch_size)
            except ImportError:
                pass

        out: list[np.ndarray] = []
        for start in iterator:
            out.append(self._encode_batch(texts[start : start + batch_size]))
        return np.concatenate(out, axis=0)

    def _encode_batch(self, texts: list[str]) -> np.ndarray:
        encs = self.tokenizer.encode_batch(texts)
        input_ids = np.array([e.ids for e in encs], dtype=np.int64)
        attention_mask = np.array([e.attention_mask for e in encs], dtype=np.int64)

        feed: dict[str, np.ndarray] = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
        }
        if self._wants_token_type_ids:
            feed["token_type_ids"] = np.array(
                [e.type_ids for e in encs], dtype=np.int64
            )

        last_hidden = self.session.run(None, feed)[0]  # (N, L, 384)

        # Mean-pool over the sequence dimension, weighted by attention_mask so
        # padding positions don't dilute the average. Clamp the divisor at 1e-9
        # to avoid a 0/0 on a fully-padded input (shouldn't happen for any real
        # text, but cheap to guard).
        mask = attention_mask[:, :, None].astype(np.float32)
        pooled = (last_hidden * mask).sum(axis=1) / np.clip(mask.sum(axis=1), 1e-9, None)

        # L2 normalize so the ranking math can treat cosine similarity as a
        # plain dot product. Matches `normalize_embeddings=True` on the
        # sentence-transformers side.
        norms = np.linalg.norm(pooled, axis=1, keepdims=True)
        return (pooled / np.clip(norms, 1e-12, None)).astype(np.float32)
