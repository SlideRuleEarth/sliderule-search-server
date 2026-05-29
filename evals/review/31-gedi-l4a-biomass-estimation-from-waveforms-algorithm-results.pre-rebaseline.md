# Row 31 results: nsidc / algorithm

> Auto-generated. Open this file alongside `31-gedi-l4a-biomass-estimation-from-waveforms-algorithm-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI L4A biomass estimation from waveforms algorithm`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 5–30
- **notes:** GEDI L4A ATBD

---

## 📚 docsearch results (top 5)

#### r1 — score 0.484

- **url:** https://docs.testsliderule.org/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['gedi', 'l4a', 'waveforms']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r2 — score 0.410

- **url:** https://docs.testsliderule.org/api_reference/gedi.html
- **title:** gedi
- **section:** gedi01b
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'waveforms']

**Full text:**

```
sliderule.gedi. gedi01b ( parm , resource ) [source] Performs GEDI L1B subsetting of elevation waveforms Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

#### r3 — score 0.433

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v03-01-00.html
- **title:** Release v3.1.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks: https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples PhoREAL functionality officially supported User Guilde: https://slideruleearth.io/user_guide/ICESat-2.html#photon-extent-parameters API Reference: https://slideruleearth.io/api_reference/icesat2.html#atl08p Example Notebooks: https://slideruleearth.io/getting_started/Examples.html (look for PhoREAL Example )
```

#### r4 — score 0.402

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v03-02-00.html
- **title:** Release v3.2.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['gedi', 'waveforms']

**Full text:**

```
GEDI L01B waveforms fixed (they were being corrupted later in the GeoDataFrame)
```

#### r5 — score 0.400

- **url:** https://docs.testsliderule.org/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04a
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.596

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 3
- **matched_tokens:** ['algorithm', 'biomass', 'gedi', 'l4a']

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

#### r2 — score 0.570

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 17
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 17
- **matched_tokens:** ['biomass', 'estimation', 'gedi', 'waveforms']

**Full text:**

```
If
successful, this could facilitate the use of machine learning in a way that is compliant with
GEDI04_B algorithms.
9. References
Baskerville, G. L. (1972). Use of Logarithmic Regression in the Estimation of Plant Biomass. Canadian
Journal of Forest Research. https://doi.org/10.1139/x72-009
Beck, J., Wirt, B., Luthcke, S., Hofton, M., & Armston, J. (2021). Global Ecosystem Dynamics Investigation
(GEDI) level 02 user guide version 2.0. U.S. Geological Survey, Earth Resources Observation and
Science Center. Beets, P., N., Kimberley, M., O., Paul, T., S. H., & Garrett, L., G. (2011). Planted Forest Carbon Monitoring
System - forest carbon model validation study for Pinus radiata. New Zealand Journal of Forestry
Science, (41), 177–189. Blair, J. B., & Hofton, M. A. (1999). Modeling laser altimeter return waveforms over complex vegetation
using high-resolution elevation data. Geophysical Research Letters, 26(16), 2509–2512.
https://doi.org/10.1029/1999GL010484
17
```

#### r3 — score 0.582

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 1
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['algorithm', 'biomass', 'from', 'gedi', 'waveforms']

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

#### r4 — score 0.563

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['algorithm', 'biomass', 'gedi', 'l4a']

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

#### r5 — score 0.534

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 2
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['algorithm', 'biomass', 'from', 'gedi', 'waveforms']

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

