#!/usr/bin/env python3
"""Crawl docs.slideruleearth.io, chunk by heading, embed, and write a static corpus.

Output: generated/docsearch/corpus.json + meta.json. Pure build-time script —
the deployed distribution has no server-side compute.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString

HOST = "docs.slideruleearth.io"
BASE_URL = f"https://{HOST}/"
SITEMAP_URL = f"https://{HOST}/sitemap.xml"
USER_AGENT = "sliderule-search-server docsearch-builder (https://slideruleearth.io)"
EMBEDDER_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_CHAR_CAP = 1500
WORKERS = 8
REQUEST_TIMEOUT = 30

HEADING_TAGS = ("h1", "h2", "h3", "h4")

CONTENT_SELECTORS = [
    ("div", {"role": "main"}),
    ("article", {}),
    ("main", {}),
    ("div", {"class": "document"}),
    ("div", {"class": "rst-content"}),
]

# URL paths that match one of these prefixes are Sphinx machinery, not
# human-authored content. Filtering them at the crawl stage (before we
# even fetch) saves bandwidth and, more importantly, keeps them out of
# the embeddings + lexical index entirely.
#
# Why each is excluded:
#
#   /_modules/   Sphinx viewcode extension. Generates one HTML page per
#                documented Python module with the entire source code
#                syntax-highlighted. These pages are token-rich copies
#                of the same identifiers the curated API reference
#                describes in prose, so they dominate IDF-weighted
#                lexical ranking and saturate top-K for identifier
#                queries (e.g. a bare "atl03" query would otherwise
#                fill top-5 with sibling sub-chunks of the icesat2
#                module dump). No new semantic information lives here.
#
#   /_sources/   Raw .rst/.md sources, linked from the "View page
#                source" footer. Same content as the rendered page
#                but without chunk-relevant structure.
#
#   /genindex    Auto-generated alphabetical index and its variants
#   /py-modindex (genindex-all.html, py-modindex.html). Pure lists of
#                links, zero prose.
#
#   /search.html Sphinx's own client-side search UI — stub page, not
#                content.
#
# /_static/, /_images/, /_downloads/ don't need to appear here because
# the crawler already rejects non-HTML Content-Type responses (see
# is_html_response + fetch_page).
SKIP_PATH_PREFIXES = (
    "/_modules/",
    "/_sources/",
    "/genindex",
    "/py-modindex",
    "/search.html",
)


# URL-path → category label. Each chunk carries the category through
# to search output so AI agent consumers can weigh content types on
# their own. We're *labeling*, not filtering — release_notes stays
# in the corpus because it's the authoritative answer for version/
# history queries, it just shouldn't dominate top-K for conceptual
# questions. First-match wins; order matters — release_notes must
# come before the broader developer_guide prefix since release notes
# live under it.
CATEGORY_RULES = (
    ("/user_guide/",                      "user_guide"),
    ("/api_reference/",                   "api_reference"),
    ("/developer_guide/release_notes/",   "release_notes"),
    ("/developer_guide/",                 "developer_guide"),
    ("/getting_started/",                 "getting_started"),
    ("/assets/",                          "tutorial"),
    ("/background/",                      "background"),
)
DEFAULT_CATEGORY = "other"


STRIP_SELECTORS = [
    ("nav", {}),
    ("header", {}),
    ("footer", {}),
    ("aside", {}),
    ("form", {"role": "search"}),
    ("div", {"class": "rst-footer-buttons"}),
    ("div", {"class": "wy-nav-side"}),
    ("div", {"class": "wy-nav-top"}),
    ("div", {"class": "wy-breadcrumbs"}),
    ("a", {"class": "headerlink"}),
    ("a", {"class": "fa-github"}),
]


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def fetch_sitemap(session: requests.Session) -> list[str] | None:
    try:
        resp = session.get(SITEMAP_URL, timeout=REQUEST_TIMEOUT)
        if resp.status_code != 200:
            return None
        root = ET.fromstring(resp.text)
    except (requests.RequestException, ET.ParseError):
        return None

    urls: list[str] = []
    for loc in root.iter():
        if loc.tag.endswith("}loc") or loc.tag == "loc":
            text = (loc.text or "").strip()
            if text and urlparse(text).netloc == HOST:
                urls.append(urldefrag(text).url)
    # Drop Sphinx machinery URLs before we ever hit the network — some
    # sitemaps dutifully list /_modules/* and /genindex.html, and we'd
    # rather not waste bandwidth fetching them only to throw away.
    urls = [u for u in urls if is_content_url(u)]
    return sorted(set(urls)) if urls else None


def is_html_response(resp: requests.Response) -> bool:
    ctype = resp.headers.get("Content-Type", "").lower()
    return "text/html" in ctype or "application/xhtml" in ctype


def normalize_url(url: str) -> str:
    return urldefrag(url).url.rstrip("/") or url


def is_content_url(url: str) -> bool:
    """Return False for Sphinx machinery pages that we've decided not
    to include in the corpus (see SKIP_PATH_PREFIXES).

    Operates on the URL's path component only, so it's host-agnostic:
    it works on absolute URLs (from the sitemap or BFS), relative URLs
    that have been resolved via urljoin, and local dev URLs equally.
    """
    path = urlparse(url).path
    return not any(path.startswith(prefix) for prefix in SKIP_PATH_PREFIXES)


def categorize_url(url: str) -> str:
    """Classify a page by URL path. Returns a category label that will
    be stored on every chunk from that page and surfaced in search
    output. See CATEGORY_RULES for the mapping and DEFAULT_CATEGORY
    for the fallback. Path-only (not host-dependent) so it works
    regardless of whether the URL is absolute or relative-resolved.
    """
    path = urlparse(url).path
    for prefix, label in CATEGORY_RULES:
        if path.startswith(prefix):
            return label
    return DEFAULT_CATEGORY


def crawl_from_seed(session: requests.Session, max_pages: int) -> list[str]:
    seen: set[str] = set()
    queue: list[str] = [BASE_URL]
    found: list[str] = []

    while queue and len(found) < max_pages:
        batch = queue[:WORKERS]
        queue = queue[WORKERS:]
        fresh = [u for u in batch if normalize_url(u) not in seen]
        for u in fresh:
            seen.add(normalize_url(u))

        results: list[tuple[str, str | None]] = []
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = {pool.submit(fetch_page, session, u): u for u in fresh}
            for fut in as_completed(futures):
                u = futures[fut]
                try:
                    html = fut.result()
                except Exception:
                    html = None
                results.append((u, html))

        for u, html in results:
            if html is None:
                continue
            found.append(u)
            if len(found) >= max_pages:
                break
            for link in extract_links(html, u):
                if normalize_url(link) not in seen:
                    queue.append(link)

    return found[:max_pages]


def fetch_page(session: requests.Session, url: str) -> str | None:
    try:
        resp = session.get(url, timeout=REQUEST_TIMEOUT)
    except requests.RequestException:
        return None
    if resp.status_code != 200 or not is_html_response(resp):
        return None
    return resp.text


def extract_links(html: str, base: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("mailto:", "javascript:", "#")):
            continue
        full = urljoin(base, href)
        if urlparse(full).netloc != HOST:
            continue
        # Filter machinery links here so the BFS queue never enqueues
        # them. Every rendered Sphinx page has "View page source" and
        # "[source]" links pointing at /_sources/ and /_modules/, so
        # without this filter BFS would discover and fetch hundreds of
        # them transitively.
        full = urldefrag(full).url
        if not is_content_url(full):
            continue
        links.append(full)
    return links


def fetch_all_pages(
    session: requests.Session, urls: list[str]
) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(fetch_page, session, u): u for u in urls}
        for fut in as_completed(futures):
            u = futures[fut]
            try:
                html = fut.result()
            except Exception:
                html = None
            if html is not None:
                out.append((u, html))
    out.sort(key=lambda pair: pair[0])
    return out


def select_main_content(soup: BeautifulSoup):
    for tag, attrs in CONTENT_SELECTORS:
        node = soup.find(tag, attrs) if attrs else soup.find(tag)
        if node is not None:
            return node
    return soup.body or soup


def strip_chrome(node) -> None:
    for tag, attrs in STRIP_SELECTORS:
        for match in list(node.find_all(tag, attrs) if attrs else node.find_all(tag)):
            match.decompose()


def extract_text(node) -> str:
    parts: list[str] = []
    for descendant in node.descendants:
        if isinstance(descendant, NavigableString):
            parts.append(str(descendant))
    text = " ".join(parts)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def page_title(soup: BeautifulSoup, main) -> str:
    h1 = main.find("h1")
    if h1:
        title = extract_text(h1)
        if title:
            return title
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""


def split_long_text(text: str, cap: int) -> list[str]:
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
    final: list[str] = []
    for c in chunks:
        if len(c) <= cap:
            final.append(c)
        else:
            for i in range(0, len(c), cap):
                final.append(c[i : i + cap])
    return final


def collect_text_until_next_heading(start_heading) -> str:
    """Walk forward from a heading, gathering text until the next heading of any level."""
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
    text = " ".join(pieces)
    return re.sub(r"\s+", " ", text).strip()


def chunk_page(url: str, html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    main = select_main_content(soup)
    strip_chrome(main)
    title = page_title(soup, main)

    # Category is a page-level property (URL-derived), so compute it
    # once and attach to every chunk emitted below.
    category = categorize_url(url)

    headings = main.find_all(HEADING_TAGS)

    chunks: list[dict] = []

    if not headings:
        text = extract_text(main)
        for sub_idx, piece in enumerate(split_long_text(text, CHUNK_CHAR_CAP)):
            piece = piece.strip()
            if len(piece) < 40:
                continue
            chunks.append(
                {
                    "url": url,
                    "title": title,
                    "section": title,
                    "category": category,
                    "text": piece,
                    "_order": sub_idx,
                }
            )
        return chunks

    for idx, heading in enumerate(headings):
        heading_text = extract_text(heading)
        body = collect_text_until_next_heading(heading)
        if not body:
            continue
        for sub_idx, piece in enumerate(split_long_text(body, CHUNK_CHAR_CAP)):
            piece = piece.strip()
            if len(piece) < 40:
                continue
            chunks.append(
                {
                    "url": url,
                    "title": title,
                    "section": heading_text or title,
                    "category": category,
                    "text": piece,
                    "_order": idx * 1000 + sub_idx,
                }
            )
    return chunks


def chunk_id(url: str, section: str, order: int) -> str:
    h = hashlib.sha1(f"{url}|{section}|{order}".encode("utf-8")).hexdigest()
    return h[:16]


def round_embedding(vec) -> list[float]:
    return [round(float(x), 6) for x in vec]


def build_corpus(
    pages: list[tuple[str, str]],
) -> tuple[list[dict], str, int]:
    from sentence_transformers import SentenceTransformer

    all_chunks: list[dict] = []
    for url, html in pages:
        all_chunks.extend(chunk_page(url, html))

    all_chunks.sort(key=lambda c: (c["url"], c["_order"]))

    log(f"Embedding {len(all_chunks)} chunks with {EMBEDDER_NAME}...")
    model = SentenceTransformer(EMBEDDER_NAME)
    texts = [c["text"] for c in all_chunks]
    t0 = time.time()
    vectors = (
        model.encode(texts, batch_size=32, show_progress_bar=True, convert_to_numpy=True)
        if texts
        else []
    )
    embed_seconds = time.time() - t0
    dim = int(vectors.shape[1]) if len(texts) else 0

    out_chunks: list[dict] = []
    for chunk, vec in zip(all_chunks, vectors):
        out_chunks.append(
            {
                "id": chunk_id(chunk["url"], chunk["section"], chunk["_order"]),
                "url": chunk["url"],
                "title": chunk["title"],
                "section": chunk["section"],
                # Category is a URL-derived content-type tag (user_guide,
                # api_reference, release_notes, ...). Travels into each
                # search result so AI agent consumers can weigh types.
                "category": chunk.get("category", DEFAULT_CATEGORY),
                "text": chunk["text"],
                "embedding": round_embedding(vec),
            }
        )

    log(f"Embedded with {EMBEDDER_NAME} in {embed_seconds:.1f}s")
    return out_chunks, EMBEDDER_NAME, dim


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


# Stream the file through sha256 so we don't have to re-read corpus.json
# into memory just to fingerprint it — corpus.json can be tens of MB and
# we've already written it to disk at this point.
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


# meta.json is the public "what is currently deployed" record. The skill
# client fetches it on every query (tiny) and uses corpus_sha256 to decide
# whether its local corpus cache is still valid. Because the client keys
# its cache by this hash, meta.json is effectively the cache-invalidation
# signal for the entire distribution.
def write_meta(
    out_dir: Path,
    pages_crawled: int,
    chunk_count: int,
    dim: int,
    crawl_strategy: str,
    corpus_bytes: int,
    corpus_sha256: str,
) -> Path:
    meta = {
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_host": HOST,
        "crawl_strategy": crawl_strategy,
        "pages_crawled": pages_crawled,
        "chunk_count": chunk_count,
        "embedder": EMBEDDER_NAME,
        "embedding_dim": dim,
        "corpus_bytes": corpus_bytes,
        # Fingerprint of the corpus.json bytes this meta was written
        # alongside. The skill's cache is keyed by this value.
        "corpus_sha256": corpus_sha256,
    }
    path = out_dir / "meta.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, sort_keys=False, ensure_ascii=False)
        f.write("\n")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default="generated/docsearch",
        help="Directory to write corpus.json and meta.json into.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=200,
        help="Cap on the number of pages to fetch.",
    )
    # --min-pages / --min-chunks are the empty-corpus guards. If the docs
    # site goes down mid-build, or if a site restructure breaks the
    # content extractor, we'd otherwise silently ship a zero-chunk corpus
    # as a successful deploy. These thresholds abort the build *before*
    # touching corpus.json/meta.json, so the previous known-good
    # artifacts stay in place.
    parser.add_argument(
        "--min-pages",
        type=int,
        default=20,
        help=(
            "Abort (non-zero exit) if fewer than this many pages crawled "
            "successfully. Guards against transient docs-site outages "
            "silently deploying an empty corpus. Lower intentionally if "
            "you really want to ship a tiny build."
        ),
    )
    parser.add_argument(
        "--min-chunks",
        type=int,
        default=100,
        help=(
            "Abort if fewer than this many chunks were produced. Catches "
            "the case where pages fetched but nothing usable came out of "
            "the extractor (site restructure, selector mismatch, etc)."
        ),
    )
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = make_session()

    log("Resolving page list...")
    t0 = time.time()
    urls = fetch_sitemap(session)
    if urls:
        strategy = "sitemap"
        urls = urls[: args.max_pages]
        log(f"  sitemap.xml -> {len(urls)} URLs")
    else:
        strategy = "bfs"
        log("  sitemap unavailable, falling back to BFS crawl")
        urls = crawl_from_seed(session, args.max_pages)
        log(f"  BFS -> {len(urls)} URLs")

    pages = fetch_all_pages(session, urls)
    crawl_seconds = time.time() - t0
    log(f"Crawled {len(pages)} pages in {crawl_seconds:.1f}s")

    # Guard #1: not enough pages means the site is probably down or the
    # crawler is broken. Bail before we touch the on-disk artifacts.
    if len(pages) < args.min_pages:
        log(
            f"ERROR: only {len(pages)} pages fetched successfully "
            f"(minimum {args.min_pages}). Refusing to overwrite "
            f"corpus.json/meta.json — a transient docs outage is the "
            f"likely cause. Re-run later, or lower --min-pages if you "
            f"really mean to ship this."
        )
        return 1

    chunks, embedder, dim = build_corpus(pages)
    log(f"Chunked to {len(chunks)} pieces")

    # Guard #2: pages fetched but extractor produced nothing useful.
    # Usually means upstream HTML structure changed and CONTENT_SELECTORS
    # no longer matches. Bail so the old corpus isn't clobbered by an
    # empty one.
    if len(chunks) < args.min_chunks:
        log(
            f"ERROR: only {len(chunks)} chunks produced "
            f"(minimum {args.min_chunks}). Refusing to overwrite "
            f"corpus.json/meta.json. Likely cause: upstream HTML "
            f"restructure — check CONTENT_SELECTORS / STRIP_SELECTORS."
        )
        return 1

    # Past the guards. Write corpus first so we can hash it, then write
    # meta pointing at that hash.
    corpus_path = write_corpus(out_dir, chunks, dim)
    corpus_bytes = corpus_path.stat().st_size
    corpus_sha = sha256_of(corpus_path)
    meta_path = write_meta(
        out_dir,
        pages_crawled=len(pages),
        chunk_count=len(chunks),
        dim=dim,
        crawl_strategy=strategy,
        corpus_bytes=corpus_bytes,
        corpus_sha256=corpus_sha,
    )

    print(f"Crawled {len(pages)} pages in {crawl_seconds:.1f}s")
    print(f"Chunked to {len(chunks)} pieces")
    print(f"Embedded with {embedder}")
    mb = corpus_bytes / (1024 * 1024)
    print(f"Wrote {corpus_path} ({mb:.1f} MB)")
    print(f"Wrote {meta_path}  (corpus_sha256={corpus_sha[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
