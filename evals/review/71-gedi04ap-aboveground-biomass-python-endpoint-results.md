# Row 71 results: docsearch / identifier

> Auto-generated. Open this file alongside `71-gedi04ap-aboveground-biomass-python-endpoint-review.md` —
> verdicts go there, this side is read-only.

**Query:** `gedi04ap aboveground biomass python endpoint`
**Panel signature:** `cd8dfa850582`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/gedi.html
  - https://docs.slideruleearth.io/user_guide/gedi.html
- **expected_sections:**
  - `gedi04ap`
  - `gedi04a`
- **expected_pages:** (none)
- **notes:** gedi04ap identifier

---

## 📚 docsearch results (top 5)

#### r1 — score 0.510

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04ap
- **category:** `api_reference`
- **matched_tokens:** ['gedi04ap']

**Full text:**

```
sliderule.gedi. gedi04ap ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs subsetting in parallel on GEDI data and returns elevation footprints. This function expects that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. If resources is specified then any polygon or resource filtering options supplied in parm are ignored.
```

#### r2 — score 0.435

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-09-00.html
- **title:** Release v4.9.x
- **section:** Changes
- **category:** `release_notes`
- **matched_tokens:** ['gedi04ap', 'python']

**Full text:**

```
v4.9.2 - Optimized raster sampling code v4.9.2 - Fixed Python client to support output format specified as geoparquet with open_on_complete v4.9.2 - Changed default atl03 confidence flags to low, medium, and high v4.9.2 - Added separate geophysical corrections ancillary fields list in support of future ATL03 dataframe class v4.9.0 - Added ancillary field support to GEDI ( gedi01bp , gedi02ap , gedi04ap ) Bathy Version #15 - Separated out processing flags into their own variables in the h5 file: sensor depth exceeded, invalid kd, invalid wind speed, night flight Bathy Version #15 - Added low confidence flag to h5 Bathy Version #15 - Added ensemble confidence to h5 Bathy Version #15 - ISO.XML polygon is now taken directly from ATL03 Bathy Version #14 - Updated ensemble
```

#### r3 — score 0.437

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** New Functionality
- **category:** `release_notes`
- **matched_tokens:** ['endpoint', 'python']

**Full text:**

```
Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and GEDI01B ( gedi01bx ) v5.0.2 - ATL24 uses release 002 by default, which uses the internal Asset Metadata Service (AMS). v5.0.2 - #549 - h5p now supports slices. v5.0.2 - earthdata.py is no longer a standalone implementation of an interface to CMR and TNM, but instead makes a request to the SlideRule cluster to execute the server-side implementations in earth_data_query.lua . This consolidates the interface to these services in one place, and also provides a consistent interface between the web and Python clients. v5.0.2 - Added the 3dep1m asset which accesses the same USGS 3DEP data product but uses the internal AMS service for STAC queries. This is an attempt to alleviate issues with inconsistent availability and functionality in The National Map (TNM) service which made using 3DEP difficult.
```

#### r4 — score 0.393

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.0: APIs
- **category:** `developer_guide`
- **matched_tokens:** ['gedi04ap']

**Full text:**

```
The following APIs shall be supported: atl03sp atl06sp atl06p atl08sp - future atl08p atl024sp - future atl024p - future gedi04ap gedi02ap gedi01bp samples subsets
```

#### r5 — score 0.481

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-13-00.html
- **title:** Release v4.13.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['endpoint']

**Full text:**

```
v4.13.1 - #266 - GEDI rasters support vertical shifts v4.13.1 - #487 - atl24x queries CMR for ATL24 dataset v4.13.1 - #463 - YAPC version 3 fixed v4.13.0 - 8814ffc - CMR max resources reached returns error instead of silently truncating (matches client behavior) v4.13.0 - 97a55ae - fixed access to BlueTopo v4.13.0 - 5a04947 - fixed access to Meta Global Canopy v4.13.0 - db38b4c - s3 retries always rebuild header v4.13.0 - db38b4c - the endpoint being called is now provided in the metadata of the return dataframe v4.13.0 - 5b95dc4 - more robust error handling in metric gathering in orchestrator v4.13.0 - d8a813a - fixed GEDI raster sampling code to apply vertical offset when necessary
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.605

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 1
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['aboveground', 'biomass']

**Full text:**

```
Title:
Algorithm theoretical basis document for GEDI footprint aboveground biomass density
Authors and affiliations:
James R. Kellner1,2, John Armston3, Laura Duncanson4
1. Institute at Brown for Environment and Society, Brown University, Providence RI,
ORCID ID: 0000-0002-9861-4857
2. Department of Ecology, Evolution and Organismal Biology, Brown University,
Providence RI
3. Department of Geographical Sciences, University of Maryland College Park, College
Park MD, ORCID ID: 0000-0003-1232-3424
4. Department of Geographical Sciences, University of Maryland College Park, College
Park MD, ORCID ID: 0000-0003-4031-3493
This paper is a non-peer reviewed preprint submitted to EarthArXiv. This paper is currently
being peer reviewed by Earth and Space Science. Author contributions:
JRK, LD and JA developed the algorithm and approach to calibration and validation. JRK wrote
the original draft and JRK, JA and LD reviewed and edited the document. JA, LD and JRK
oversaw field data curation, waveform simulation and generation of the GEDI FSBD. JRK, LD and
JA developed the code to fit candidate GEDI04_A models and apply them to on-orbit
observations. JRK, LD, and JA designed and conducted the analysis and selected the models. Corresponding author:
James R. Kellner, james_r_kellner@brown.edu
Key points:
1. GEDI aboveground biomass density is from models trained on a comprehensive
database of field measurements and simulated GEDI waveforms
2.
```

#### r2 — score 0.490

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 2
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['aboveground', 'biomass']

**Full text:**

```
biomass density (AGBD) data product. The GEDI04_A data product contains estimates of AGBD
for individual GEDI footprints and associated prediction intervals. The algorithm uses GEDI02_A
relative height (RH) metrics and 13 linear models to predict AGBD in 32 combinations of plant
functional type (PFT) and world region within the observation limits of the ISS. GEDI04_A
models for the release 1 and release 2 data products were developed using 8,587 quality-
filtered simulated GEDI waveforms associated with field estimates of AGBD in 21 countries. Although this is the most geographically comprehensive data available for the development of
AGBD models using lidar remote sensing, important regions are underrepresented, including
the forests of continental Asia, deciduous broadleaf forests and savannas of the dry tropics, and
evergreen broadleaf forests north of Australia. We describe the scientific and mathematical
assumptions required to develop globally representative estimates of AGBD using GEDI lidar,
including generalization beyond training data, and exclusion of GEDI02_A observations that do
not meet requirements of the GEDI04_A algorithm. The footprint-level predictions generated
by this process provide globally comprehensive estimates of AGBD. These footprint-level
predictions are a prerequisite for the GEDI GEDI04_B gridded AGBD data product. Plain language summary / significance:
The amount of carbon stored in aboveground vegetation is uncertain.
```

#### r3 — score 0.617

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 3
- **matched_tokens:** ['aboveground', 'biomass']

**Full text:**

```
Foreword
This document is the Algorithm Theoretical Basis Document for the GEDI Level-4A (L4A)
Footprint Level Aboveground Biomass Density product. The GEDI Science Team assumes
responsibility for this document and updates it, as required, as algorithms are refined. Reviews of
this document are performed when appropriate and as needed updates to this document are made.
This document is a GEDI ATBD controlled document. Changes to this document require prior
approval of the project. Proposed changes shall be noted in the change log, as well as
incrementing the document version number.
Questions or comments concerning this document should be addressed to:
James R. Kellner
Department of Ecology, Evolution and Organismal Biology
Institute at Brown for Environment and Society
Brown University, Providence RI 02912
james_r_kellner@brown.edu
+1 (401) 863 5768
John Armston
2181 Lefrak Hall, Department of Geographical Sciences
University of Maryland, College Park MD 20742
armston@umd.edu
+1 (301) 405 8444
Laura Duncanson
2181 Lefrak Hall, Department of Geographical Sciences
University of Maryland, College Park MD 20742
lduncans@umd.edu
+1 (301) 405 3076
Ralph Dubayah
2181 Lefrak Hall, Department of Geographical Sciences
University of Maryland, College Park MD 20742
dubayah@umd.edu
+1 (301) 405 4069
2
```

#### r4 — score 0.564

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['aboveground', 'biomass']

**Full text:**

```
Algorithm Theoretical Basis Document (ATBD)
for
GEDI Level-4A (L4A) Footprint Level Aboveground
Biomass Density
James R. Kellner1,2, John Armston3, Laura Duncanson3
1 Institute at Brown for Environment and Society, Brown University, Providence RI
2 Department of Ecology, Evolution and Organismal Biology, Brown University,
Providence RI
3 Department of Geographical Sciences, University of Maryland, College Park MD
Version 1.0
Release date: August 11th, 2021
University of Maryland, College Park MD
Authors: Principal Investigator:
________________________________ ________________________________
________________________________
________________________________
```

#### r5 — score 0.539

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 9
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 9
- **matched_tokens:** ['aboveground', 'biomass']

**Full text:**

```
This uncertainty propagates
through GEDI level-2A (GEDI02_A) RH metrics that are used to predict AGBD (Dubayah et al.,
2020b). The first release of the GEDI level-4A (GEDI04_A) data product is based on Version 1
of GEDI02_A (Dubayah et al., 2020b), and uses one of six algorithm setting groups to interpret
the received waveform and identify the elevation of the lowest mode (Hofton and Blair, 2020). The Version 1 of GEDI04_A uses linear statistical models selected from an ensemble of
candidates that predict AGBD as a function of one or more RH metrics. GEDI04_A models are a
required input to the 1 km GEDI level-4B (GEDI04_B) AGBD data product (Patterson et al.,
2019).
2. HISTORICAL PERSPECTIVE
Estimating AGBD using remote sensing requires aboveground biomass, 𝑀!, for a sample
of trees that has been computed using an allometric model in a fixed area, such as a field-
inventory plot or lidar footprint. Summing the 𝑀! over all individuals in the plot or footprint and
expressing it per unit ground area produces an estimate of AGBD. Coincident remote sensing
data are used to develop an empirical relationship between AGBD and a remotely sensed
measurement. This relationship can then be used to predict AGBD using remotely sensed data
(Drake et al., 2002; Lefsky et al., 2002).
```

---

