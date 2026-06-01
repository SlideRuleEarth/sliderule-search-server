#!/usr/bin/env python3
"""Golden-set authoring aid: audit rows against the live corpora and
calibrate narrowing (expected_sections / expected_pages) to where the
answer actually lives.

This is a POC helper for the retrieval-quality eval, used when editing
evals/golden_set.jsonl. It reuses tools/eval_retrieval.py's loading and
matching helpers so its verdicts match the harness exactly.

Usage:
  # Audit every row: rank + flags (URL missing, narrowing can't match, no hit)
  .venv/bin/python tools/gs_audit.py audit [path/to/golden_set.jsonl]

  # Calibrate: for a query, show the best-matching chunks on given URLs
  # (their section + source_page), so you can set accurate narrowing.
  .venv/bin/python tools/gs_audit.py calibrate "ATL03 signal finding" \
      nsidc icesat2_atl03_atbd_v006.pdf

  # Grep: list chunk (section, page) on a URL whose text contains a term
  .venv/bin/python tools/gs_audit.py grep nsidc atl06-v006-userguide.pdf "quality"
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import eval_retrieval as E  # noqa: E402
from server import ranking  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CORPUS = {
    "docsearch": ROOT / "generated/docsearch/corpus.json",
    "nsidc": ROOT / "generated/nsidc/corpus.json",
}


def _load():
    corpora = {k: E.load_corpus_state(p) for k, p in CORPUS.items()}
    model = E.MiniLMEmbedder(
        str(ROOT / "generated/shared/model.onnx"),
        str(ROOT / "generated/shared/tokenizer.json"),
    )
    return corpora, model


def _rank(corpora, model, corpus, query, k=20):
    st = corpora[corpus]
    vec = model.encode([query])[0]
    return ranking.rank(st["chunks"], st["matrix"], st["per_chunk_tokens"], query, vec, k)


def cmd_audit(args):
    path = Path(args[0]) if args else ROOT / "evals/golden_set.jsonl"
    corpora, model = _load()
    paths = {k: {E._url_path(c["url"]) for c in v["chunks"]} for k, v in corpora.items()}
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    issues = 0
    for i, r in enumerate(rows, 1):
        corp = r["corpus"]
        exp = [E._url_path(u) for u in r["expected_urls"]]
        missing = [u for u in exp if u not in paths[corp]]
        res = _rank(corpora, model, corp, r["query"], 20)
        full = E.first_expected_rank(
            res, r["expected_urls"], r.get("expected_sections"), r.get("expected_pages")
        )
        url_rank = next((n for n, x in enumerate(res, 1) if E._url_path(x["url"]) in exp), None)
        flags = []
        if missing:
            flags.append(f"URL_MISSING:{missing}")
        if full is None and url_rank is not None:
            flags.append(f"NARROW_FAILS(url@{url_rank})")
        if url_rank is None:
            flags.append("RANKER_MISS(url not in top20)")
        if flags:
            issues += 1
        fr = str(full) if full is not None else "-"
        print(f"{i:>3} {corp[:4]} {r['type']:22} rk={fr:>4} {'  '.join(flags) if flags else 'ok':<40} {r['query'][:40]}")
    print(f"\nrows with issues: {issues}/{len(rows)}  (full=harness rank within top20, '-'=miss)")


def cmd_calibrate(args):
    query, corpus, *url_frags = args
    corpora, model = _load()
    res = _rank(corpora, model, corpus, query, 40)
    fragset = [u.lower() for u in url_frags]
    print(f"query={query!r} corpus={corpus}")
    print("rank  page  section  (chunks on matching URLs, by rank)")
    shown = 0
    for n, x in enumerate(res, 1):
        if fragset and not any(f in x["url"].lower() for f in fragset):
            continue
        pg = x.get("source_page")
        print(f"  {n:>3}  {str(pg):>4}  {x['section'][:60]!r}")
        shown += 1
        if shown >= 15:
            break
    if not shown:
        print("  (no chunks from those URLs in top 40 — likely a ranker miss)")


def cmd_grep(args):
    corpus, url_frag, term = args
    corpora, _ = _load()
    term_l = term.lower()
    hits = [
        c for c in corpora[corpus]["chunks"]
        if url_frag.lower() in c["url"].lower() and term_l in c.get("text", "").lower()
    ]
    print(f"{len(hits)} chunks on '{url_frag}' contain {term!r}:")
    for c in sorted(hits, key=lambda c: (c.get("source_page") or 0)):
        print(f"  page={str(c.get('source_page')):>4}  section={c['section'][:55]!r}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd, args = sys.argv[1], sys.argv[2:]
    {"audit": cmd_audit, "calibrate": cmd_calibrate, "grep": cmd_grep}[cmd](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
