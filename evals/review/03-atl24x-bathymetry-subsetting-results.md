# Row 3 results: docsearch / identifier

> Auto-generated. Open this file alongside `03-atl24x-bathymetry-subsetting-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl24x bathymetry subsetting`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl24x`
  - `5. atl24`
- **expected_pages:** (none)
- **notes:** atl24x is documented in user_guide/icesat2.html section 5 (assets/atl24_access tutorial dropped after testsliderule.org rebaseline)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.691

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl24x', 'bathymetry', 'subsetting']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r2 — score 0.616

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['bathymetry']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r3 — score 0.555

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Statistics
- **category:** `developer_guide`
- **matched_tokens:** ['bathymetry']

**Full text:**

```
452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea surface 0.73% of classified photons were bathymetry
```

#### r4 — score 0.494

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** 2025-03-28: ATL24 Processing Run
- **category:** `developer_guide`
- **matched_tokens:** ['bathymetry']

**Full text:**

```
Note SlideRule processed ICESat-2 cycles 1 through 25 to produce the first release of the Near-Shore Coastal Bathymetry Product (ATL24) for ICESat-2.
```

#### r5 — score 0.578

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['bathymetry']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.534

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 13
- **matched_tokens:** ['bathymetry']

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

#### r2 — score 0.634

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Introduction
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 10
- **matched_tokens:** ['bathymetry']

**Full text:**

```
This new product, ATL24, will provide
automated bathymetry extraction, sea surface/wave parameters, and water column statistics
in all regions that provide adequate conditions for probable measurements. In contrast to
other ATLAS data products that were designed pre-launch, a great benefit to the ATL24
development effort is the opportunity to learn from and leverage the great wealth of ICESat-2
bathymetry studies that have been published over the past six years.
3
```

#### r3 — score 0.598

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['bathymetry']

**Full text:**

```
3 ATL24 Overview
3.1 ATL24 Data Workflow
Similar to other ICESat-2 Level 3a products, the input to the ATL24 pipeline is Level 2a,
Global geolocated point cloud data; ATL03 (T. A. Neumann et al. 2019b). ATL03 provides
every detected photon (signal and noise), with the calculated geolocation (geodetic latitude
and longitude) and associated parameters (operational) for each of ATLAS’s six beams. The
ATL03 product also provides signal confidence flags and estimated uncertainties at the photon
level. Gridded surface masks for land ice, sea ice, land, ocean and inland water products are
used within the L3b processing workflows to reduce the volume of data processed and guide
the production of these surface-specific, higher-level ICESat-2 data products. The ATL24
workflow requires a similar search approach to limit data processing to coastal and nearshore
environments that present a reasonable opportunity for capturing bathymetry. As such, a
gridded bathymetry mask based on possible retrievability was created to guide the processing
extents and is discussed in detail in section subsection 6.4. Figure 1 provides the overarching processing pipeline for ATL24, including the search
mask step to identify relevant ATL03 granules. The ATL24 algorithm’s main goal is to
provide a solution for robust, global bathymetric and sea surface signal extraction and
classification.
```

#### r4 — score 0.598

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 16
- **matched_tokens:** ['bathymetry']

**Full text:**

```
Roughly following the procedures used in airborne bathymetric lidar,
we start with return photon coordinates that assume topograpy, rather than bathymetry, and
then apply refraction correction. The initial coordinates are from ATL03: specifically, the
lat_ph, lon_ph, and h_ph in the /gtx/heights group.
4.2 ATL24 Input Variables
Table 2 captures each stage of the processing phase in the production of the ATL24 granule
and explains the significance of each step. Table 2 also lists the required inputs for that stage
with brief explanation. ATL03, the primary input, provides the heights above the WGS84
ellipsoid (ITRF2014 reference frame, through Release 06 of ATL03, after which ITRF2020
9
```

#### r5 — score 0.503

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.5.6 Estimation of short segment bathymetry other subsurface anomalies
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 68
- **matched_tokens:** ['bathymetry']

**Full text:**

```
The beginning point to which the IRF is pinned is defined as
“3xσh_obs + 1.0m above the mean of the best fit Gaussian fit to the observed water surface
returns.
4.5.5.5 Deconvolution
The “deconvolution“ is solved through constrained “convolution” of the IRF histogram with the
unit (or true) water profile histogram. The solution is achieved by iterating through the four
parameters of the unit water profile (mean, σh, β and α) until the mean, standard deviation and
peak of integrated histogram best matches the observed (ATLAS) histogram, as described in
sections 4.5.1 through 4.5.4.
4.5.6 Estimation of short segment bathymetry other subsurface anomalies
The short segment bathymetry originally published in ATL13 Release 002 has been significantly
upgraded for ATL13 Rel 7. The algorithm provides an estimate of the along track bottom
topography and water depth over the telemetry range, assuming favorable water clarity and
relatively cloudless skies. The overall approach relies on analysis of ATL03 signal photons,
starting with the above ATL13 analysis of surface water height combined with an empirical
analysis of the density variation in subsurface photons (E.g. Nagle and Wright, 2016 among
many others).
45
Release 007, January 31, 2025
```

---

