# Row 14 results: docsearch / example

> Auto-generated. Open this file alongside `14-example-atl03-photon-classification-with-yapc-tutorial-review.md` —
> verdicts go there, this side is read-only.

**Query:** `example ATL03 photon classification with YAPC tutorial`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl03 classification tutorial

---

## 📚 docsearch results (top 5)

#### r1 — score 0.758

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Generating ATL03 photon classifications using ATL08 and YAPC
- **category:** `tutorial`
- **matched_tokens:** ['atl03', 'classification', 'photon', 'yapc']

**Full text:**

```
Plot ATL03 data with different classifications for a region over the Grand Mesa, CO region ATL08 Land and Vegetation Height product photon classification Experimental YAPC (Yet Another Photon Classification) photon-density-based classification
```

#### r2 — score 0.728

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.2 YAPC Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'example', 'photon', 'yapc']

**Full text:**

```
The experimental YAPC (Yet Another Photon Classifier) photon-classification scheme assigns each photon a score based on the number of adjacent photons. YAPC parameters are provided as a dictionary, with entries described below: yapc : settings for the yapc algorithm; if provided then SlideRule will execute the YAPC classification on all photons score : the minimum yapc classification score of a photon to be used in the processing request knn : the number of nearest neighbors to use, or specify 0 to allow automatic selection of the number of neighbors (version 2 only) min_knn : minimum number of k-nearest neighbors (version 3 only) win_h : the window height used to filter the nearest neighbors (overrides calculated value if non-zero) win_x : the window width used to filter the nearest neighbors version : the version of the YAPC algorithm to use; 0:read from ATL03 granule, 1-3:algorithm version (not supported by atl03x ) To run the YAPC algorithm, specify the YAPC settings as a sub-dictionary. Here is an example set of parameters that runs YAPC: parms = { "cnf" : 0 , "yapc" : { "score" : 0 , "version" : 3 , "knn" : 4 }, "ats" : 10.0 , "cnt" : 5 , "len" : 20.0 , "res" : 20.0 }
```

#### r3 — score 0.839

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'photon', 'yapc']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

#### r4 — score 0.646

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Intro
- **category:** `tutorial`
- **matched_tokens:** ['atl03', 'photon', 'yapc']

**Full text:**

```
This notebook demonstrates how to use the SlideRule Icesat-2 API to retrieve ATL03 data with two different classifications, one based on the external ATL08-product classifications, designed to distinguish between vegetation and ground returns, and the other based on the experimental YAPC (Yet Another Photon Class) algorithm.
```

#### r5 — score 0.564

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'photon', 'yapc']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.612

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 111
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 111
- **matched_tokens:** ['atl03', 'classification', 'photon', 'yapc']

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

#### r2 — score 0.588

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 115
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 115
- **matched_tokens:** ['atl03', 'classification', 'photon', 'yapc']

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

#### r3 — score 0.593

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.3 ATL03 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 25
- **matched_tokens:** ['atl03', 'classification', 'example', 'photon']

**Full text:**

```
This designation provides guidance to some aspects
of the photon classification algorithm (section 5.0) and guides high-level data products to the
ATL03 data of interest. There is an overlap of approximately ten kilometers between adjacent
surface classifications, and therefore some regions on the Earth have multiple surface
classifications. For example, areas along the edges of the Arctic Ocean are classified as ocean,
sea ice, and land. Section 5.0 describes the photon classification algorithm. This algorithm classifies each
geolocated photon event as being a likely signal photon event or a background photon event. This designation can be used by higher-level data products to further reduce the data volume
considered by that algorithm. The guiding philosophy of the photon classification algorithm is to
avoid false negatives (i.e. signal photon events misclassified as background) at the expense of
including false positives (i.e. background photon events misclassified as signal). This
classification algorithm also generates a parameter to identify the degree of confidence in
designating a particular photon event as signal or background. In release 006 and later, ATL03 contains a photon-rate parameter that provides a metric of
relative photon density, along with a segment-rate parameter that indicates the number of
photons used in the computation of weight values. Section 5.2 describes the photon weighting
algorithm.
```

#### r4 — score 0.580

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.1 ATL03 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['atl03', 'example', 'photon']

**Full text:**

```
Those photon events in
bins with a signal-to-noise ratio greater than a threshold are classified as signal, while other
photon events are classified as background. ATL03 applies multiple geophysical corrections to provide corrected heights for all the
downlinked photon events. Additionally, ATL03 also supplies certain geophysical corrections as
reference values to be applied at the end users’ discretion (i.e., geoid, ocean tides, dynamic
atmospheric correction). These corrections include the effects of the atmosphere, as well as tides
and solid earth deformation. By design, each of the corrections applied to the photon cloud can
easily be removed by the end user from the ATL03 data products if desired. By default, they are
applied to generate a best estimate of the photon height. Lastly, ATL03 provides all other spacecraft or instrument information needed by the higher-level
data products. For example, the algorithms for sea ice height and ocean height require some
knowledge of the ATLAS transmitted pulse shape or the ATLAS impulse-response function. While not explicitly needed to generate the ATL03 data product, the parameters are included in
the ATL03 product files to provide a single source for all subsequent data products. ATL03 uses the product from ATL02 and the POD and PPD processes to create its output. The
surface masks and geophysical corrections require a number of models and data products that
have been assembled with the participation of the science community.
```

#### r5 — score 0.594

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.3 Background Count Parameters
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 140
- **matched_tokens:** ['atl03', 'classification', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Count the number of TEP photons in the primary and secondary peaks. Determine the number of
photons to flag in each peak by subtracting the TEP background from the number of TEP
photons in each peak. Limit the number of photons to flag to be between 0 and 10 to prevent
unintentionally flagging return signal photons as possible TEP. Reduce the number of photons
within the primary and secondary peaks by the respective number of TEPs flagged to prevent
unintentionally flagging surface background photons as possible TEP. Add 10 to the ATL02
tof_flag corresponding to the photons flagged as possible TEP. Photons with tof_flag values
greater than 20 will be ignored by the signal classification algorithm, and will be flagged as
possible TEP with a value of -2 in signal_conf_ph on ATL03.
7.3 Background Count Parameters
As described in section 1.1, ATLAS uses a multi-step process to reduce the number of photon
events that are time tagged on board, and a reduced number of photon time tags are telemetered
to the ground. Since the telemetry band is relatively narrow (~30 meters to ~1500 meters), it
does not typically include enough background photons for a robust determination of the
background photon rate.
```

---

