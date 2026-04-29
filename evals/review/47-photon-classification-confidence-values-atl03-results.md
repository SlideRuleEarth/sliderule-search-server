# Row 47 results: nsidc / cross_product

> Auto-generated. Open this file alongside `47-photon-classification-confidence-values-atl03-review.md` —
> verdicts go there, this side is read-only.

**Query:** `photon classification confidence values ATL03`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **expected_sections:**
  - `photon classification`
  - `confidence`
- **expected_pages:** (none)
- **notes:** confidence is ATL03 concept, also used by ATL08/ATL24

---

## 📚 docsearch results (top 5)

#### r1 — score 0.713

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon', 'values']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r2 — score 0.684

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'values']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r3 — score 0.751

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'photon']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

#### r4 — score 0.678

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'values']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r5 — score 0.566

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.666

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.3 ATL03 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 25
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon', 'values']

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

#### r2 — score 0.684

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Quality and Filtering Flags
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 48
- **matched_tokens:** ['classification', 'confidence', 'photon', 'values']

**Full text:**

```
5.3 Data Quality and Filtering Flags
For the initial release of ATL24 the product provides some parameter values and binary
flags to assist users with filtering data that meets certain criteria or requirements. One of
the most useful parameters for filtering on the general quality of the classification accuracy
is the confidence variable. The confidence value is a per photon value determined by the
ensemble as a prediction probability. The prediction probability is determined similar to
a softmax function but has a few differences. Ultimately, the prediction probability is the
confidence that the classification is correct for each of the three classes (surface, bathymetry
and other). These values are combined as log-odds scores across all decision trees in the
model. By passing the combined score through a logistic function (the inverse of the logit
function) the ensemble transforms the log-odds scores into a range of 0 to 1 as the prediction
probability for that classification. The classification with the maximum prediction probability
is used as the photon’s classification (the argmax). The numerical value of the maximum
prediction probability is used as the photon’s confidence score. Related to this confidence parameter is the low_confidence_flag parameter. This value
is currently set to 0.6 as a best-estimate for removing those photon classification that have
a lower probability of being correct.
```

#### r3 — score 0.658

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon', 'values']

**Full text:**

```
1793 For this release of the software, we want to mention that there are cases of after-pulsing
1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20.
1795 For this release of the software, we have determined that we will include saturated photons.
1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to
1797 a value of 0 when ATL03 quality_ph flags photons with values other than 0, 10, or 20 such
1798 that they are ignored in the ATL08 algorithm.
1799 A third quality check pertains to the signal photons (DRAGANN + ATL03 signal
1800 confidence photons) and whether those heights are near the surface heights. To pass this
1801 check, signal photons that lie 120 m above the reference DEM will be disregarded. Signal
1802 photons lying below the reference DEM will be allowed to continue for additional ATL08
1803 processing. The motivation for this quality check is to eliminate ICESat-2 photons that are
1804 reflecting from clouds rather than the true surface.
1805 Table 4.1. Input parameters to ATL08 classification algorithm. Name Data Type Long Units Description Source
Name
delta_time DOUBLE GPS seconds Elapsed GPS seconds since start of ATL03
elapsed the granule for a given photon. Use
time the metadata attribute
granule_start_seconds to compute
full gps time.
lat_ph FLOAT latitude of degrees Latitude of each received photon.
```

#### r4 — score 0.675

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.2.2 gt1l–gt3r
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 4
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon']

**Full text:**

```
This may include product and instrument
characteristics and/or processing constants.
1.2.2.2 gt1l–gt3r
Six ground track groups (gt1l–gt3r) that contain the per-beam data parameters for the
specified ATLAS ground track, as follows:
• class_ph: classification of photon (0 = unclassified, 1 = other, 40 = bathymetry, 41 = sea
surface)
• confidence: floating point value in the range 0 to 1 indicating the confidence in the point
classification from the ensemble output statistics
• delta_time: the transmit time of a given photon, measured in seconds from the ATLAS
Standard Data Product Epoch
• ellipse_h: WGS84 ellipsoid height of photon (m)
• index_ph: unique index of photon in corresponding ATL03 file
• index_seg: segment index
• invalid_kd: binary flag that indicates the absence (value = 1) of Visible Infrared Imaging
Radiometer Suite (VIIRS) data within the required timespan around the ATL03 acquisition
time-tag; when VIIRS diffuse attenuation coefficient of downwelling irradiance is available,
the flag is equal to 0
• invalid_wind_speed: binary flag that indicates the absence (value = 1) of ATL09 wind
speed, which is used in the uncertainty estimation; when wind speed is available, the flag
is equal to 0
• lat_ph: ITRF2014 latitude of each received photon (degrees north); computed from the
Earth Centered Earth Fixed Cartesian coordinates of the bounce point
• lon_ph: ITRF2014 longitude of each received photon (degrees east); computed from the
Earth Centered Earth Fixed Cartesian
```

#### r5 — score 0.597

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.2 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 69
- **matched_tokens:** ['atl03', 'classification', 'confidence', 'photon', 'values']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Figure 5-4. Final Classified Likely Signal Photons. Confidence level - high (blue, 29153 photons), medium (green, 12587 photons),
low (red, 4292), padding (black, 3393 photons). The figures above illustrate the algorithm performance on a segment of MABEL data over land
ice. As the algorithm development progressed, it became clear that different surfaces, and
different beam energies required different parameter values in order to best identify likely signal
photon events and minimize the number of false positives. As described in detail in a companion
document, Optimization of Signal Finding Algorithm, we optimized the parameter settings
according to surface type (land, ocean, sea ice, land ice, inland water) and beam energy (strong
and weak). Consequently, many parameters in Table 5-2 are surface type or beam energy
dependent. The likelihood of identifying likely signal photons varies as a function of background rate. We
simulated a surface and varied the background photon rate to determine the sensitivity of the
photon classification algorithm to background photon rate. In Figure 5-5, the simulated surface
is shown on the left with two different background rates. On the right of Figure 5-5, we
summarize the results of seven simulations. In general, the surface is classified with high
confidence up to a few MHz of background photon events.
```

---

