# Row 22 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `22-gedi-l4a-python-api-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI L4A python API parameters`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/gedi.html
- **expected_sections:**
  - `gedi04ap`
  - `gedi04a`
- **expected_pages:** (none)
- **notes:** GEDI module api reference; query uses human-facing product name not the gedi04ap identifier

---

## 📚 docsearch results (top 5)

#### r1 — score 0.564

- **url:** https://docs.testsliderule.org/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04a
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'l4a', 'parameters']

**Full text:**

```
sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

#### r2 — score 0.538

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v03-01-00.html
- **title:** Release v3.1.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['api', 'gedi', 'l4a', 'parameters', 'python']

**Full text:**

```
GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks: https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples PhoREAL functionality officially supported User Guilde: https://slideruleearth.io/user_guide/ICESat-2.html#photon-extent-parameters API Reference: https://slideruleearth.io/api_reference/icesat2.html#atl08p Example Notebooks: https://slideruleearth.io/getting_started/Examples.html (look for PhoREAL Example )
```

#### r3 — score 0.459

- **url:** https://docs.testsliderule.org/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['api', 'gedi', 'l4a']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r4 — score 0.532

- **url:** https://docs.testsliderule.org/api_reference/gedi.html
- **title:** gedi
- **section:** gedi
- **category:** `api_reference`
- **matched_tokens:** ['api', 'gedi', 'python']

**Full text:**

```
The GEDI Python API gedi.py is used to access the services provided by the gedi plugin for SlideRule. From Python, the module can be imported via: from sliderule import gedi
```

#### r5 — score 0.516

- **url:** https://docs.testsliderule.org/api_reference/gedi.html
- **title:** gedi
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['api', 'gedi', 'python']

**Full text:**

```
sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.442

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 5
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 5
- **matched_tokens:** ['gedi']

**Full text:**

```
of southern Mexico. The continent of Asia is divided into north and south regions that
approximately correspond to temperate and tropical forests (Fig. 2). GEDI04_A models are stratified by combinations of PFT derived from an infilled and
error-corrected version MODIS data product MCD12Q1 V006 (Friedl et al., 2002, 2010). These
are deciduous broadleaf trees (DBT; class 4), deciduous needleleaf trees (DNT; class 3),
evergreen broadleaf trees (EBT, class 2), evergreen needleleaf trees (ENT, class 1), and grasses,
shrubs, and woodlands (GSW, classes 5, 6, and 11; Fig. 2). In MCD12Q1 V006, class 5 is shrub,
class 6 is grass, and class 11 is barren.
3.2 Training data quality-control filters
The data being used to develop GEDI04_A models accumulate over time as new data are
assimilated and improvements are made to existing records. The unfiltered database used for
releases 1 and 2 of GEDI04_A contains 31,414 simulated GEDI waveforms. After excluding
incomplete projects and others that cannot be used, the unfiltered database contains 12,140
simulated GEDI waveforms. After applying quality-control filters, the database used to develop
releases 1 and 2 of the GEDI04_A data product contains 8,587 simulated waveforms from 21
countries (Table 1). The analysis below indicates the number of simulated waveforms that were
flagged by each quality-control filter.
```

#### r2 — score 0.459

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 14
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 14
- **matched_tokens:** ['gedi']

**Full text:**

```
Algorithm implementations
The software that generates the GEDI04_A product was implemented at the GEDI
Science Office at the Department of Geographical Sciences, University of Maryland, College
Park (UMD), in collaboration with the GEDI Science Data Processing System at the NASA
Goddard Space Flight Center (GSFC) in Greenbelt, Maryland and the Institute at Brown for
Environment and Society (IBES) at Brown University.
6. Algorithm usage constraints
14
```

#### r3 — score 0.335

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['gedi', 'l4a']

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

#### r4 — score 0.380

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 22
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 22
- **matched_tokens:** ['gedi', 'parameters']

**Full text:**

```
𝑆𝐸< = 6𝑀𝑆𝐸= + 𝐗< Cov(𝛃) 𝐗<> (9)
Here, 𝑀𝑆𝐸= is the square of the residual standard error from the linear regression applied to
prediction stratum 𝑘 containing GEDI footprint h, 𝐗< is the row vector of scaled and transformed
RH metrics for GEDI footprint h, and Cov(𝛃) is the variance-covariance matrix for the model
parameters in transformed units (i.e. natural-logarithm, square-root, or none). Prediction intervals are calculated for every predicted value of AGBD according to:
(10) 𝐴𝐺𝐵𝐷A < ± 𝑡?"5' × 𝑆𝐸< %,$5(@
The 𝑡 multiplier is the value from a 𝑡 distribution with confidence level 𝛼 and 𝑛−2 degrees of
freedom. Users can compute prediction intervals for arbitrary values of 𝛼 using the degrees of
freedom within the model_data group of the GEDI04_A product.
4.4. Mathematical assumptions
Fitting linear models to transformed AGBD requires the assumption that transformations
linearize the relationship between AGBD and RH metrics and reduce heteroskedasticity. Both of
these assumptions underpin the methods used to propagate model parameter uncertainty in
GEDI04_A models to the 1 km GEDI04_B AGBD data product (Ståhl et al., 2011). We also
assume that a single bias-correction coefficient produces an unbiased estimate of AGBD after
back-transformation across the range of AGBD. Flewelling and Pienaar (1981) demonstrated that
this assumption can be violated at large values of predicted AGBD.
4.5.
```

#### r5 — score 0.376

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 17
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 17
- **matched_tokens:** ['gedi', 'parameters']

**Full text:**

```
The hybrid-inference framework selected for GEDI04_B requires footprint models that
produce a covariance matrix that describes relationships among model parameters. This
covariance matrix enables a closed-form estimate of uncertainty when GEDI04_A predictions
are aggregated to large areas (e.g., the 1 km GEDI04_B grid, or other arbitrary regions;
Patterson et al., 2019; Ståhl et al., 2016). This requirement ruled out non-parametric methods
and some approaches based on machine learning in the development of GEDI04_A models
(e.g., ensemble-based decision trees and neural networks; Lang et al., 2021). Whether
alternative specifications based on machine learning can improve the quality of GEDI04_A
predictions is not known. Reducing uncertainty in GEDI04_A independent of GEDI04_B would
improve the GEDI04_A data product and support investigations that require footprint-level
resolution. This includes integration of footprint AGBD with Landsat forest cover loss (Hansen et
al., 2010; Healey et al., 2020), fusion of GEDI04_A with TanDEM-X to produce gridded AGBD at
a finer resolution than the 1 km GEDI04_B data product (Qi et al., 2019) , and simulations from
prognostic ecosystem model outputs (Ma et al., 2019; Medvigy et al., 2010), all of which are
GEDI demonstrative products that require footprint AGBD. It may also be possible to use
machine learning to identify or engineer features that are linearly related to footprint AGBD.
```

---

