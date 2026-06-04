# Row 29 review

> Companion to `29-how-does-atl13-derive-inland-water-surface-height-results.md`. Open both side-by-side;
> this file is your editable form.

**Query:** `how does ATL13 derive inland water surface height`
**Labeled corpus:** `nsidc`
**Panel signature:** `37c2b0c07384` — do not edit; identifies the result
panel these verdicts were scored against (ingest flags this row stale
if the corpus is rechunked out from under it).

---

## Per-result verdicts

Mark each result `correct`, `partial`, or `wrong`. Leave blank to skip.

**docsearch:**

- r1: partial
- r2: wrong
- r3: wrong
- r4: wrong
- r5: wrong

**nsidc:**

- r1: wrong
- r2: partial
- r3: wrong
- r4: wrong
- r5: partial

## Overall verdict

One of: `correct` | `partial` | `wrong`

- overall: partial

## Cross-corpus routing

Should this query target a different corpus? One of:
`keep` | `redirect-to-docsearch` | `redirect-to-nsidc` | `both-corpora`

- routing: keep

## Human truth (the actual right answer)

If the right answer was returned at some rank, you can leave these
blank — the per-result verdicts above already capture that. Fill
these in **only if** the correct answer is not in either result set,
or if you want to override what's correct.

Repeat any field on a new `- field: value` line for multiple values.

- corpus: 
- url: 
- section: 
- pages: 
- notes: 
BROAD: methodological "how is it derived" query; true answer is the ATL13
ATBD retrieval method (Ch 2-4), distributed across pages, no standalone chunk.

Scored on content, not document-match:
- r2 (ATL03 ATBD, wrong doc) = partial: states ATL13 draws from ATL03
  geolocated photon heights — a real input fact for the derivation.
- r5 (Physics of Open Water) = partial: names the physical processes the
  retrieval considers. Best "how" content in the panel — but ranked LAST.
- r1/r3/r4 = wrong: correct document, but abstract / changelog / goals text
  carries no derivation info. Document-match earned them rank, not relevance.

Recall/ranking gap: the substantive content (r5) is buried at rank 5 while
three contentless same-doc chunks rank above it. If the Ch 3/4 algorithm
section is chunked, it should be the top hit and isn't surfaced.

