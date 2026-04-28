# Row 30 results: nsidc / algorithm

> Auto-generated. Open this file alongside `30-atl24-pointnet-bathymetric-photon-classification-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL24 PointNet++ bathymetric photon classification`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **expected_sections:**
  - `pointnet`
  - `ensemble classification`
  - `classification algorithm`
- **expected_pages:** (none)
- **notes:** ATL24 ATBD PointNet++

---

## 📚 docsearch results (top 5)

#### r1 — score 0.592

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['atl24', 'classification', 'photon']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r2 — score 0.709

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'classification']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r3 — score 0.543

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'classification', 'photon']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r4 — score 0.616

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['classification', 'photon']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

#### r5 — score 0.490

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'classification']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.572

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.4 PointNet++ Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 8
- **matched_tokens:** ['bathymetric', 'classification', 'photon', 'pointnet']

**Full text:**

```
A group of photons
are then passed into the prediction model, and the output of the prediction model assigns each
photon a classification value of “0” (non-bathymetric point) and “1” (bathymetric point). At this time,
Page 7 of 15National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.553

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.8 Ensemble Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 9
- **matched_tokens:** ['atl24', 'bathymetric', 'classification', 'photon', 'pointnet']

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

#### r3 — score 0.540

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.4 PointNet++ Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 8
- **matched_tokens:** ['bathymetric', 'classification', 'photon', 'pointnet']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
2.3.1 Classification Models
2.3.1.1 CoastNet Classification
CoastNet employs a convolutional neural network designed for network architectures with
significant depth and can effectively extract spatial features from input images. Fixed-size samples
are selected from a 2D raster of the along-track profile, then training sample pixels are determined
to contain or not contain a photon. The network then determines if each sample contains a noise
photon, a bathymetry photon, or a sea surface photon at its center.
2.3.1.2 BathyPathFinder Classification
This bathymetric surface extraction algorithm leverages techniques from network analysis to
extract a representative sample of seafloor photon returns from an ATLAS profile containing
bathymetry. All subaqueous photon returns are organized into a weighted, undirected graph. The
edges are weighted proportional to the distance between the pairs of photons to which they are
connected. Edges with outlier weights are removed, and the algorithm selects pairs of “target” and
“source” photons that represent photons at either end of a contiguous bathymetry surface. Using
the target and source pairs, the algorithm performs an optimal “least-cost” network traversal.
```

#### r4 — score 0.585

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['atl24', 'bathymetric', 'photon']

**Full text:**

```
The many algorithms combined to provide a
robust means to signal finding and photon labeling are presented in Section 4.1. This section
describes 7 independent methods that each produce predictive classes within the granule
and then describes an innovative ensemble machine learning model that provides the final
label. Additional description in Section 4.1 is given for the specific input variables and
output variables of the ATL24 workflow. After the photons are labeled, there is a correction
applied to adjust the spatial coordinates for refraction at the air-water interface. The theory
and application of this correction is also provided in Section 4.1. The performance of the
algorithm/workflow output is discussed in Section 5. This section includes both the quality
or accuracy of the photon labels but also the accuracy of the bathymetric heights relative to
independent data sources. Section 5 also contains the approach to modeling the uncertainty
of the ATL24 output, which is a parameter included on data product. Section 6 provides the
approach to ATL24 production and dissemination, as this product will be the first provided
as an on-demand, science ready product for the user as a web service. Section 6 will provide
descriptions of SlideRule and both the deployment and development environments. The
appendices contain the many acronyms used in the ATL24 ATBD lexicon.
7
```

#### r5 — score 0.551

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.4 PointNet++ Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 8
- **matched_tokens:** ['classification', 'photon', 'pointnet']

**Full text:**

```
The
photons that connect the target and source photons are then extracted and classified as
bathymetry.
2.3.1.3 OpenOceans Classification
OpenOceans is designed to leverage physical processes and principles for sea surface, seafloor,
and water column photon classifications. The approach involves first generating a histogram of
photon return heights through vertical binning of photon returns within a defined horizontal along-
track window. The sea surface peak is then identified. Next, a set of Gaussian functions is fit to the
histogram (a process known as Gaussian mixture model fitting), and bathymetry peaks are
extracted. These bathymetry peaks are then refined and used to classify seafloor points. The final
step involves calculating confidence values and implementing quality checks.
2.3.1.4 PointNet++ Classification
PointNet++ is a seafloor point classification model that is effective for segmentation of point clouds. After preprocessing, the photons are divided into groups of 8192 with easting, northing, EGM08
orthometric height, and maximum signal confidence. The values of these features are normalized,
and any “remainder” photons after division are added to a photon group that has been padded out
to 8192 to preserve input size; all padded photons have feature values of “1”.
```

---

