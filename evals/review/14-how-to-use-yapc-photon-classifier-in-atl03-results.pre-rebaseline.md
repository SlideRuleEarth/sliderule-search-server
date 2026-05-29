# Row 14 results: docsearch / example

> Auto-generated. Open this file alongside `14-how-to-use-yapc-photon-classifier-in-atl03-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to use yapc photon classifier in atl03`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `yapc`
  - `atl03`
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: assets/grandmesa_atl03_classification.html removed; user_guide yapc/atl03 sections are closest substitute

---

## 📚 docsearch results (top 5)

#### r1 — score 0.733

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.2 YAPC Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classifier', 'photon', 'use', 'yapc']

**Full text:**

```
The experimental YAPC (Yet Another Photon Classifier) photon-classification scheme assigns each photon a score based on the number of adjacent photons. YAPC parameters are provided as a dictionary, with entries described below: yapc : settings for the yapc algorithm; if provided then SlideRule will execute the YAPC classification on all photons score : the minimum yapc classification score of a photon to be used in the processing request knn : the number of nearest neighbors to use, or specify 0 to allow automatic selection of the number of neighbors (version 2 only) min_knn : minimum number of k-nearest neighbors (version 3 only) win_h : the window height used to filter the nearest neighbors (overrides calculated value if non-zero) win_x : the window width used to filter the nearest neighbors version : the version of the YAPC algorithm to use; 0:read from ATL03 granule, 1-3:algorithm version (not supported by atl03x ) To run the YAPC algorithm, specify the YAPC settings as a sub-dictionary. Here is an example set of parameters that runs YAPC: parms = { "cnf" : 0 , "yapc" : { "score" : 0 , "version" : 3 , "knn" : 4 }, "ats" : 10.0 , "cnt" : 5 , "len" : 20.0 , "res" : 20.0 }
```

#### r2 — score 0.784

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

#### r3 — score 0.479

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r4 — score 0.496

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** References
- **category:** `background`
- **matched_tokens:** ['atl03', 'photon']

**Full text:**

```
ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03
```

#### r5 — score 0.424

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.1 PhoREAL Parameters
- **category:** `user_guide`
- **matched_tokens:** ['classifier', 'photon', 'use']

**Full text:**

```
The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the median value across all photons in the segment; âcenterâ - takes the halfway value calculated by the average of the first and last photon in the segment use_abs_h : boolean whether the absolute photon heights are used instead of the normalized heights send_waveform : boolean whether to send to the client the photon height histograms in addition to the vegetation statistics above_classifier : boolean whether to use the ABoVE photon classifier when determining top of canopy photons
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.596

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 111
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 111
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
If signal photon classification is available from ATL03 and/or DRAGANN
2198 processes, choose photons with residual heights within the maximum count
2199 histogram bin and classified as signal in a mask of initial ground photons to be
2200 considered by YAPC in following steps. Otherwise, choose all photons with
2201 residual heights within maximum count histogram bin.
2202 10. For all of the above, track which photons come from segments with a detected
2203 single surface.
2204 11. For segments with 5 or less signal photons, assume all signal photons are
2205 appropriate for the initial ground “guess”. Linear regression and histogramming
2206 would not have reliably succeeded, further analysis steps will cull errors.
2207
111
```

#### r2 — score 0.557

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 115
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 115
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
2297 4.7 De-trend Data
2298 In this next phase of the ATL08 process, we will utilize signal photons identified by
2299 DRAGANN and the ATL03 classification (signal_conf_ph) values of 3 and 4 as well as
2300 the YAPC photon weights on the ATL03 data product. In lieu of the steps presented in
2301 4.5.2 through 4.5.3, we are now using the photon weights from the YAPC algorithm
2302 provided on the ATL03 data product as a better initial estimate of the ground surface. Early
2303 results indicate that the highest 5-10% of photon weights correspond to the ground surface
2304 except in areas of dense vegetation. We have found that in areas of high topographic
2305 change, the utilization of the yapc photons weights out-performs the previous approach of
2306 iterative filtering to estimate the initial ground line.
2307 Evaluate YAPC weights, inclusive of DEM, DRAGANN, signal_conf, initial ground
2308 “guess”, and median DEM bias via:
2309 1. Obtain snow_ice flag results from ATL09, mapped to each 20m geosegment
2310 For each 20m segment:
2311 2. Normalize YAPC weights for each segment via ATL03 YAPC
2312 weight*sqrt(segment_ph_cnt), while setting zero for any photons beyond 10m above
2313 DEM elevation, minus DEM bias median, if valid. Divide these values by the
2314 maximum value of the same for normalization. Limit to a maximum value of 1.0
2315 3.
```

#### r3 — score 0.473

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 112
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 112
- **matched_tokens:** ['photon', 'use', 'yapc']

**Full text:**

```
2208 4.6 Look for potential ground photons
2209 For each 20m segment, develop a mask of likely ground photons to use for limiting
2210 those returned by YAPC analysis by executing the following.
2211 Using variable histogram bin heights, step through geosegments to analyze the
2212 lowest bins with populations higher than noise to build an initial ground “guess”
2213 mask.
2214 1. If any geosegment does not provide at least 2 signal photons, bypass all remaining
2215 steps for this section for that geosegment.
2216 2. If the vegetation fraction < 50%, and the single surface linear regression standard
2217 deviation < 2.0m, difference the linear regression applied to all photon times from the
2218 photon heights yielding a residual to use for all remaining steps. Otherwise, the
2219 following is carried out with the original photon heights.
2220 3. Build histograms of heights of all photons with 0.5m bin size
2221 4. If fewer than 3 bins, and expanded to 6m bin size, assume all signal photons apply to
2222 initial ground “guess”; YAPC and filtering will separate canopy, if any, from ground.
2223 5. Using only the 0.5m bin size histograms, determine noise bin count via 25th
2224 percentile of lowest 10% of bin count
2225 6. If the above doesn't produce a valid number, such as in the case of few histogram
2226 bins, recalculate via median of lowest 10% of bin count
2227 7. Enforce a minimum noise count of 1
2228 8.
```

#### r4 — score 0.465

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 8
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 8
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
Removed all reference to Landsat
from the ATBD.
2021 September Added section 4.16 on quality control for the final products
1
2021 September Change histogram height bin from 0.5 m to 1 m in section
1 4.7, step 3 and 8
2021 November Added Final segment QA/QC Check for canopy photons that
1 fall more than 150 m below the reference DEM. Section
4.16.1
January 15, 2022 Calculate number of background noise photons within
canopy Section 2.2.26
January 15, 2022 Adjust canopy radiometry value by removing canopy noise
photons from calculation Section 2.2.25
January 15, 2022 Add Final segment QA/QC check based on radiometric
values. Section 4.16.2
January 15, 2022 Add Final segment QA/QC check to reassign noise photons
mislabeled as canopy photons. Section 4.16.3
15 April 2022 Incorporate YAPC photon weights from ATL03 data product
to ground finding approach. Section 4.7
8
```

#### r5 — score 0.517

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 190
- **matched_tokens:** ['atl03', 'photon', 'use']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
htspanmin FLOAT minimum height meters Minimum height span for each ATL03, Section
span time interval of photons with 5, Htspanmin
confidence flag > 0. If the
height span is < htspanmin
then all photons not previously
selected within +/-
htspanmin/2 of the median
height of the signal photons
selected are marked with a
confidence flag of 1. Surface-
type dependent.
out_edit_flag INTEGER flag to request unitless Binary (logical) flag: if true (=1) ATL03, Section
outlier editing then perform an nσ edit on a 5, Ledit
running linear fit to identified
signal to remove outliers. Surface-type dependent.
pc_bckgrd_flag INTEGER flag to request unitless Binary (logical) flag: if true (=1) ATL03, Section
using photon then always use the photon 5, Lpcbg
cloud to cloud to calculate the
calculate background photon rate, if
background rate false only use the photon cloud
in the absence of the
atmospheric histogram. Surface-type dependent.
lslant_flag INTEGER flag to request unitless Binary (logical) flag: if true (=1) ATL03, Section
slant then perform slant 5, lslant
histogramming histogramming for the strong
for strong beam.
```

---

