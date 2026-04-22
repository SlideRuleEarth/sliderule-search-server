"""Download NSIDC + ORNL reference docs, extract, chunk, embed.

Writes generated/nsidc/corpus.json + meta.json — the same schema the
sliderule-docsearch corpus uses, so both can ride through
server/ranking.py and the skill client unchanged. Per-chunk metadata
adds `source_product` (ATL03 / ATL06 / ... / GEDI_L4A),
`source_version` (v006 / v007 / v2.1), `source_url`, and (for PDFs)
`source_page`.

Two content paths in one builder, routed by Content-Type on fetch:

  application/pdf        → PyMuPDF (fitz) → text + page numbers
  text/html              → BeautifulSoup  → text + headings

The skill never sees the distinction; both paths emit the same
chunk schema.

Pure build-time script. The Lambda image never ships pymupdf or the
crawler — it only ships corpus.json + meta.json.

On PyMuPDF's AGPL-3.0 license:

  PyMuPDF (and the MuPDF library it wraps) is released under AGPL-3.0.
  The AGPL's copyleft terms apply to *distribution* of (or network
  service based on) the AGPL'd work itself, including modified
  versions. In this project:

    - pymupdf is a BUILD-TIME dependency only. It's used by this
      script to extract text from PDFs once; the output is plain
      JSON (chunks + embeddings). The Lambda image does not install
      pymupdf (see server/Dockerfile — the runtime requirements
      don't include it), the skill clients never touch it, and
      neither does the web-facing service.
    - We do not distribute pymupdf itself. We don't modify it. We
      don't expose it over a network. The extracted text is an
      output artifact of using the tool, not a derivative of the
      tool's source code.
    - Commercial licenses are available from Artifex if a project
      needs to distribute modified PyMuPDF, but we don't.

  Net: running pymupdf locally / in CI to produce an open-data
  corpus of extracted text is uncontroversial under AGPL-3.0. We
  revisit only if pymupdf's usage mode changes (e.g. we ever ship
  it inside the Lambda image or a distributed client).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString


# -- Configuration ------------------------------------------------------------

USER_AGENT = "sliderule-search-server nsidc-builder (https://slideruleearth.io)"
EMBEDDER_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_CHAR_CAP = 1500
WORKERS = 4  # polite to NSIDC; they host a lot of data
REQUEST_TIMEOUT = 60  # PDFs can be ~12 MB

# Cache directory for downloaded documents. Gitignored. Skips re-fetch
# unless the remote reports a different Content-Length (best-effort
# freshness check; the canonical "did the doc change?" answer is a
# full rebuild with --force-refresh).
CACHE_DIR = Path(__file__).parent / ".cache" / "nsidc"


# The source inventory. Order determines deterministic chunk IDs, so
# append new entries rather than rearranging. Each entry needs every
# field the chunker propagates into per-chunk metadata.
SOURCES: list[dict] = [
    # ICESat-2 user guides (NSIDC)
    {"product": "ATL03",    "version": "v006", "doc_type": "user_guide",
     "url": "https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf"},
    {"product": "ATL06",    "version": "v006", "doc_type": "user_guide",
     "url": "https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf"},
    {"product": "ATL08",    "version": "v006", "doc_type": "user_guide",
     "url": "https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf"},
    {"product": "ATL13",    "version": "v007", "doc_type": "user_guide",
     "url": "https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf"},
    {"product": "ATL24",    "version": "v001", "doc_type": "user_guide",
     "url": "https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf"},

    # ICESat-2 ATBDs (NSIDC)
    {"product": "ATL03",    "version": "v006", "doc_type": "atbd",
     "url": "https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf"},
    {"product": "ATL06",    "version": "v006", "doc_type": "atbd",
     "url": "https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf"},
    {"product": "ATL08",    "version": "v007", "doc_type": "atbd",
     "url": "https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf"},
    {"product": "ATL13",    "version": "v007", "doc_type": "atbd",
     "url": "https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf"},
    {"product": "ATL24",    "version": "v001", "doc_type": "atbd",
     "url": "https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf"},

    # GEDI L4A (ORNL DAAC) — one ATBD (PDF) + one User Guide (HTML).
    # The HTML case is why the extractor has two branches; same chunk
    # schema out either way.
    {"product": "GEDI_L4A", "version": "v1.0", "doc_type": "atbd",
     "url": "https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf"},
    {"product": "GEDI_L4A", "version": "v2.1", "doc_type": "user_guide",
     "url": "https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html"},
]


# -- Small utilities ----------------------------------------------------------

def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def slugify_for_cache(url: str) -> str:
    """Stable filename for a cached download, derived from the URL."""
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


# -- Fetch layer --------------------------------------------------------------

def fetch(session: requests.Session, url: str,
          force_refresh: bool = False) -> tuple[bytes, str] | None:
    """Return (bytes, content_type) for a URL, using the local cache.

    Cache hit: return bytes immediately. Cache miss or force_refresh:
    download, persist, return. Returns None if the fetch fails — the
    caller decides whether a single-source failure aborts the build.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify_for_cache(url)
    body_path = CACHE_DIR / f"{slug}.body"
    meta_path = CACHE_DIR / f"{slug}.meta.json"

    if not force_refresh and body_path.exists() and meta_path.exists():
        try:
            m = json.loads(meta_path.read_text())
            log(f"  cache hit: {url}")
            return body_path.read_bytes(), m.get("content_type", "")
        except (OSError, json.JSONDecodeError):
            # Corrupt cache entry — fall through to refetch.
            pass

    log(f"  fetching: {url}")
    try:
        resp = session.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
    except requests.RequestException as e:
        log(f"    ERROR: {type(e).__name__}: {e}")
        return None
    if resp.status_code != 200:
        log(f"    ERROR: HTTP {resp.status_code}")
        return None

    ctype = resp.headers.get("Content-Type", "").lower()
    body_path.write_bytes(resp.content)
    meta_path.write_text(json.dumps({
        "url": url,
        "content_type": ctype,
        "content_length": len(resp.content),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }))
    return resp.content, ctype


# -- Text splitting (shared by PDF + HTML paths) ------------------------------

def split_long_text(text: str, cap: int) -> list[str]:
    """Break a too-long text into cap-sized chunks on paragraph, then
    sentence, then hard boundaries.

    Copy of the docsearch builder's split (same semantics), kept local
    so this script has no cross-file dependencies within tools/.
    """
    if len(text) <= cap:
        return [text] if text else []
    paragraphs = [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]
    if len(paragraphs) <= 1:
        paragraphs = [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-Z])", text) if p.strip()]
    chunks: list[str] = []
    buf = ""
    for para in paragraphs:
        if not buf:
            buf = para
        elif len(buf) + 1 + len(para) <= cap:
            buf = f"{buf} {para}"
        else:
            chunks.append(buf)
            buf = para
    if buf:
        chunks.append(buf)
    # Hard-cap anything still above the threshold (prose without
    # paragraph breaks — rare in PDFs, common in HTML with <br>s).
    final: list[str] = []
    for c in chunks:
        if len(c) <= cap:
            final.append(c)
        else:
            for i in range(0, len(c), cap):
                final.append(c[i:i + cap])
    return final


# -- PDF extraction -----------------------------------------------------------

def _toc_lookup_for(doc) -> dict[int, str]:
    """Map page-number (1-indexed) → nearest TOC entry title.

    PyMuPDF's `get_toc()` returns [[level, title, page], ...]. We
    collapse to a "last TOC entry at or before page N" lookup so
    every page has a citable section even if no TOC entry starts
    exactly on it.
    """
    toc = doc.get_toc(simple=True) or []
    if not toc:
        return {}
    # Sort by page just to be safe; PyMuPDF usually returns them in order.
    toc_sorted = sorted(toc, key=lambda e: e[2])
    result: dict[int, str] = {}
    pending_title: str | None = None
    toc_idx = 0
    for page_num in range(1, doc.page_count + 1):
        while toc_idx < len(toc_sorted) and toc_sorted[toc_idx][2] <= page_num:
            pending_title = toc_sorted[toc_idx][1].strip()
            toc_idx += 1
        if pending_title:
            result[page_num] = pending_title
    return result


def chunk_pdf(body: bytes, source: dict) -> list[dict]:
    """Extract text from a PDF, one chunk per page (split further if
    a page exceeds CHUNK_CHAR_CAP). Each chunk carries the PDF's
    source metadata plus a 1-indexed page number."""
    import fitz  # imported lazily so --help doesn't pay PyMuPDF's init cost

    doc = fitz.open(stream=body, filetype="pdf")
    toc = _toc_lookup_for(doc)
    chunks: list[dict] = []
    try:
        title_guess = (doc.metadata or {}).get("title", "").strip() or None
        default_title = title_guess or f"{source['product']} {source['version']} {source['doc_type'].replace('_', ' ')}"

        for page_idx, page in enumerate(doc):
            page_num = page_idx + 1
            text = page.get_text("text", sort=True) or ""
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r"\s*\n\s*", "\n", text).strip()
            if len(text) < 40:
                continue

            section = toc.get(page_num) or f"Page {page_num}"

            for sub_idx, piece in enumerate(split_long_text(text, CHUNK_CHAR_CAP)):
                chunks.append({
                    "url": source["url"],
                    "title": default_title,
                    "section": section,
                    "category": source["doc_type"],
                    "text": piece,
                    "source_product": source["product"],
                    "source_version": source["version"],
                    "source_page": page_num,
                    "source_url": source["url"],
                    "_order": page_num * 1000 + sub_idx,
                })
    finally:
        doc.close()
    return chunks


# -- HTML extraction ----------------------------------------------------------

HEADING_TAGS = ("h1", "h2", "h3", "h4")

STRIP_SELECTORS = [
    ("nav", {}),
    ("header", {}),
    ("footer", {}),
    ("aside", {}),
    ("script", {}),
    ("style", {}),
    ("form", {}),
]


def _extract_text(node) -> str:
    parts: list[str] = []
    for descendant in node.descendants:
        if isinstance(descendant, NavigableString):
            parts.append(str(descendant))
    text = " ".join(parts)
    return re.sub(r"\s+", " ", text).strip()


def _collect_text_until_next_heading(start_heading) -> str:
    """Walk forward from a heading, gathering text until the next heading."""
    heading_descendant_ids = {id(d) for d in start_heading.descendants}
    pieces: list[str] = []
    for node in start_heading.next_elements:
        if node is start_heading:
            continue
        if id(node) in heading_descendant_ids:
            continue
        if getattr(node, "name", None) in HEADING_TAGS:
            break
        if isinstance(node, NavigableString):
            parent_names = {p.name for p in node.parents if p.name}
            if parent_names & {"script", "style"}:
                continue
            s = str(node)
            if s.strip():
                pieces.append(s)
    return re.sub(r"\s+", " ", " ".join(pieces)).strip()


def chunk_html(body: bytes, source: dict) -> list[dict]:
    """Extract + chunk an HTML page. Shape matches chunk_pdf; the only
    difference is `source_page` is omitted (HTML has no pages)."""
    soup = BeautifulSoup(body, "html.parser")
    main = soup.find("main") or soup.find("article") or soup.find("body") or soup

    for tag, attrs in STRIP_SELECTORS:
        for match in list(main.find_all(tag, attrs) if attrs else main.find_all(tag)):
            match.decompose()

    # Title preference: <title> → first <h1> → synthesized.
    if soup.title and soup.title.string:
        default_title = soup.title.string.strip()
    elif main.find("h1"):
        default_title = _extract_text(main.find("h1"))
    else:
        default_title = f"{source['product']} {source['version']} {source['doc_type'].replace('_', ' ')}"

    chunks: list[dict] = []
    headings = main.find_all(HEADING_TAGS)
    if not headings:
        text = _extract_text(main)
        for sub_idx, piece in enumerate(split_long_text(text, CHUNK_CHAR_CAP)):
            if len(piece) < 40:
                continue
            chunks.append({
                "url": source["url"],
                "title": default_title,
                "section": default_title,
                "category": source["doc_type"],
                "text": piece,
                "source_product": source["product"],
                "source_version": source["version"],
                "source_page": None,
                "source_url": source["url"],
                "_order": sub_idx,
            })
        return chunks

    for idx, heading in enumerate(headings):
        heading_text = _extract_text(heading)
        body_text = _collect_text_until_next_heading(heading)
        if not body_text:
            continue
        for sub_idx, piece in enumerate(split_long_text(body_text, CHUNK_CHAR_CAP)):
            if len(piece) < 40:
                continue
            chunks.append({
                "url": source["url"],
                "title": default_title,
                "section": heading_text or default_title,
                "category": source["doc_type"],
                "text": piece,
                "source_product": source["product"],
                "source_version": source["version"],
                "source_page": None,
                "source_url": source["url"],
                "_order": idx * 1000 + sub_idx,
            })
    return chunks


# -- Content-type routing -----------------------------------------------------

def extract_chunks(body: bytes, ctype: str, source: dict) -> list[dict]:
    """Dispatch to the PDF or HTML extractor based on content-type.

    Trailing fallback on URL suffix protects against servers returning
    an uninformative `application/octet-stream` for a file that is
    obviously a PDF from its URL.
    """
    if "application/pdf" in ctype or source["url"].lower().endswith(".pdf"):
        return chunk_pdf(body, source)
    if "text/html" in ctype or source["url"].lower().endswith((".html", ".htm")):
        return chunk_html(body, source)
    log(f"  WARN: unknown content-type {ctype!r} for {source['url']}; skipping")
    return []


# -- Embed + serialize --------------------------------------------------------

def chunk_id(url: str, section: str, order: int) -> str:
    h = hashlib.sha1(f"{url}|{section}|{order}".encode("utf-8")).hexdigest()
    return h[:16]


def round_embedding(vec) -> list[float]:
    return [round(float(x), 6) for x in vec]


def build_corpus(
    all_chunks: list[dict],
) -> tuple[list[dict], str, int]:
    """Sort deterministically, embed, return the serializable shape."""
    # Import the shared embedder here (not at module scope) so the script
    # parses and --help runs even if onnxruntime isn't installed yet.
    # sys.path prepend lets tools/ scripts import the server.* package
    # without turning the repo into an installable package.
    repo_root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(repo_root))
    from server.embedder import EMBEDDING_DIM, MiniLMEmbedder

    # Stable ordering: (url, in-page order). chunks from the same PDF
    # stay contiguous, pages in natural order, no date/time dependence.
    all_chunks.sort(key=lambda c: (c["url"], c["_order"]))

    log(f"Embedding {len(all_chunks)} chunks with {EMBEDDER_NAME}...")
    model = MiniLMEmbedder(
        repo_root / "generated" / "shared" / "model.onnx",
        repo_root / "generated" / "shared" / "tokenizer.json",
    )
    texts = [c["text"] for c in all_chunks]
    t0 = time.time()
    if texts:
        vectors = model.encode(texts, batch_size=32, show_progress=True)
        dim = EMBEDDING_DIM
    else:
        vectors = []
        dim = 0
    embed_seconds = time.time() - t0

    out_chunks: list[dict] = []
    for chunk, vec in zip(all_chunks, vectors):
        out_chunks.append({
            "id": chunk_id(chunk["url"], chunk["section"], chunk["_order"]),
            "url": chunk["url"],
            "title": chunk["title"],
            "section": chunk["section"],
            "category": chunk["category"],
            "source_product": chunk["source_product"],
            "source_version": chunk["source_version"],
            "source_page": chunk["source_page"],
            "source_url": chunk["source_url"],
            "text": chunk["text"],
            "embedding": round_embedding(vec),
        })

    log(f"Embedded with {EMBEDDER_NAME} in {embed_seconds:.1f}s")
    return out_chunks, EMBEDDER_NAME, dim


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def write_corpus(out_dir: Path, chunks: list[dict], dim: int) -> Path:
    corpus = {
        "version": 1,
        "embedder": EMBEDDER_NAME,
        "embedding_dim": dim,
        "chunks": chunks,
    }
    path = out_dir / "corpus.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, sort_keys=False, ensure_ascii=False)
        f.write("\n")
    return path


def write_meta(
    out_dir: Path,
    sources_total: int,
    sources_ok: int,
    chunk_count: int,
    dim: int,
    corpus_bytes: int,
    corpus_sha256: str,
) -> Path:
    meta = {
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_host": "nsidc.org + ornldaac.earthdata.nasa.gov",
        "crawl_strategy": "url_list",
        "sources_total": sources_total,
        "sources_ok": sources_ok,
        "pages_crawled": sources_ok,  # kept for schema parity with docsearch
        "chunk_count": chunk_count,
        "embedder": EMBEDDER_NAME,
        "embedding_dim": dim,
        "corpus_bytes": corpus_bytes,
        "corpus_sha256": corpus_sha256,
    }
    path = out_dir / "meta.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, sort_keys=False, ensure_ascii=False)
        f.write("\n")
    return path


# -- Orchestration ------------------------------------------------------------

def fetch_and_chunk_all(
    sources: list[dict], force_refresh: bool,
) -> tuple[list[dict], int]:
    """Parallel-fetch every source, extract chunks, concat.

    Returns (all_chunks, n_sources_ok). A single bad URL (404, timeout,
    unparseable PDF) reduces n_sources_ok but does not fail the build
    by itself — the --min-sources guard downstream is the backstop.
    """
    session = make_session()
    all_chunks: list[dict] = []
    sources_ok = 0

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(fetch, session, s["url"], force_refresh): s for s in sources}
        for fut in as_completed(futures):
            source = futures[fut]
            try:
                result = fut.result()
            except Exception as e:
                log(f"  ERROR fetching {source['url']}: {type(e).__name__}: {e}")
                result = None
            if result is None:
                continue
            body, ctype = result
            try:
                chunks = extract_chunks(body, ctype, source)
            except Exception as e:
                log(f"  ERROR extracting {source['url']}: {type(e).__name__}: {e}")
                continue
            if not chunks:
                log(f"  WARN: no chunks from {source['url']}")
                continue
            all_chunks.extend(chunks)
            sources_ok += 1
            log(f"  {source['product']} {source['version']} {source['doc_type']}: {len(chunks)} chunks")
    return all_chunks, sources_ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="generated/nsidc",
                        help="Where to write corpus.json + meta.json.")
    parser.add_argument("--force-refresh", action="store_true",
                        help="Ignore the local download cache; re-fetch every source.")
    parser.add_argument("--min-sources", type=int, default=8,
                        help=(
                            "Abort if fewer than this many sources yielded chunks "
                            "successfully. Guards against a transient outage on "
                            "nsidc.org silently deploying a thin corpus."
                        ))
    parser.add_argument("--min-chunks", type=int, default=500,
                        help="Abort if fewer than this many chunks total.")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    log(f"Fetching {len(SOURCES)} sources (cache at {CACHE_DIR})...")
    t0 = time.time()
    all_chunks, sources_ok = fetch_and_chunk_all(SOURCES, force_refresh=args.force_refresh)
    log(f"Fetch+extract: {sources_ok}/{len(SOURCES)} sources in {time.time() - t0:.1f}s")

    if sources_ok < args.min_sources:
        log(
            f"ERROR: only {sources_ok}/{len(SOURCES)} sources produced chunks "
            f"(minimum {args.min_sources}). Refusing to overwrite existing "
            f"corpus.json/meta.json — a transient outage is the likely cause."
        )
        return 1
    if len(all_chunks) < args.min_chunks:
        log(
            f"ERROR: only {len(all_chunks)} chunks produced (minimum "
            f"{args.min_chunks}). Refusing to overwrite. Check extractor output."
        )
        return 1

    chunks, embedder, dim = build_corpus(all_chunks)
    log(f"Chunked to {len(chunks)} pieces")

    corpus_path = write_corpus(out_dir, chunks, dim)
    corpus_bytes = corpus_path.stat().st_size
    corpus_sha = sha256_of(corpus_path)
    meta_path = write_meta(
        out_dir,
        sources_total=len(SOURCES),
        sources_ok=sources_ok,
        chunk_count=len(chunks),
        dim=dim,
        corpus_bytes=corpus_bytes,
        corpus_sha256=corpus_sha,
    )

    print(f"Sources: {sources_ok}/{len(SOURCES)} ok")
    print(f"Chunks : {len(chunks)}")
    print(f"Wrote  : {corpus_path}  ({corpus_bytes / (1024 * 1024):.1f} MB)")
    print(f"Wrote  : {meta_path}    (corpus_sha256={corpus_sha[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
