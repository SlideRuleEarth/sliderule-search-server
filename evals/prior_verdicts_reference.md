# Prior verdicts — re-scoring reference

> **Read me.** These are your **April verdicts**, scored against an *earlier*
> corpus, shown next to the **current** result panels. Use them as a memory
> aid, **not** as ground truth: the corpus was rechunked since, so rank slots
> and chunk text may have shifted. Where the current chunk at a rank looks
> different from what your old verdict assumed, re-judge from scratch.
>
> Workflow: open a row's `*-review.md` (blank) + `*-results.md` (current),
> glance here for your prior call, then fill the verdict.

Covers 66 rows that had completed reviews. Generated from the
pre-reset `human_review.json` (git HEAD) + current `-results.md` panels.

## Row 1 — labeled `docsearch` — `atl03x X-Series API photon processing`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r2 | 🟡 partial | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Overview |
| r3 | 🟡 partial | /user_guide/icesat2.html — A.1 Segmented Photon Data - atl03sp |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.4 Ancillary Data |
| r5 | 🟡 partial | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Request builder |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 28 |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.3.1 Range bias determination |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.2 Data Flow Within ATL03 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 96 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Input Variables |

---

## Row 2 — labeled `docsearch` — `atl06x surface fit elevation`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"corpus": "docsearch", "urls": ["https://docs.slideruleearth.io/user_guide/icesat2.html"], "sections": ["2", "atl06-atl06x"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Panel visibility by endpoint |
| r2 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r3 | 🟡 partial | /user_guide/icesat2.html — A.2 Elevations - atl06p |
| r4 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r5 | ❌ wrong | /user_guide/icesat2.html — 2. ATL06 - atl06x |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 19 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 41 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 130 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.8 Quality and classification flags throughout flow of analysis |

---

## Row 3 — labeled `docsearch` — `atl24x bathymetry subsetting`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 5. ATL24 - atl24x |
| r2 | 🟡 partial | /user_guide/articles/250328_atl24_golden_run.html — Background |
| r3 | 🟡 partial | /getting_started/Examples.html — Examples |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r5 | 🟡 partial | /user_guide/articles/250328_atl24_golden_run.html — Statistics |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — Change History Log |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Introduction |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Data Workflow |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Input Variables |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.5.6 Estimation of short segment bathymetry other subsurface anomalies |

---

## Row 4 — labeled `docsearch` — `yapc photon classifier`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/icesat2.html — 1.2.2 YAPC Classification |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1.6.1 PhoREAL Parameters |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r5 | 🟡 partial | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Request builder |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 111 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 112 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 115 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Quantile Trees Classification |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.8 Ensemble Classification |

---

## Row 5 — labeled `docsearch` — `cnf confidence filter parameter`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r2 | ✅ correct | /user_guide/icesat2.html — 5.1 Query Parameters |
| r3 | 🟡 partial | /user_guide/basic_usage.html — Define the Request Parameters |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v04-04-00.html — New Features |
| r5 | ❌ wrong | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Request builder |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — Change History Log |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 3 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.2 Photon Weights |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 78 |

---

## Row 6 — labeled `docsearch` — `srt surface reference type parameter`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 2. ATL06 - atl06x |
| r2 | ❌ wrong | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r3 | ❌ wrong | /user_guide/icesat2.html — 4. ATL13 - atl13x |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r5 | ✅ correct | /user_guide/icesat2.html — A.2 Elevations - atl06p |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.2 Land Ice |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 98 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 8.0 The Quality Assessment Group |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |

---

## Row 7 — labeled `docsearch` — `how to filter ICESat-2 photons by confidence`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — ICESat-2 Module |
| r2 | ✅ correct | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r3 | 🟡 partial | /user_guide/icesat2.html — 5.1 Query Parameters |
| r4 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r5 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.2 Overview |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.3 Definitions of Variables used in Algorithm |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.1 Introduction |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.2 Overview |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |

---

## Row 8 — labeled `docsearch` — `how to run atl06 with raster DEM sampling`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 2. ATL06 - atl06x |
| r2 | ❌ wrong | /user_guide/raster_sampling.html — Overview |
| r3 | 🟡 partial | /developer_guide/release_notes/release-v03-03-00.html — Major Changes |
| r4 | ❌ wrong | /getting_started/Examples.html — Examples |
| r5 | 🟡 partial | /developer_guide/design/SlideRuleWebClient.html — SRWC-5.1: Raster Sampling |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 72 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 66 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 117 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 57 |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 4 Version History |

---

## Row 9 — labeled `docsearch` — `how to use SlideRule Python client install`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /getting_started/Install.html — PyPI |
| r2 | ✅ correct | /getting_started/Install.html — Installation |
| r3 | ✅ correct | /getting_started/Install.html — Developer Install |
| r4 | 🟡 partial | /developer_guide/release_notes/release-v01-04-00.html — Required Updates |
| r5 | ❌ wrong | /api_reference/gedi.html — init |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |

---

## Row 10 — labeled `docsearch` — `what is the X-Series API in SlideRule`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/xseries.html — X-Series APIs |
| r2 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — SRWC-4.3: Tutorial |
| r3 | ❌ wrong | /user_guide/icesat2.html — ICESat-2 Module |
| r4 | ❌ wrong | /api_reference/sliderule.html — sliderule |
| r5 | ❌ wrong | / — SlideRule v5.4.2 |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |

---

## Row 11 — labeled `docsearch` — `earthdata authentication credentials sliderule`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://docs.slideruleearth.io/developer_guide/how_tos/accessing_earthdata_cloud.html"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/articles/260312_security_model.html — Overview |
| r2 | ❌ wrong | /user_guide/raster_sampling.html — Overview |
| r3 | ❌ wrong | /user_guide/articles/260120_private_clusters.html — SlideRule Authenticator |
| r4 | ❌ wrong | /developer_guide/how_tos/amazon_linux_arm_setup.html — 2-Factor Authentication |
| r5 | 🟡 partial | /background/NASA-Earthdata.html — Steps to Sync from NSIDC |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Historical Perspective |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |

---

## Row 12 — labeled `docsearch` — `output SlideRule results as GeoParquet format`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/articles/230224_geoparquet.html — Overview |
| r2 | ✅ correct | /user_guide/arrow_output.html — Parameters |
| r3 | 🟡 partial | /user_guide/arrow_output.html — Overview |
| r4 | 🟡 partial | /user_guide/articles/230224_geoparquet.html — Constraints |
| r5 | 🟡 partial | /user_guide/articles/230224_geoparquet.html — 2023-02-24: GeoParquet |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Page 6 |

---

## Row 13 — labeled `docsearch` — `how to process atl06 elevations`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://docs.slideruleearth.io/user_guide/icesat2.html"], "sections": ["ICESat-2 Module", "atl06-atl06x"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /api_reference/icesat2.html — atl06 |
| r2 | ❌ wrong | /api_reference/icesat2.html — atl08 |
| r3 | ❌ wrong | /api_reference/icesat2.html — atl06sp |
| r4 | ❌ wrong | /api_reference/icesat2.html — atl06s |
| r5 | ❌ wrong | /getting_started/Examples.html — Examples |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 23 |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.1 ATL03 Overview |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 32 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 66 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 32 |

---

## Row 14 — labeled `docsearch` — `how to use yapc photon classifier in atl03`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/icesat2.html — 1.2.2 YAPC Classification |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r4 | ❌ wrong | /user_guide/articles/260528_web_client_endpoint_scoped_params.html — Request builder |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1.6.1 PhoREAL Parameters |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 111 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 115 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 112 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 8 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |

---

## Row 15 — labeled `docsearch` — `how to sample ArcticDEM raster mosaic`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"notes": "complete answer is in examples github repo"}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/raster_sampling.html — Parameters |
| r2 | 🟡 partial | /user_guide/articles/221110_gdal_vrt_benchmark.html — Overview |
| r3 | 🟡 partial | /developer_guide/design/SlideRuleWebClient.html — SRWC-5.1: Raster Sampling |
| r4 | ❌ wrong | /getting_started/Examples.html — Examples |
| r5 | ❌ wrong | /user_guide/articles/221110_gdal_vrt_benchmark.html — 2022-11-10: VRT Performance Benchmarking |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.3.2 Mask Generation |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 104 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.3.2 Mask Generation |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 66 |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl06-v006-userguide.pdf — 5.2 Date Last Updated |

---

## Row 16 — labeled `docsearch` — `how to subset atl24 bathymetry data`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"notes": "examples exist in examples github repo"}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /getting_started/Examples.html — Examples |
| r2 | 🟡 partial | /user_guide/articles/250328_atl24_golden_run.html — Background |
| r3 | 🟡 partial | /user_guide/icesat2.html — 5. ATL24 - atl24x |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r5 | ❌ wrong | /user_guide/articles/250328_atl24_golden_run.html — Statistics |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Introduction |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Input Variables |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Output Variables |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Data Workflow |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |

---

## Row 17 — labeled `docsearch` — `how to query atl13 lake by name`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"notes": "real answer is in examples github repo"}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/articles/250530_arbitrary_code_execution.html — Example Use Case - ATL13 Lake ID Mapping |
| r2 | 🟡 partial | /user_guide/icesat2.html — 4.1 Inland Lake Parameters |
| r3 | ❌ wrong | /getting_started/Examples.html — Examples |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v04-14-00.html — New/Improved Functionality |
| r5 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — Example Use Case - ATL13 Lake ID Mapping |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 3.4.1 The ATL13 Inland Water Body Mask |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl13-v007-userguide.pdf — 1.2.2.3 METADATA |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.7.1.2 Water Body Reference Identification Scheme: |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.1 Overall Approach |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl13-v007-userguide.pdf — 2.3.2.1 Inland Water Backscatter |

---

## Row 18 — labeled `docsearch` — `when was atl24x added to sliderule release`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /developer_guide/release_notes/release-v04-11-00.html — Major Changes |
| r2 | ❌ wrong | /user_guide/icesat2.html — 5. ATL24 - atl24x |
| r3 | ❌ wrong | /user_guide/icesat2.html — 5.2 Ancillary Data |
| r4 | 🟡 partial | /developer_guide/release_notes/release-v05-00-00.html — New Functionality |
| r5 | 🟡 partial | /developer_guide/release_notes/release-v03-05-00.html — Release v3.5.x |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |

---

## Row 19 — labeled `docsearch` — `yapc added to sliderule version release notes`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"corpus": "docsearch", "urls": ["https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-03-00.html"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/articles/260120_private_clusters.html — 2026-01-20: Private Clusters |
| r2 | ❌ wrong | /user_guide/articles/251208_v5_server_release.html — 2025-12-08: Public Cluster Release v5 |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v03-05-00.html — Release v3.5.x |
| r4 | ❌ wrong | /developer_guide/release_notes/web-release-v04-00-03.html — Summary |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v02-00-00.html — New Features |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r4 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.3 Naming Convention |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |

---

## Row 20 — labeled `docsearch` — `sliderule version 5 breaking changes new functionality`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /developer_guide/release_notes/release-v02-00-00.html — New Features |
| r2 | ❌ wrong | /user_guide/versioning.html — Library Version ( version ) |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v05-00-00.html — Breaking Changes |
| r4 | ✅ correct | /user_guide/versioning.html — Note on Reproducibility |
| r5 | 🟡 partial | /user_guide/articles/251208_v5_server_release.html — 2025-12-08: Public Cluster Release v5 |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |

---

## Row 21 — labeled `docsearch` — `recent changes to atl06x release notes`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"corpus": "docsearch", "urls": ["https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-03-00.html"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/articles/251208_v5_server_release.html — 2025-12-08: Public Cluster Release v5 |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v04-11-00.html — Major Changes |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v05-00-00.html — New Functionality |
| r4 | ❌ wrong | /user_guide/articles/251208_v5_server_release.html — TL;DR |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v05-02-00.html — Issues Resolved |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.5 Goals of ICESat-2 Inland Water Body Height Data Products |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 7.7 Other ATLAS and Spacecraft Parameters |
| r3 | ❌ wrong | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 4 Version History |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 7.2.1 ATLAS Start Pulse Detector |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |

---

## Row 22 — labeled `docsearch` — `GEDI L4A python API parameters`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /api_reference/gedi.html — gedi04a |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v03-01-00.html — Major Changes |
| r3 | ❌ wrong | /user_guide/gedi.html — 1. Overview |
| r4 | 🟡 partial | /api_reference/gedi.html — gedi |
| r5 | ✅ correct | /api_reference/gedi.html — init |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 5 |
| r2 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 14 |
| r3 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 1 |
| r4 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 22 |
| r5 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 17 |

---

## Row 23 — labeled `docsearch` — `raster sampling API function parameters`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/raster_sampling.html — Parameters |
| r2 | 🟡 partial | /user_guide/raster_sampling.html — Parameters |
| r3 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — SRWC-3.3: Advanced Mode |
| r4 | ❌ wrong | /user_guide/raster_sampling.html — Parameters |
| r5 | 🟡 partial | /developer_guide/release_notes/release-v04-00-00.html — Major Changes |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 72 |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.4.2.1 /atlas_impulse_response/pce1_spot1 or /pce2_spot3 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.5.2 Solution Approach |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 2.3.3 The Multiple Altimeter Beam Experimental Lidar (MABEL) |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 4.5.2 Solution Approach |

---

## Row 24 — labeled `docsearch` — `getting canopy height from atl03 photons using atl08`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r2 | 🟡 partial | /user_guide/icesat2.html — A.1 Segmented Photon Data - atl03sp |
| r3 | 🟡 partial | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 4.2 Date Last Updated |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 7 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 44 |
| r4 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.1 Noise Filtering |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 54 |

---

## Row 25 — labeled `docsearch` — `add ancillary fields to sliderule atl06 output`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 2.1 Ancillary Data |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v04-01-00.html — Release v4.1.x |
| r3 | ❌ wrong | /user_guide/icesat2.html — 3.2 Ancillary Data |
| r4 | ❌ wrong | /user_guide/icesat2.html — 5.2 Ancillary Data |
| r5 | ❌ wrong | /user_guide/icesat2.html — 4.2 Ancillary Data |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 53 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 6 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 69 |

---

## Row 26 — labeled `nsidc` — `how does ATL03 signal finding algorithm work`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"corpus": "nsidc", "urls": ["https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf"], "sections": ["5.1.4"]}`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r2 | ❌ wrong | /user_guide/icesat2.html — 1.5.2 ATL06-SR Ancillary Data |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r4 | ❌ wrong | /api_reference/icesat2.html — atl08 |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1. ATL03 - atl03x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — List of Tables |
| r2 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.1 Noise Filtering |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 30 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 95 |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.1 Appendix A – ATL03 Output Parameter Table. |

---

## Row 27 — labeled `nsidc` — `how does ATL06 surface fit algorithm compute elevation`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 1.5.2 ATL06-SR Ancillary Data |
| r2 | ❌ wrong | /user_guide/icesat2.html — A.2 Elevations - atl06p |
| r3 | 🟡 partial | /developer_guide/release_notes/release-v04-15-00.html — Compatibility Changes |
| r4 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r5 | 🟡 partial | /user_guide/icesat2.html — 1.5 ATL06-SR Algorithm |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 73 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 56 |
| r4 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 33 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 5.3.3 Compute signal photon histogram of long segments per ground track |

---

## Row 28 — labeled `nsidc` — `how does ATL08 classify photons into ground canopy noise`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 1.6.2 ATL08-PhoREAL Ancillary Data |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |
| r3 | 🟡 partial | /user_guide/icesat2.html — A.1 Segmented Photon Data - atl03sp |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1.5 ATL06-SR Algorithm |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.1 Noise Filtering |
| r2 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 4.2 Date Last Updated |
| r3 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 76 |
| r4 | ✅ correct | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.5 Refining the Photon Classifications |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 31 |

---

## Row 29 — labeled `nsidc` — `how does ATL13 derive inland water surface height`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"corpus": "nsidc", "urls": ["https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf"], "sections": ["4.1"]}`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 4. ATL13 - atl13x |
| r2 | ❌ wrong | /user_guide/icesat2.html — 4.1 Inland Lake Parameters |
| r3 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — Example Use Case - ATL13 Lake ID Mapping |
| r4 | ❌ wrong | /getting_started/Examples.html — Examples |
| r5 | ❌ wrong | /api_reference/icesat2.html — atl13s |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — Abstract |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 1.2 Data Product Overview |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — Change History Log |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.5 Goals of ICESat-2 Inland Water Body Height Data Products |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 2.0 PHYSICS OF OPEN WATER |

---

## Row 30 — labeled `nsidc` — `ATL24 PointNet++ bathymetric photon classification`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/articles/250328_atl24_golden_run.html — Background |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r3 | 🟡 partial | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r5 | 🟡 partial | /user_guide/icesat2.html — 5.1 Query Parameters |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.4 PointNet++ Classification |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.8 Ensemble Classification |
| r3 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.4 PointNet++ Classification |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r5 | ✅ correct | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.4 PointNet++ Classification |

---

## Row 31 — labeled `nsidc` — `GEDI L4A biomass estimation from waveforms algorithm`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"corpus": "nsidc", "urls": ["https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf"], "notes": "\"broad-scope query \u2014 entire ATBD is on-topic\""}`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/gedi.html — 1. Overview |
| r2 | ❌ wrong | /api_reference/gedi.html — gedi01b |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v03-01-00.html — Major Changes |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v03-02-00.html — Issues Resolved |
| r5 | ❌ wrong | /api_reference/gedi.html — gedi04a |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 3 |
| r2 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 17 |
| r3 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 1 |
| r4 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 1 |
| r5 | 🟡 partial | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 2 |

---

## Row 32 — labeled `nsidc` — `ATL03 geophysical corrections ocean tides solid earth`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /background/ICESat-2.html — References |
| r2 | 🟡 partial | /user_guide/icesat2.html — 2. ATL06 - atl06x |
| r3 | 🟡 partial | /developer_guide/release_notes/release-v04-09-00.html — Changes |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v05-03-00.html — Release v5.3.x |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v04-09-00.html — Release v4.9.x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/user-guide/atl06-v006-userguide.pdf — 1.2.3 File Contents |
| r2 | ❌ wrong | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.3 File Contents |
| r3 | ✅ correct | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 2.3.2.2 Photon round-trip range correction |
| r4 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.2.3 File Contents |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — Appendix A – ICEsat-2/atlas description |

---

## Row 33 — labeled `nsidc` — `ATL08 canopy height calculation method`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /developer_guide/release_notes/release-v02-01-00.html — Known Issues |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v03-00-00.html — Issues Resolved |
| r3 | ❌ wrong | /user_guide/icesat2.html — 3. ATL08 - atl08x |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |
| r5 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — Appendix A. Parameter Components |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 7 |
| r2 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.2.5 Ground-Finding Filter |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 121 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 49 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 44 |

---

## Row 34 — labeled `nsidc` — `ATL03 HDF5 file structure data groups photon fields`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.4 Ancillary Data |
| r3 | ❌ wrong | /api_reference/icesat2.html — atl03s |
| r4 | ❌ wrong | /api_reference/icesat2.html — atl03v |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.2.5 HDF5 Dataset Information |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.4 ATL03 Data Structure for Each Ground Track |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 9.0 METADATA |
| r4 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.4.1 METADATA |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.4.5 gt1l–gt3r |

---

## Row 35 — labeled `nsidc` — `ATL06 quality flags values interpretation`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r2 | ❌ wrong | /user_guide/icesat2.html — 3.1 Quality Filter Parameters |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v04-08-00.html — General Changes |
| r4 | ❌ wrong | /user_guide/icesat2.html — A.1 Segmented Photon Data - atl03sp |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v04-00-00.html — Issues Resolved |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 96 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 7.7.5 Geolocation and Calibration Data Quality flag |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Quality and Filtering Flags |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Quality and Filtering Flags |
| r5 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 57 |

---

## Row 36 — labeled `nsidc` — `ATL08 terrain classification output variables HDF5`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 3.1 Quality Filter Parameters |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v04-09-00.html — Changes |
| r3 | ❌ wrong | /api_reference/icesat2.html — atl08 |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.2.5 Naming Convention |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.2.2 ATLAS/ICESat-2 Description |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 34 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 7 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Classification Algorithms |

---

## Row 37 — labeled `nsidc` — `ATL13 file naming convention granule filename`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /api_reference/icesat2.html — atl13s |
| r2 | ❌ wrong | /user_guide/icesat2.html — 4.2 Ancillary Data |
| r3 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — User Lua Script |
| r4 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — Example Use Case - ATL13 Lake ID Mapping |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v05-01-00.html — Issues Resolved |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/user-guide/atl13-v007-userguide.pdf — 1.2.3 File Naming Convention |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl13-v007-userguide.pdf — 1.2.3 File Naming Convention |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 35 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Classification Algorithms |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.3 Naming Convention |

---

## Row 38 — labeled `nsidc` — `ATL24 file contents and spatial coverage`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /getting_started/Examples.html — Examples |
| r2 | 🟡 partial | /developer_guide/release_notes/release-v04-08-00.html — Known Issues and Remaining Tasks |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r4 | ❌ wrong | /user_guide/articles/250328_atl24_golden_run.html — Lessons Learned |
| r5 | ❌ wrong | /user_guide/icesat2.html — 5. ATL24 - atl24x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.3.2 Resolution |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Page 4 |
| r3 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.2 File Contents |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Performance Assessment and Validation |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.3 Naming Convention |

---

## Row 39 — labeled `nsidc` — `GEDI L4A footprint geolocation variables AGBD`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/gedi.html — 3.4 L4A Footprints |
| r2 | 🟡 partial | /user_guide/gedi.html — 1. Overview |
| r3 | ❌ wrong | /api_reference/gedi.html — gedi04a |
| r4 | ❌ wrong | /background/GEDI.html — References |
| r5 | ❌ wrong | /user_guide/gedi.html — 3.2 L2A Footprints |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 3 |
| r2 | 🟡 partial | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 10 |
| r3 | 🟡 partial | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 9 |
| r4 | 🟡 partial | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 2 |
| r5 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 1 |

---

## Row 41 — labeled `nsidc` — `ATL06 data groups structure for land ice`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r2 | ❌ wrong | /background/NASA-Earthdata.html — NSIDC |
| r3 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — SRWC-5.1: Raster Sampling |
| r4 | ❌ wrong | /user_guide/icesat2.html — 3. ATL08 - atl08x |
| r5 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 53 |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl06-v006-userguide.pdf — 1.2.4.5 quality_assessment |
| r3 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.2.4.6 Dimension Scales |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 55 |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 53 |

---

## Row 42 — labeled `nsidc` — `ATL08 DRAGANN noise filtering algorithm`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 1.5 ATL06-SR Algorithm |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.6.2 ATL08-PhoREAL Ancillary Data |
| r3 | 🟡 partial | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 15 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 95 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 2 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 57 |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 102 |

---

## Row 43 — labeled `nsidc` — `ATL24 ensemble classification bathymetry`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/articles/250328_atl24_golden_run.html — Background |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r3 | 🟡 partial | /developer_guide/release_notes/release-v04-07-00.html — Known Issues and Remaining Tasks |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r5 | 🟡 partial | /user_guide/icesat2.html — 5.1 Query Parameters |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Data Workflow |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3 Processing |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Known Issues |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Quality and Filtering Flags |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 2.3.1.8 Ensemble Classification |

---

## Row 44 — labeled `nsidc` — `ATL13 processing workflow and goals`

Prior overall=`partial`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf"], "notes": "\"broad-scope: entire ATBD covers this query; URL-only match by design\""}`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /api_reference/icesat2.html — atl13sp |
| r2 | 🟡 partial | /user_guide/icesat2.html — 4. ATL13 - atl13x |
| r3 | 🟡 partial | /user_guide/articles/250530_arbitrary_code_execution.html — Example Use Case - ATL13 Lake ID Mapping |
| r4 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — User Python Script |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v04-14-00.html — New/Improved Functionality |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Input Variables |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.5 Goals of ICESat-2 Inland Water Body Height Data Products |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Data Workflow |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Page 4 |

---

## Row 45 — labeled `nsidc` — `strong versus weak beams ICESat-2 ATLAS`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /background/ICESat-2.html — Mission |
| r2 | 🟡 partial | /background/ICESat-2.html — Mission |
| r3 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v02-00-00.html — Release v2.0.x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 1.1 Background |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 7.5 The Spacecraft Orientation Parameter |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.4 Algorithm Implementation |
| r4 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 2.2 Acquisition |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.2 ATLAS/ICESat-2 Description |

---

## Row 46 — labeled `nsidc` — `how ATL08 uses ATL03 photons for classification`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v01-01-00.html — New Features |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v04-07-00.html — Development Updates |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.1 Noise Filtering |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 3 SOFTWARE AND TOOLS |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 28 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 96 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.1 Introduction |

---

## Row 47 — labeled `nsidc` — `photon classification confidence values ATL03`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/icesat2.html — 1.2.1 Native ATL03 Photon Classification |
| r2 | ❌ wrong | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1.2.4 ATL24 Classification |
| r4 | ❌ wrong | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1. ATL03 - atl03x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.3 ATL03 ATBD Sections |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Quality and Filtering Flags |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 96 |
| r4 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.2.2 gt1l–gt3r |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 5.1.2 Overview |

---

## Row 48 — labeled `nsidc` — `ATLAS laser altimeter instrument specifications`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /background/ICESat-2.html — Mission |
| r2 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r3 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r4 | ❌ wrong | /background/ICESat-2.html — Mission |
| r5 | ❌ wrong | /user_guide/icesat2.html — A.2 Elevations - atl06p |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 24 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 1.1 Background |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.3 ICESat-2 ATLAS Instrument |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 104 |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.2 ATLAS/ICESat-2 Description |

---

## Row 49 — labeled `nsidc` — `ATL03 photon geolocation algorithm method`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 1.6.1 PhoREAL Parameters |
| r2 | ❌ wrong | /background/ICESat-2.html — References |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r4 | ❌ wrong | /user_guide/icesat2.html — A.1 Segmented Photon Data - atl03sp |
| r5 | ❌ wrong | /api_reference/icesat2.html — atl03sp |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.3 ATL03 ATBD Sections |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.1 The ICESat-2 Geolocation Along-Track Segments |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.3 ATL03 ATBD Sections |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.1 The ICESat-2 Geolocation Along-Track Segments |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — Change History Log |

---

## Row 50 — labeled `nsidc` — `GEDI shot footprint size geometry`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/gedi.html — 3. Returned data |
| r2 | 🟡 partial | /user_guide/gedi.html — 3.2 L2A Footprints |
| r3 | 🟡 partial | /user_guide/gedi.html — 3.4 L4A Footprints |
| r4 | 🟡 partial | /user_guide/gedi.html — 1. Overview |
| r5 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — Appendix A. Parameter Components |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 6 |
| r2 | 🟡 partial | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 11 |
| r3 | 🟡 partial | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 19 |
| r4 | 🟡 partial | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 14 |
| r5 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 42 |

---

## Row 51 — labeled `docsearch` — `sliderule module initialization session setup`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://docs.testsliderule.org/api_reference/sliderule.html"], "sections": ["init"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /developer_guide/release_notes/release-v05-00-00.html — Breaking Changes |
| r2 | ❌ wrong | /api_reference/sliderule.html — set_url |
| r3 | ❌ wrong | /user_guide/versioning.html — Python Client |
| r4 | ❌ wrong | /getting_started/Getting-Started.html — Common Package Modules |
| r5 | ❌ wrong | /user_guide/articles/260120_private_clusters.html — Access |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |

---

## Row 52 — labeled `docsearch` — `h5 hdf5 read function parameters h5p h5x`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /api_reference/h5.html — h5 |
| r2 | 🟡 partial | /user_guide/articles/210423_h5coro.html — H5Coro::read |
| r3 | 🟡 partial | /api_reference/h5.html — h5p |
| r4 | 🟡 partial | /api_reference/h5.html — h5x |
| r5 | 🟡 partial | /api_reference/h5.html — h5 |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.2.5 HDF5 Dataset Information |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.2.5 HDF5 Dataset Information |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Classification Algorithms |
| r4 | ❌ wrong | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.4.5 gt1l–gt3r |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 1.2.5 Naming Convention |

---

## Row 53 — labeled `docsearch` — `icesat2 atl06p python function parameters`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /api_reference/icesat2.html — atl06p |
| r2 | ❌ wrong | /developer_guide/release_notes/release-v04-00-00.html — Breaking Changes |
| r3 | 🟡 partial | /user_guide/basic_usage.html — Issue the Processing Request |
| r4 | ❌ wrong | /api_reference/icesat2.html — init |
| r5 | ❌ wrong | /api_reference/icesat2.html — atl13sp |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 58 |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 2.0 PHYSICS OF OPEN WATER |
| r3 | ❌ wrong | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.4.5 gt1l–gt3r |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.1 ATL03 Overview |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 7.2.2 ATLAS Transmitter Echo Path |

---

## Row 54 — labeled `docsearch` — `earthdata CMR search function signature`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /api_reference/earthdata.html — cmr |
| r2 | 🟡 partial | /api_reference/earthdata.html — search |
| r3 | 🟡 partial | /api_reference/earthdata.html — stac |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v04-20-00.html — Issues Resolved |
| r5 | ❌ wrong | /api_reference/earthdata.html — cmr |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Appendix A: Acronyms |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — CM Foreword |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 9.0 METADATA |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Historical Perspective |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — Glossary/Acronyms |

---

## Row 55 — labeled `docsearch` — `generate a DEM from ICESat-2 data over my area of interest`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"notes": "Examples hold the answer but they are only available thru a url to the examples repo"}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /developer_guide/why_sliderule.html — Why Develop SlideRule? |
| r2 | ❌ wrong | /getting_started/Examples.html — Examples |
| r3 | ❌ wrong | /user_guide/articles/210423_h5coro.html — SlideRule Project Background |
| r4 | ❌ wrong | /user_guide/articles/250328_atl24_golden_run.html — Background |
| r5 | ❌ wrong | /user_guide/gedi.html — 1. Overview |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.2 Land Ice |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.4.1.2 MOD44W |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 66 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 4.2.1.5 Permafrost |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — Change History Log |

---

## Row 56 — labeled `docsearch` — `combine multiple ATL products in one processing pipeline`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"notes": "none of the partials really explained the concept"}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /developer_guide/why_sliderule.html — Why Develop SlideRule? |
| r2 | 🟡 partial | /developer_guide/why_sliderule.html — Why Develop SlideRule? |
| r3 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — User Lua Script |
| r4 | ❌ wrong | /user_guide/articles/250530_arbitrary_code_execution.html — User Python Script |
| r5 | 🟡 partial | /user_guide/icesat2.html — 1.4 Ancillary Data |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Input Variables |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Page 6 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 Data Workflow |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — Abstract |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |

---

## Row 57 — labeled `docsearch` — `filter only vegetation photons from ICESat-2 atl03`

Prior overall=`partial`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — ICESat-2 Module |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.2.3 ATL08 Classification |
| r3 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.2 Photon-selection Parameters |
| r5 | ❌ wrong | /user_guide/icesat2.html — A.2 Elevations - atl06p |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.5 Refining the Photon Classifications |
| r2 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.2.1 Signal Photon De-trending |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 3 |
| r4 | 🟡 partial | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 2.3.1 Noise Filtering |
| r5 | ❌ wrong | /sites/default/files/documents/user-guide/atl08-v006-userguide.pdf — 4.2 Date Last Updated |

---

## Row 58 — labeled `docsearch` — `save sliderule output to a parquet file for later analysis`

Prior overall=`correct`  ·  routing=`keep`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /user_guide/articles/230224_geoparquet.html — Overview |
| r2 | 🟡 partial | /user_guide/arrow_output.html — S3 Staging |
| r3 | ✅ correct | /user_guide/arrow_output.html — Parameters |
| r4 | 🟡 partial | /user_guide/arrow_output.html — S3 Output to User Bucket |
| r5 | 🟡 partial | /user_guide/arrow_output.html — Parameters |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |
| r4 | ❌ wrong | /sites/default/files/documents/user-guide/atl24-v001-userguide.pdf — 1.2.3 Naming Convention |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |

---

## Row 59 — labeled `docsearch` — `phoreal added sliderule release notes version`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/articles/251208_v5_server_release.html — 2025-12-08: Public Cluster Release v5 |
| r2 | ❌ wrong | /user_guide/articles/251208_v5_server_release.html — Full release notes |
| r3 | ❌ wrong | /user_guide/articles/260120_private_clusters.html — 2026-01-20: Private Clusters |
| r4 | ❌ wrong | /developer_guide/release_notes/web-release-v04-00-03.html — Summary |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v04-09-00.html — Release v4.9.x |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — ATL24 ATBD Sections |

---

## Row 60 — labeled `docsearch` — `sliderule api deprecation breaking removed old function`

Prior overall=`wrong`  ·  routing=`keep`

Prior human_truth: `{"urls": ["https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-00-00.html"]}`

**docsearch (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/versioning.html — Note on Reproducibility |
| r2 | ❌ wrong | /api_reference/gedi.html — init |
| r3 | 🟡 partial | /developer_guide/release_notes/release-v01-04-00.html — Required Updates |
| r4 | ❌ wrong | /api_reference/sliderule.html — init |
| r5 | ❌ wrong | /user_guide/articles/250910_plugins.html — Shared Object |

**nsidc** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Data Dissemination |
| r2 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Development Environment |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — Deployment Environment |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf — SlideRule Overview |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 155 |

---

## Row 61 — labeled `nsidc` — `ICESat-2 ground track beam naming GT1L GT1R GT2L convention`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — A.2 Elevations - atl06p |
| r2 | 🟡 partial | /background/ICESat-2.html — Mission |
| r3 | 🟡 partial | /user_guide/icesat2.html — 1. ATL03 - atl03x |
| r4 | 🟡 partial | /user_guide/icesat2.html — 1.5 ATL06-SR Algorithm |
| r5 | 🟡 partial | /user_guide/icesat2.html — 3. ATL08 - atl08x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.3 Appendix D - Lexicon for ATBD Writing |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 10.3 Appendix D - Lexicon for ATBD Writing |
| r3 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 62 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.4.1.3 Group: /gtx/geophys_corr |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 98 |

---

## Row 62 — labeled `nsidc` — `reference ground track RGT cycle number ICESat-2 granule`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/icesat2.html — A.2 Elevations - atl06p |
| r2 | 🟡 partial | /user_guide/icesat2.html — 3. ATL08 - atl08x |
| r3 | 🟡 partial | /user_guide/icesat2.html — ICESat-2 Module |
| r4 | 🟡 partial | /user_guide/icesat2.html — 2. ATL06 - atl06x |
| r5 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — Appendix A. Parameter Components |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 1.2.2 ATLAS/ICESat-2 Description |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 71 |
| r3 | ✅ correct | /sites/default/files/documents/user-guide/atl13-v007-userguide.pdf — Appendix A – ICEsat-2/atlas description |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.5 ATL03 Granules |
| r5 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 97 |

---

## Row 64 — labeled `nsidc` — `ICESat-2 orbit altitude inclination mission specifications`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /background/ICESat-2.html — Mission |
| r2 | ❌ wrong | /user_guide/icesat2.html — ICESat-2 Module |
| r3 | ❌ wrong | /user_guide/icesat2.html — 1.5 ATL06-SR Algorithm |
| r4 | ❌ wrong | /developer_guide/release_notes/release-v02-00-00.html — Release v2.0.x |
| r5 | ❌ wrong | /developer_guide/release_notes/release-v02-01-00.html — Release v2.1.x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.3 ICESat-2 ATLAS Instrument |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 26 |
| r3 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.3.1 Range bias determination |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 71 |
| r5 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 2 |

---

## Row 65 — labeled `nsidc` — `GEDI laser channels power modes beam configuration`

Prior overall=`wrong`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /user_guide/gedi.html — 3. Returned data |
| r2 | ❌ wrong | /background/ICESat-2.html — Mission |
| r3 | ❌ wrong | /developer_guide/release_notes/release-v03-02-00.html — Development Updates |
| r4 | 🟡 partial | /user_guide/gedi.html — 2. Parameters |
| r5 | ❌ wrong | /user_guide/icesat2.html — 1.1 Photon-input Parameters |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf — Page 19 |
| r2 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 11 |
| r3 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 16 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf — 1.3 ICESat-2 ATLAS Instrument |
| r5 | ❌ wrong | /GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html — Page 15 |

---

## Row 66 — labeled `nsidc` — `ATL03 pointing biases beam geolocation error model`

Prior overall=`partial`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r2 | ❌ wrong | /api_reference/icesat2.html — atl06p |
| r3 | ❌ wrong | /api_reference/icesat2.html — atl03sp |
| r4 | ❌ wrong | /background/ICESat-2.html — References |
| r5 | ❌ wrong | /api_reference/icesat2.html — atl03vp |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 2.2 Data Flow Within ATL03 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.3.2 Range bias uncertainty |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf — 3.3.1 Range bias determination |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 62 |
| r5 | 🟡 partial | /sites/default/files/documents/user-guide/atl03-v006-userguide.pdf — 2.3.6 Surface Masks |

---

## Row 67 — labeled `nsidc` — `ATL06 land ice along-track segment elevation`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 3. ATL08 - atl08x |
| r2 | 🟡 partial | /user_guide/icesat2.html — A.2 Elevations - atl06p |
| r3 | ❌ wrong | /background/ICESat-2.html — ATL03 - Global Geolocated Photon Data |
| r4 | 🟡 partial | /user_guide/icesat2.html — ICESat-2 Module |
| r5 | ❌ wrong | /user_guide/icesat2.html — 2. ATL06 - atl06x |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 19 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 27 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 25 |
| r4 | ❌ wrong | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 1 |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf — Page 23 |

---

## Row 68 — labeled `nsidc` — `ATL08 100-meter segment terrain canopy height`

Prior overall=`correct`  ·  routing=`keep`

**docsearch** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ❌ wrong | /user_guide/icesat2.html — 3. ATL08 - atl08x |
| r2 | 🟡 partial | /user_guide/icesat2.html — 1.6 PhoREAL Algorithm |
| r3 | 🟡 partial | /user_guide/icesat2.html — A.3 Vegetation Metrics (PhoREAL) - atl08p |
| r4 | ❌ wrong | /developer_guide/design/SlideRuleWebClient.html — Appendix A. Parameter Components |
| r5 | 🟡 partial | /user_guide/icesat2.html — 3.1 Quality Filter Parameters |

**nsidc (labeled)** — prior verdict vs current chunk:

| rank | prior verdict | current chunk (path — section) |
| --- | --- | --- |
| r1 | ✅ correct | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 44 |
| r2 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 94 |
| r3 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 20 |
| r4 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 49 |
| r5 | 🟡 partial | /sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf — Page 48 |

---
