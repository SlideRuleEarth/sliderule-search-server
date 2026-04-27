# Row 4 results: docsearch / identifier

> Auto-generated. Open this file alongside `04-yapc-photon-classifier-review.md` —
> verdicts go there, this side is read-only.

**Query:** `yapc photon classifier`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `yapc`
- **expected_pages:** (none)
- **notes:** yapc = Yet Another Photon Classifier; tutorial demonstrates it

---

## 📚 docsearch results (top 5)

#### r1 — score 0.792

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.2 YAPC Classification
- **category:** `user_guide`
- **matched_tokens:** ['classifier', 'photon', 'yapc']

**Full text:**

```
The experimental YAPC (Yet Another Photon Classifier) photon-classification scheme assigns each photon a score based on the number of adjacent photons. YAPC parameters are provided as a dictionary, with entries described below: yapc : settings for the yapc algorithm; if provided then SlideRule will execute the YAPC classification on all photons score : the minimum yapc classification score of a photon to be used in the processing request knn : the number of nearest neighbors to use, or specify 0 to allow automatic selection of the number of neighbors (version 2 only) min_knn : minimum number of k-nearest neighbors (version 3 only) win_h : the window height used to filter the nearest neighbors (overrides calculated value if non-zero) win_x : the window width used to filter the nearest neighbors version : the version of the YAPC algorithm to use; 0:read from ATL03 granule, 1-3:algorithm version (not supported by atl03x ) To run the YAPC algorithm, specify the YAPC settings as a sub-dictionary. Here is an example set of parameters that runs YAPC: parms = { "cnf" : 0 , "yapc" : { "score" : 0 , "version" : 3 , "knn" : 4 }, "ats" : 10.0 , "cnt" : 5 , "len" : 20.0 , "res" : 20.0 }
```

#### r2 — score 0.652

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Generating ATL03 photon classifications using ATL08 and YAPC
- **category:** `tutorial`
- **matched_tokens:** ['photon', 'yapc']

**Full text:**

```
Plot ATL03 data with different classifications for a region over the Grand Mesa, CO region ATL08 Land and Vegetation Height product photon classification Experimental YAPC (Yet Another Photon Classification) photon-density-based classification
```

#### r3 — score 0.549

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Retrieve ATL03 elevations with ATL08 classifications
- **category:** `tutorial`
- **matched_tokens:** ['photon', 'yapc']

**Full text:**

```
SRT_LAND , "len" : 20 , "res" : 20 , # classification and checks # still return photon segments that fail checks "pass_invalid" : True , # all photons "cnf" : - 2 , # all land classification flags "atl08_class" : [ "atl08_noise" , "atl08_ground" , "atl08_canopy" , "atl08_top_of_canopy" , "atl08_unclassified" ], # all photons "yapc" : dict ( knn = 0 , win_h = 6 , win_x = 11 , min_ph = 4 , score = 0 ), } # ICESat-2 data release release = '006' # region of interest poly = [ { 'lat' : 39.34603060272382 , 'lon' : - 108.40601489205419 }, { 'lat' : 39.32770853617356 , 'lon' : - 107.68485163209928 }, { 'lat' : 38.770676045922684 , 'lon' : - 107.71081820956682 }, { 'lat' : 38.788639821001155 , 'lon' : - 108.42635020791396 }, { 'lat' : 39.34603060272382 , 'lon' : - 108.40601489205419 } ] # time bounds for CMR query time_start = '2019-11-14' time_end = '2019-11-15' # find granule for each region of interest granules_list = earthdata . cmr ( short_name = 'ATL03' , polygon = poly , time_start = time_start , time_end = time_end , version = release ) # create geodataframe gdf = sliderule . run ( "atl03x" , parms , aoi = poly , resources = granules_list ) HTTP Request Error: HTTP Error 400: Bad Request Using simplified polygon (for CMR request only!), 5 points using tolerance of 0.0001 Starting proxy for atl03x to process 1 resource(s) with 1 thread(s) request <AppServer.78978> on ATL03_20191114034331_07370502_006_01.h5 generated dataframe [gt1l] with 66779 rows and 14 columns request <AppSe
```

#### r4 — score 0.540

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Intro
- **category:** `tutorial`
- **matched_tokens:** ['photon', 'yapc']

**Full text:**

```
This notebook demonstrates how to use the SlideRule Icesat-2 API to retrieve ATL03 data with two different classifications, one based on the external ATL08-product classifications, designed to distinguish between vegetation and ground returns, and the other based on the experimental YAPC (Yet Another Photon Class) algorithm.
```

#### r5 — score 0.656

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['photon', 'yapc']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.618

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 111
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 111
- **matched_tokens:** ['photon', 'yapc']

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

#### r2 — score 0.568

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 112
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 112
- **matched_tokens:** ['photon', 'yapc']

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

#### r3 — score 0.525

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 115
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 115
- **matched_tokens:** ['photon', 'yapc']

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

#### r4 — score 0.466

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Quantile Trees Classification
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 33
- **matched_tokens:** ['classifier', 'photon']

**Full text:**

```
The quantile boundaries are then used as features, along with the target photon’s
elevation, which are used as inputs to an XGBoost classifier.
26
```

#### r5 — score 0.470

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.8 Ensemble Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 9
- **matched_tokens:** ['classifier', 'photon']

**Full text:**

```
Quantile
Trees provides the surface input, and the threshold is calculated for 85% and 65%.
2.3.1.7 Quantile Trees Classification
Quantile Trees arranges ground track profiles as 2D profile images. For each photon, the algorithm
constructs an image centered on the target photon, and the distribution of photons within columns
is placed into quantiles. The quantile bins in each column of the image are then used as features
for a supervised learning algorithm (XGBoost). The algorithm then trains on ground tracks from
hundreds of labeled data sets to produce a model that can predict noise, sea surface, and
bathymetry labels for any given input ground track.
2.3.1.8 Ensemble Classification
The supervised stacking ensemble method uses predictions from the other classifiers as inputs to
predict a final classification, allowing the model to learn which combinations of predictions produce
the best results. Further, more features can be added to the classifier to learn which models
(mentioned above) to trust under certain conditions. Importantly, the ensemble outputs a
confidence score, which provides a method of evaluating the confidence of the classification (sea
surface or seafloor). Page 8 of 15National Snow and Ice Data Center
nsidc.org
```

---

