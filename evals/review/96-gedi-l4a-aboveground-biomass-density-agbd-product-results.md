# Row 96 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `96-gedi-l4a-aboveground-biomass-density-agbd-product-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI L4A aboveground biomass density AGBD product`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** GEDI L4A AGBD product; must not return ICESat-2 docs

---

## 📚 docsearch results (top 5)

#### r1 — score 0.441

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04a
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

#### r2 — score 0.426

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['density', 'gedi', 'l4a', 'product']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r3 — score 0.418

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-01-00.html
- **title:** Release v3.1.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks: https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples PhoREAL functionality officially supported User Guilde: https://slideruleearth.io/user_guide/ICESat-2.html#photon-extent-parameters API Reference: https://slideruleearth.io/api_reference/icesat2.html#atl08p Example Notebooks: https://slideruleearth.io/getting_started/Examples.html (look for PhoREAL Example )
```

#### r4 — score 0.361

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.4 L4A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['agbd', 'gedi', 'l4a']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation" : elevation in meters of the surface of the earth "agbd" : above ground biodensity "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

#### r5 — score 0.344

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-00-00.html
- **title:** Release v3.0.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
PhoREAL/atl08 endpoint still a feature-preview GEDI L4A subsetting endpoint still a feature-preview
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.655

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 3
- **matched_tokens:** ['aboveground', 'biomass', 'density', 'gedi', 'l4a', 'product']

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

#### r2 — score 0.613

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['aboveground', 'biomass', 'density', 'gedi', 'l4a']

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

#### r3 — score 0.570

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 2
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['aboveground', 'agbd', 'biomass', 'density', 'gedi', 'product']

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

#### r4 — score 0.647

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 9
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 9
- **matched_tokens:** ['aboveground', 'agbd', 'biomass', 'gedi', 'product']

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

#### r5 — score 0.548

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 2
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['aboveground', 'agbd', 'biomass', 'density', 'gedi', 'product']

**Full text:**

```
Abstract
The Global Ecosystem Dynamics Investigation (GEDI) lidar is a multibeam laser altimeter on
the International Space Station. GEDI is the first spaceborne instrument designed specifically to
measure vegetation structure and estimate aboveground carbon stocks in temperate and tropical
forests and woodlands. This document describes the algorithm theoretical basis underpinning the
development of the GEDI Level-4A (GEDI04_A) footprint aboveground biomass density
(AGBD) data product. The GEDI04_A data product contains footprint-level AGBD (Mg · ha-1)
for individual GEDI footprints and the associated prediction uncertainty. GEDI04_A is a
standalone data product, and GEDI04_A models are an input to the GEDI Level-4B
(GEDI04_B) gridded AGBD data product. The GEDI04_A algorithm uses GEDI Level-2A
(GEDI02_A) relative height metrics as input to parametric linear models to predict AGBD. GEDI04_A models were developed from a quality-filtered data set of GEDI footprint sized field
plots paired with simulated GEDI waveforms across 21 countries and all continents within the
GEDI domain (51.6 degrees N – S latitude). The models are stratified by combinations of world
region and plant functional type (PFT). We describe the development of the GEDI04_A models
and algorithm implementation for on-orbit prediction, including geographic transferability,
elimination of GEDI02_A observations that do not meet requirements of the GEDI04_A
algorithm, and quality flagging of GEDI04_A predictions.
```

---

