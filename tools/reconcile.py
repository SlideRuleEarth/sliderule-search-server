"""Interactive walker for auto-vs-human disagreements.

For each row where the auto-metric and human-metric disagree on whether
the right answer landed in top-5, show the chunk evidence and prompt
for a label fix. Edits write back to evals/golden_set.jsonl
incrementally — quit anytime, re-run to continue.

Two kinds of disagreement:
  AUTO_GENEROUS — auto says hit, human says no `correct` chunk in top-5.
                  Usual fix: tighten expected_sections/pages or drop a URL.
  AUTO_NARROW   — auto says miss, human marked a chunk `correct`.
                  Usual fix: widen expected_sections/urls/pages.

Usage
-----
    python tools/reconcile.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from server.embedder import MiniLMEmbedder
from tools.eval_retrieval import (
    CORPUS_PATHS, MODEL_PATH, TOKENIZER_PATH, GOLDEN_SET_PATH, K_RECALL,
    chunk_full_match, evaluate, first_human_rank, load_corpus_state,
    load_human_review, _url_path,
)


def find_disagreements(records: list[dict]) -> list[tuple[str, dict]]:
    out = []
    for r in records:
        if not r.get("human_available"):
            continue
        auto_hit = r["first_rank"] is not None and r["first_rank"] <= K_RECALL
        human_hit = r["human_first_rank"] is not None
        if auto_hit and not human_hit:
            out.append(("AUTO_GENEROUS", r))
        elif human_hit and not auto_hit:
            out.append(("AUTO_NARROW", r))
    return out


def recompute_match(row: dict, top_results: list[dict]) -> int | None:
    """Compute first_rank against the row's CURRENT labels (after edits)."""
    expected_paths = {_url_path(u) for u in row.get("expected_urls", [])}
    sections = row.get("expected_sections")
    pages = row.get("expected_pages")
    for tr in top_results:
        chunk_like = {
            "url": tr["url"],
            "section": tr.get("section", ""),
            "source_page": tr.get("source_page"),
        }
        if chunk_full_match(chunk_like, expected_paths, sections, pages):
            return tr["rank"]
    return None


def text_preview(text: str, n: int = 200) -> str:
    t = " ".join((text or "").split())
    return (t[:n] + "…") if len(t) > n else t


def show_disagreement(kind: str, idx: int, total: int, r: dict, row: dict) -> None:
    print(f"\n{'=' * 78}")
    print(f"[{idx}/{total}] Row {r['row_index']} — {r['corpus']}/{r['type']} — {kind}")
    print(f"  query: {r['query']}")
    print()
    print(f"  expected_urls:")
    for u in row.get("expected_urls", []):
        print(f"    - {u}")
    if row.get("expected_sections"):
        print(f"  expected_sections: {row['expected_sections']}")
    if row.get("expected_pages"):
        print(f"  expected_pages: {row['expected_pages']}")
    if row.get("notes"):
        print(f"  notes: {row['notes']}")
    print()
    print(f"  auto first_rank: {r['first_rank']}; human first `correct` rank: {r['human_first_rank']}")
    print()
    print(f"  top-5 chunks (✓✓ = full auto-match; ✓  = URL-match only; '  ' = no auto-match):")
    for tr in r["top_results"]:
        verdict = tr.get("human_verdict") or "(none)"
        if tr["match"]:
            mark = "✓✓"
        elif tr.get("url_match"):
            mark = "✓ "
        else:
            mark = "  "
        path = _url_path(tr["url"])
        sec = tr.get("section") or "(no section)"
        page = tr.get("source_page")
        page_str = f" p.{page}" if page else ""
        print(f"    r{tr['rank']} [{mark}] {verdict:8s} {path}{page_str}")
        print(f"          section: {sec}")
        print(f"          text: {text_preview(tr['text'])}")
    print()


def prompt_choice(prompt: str, options: dict[str, str]) -> str:
    print(prompt)
    for key, label in options.items():
        print(f"  {key} = {label}")
    while True:
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print(f"  unrecognized; pick one of: {', '.join(options.keys())}")


def edit_list_field(row: dict, field: str, label: str) -> None:
    """Generic editor for a list field (expected_urls / expected_sections)."""
    while True:
        current = row.get(field) or []
        print(f"  current {label}:")
        if not current:
            print(f"    (empty)")
        for i, item in enumerate(current):
            print(f"    [{i}] {item}")
        print("  enter index to remove, `+ <value>` to add, `c` to clear, blank to finish:")
        cmd = input("  > ").strip()
        if not cmd:
            return
        if cmd == "c":
            row.pop(field, None)
            print(f"  cleared {label}.")
            return
        if cmd.startswith("+"):
            new = cmd[1:].strip()
            if new:
                row.setdefault(field, []).append(new)
                print(f"  added.")
            continue
        if cmd.isdigit():
            i = int(cmd)
            if 0 <= i < len(current):
                removed = current.pop(i)
                if not current:
                    row.pop(field, None)
                else:
                    row[field] = current
                print(f"  removed: {removed}")
            else:
                print(f"  index out of range")
            continue
        print(f"  unrecognized command")


def edit_pages(row: dict) -> None:
    """expected_pages takes a list of [start, end] pairs."""
    while True:
        current = row.get("expected_pages") or []
        print(f"  current expected_pages:")
        if not current:
            print(f"    (empty)")
        for i, pair in enumerate(current):
            print(f"    [{i}] {pair[0]}-{pair[1]}")
        print("  enter index to remove, `+ start end` to add, `c` to clear, blank to finish:")
        cmd = input("  > ").strip()
        if not cmd:
            return
        if cmd == "c":
            row.pop("expected_pages", None)
            return
        if cmd.startswith("+"):
            parts = cmd[1:].strip().split()
            if len(parts) == 2:
                try:
                    start, end = int(parts[0]), int(parts[1])
                    row.setdefault("expected_pages", []).append([start, end])
                    print(f"  added [{start}, {end}].")
                except ValueError:
                    print(f"  start and end must be integers")
            else:
                print(f"  format: + start end")
            continue
        if cmd.isdigit():
            i = int(cmd)
            current = row.get("expected_pages") or []
            if 0 <= i < len(current):
                current.pop(i)
                if not current:
                    row.pop("expected_pages", None)
                else:
                    row["expected_pages"] = current
                print(f"  removed.")
            else:
                print(f"  index out of range")
            continue
        print(f"  unrecognized command")


def write_golden_set(rows: list[dict]) -> None:
    GOLDEN_SET_PATH.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n"
    )


def main() -> int:
    rows = [json.loads(l) for l in GOLDEN_SET_PATH.read_text().splitlines() if l.strip()]
    print(f"loaded {len(rows)} golden-set rows", file=sys.stderr)

    human_records = load_human_review()
    if not human_records:
        print("no human reviews — run tools/ingest_review.py first", file=sys.stderr)
        return 1
    print(f"loaded {len(human_records)} human reviews", file=sys.stderr)

    corpora = {name: load_corpus_state(path) for name, path in CORPUS_PATHS.items()}
    for name, s in corpora.items():
        print(f"loaded {name}: {len(s['chunks'])} chunks", file=sys.stderr)
    model = MiniLMEmbedder(MODEL_PATH, TOKENIZER_PATH)
    print("loaded embedder", file=sys.stderr)

    records = evaluate(rows, corpora, model, human_records=human_records)
    disagreements = find_disagreements(records)

    if not disagreements:
        print("\nNo disagreements. Auto and human metrics agree on every row.")
        return 0

    print(f"\n{len(disagreements)} disagreement(s) to walk.")
    print("After each fix, the row's auto-match is recomputed against the new labels.")
    print("If the disagreement is resolved, we move on.\n")

    options = {
        "s": "edit expected_sections (tighten or widen)",
        "u": "edit expected_urls (add/remove URL)",
        "p": "edit expected_pages (page-range narrowing)",
        "d": "drop all narrowing (URL-only matching)",
        "n": "add a `notes` line",
        "k": "skip — decide later",
        "v": "verdict revisit — flag in notes (no label change)",
        "q": "quit (changes saved incrementally)",
    }

    quit_now = False
    for i, (kind, r) in enumerate(disagreements, 1):
        if quit_now:
            break
        row = rows[r["row_index"] - 1]

        # Re-show until the disagreement is resolved or skipped/quit
        while True:
            # Recompute auto-match against current labels in case we just edited
            new_first_rank = recompute_match(row, r["top_results"])
            r["first_rank"] = new_first_rank
            r["top_results"] = [
                {**tr, "match": chunk_full_match(
                    {"url": tr["url"], "section": tr.get("section", ""),
                     "source_page": tr.get("source_page")},
                    {_url_path(u) for u in row.get("expected_urls", [])},
                    row.get("expected_sections"),
                    row.get("expected_pages"),
                )}
                for tr in r["top_results"]
            ]
            auto_hit_now = new_first_rank is not None and new_first_rank <= K_RECALL
            human_hit = r["human_first_rank"] is not None
            if (auto_hit_now and not human_hit) or (human_hit and not auto_hit_now):
                pass  # still disagreeing — keep editing
            else:
                print("  -> disagreement resolved.")
                break

            show_disagreement(kind, i, len(disagreements), r, row)
            choice = prompt_choice("Action:", options)
            if choice == "q":
                quit_now = True
                break
            if choice == "k":
                print("  -> skipped.")
                break
            if choice == "s":
                edit_list_field(row, "expected_sections", "expected_sections")
            elif choice == "u":
                edit_list_field(row, "expected_urls", "expected_urls")
            elif choice == "p":
                edit_pages(row)
            elif choice == "d":
                row.pop("expected_sections", None)
                row.pop("expected_pages", None)
                print("  -> narrowing cleared.")
            elif choice == "n":
                existing = row.get("notes", "") or ""
                print(f"  current notes: {existing}")
                print(f"  enter new notes (or blank to keep current):")
                new = input("  > ").strip()
                if new:
                    row["notes"] = (existing + "; " + new) if existing else new
            elif choice == "v":
                flag = "verdict revisit needed at reconciliation"
                existing = row.get("notes", "") or ""
                row["notes"] = (existing + "; " + flag) if existing else flag
                print(f"  -> flagged in notes; no label change made.")
                break
            write_golden_set(rows)
            print(f"  -> saved.")

    print("\nDone.")
    print("Re-run `tools/eval_retrieval.py` to see the updated metrics.")
    print("Re-run `tools/reconcile.py` to walk any remaining disagreements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
