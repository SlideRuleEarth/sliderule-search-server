# Row 95 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `95-atl03-signal-conf-ph-photon-confidence-flag-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 signal_conf_ph photon confidence flag`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 80–135
- **notes:** ATL03-specific confidence flag; must not return ATL08

---

## 📚 docsearch results (top 5)

#### r1 — score 0.622

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'confidence', 'photon']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r2 — score 0.484

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.3 Photon-extent Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'flag', 'photon']

**Full text:**

```
Selected photons are divided and aggregated using along-track samples (âextentsâ) with user-specified length. These extends may or may not align with the original 20-m segments of ATL03 photons. The len parameter specifies the length of each extent, and the _res_parameter specifies the distance between subsequent extent centers. If res is less than len , subsequent segments will contain duplicate photons. The API may also select photons based on their along-track distance, or based on the segment-id parameters in the ATL03 product (see the dist_in_seg parameter). len : length of each extent in meters res : step distance for successive extents in meters dist_in_seg : true|false flag indicating that the units of the len and res are in ATL03 segments (e.g. if true then a len=2 is exactly 2 ATL03 segments which is approximately 40 meters) Extents are optionally filtered based on the number of photons in each extent and the distribution of those photons. If the pass_invalid parameter is set to False , only those extents fulfilling these criteria will be returned. pass_invalid : true|false flag indicating whether or not extents that fail validation checks are still used and returned in the results ats : minimum along track spread, which is the distance in meters between the outermost valid photons in the variable length segment cnt : minimum photon count in segment
```

#### r3 — score 0.550

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['confidence', 'flag']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

#### r4 — score 0.448

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-01-00.html
- **title:** Release v1.1.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['atl03', 'confidence', 'photon']

**Full text:**

```
A roughly 30% performance improvement was measured as a result of this change. v1.1.5 - HttpServer (via the LuaEndpoint module) now monitors memory usage on the local system and will return a 503 response to any streaming requests made when the current memory usage exceeds a preconfigured threshold. v1.1.5 - Test framework (pytest) and GitHub actions added to sliderule-python repository: #56 v1.1.5 - Polygon information extracted from icepyx region when using the ipxapi.py APIs: #60 v1.1.3 - In the atl03rec record (icesat2.atl03s and icesat2.atl03sp APIs), the info field has been replaced by the atl08_class and atl03_cnf fields which hold the ATL08 photon classification, and ATL03 photon confidence level respectively. v1.1.3 - The default confidence level for all APIs that accept a confidence level has been changed to background (0) from high (4). v1.1.2 - The api_widgets_demo updated to provide interface for creating polygon/bounding boxes, and to select a land class. v1.1.1 - Added ipxapi.py module to Python client to support ICEPyx users. v1.1.1 - GeoDataFrames are now sorted by time.
```

#### r5 — score 0.434

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'confidence', 'flag', 'photon']

**Full text:**

```
Some photons will be returns from the Transmit Echo Path (TEP) Some photons are from the ATLAS instrument that have reflected off the surface or vegetation (these are our signal photons). The ATLAS instrument receives a vast amount of data and decides on-board whether or not to telemeter packets of received photons back to Earth. ATLAS uses a digital elevation model (DEM) and a few simple rules when making this decision. The photon events (PEs) that are returned are classified as being either signal or background for different surface types (land ice, sea ice, land, and ocean). These PEs have a confidence level flag associated with it for each surface type: -2 : possible Transmit Echo Path (TEP) photons -1 : events not associated with a specific surface type 0 : noise 1 : buffer but algorithm classifies as background 2 : low 3 : medium 4 : high There will be photons transmitted by the ATLAS instrument will never be recorded back. The vast majority of these photons never reached the ATLAS instrument again (only about 10 out of the 10 14 photons transmitted are received), but some are not detected due to the âdead timeâ of the instrument. This can create a bias towards the first photons that were received by the instrument, particularly for smooth and highly reflective surfaces. The transmitted pulse is also not symmetric in time, which can introduce a bias when calculating average surfaces.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.699

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['atl03', 'confidence', 'photon', 'signal_conf_ph']

**Full text:**

```
ATL03
photon Computed from the ECEF Cartesian
coordinates of the bounce point.
lon_ph FLOAT longitude degrees Longitude of each received photon. ATL03
of photon Computed from the ECEF Cartesian
coordinates of the bounce point.
h_ph FLOAT height of meters Height of each received photon, ATL03
photon relative to the WGS-84 ellipsoid.
sigma_h FLOAT height m Estimated height uncertainty (1- ATL03
uncertainty sigma) for the reference photon.
signal_conf_ph UINT_1_LE photon counts Confidence level associated with ATL03
signal each photon event selected as signal
confidence (0-noise. 1- added to allow for buffer
but algorithm classifies as
background, 2-low, 3-med, 4-high).
96
```

#### r2 — score 0.694

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 163
- **matched_tokens:** ['atl03', 'flag', 'photon', 'signal_conf_ph']

**Full text:**

```
Use this
flag in conjunction with
signal_conf_ph to identify
those photons that are likely
noise or likely signal.
weight_ph INTEGER Photon weight n/a Computed weight of each ATL03, Section
photon. The weight is 5.2
calculated by a windowed KNN
algorithm using the distances
between each photon and its K
nearest neighbors. Values
range from 0 to 255, where 255
is the most heavily weighted
photon and would be
considered likely signal.
147 Release Date: Fall 2022
```

#### r3 — score 0.593

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 2.3.2.2 Photon round-trip range correction
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 17
- **matched_tokens:** ['confidence', 'flag', 'photon', 'signal_conf_ph']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
After all signal photons have been identified, the algorithm generates a flag for each photon event
indicating whether it is likely signal or background, or a photon event that was added as a buffer1
(as well as the parameters used to classify the photons). This flag,
gt[x]/heights/signal_conf_ph, also includes a confidence parameter for each likely signal
photon event—high, medium, or low confidence—based on the signal-to-noise ratio of each
histogram bin. signal_conf_ph is a 5 x N array, where N is the number of photons in the ground
track group and the 5 rows indicate signal finding for each surface type: in order, land, ocean, sea
ice, land ice, and inland water. The surface-type-specific confidence levels associated with each
photon event are 0 (noise), 1 (added as buffer but classified by the algorithm as background), 2
(low confidence signal), 3 (medium confidence signal), and 4 (high confidence signal). Additionally,
events not associated with a specific surface type are assigned a confidence level of -1, while
events evaluated as transmitter echo path (TEP) returns are assigned a confidence level of -2.
2.3.2 Geophysical Corrections
ATLAS-emitted photons pass through the atmosphere and experience delays that depend on the
refractive index along the optical path. The round-trip time of a photon is what constitutes its base
input measurement for geolocation.
```

#### r4 — score 0.579

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.2 Photon Weights
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 110
- **matched_tokens:** ['atl03', 'confidence', 'flag', 'photon', 'signal_conf_ph']

**Full text:**

```
Zmin_slct(n) = Zmid(n) – htspanmin / 2
For any photon event where Tp(i) is within the nth Δtime increment and Zmin_slct(n) ≤ Hp(i) ≤
Zmax_slct(n), reset conf(i) = max(1,conf(i)). This sets the confidence flag to 1 if it was not
previously selected as signal or to the confidence level already set if previously selected as
signal. At this point, all output parameters defined in Table 5-4 have been defined and the algorithm
output is consistent with the needs of the higher-level data products.
5.2 Photon Weights
In release 006 and later, ATL03 provides a unitless weight value at the photon rate as
/gtx/heights/weight_ph. These photon weights provide a metric of relative photon density. The
weight value is determined by calculating the KNN mean inverse vertical distance between a
single target photon and its “K” Number of Neighbors, /gtx/geolocation/knn, within the area of a
predefined selection window centered on the target photon. The weight_ph is stored on ATL03
as an unsigned one-byte integer ranging in values from 0-255, where 255 is the highest possible
weight. Weight values are intended for use in conjunction with the quality_ph parameter (Section
7.7.3) to identify photons that are likely due to instrument effects or considered TEP. Weights
can also be used with or without signal_conf_ph.
94 Release Date: Fall 2022
```

#### r5 — score 0.573

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 3
- **matched_tokens:** ['atl03', 'confidence', 'flag', 'photon', 'signal_conf_ph']

**Full text:**

```
2017 September Modified 500 canopy photon segment filter (Sec 3.5 (c), Sec
4.14 (6))
2017 November Added solar_azimuth, solar_elevation, and n_seg_ph to
Reference Data group; parameters were already in product
(Sec 2.4)
2017 November Specified number of ground photons threshold for relative
canopy product calculations (Sec 4.18 (2)); no number of
ground photons threshold for absolute canopy heights (Sec
4.18.1 (1))
2017 November Changed the ATL03 signal used in superset from all ATL03
signal (signal_conf_ph flags 1-4) to the medium-high
confidence flags (signal_conf_ph flags 3-4) (Sec 3.1, Sec 4.3
(17))
2017 November Removed Date parameter from Table 2.4 since UTC date is in
file metadata
2018 March Clarified that cloud flag filtering option should be turned off
by default
2018 March Changed h_diff_ref QA threshold from 10 m to 25 m (Table
5.2)
2018 March Added absolute canopy height quartiles,
canopy_h_quartile_abs (Later removed)
2018 March Removed psf_flag from main product; psf_flag will only be a
QAQC alert (Sec 5.2)
2018 March Added an Asmooth filter based on the reference DEM value
(Sec 4.6 (4-5))
2018 March Changed relief calculation to 95th – 5th signal photon heights.
(Sec 4.6 (6))
2018 March Adjusted the Asmooth smoothing methodology (Sec 4.6 (8))
2018 March Recalculate the Asmooth surface after filtering outlying noise
from signal, then detrend signal height data (Sec 4.9 (3-4))
2018 March Added option to run alternative DRAGANN process again in
high noise cases (
```

---

