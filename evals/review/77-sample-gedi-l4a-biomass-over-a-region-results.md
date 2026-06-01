# Row 77 results: docsearch / example

> Auto-generated. Open this file alongside `77-sample-gedi-l4a-biomass-over-a-region-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sample GEDI L4A biomass over a region`
**Panel signature:** `1d2467a05a2e`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/gedi.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** GEDI usage page

---

## 📚 docsearch results (top 5)

#### r1 — score 0.603

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r2 — score 0.474

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04a
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

#### r3 — score 0.518

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-01-00.html
- **title:** Release v3.1.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks: https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples PhoREAL functionality officially supported User Guilde: https://slideruleearth.io/user_guide/ICESat-2.html#photon-extent-parameters API Reference: https://slideruleearth.io/api_reference/icesat2.html#atl08p Example Notebooks: https://slideruleearth.io/getting_started/Examples.html (look for PhoREAL Example )
```

#### r4 — score 0.467

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.3 L4B Raster
- **category:** `user_guide`
- **matched_tokens:** ['gedi', 'sample']

**Full text:**

```
The following raster datasets are available to sample: "gedil4b" : GEDI04_B_MW019MW138_02_002_05_R01000M_V2.tif For example, if you wanted to sample the GEDI L4B biodensity raster and calculate zonal statistics for every ICESat-2 PhoREAL data point, then you could add the following entry to your parameters for your PhoREAL request: parms [ "samples" ]: { "agdb" : { "asset" : "gedil4b" , "radius" : 10.0 , "zonal_stats" : True }}
```

#### r5 — score 0.385

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.4 L4A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation" : elevation in meters of the surface of the earth "agbd" : above ground biodensity "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.701

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 3
- **matched_tokens:** ['biomass', 'gedi', 'l4a']

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

#### r2 — score 0.691

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['biomass', 'gedi', 'l4a']

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

#### r3 — score 0.574

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 9
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 9
- **matched_tokens:** ['biomass', 'gedi', 'over', 'sample']

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

#### r4 — score 0.600

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 11
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 11
- **matched_tokens:** ['biomass', 'gedi', 'region']

**Full text:**

```
Figure 1. Global stratification by five combinations of error-corrected and infilled MODIS MCD12Q1 V006 PFT
(A) and world region (B) to produce GEDI04_A models. The box inset is the GEDI observation domain of 51.6
degrees N to S latitude. DBT (deciduous broadleaf trees), DNT (deciduous needleleaf trees), EBT (evergreen
broadleaf trees), ENT (evergreen needleleaf trees), GSW (grasses, shrubs and woodlands). Af (Africa), Au
(Australia and Oceania), Eu (Europe), N-Am (North America north of southern Mexico), N-As (North Asia), S-Am
(South America, Central America, southern Mexico, and the Caribbean), S-As (South Asia). GEDI04_A models were developed using a quality-filtered calibration data set that
contains simulated GEDI waveforms: the Forest Structure and Biomass Database (FSBD). This
data set is one of the most exhaustive ever compiled for remote sensing of AGBD, but important
regions are under-represented. These include the forests of continental Asia, the evergreen
broadleaf forests throughout the islands of Southeast Asia and north of Australia, and the
worldwide distribution of savannas and deciduous tropical forests (Table 1). To quantify
geographic transferability, candidate models were evaluated within sets of 5-degree grid cells
that contain simulated GEDI waveforms with coincident field data. This approach sets aside data
from one grid cell for testing, and trains the model using data within the remaining grid cells.
```

#### r5 — score 0.549

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 2
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['biomass', 'gedi', 'region']

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

---

