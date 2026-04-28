# Row 16 results: docsearch / example

> Auto-generated. Open this file alongside `16-example-atl24-subsetting-and-filtering-bathymetry-review.md` —
> verdicts go there, this side is read-only.

**Query:** `example atl24 subsetting and filtering bathymetry`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/atl24_access.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl24 access tutorial

---

## 📚 docsearch results (top 5)

#### r1 — score 0.625

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'filtering']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r2 — score 0.686

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'subsetting']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r3 — score 0.555

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'filtering']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

#### r4 — score 0.745

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.607

- **url:** https://docs.slideruleearth.io/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.624

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 17
- **matched_tokens:** ['atl24', 'bathymetry', 'filtering']

**Full text:**

```
Table 2: ATL24 input variables and processing details within each stage of the product production
Stage Processing Input Products
ATL24.g - accept an incoming Client Request ATL03 granule name HTTP request
Global Bathymetry Mask - a
shapefile capturing all areas where ATL03/09 Granule Reader there is bathymetry detectable by - subset granules to bathymetry ICESat-2 Input Data and mask
Data Configura- ATL03 Granule - ICESat- tion Photon Filtering - option- 2 standard data product h5 file ally filter photons based on
certain fields (e.g. quality_ph) ATL09 Granule - ICESat-
2 standard data product h5 file
CoastNet
ICESat-2 inputs Photon Classi- Quantile Trees fiers: Sea surface Trained ML models
OpenOceans++
CoastNet
Quantile Trees ICESat-2 inputs
C-SHELPH Trained ML models Photon Classi-
fiers: Seafloor OpenOceans++ Sea Surface - some classifi-
cation algorithms require an
BathyPathFinder initial estimate of sea surface
Median Filter
10
```

#### r2 — score 0.561

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.8 Ensemble Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 9
- **matched_tokens:** ['atl24', 'bathymetry', 'filtering']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
the PointNet++ algorithm is not being used in the ensemble, but it may be activated at a future
date.
2.3.1.5 Median Filter Classification
Median Filter is a simple empirical method for extracting bathymetry profiles from ICESat-2 data. For ATL24, all ATL03 photon ellipsoid heights are converted to orthometric heights (EGM08), and
all photons more than 1.5 m below the sea surface median are retained. The method calculates
median elevations for 50-photon windows and a moving standard deviation of elevations for 30-
photon windows. Photons remaining after filtering are separated into 0.001º latitude segments. Segments with more than 14 photons are considered bathymetry.
2.3.1.6 C-SHELPh Classification
The Classification of Sub-aquatic Height Extracted Photons (C-SHELPh) algorithm is an open-
source tool for producing bathymetric maps. The algorithm detects the dense clustering of photons
indicative of surface returns. A gridding convention provides surface heights and along-track
latitudes, where 0 m is the ocean surface. The ATL24 implementation of C-SHELPh bins photons
into 0.001º along-track blocks and 0.5 m vertical blocks. The number of photons in each block is
counted, and a threshold is calculated based on the number of photons in all blocks.
```

#### r3 — score 0.574

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Bathymetric Processing Masks
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 53
- **matched_tokens:** ['atl24', 'bathymetry', 'example']

**Full text:**

```
6.4 Bathymetric Processing Masks
Gridded surface masks for land ice, sea ice, land, ocean and inland water are used within the
processing chain of ATL03 to reduce the volume of data processed and guide the production
of surface-specific higher-level ICESat-2 data products. A key step in the ATL24 workflow is applying a bathymetric search mask (Figure 12),
which determines where to search for bathymetry. ATL03 granules within the mask are
input to the algorithm to search for bathymetry, while those outside the mask are ignored in
subsequent ATL24 processing steps. Use of the mask drastically reduces computation time
by ignoring data that are on land or far too deep and/or too turbid for ATLAS bathymetric
measurement. However, there is an important tradeoff in establishing the mask: including
too much area unnecessarily increases processing time, while being too restrictive could lead
to bathymetry being missed. Our guiding philosophy in establishing the mask was to err on
the side of including too much area, to minimize the probability of missing the discovery of
new bathymetric features, such as offshore sandbars, reefs, seamounts, or other submerged
features, including those far from shore. Since discovery of such features could lead to major
scientific advances, some increase in processing time was determined to be an acceptable
tradeoff. Figure 12: Example ATL24 bathymetric search mask. The colors in the figure correspond to ATL03
granule regions.
```

#### r4 — score 0.615

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['atl24', 'bathymetry']

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

#### r5 — score 0.614

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Introduction
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 10
- **matched_tokens:** ['atl24', 'bathymetry']

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

---

