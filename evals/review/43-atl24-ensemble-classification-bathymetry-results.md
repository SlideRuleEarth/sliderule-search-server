# Row 43 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `43-atl24-ensemble-classification-bathymetry-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL24 ensemble classification bathymetry`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL24 ensemble classification

---

## 📚 docsearch results (top 5)

#### r1 — score 0.596

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'classification']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r2 — score 0.606

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'classification']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r3 — score 0.611

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-07-00.html
- **title:** Release v4.7.x
- **section:** Known Issues and Remaining Tasks
- **category:** `release_notes`
- **matched_tokens:** ['bathymetry', 'ensemble']

**Full text:**

```
v4.7.1 - Current ensemble model is trained on refraction corrected heights though the inputs are not corrected v4.7.1 - Pointnet is identifying very low rates of bathymetry with respect to the other classifiers - we are still working through possible causes
```

#### r4 — score 0.511

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'classification']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r5 — score 0.529

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'classification']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.640

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'ensemble']

**Full text:**

```
The specific classifications in ATL24 are are sea surface (41), and bathymetry
(40), all other photons, not classified as 40 or 41 are considered unclassified (0). These point
class designations are from the American Society for Photogrammetry and Remote Sensing
(ASPRS) LAS Domain Profile for Topo-Bathy Lidar (ASPRS 2013). In many regards, the classification step in the workflow is the most important and
challenging aspect in producing the product. In airborne bathymetric lidar, significant
human analyst time is typically spent manually providing the classifications of the data. This
human-in-the-loop is primarily due to the lack of any individual algorithm capable of handling
the full extent of seafloor morphologies, substrates, depth ranges and cover types (e.g. coral,
seagrass, macroalgae) that exist worldwide. Certainly, customized classification algorithms
do currently exist for ALB as well as ICESat-2 but are all optimized for location-specific
environmental conditions which precludes the scalability of any single solution to a global
level. A novel aspect of the ATL24 workflow is to use an ensemble model for sea surface and
seafloor point classification. The overarching idea is that the whole is greater than the sum
of the parts: by combining the outputs of a number of base models or algorithms, it is
possible to attain better classification results than can be achieved with any individual model
or algorithm.
```

#### r2 — score 0.693

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3 Processing
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 7
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'ensemble']

**Full text:**

```
On-demand and customizable, science-ready bathymetry is also available via SlideRule, a public
web application programming interface for processing of science data in the cloud.
2.2 Acquisition
ATL03 provides heights above the WGS84 ellipsoid, the latitude and longitude, and time for every
ATLAS photon detection. These values and data quality flags are the primary input to ATL24.
2.3 Processing
The ATL24 workflow utilizes an ensemble of classification models to handle the full extent of
seafloor types, morphologies, depth ranges, water types, and cover types that exist throughout
coastal and nearshore areas, as described in the following sections. See "Section 4.4 Classification
Algorithms" of the ATL24 ATBD for full details. Use of a bathymetric search mask drastically
reduces computation time by removing data that are on land or too deep/turbid for measurement. Page 6 of 15National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.629

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Known Issues
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 55
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'ensemble']

**Full text:**

```
6.5 Known Issues
ATL24 product known issues can be categorized as data quality issues, user utility issues, or
product parameterization. Each of these categories has several different facets that range in
complexity of the problems and the possibility of a solution.
• Data Quality
1. Classification performance: The most notable issue with data quality will likely
be the photon-classification accuracy, namely Class 40 false positives. Although
the innovation of using an ensemble improves the classification over the individual
algorithm approaches, there are still many locations where ATL24 is reporting
bathymetry incorrectly. Certainly, the ensemble confidence score helps limit some
of these false positives but there can be improvements. Table 9 provides a summary
of the classification issues on version 1.0 of ATL24 and mentions possible solutions
for future data releases.
```

#### r4 — score 0.620

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Quality and Filtering Flags
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 48
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'ensemble']

**Full text:**

```
Removing these lower confidence photons (=1) will
certainly eliminate many bathymetry false positives but could be at the cost of removing
true positives in the case where fewer of the base algorithm inputs to the ensemble agreed. The threshold is determined by comparing the photon elevations and geolocations to a
reference data set. A direct comparison between the provided the vertical disparity. For those
comparisons that were within 5 m of separation, the corresponding F1 score was computed. This process was repeated as a function of the ensemble’s confidence score. This functional
relationship peak value occurred at 0.6. However, it should be noted that the 0.6 value
is based on evaluation of the ensemble performance metrics given the initial repository of
training data, the specific reference data and the collective contribution of the six base
classification algorithms. This value is expected to change with future iterations of the ATL24
product. In terms of ATL24 flags on the product, there are two that provide insight into situations
where some of the ancillary data were not available for a given photon. The invalid_kd flag
is a binary flag that indicates the absence (=1) of a VIIRS Kd490 value within ±1 day of
the time tag on the photon. Having the VIIRS Kd490 value is an important component in
the total propagated uncertainty calculation. An invalid flag indicates that the uncertainty
estimate may be compromised.
```

#### r5 — score 0.564

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.8 Ensemble Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 9
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'ensemble']

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

---

