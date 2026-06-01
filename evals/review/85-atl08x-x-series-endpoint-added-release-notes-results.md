# Row 85 results: docsearch / version_history

> Auto-generated. Open this file alongside `85-atl08x-x-series-endpoint-added-release-notes-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl08x x-series endpoint added release notes`
**Panel signature:** `0bcbd32a0e9f`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-03-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl08x appears in v05-00-00 / v05-03-00

---

## 📚 docsearch results (top 5)

#### r1 — score 0.472

- **url:** https://docs.slideruleearth.io/user_guide/articles/260528_web_client_endpoint_scoped_params.html
- **title:** 2026-05-28: Web Client v4.5.0 - Endpoint-Scoped Advanced Options
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['atl08x', 'endpoint', 'series']

**Full text:**

```
The Advanced Options panel now adapts to the endpoint youâve selected. The X-series endpoints ( atl06x , atl08x , atl24x , atl13x ) read pre-computed segments directly from HDF5 products, so the server discards photon-processing parameters for these endpoints. The web client now mirrors that behavior in the UI, eliminating misleading controls and preventing stale store state from leaking into the request.
```

#### r2 — score 0.390

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** New Functionality
- **category:** `release_notes`
- **matched_tokens:** ['added', 'atl08x', 'endpoint', 'release', 'series']

**Full text:**

```
Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and GEDI01B ( gedi01bx ) v5.0.2 - ATL24 uses release 002 by default, which uses the internal Asset Metadata Service (AMS). v5.0.2 - #549 - h5p now supports slices. v5.0.2 - earthdata.py is no longer a standalone implementation of an interface to CMR and TNM, but instead makes a request to the SlideRule cluster to execute the server-side implementations in earth_data_query.lua . This consolidates the interface to these services in one place, and also provides a consistent interface between the web and Python clients. v5.0.2 - Added the 3dep1m asset which accesses the same USGS 3DEP data product but uses the internal AMS service for STAC queries. This is an attempt to alleviate issues with inconsistent availability and functionality in The National Map (TNM) service which made using 3DEP difficult.
```

#### r3 — score 0.422

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['atl08x', 'endpoint']

**Full text:**

```
The SlideRule atl08x endpoint provides a service for ATL08 subsetting and custom processing. This endpoint queries ATL08 input granules for segment vegetation statistics and locations based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r4 — score 0.403

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl08x', 'endpoint']

**Full text:**

```
Ancillary data returned from the atl08x endpoint (as well as atl08 and atl08p endpoints) come from the {beam} group of the ATL08 granules. atl08_fields : fields in the beam group of the ATL08 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "asr" ], } gdf = sliderule . run ( "atl08x" , parms )
```

#### r5 — score 0.425

- **url:** https://docs.slideruleearth.io/user_guide/articles/251208_v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `user_guide`
- **matched_tokens:** ['notes', 'release']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.405

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['endpoint']

**Full text:**

```
The native runtime environment will be used for the atl24s and atl24p endpoints, but will
not be used exclusively for the atl24g endpoint, as the processing needed for that endpoint
43
```

#### r2 — score 0.390

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 13
- **matched_tokens:** ['added', 'release']

**Full text:**

```
June 22 Added updates from ATL13 rel006 final version ATBD.
2023
June 28 Added sseg_length and sseg_dist_from_eq to output.
2023
Reversed 0/1 on/off assignments used for apply_mirror September
and limit_hist_depth arrays to match convention used for 15 2023
previous parameters. Removed instrument effects from all analysis based on September
photon quality flag. Refined long segment bathymetry 29 2023
results for each member short segment based on its
individual photon distribution.
xiii
Release 007, January 31, 2025
```

#### r3 — score 0.396

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 5
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 5
- **matched_tokens:** ['added']

**Full text:**

```
2.2, Sec 4.18 (2))
2018 December Added ATL09 layer_flag to ATL08 output (Table 2.5, Table
4.2)
2019 February Adjusted cloud filtering to be based on ATL09 backscatter
analysis rather than cloud flags (Sec 4.1)
2019 March 5 Updated ATL09-based product descriptions reported on
ATL08 product (Secs 2.5.13, 2.5.14, 2.5.15, 2.5.16)
2019 March 5 Updated cloud-based low signal filter methodology, and
moved to first step of ATL08 processing (Sec 4.1)
5
```

#### r4 — score 0.242

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Table of Contents
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 13
- **matched_tokens:** ['notes', 'release']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
8.0 The Quality Assessment Group ....................................................................................... 138
9.0 METADATA ............................................................................................................................. 143
10.0 APPENDICIES ......................................................................................................................... 145
10.1 Appendix A – ATL03 Output Parameter Table. ..................................................... 145
10.2 ATL03 Users Notes ................................................................................................... 179
10.2.1 Tracing between higher-level products and the photon cloud ........................... 179
10.2.2 Apparent Return Pulse Width and Strength ....................................................... 179
10.2.3 Use of the TEP as the system impulse-response function ................................ 180
10.3 Appendix D - Lexicon for ATBD Writing ................................................................ 183
11.0 REFERENCES .......................................................................................................................... 190
Glossary/Acronyms .......................................................................................................................... 192
xiii Release Date: Fall 2022
```

#### r5 — score 0.444

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 6.2 List of Geophysical Corrections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 116
- **matched_tokens:** ['release']

**Full text:**

```
Therefore, ATL03
provides the detail necessary to enable these users to remove or apply corrections as they see fit,
and apply alternative corrections, as needed, in areas of specific interest. The ATL03 data
100 Release Date: Fall 2022
```

---

