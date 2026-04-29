# Row 5 results: docsearch / identifier

> Auto-generated. Open this file alongside `05-cnf-confidence-filter-parameter-review.md` —
> verdicts go there, this side is read-only.

**Query:** `cnf confidence filter parameter`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `native atl03`
  - `photon-selection`
  - `atl06p`
  - `atl03sp`
  - `atl06sp`
- **expected_pages:** (none)
- **notes:** cnf heavily in api_reference/icesat2.html atl06p section

---

## 📚 docsearch results (top 5)

#### r1 — score 0.331

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['confidence', 'filter']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

#### r2 — score 0.315

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['cnf', 'confidence']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r3 — score 0.227

- **url:** https://docs.slideruleearth.io/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Define the Request Parameters
- **category:** `user_guide`
- **matched_tokens:** ['cnf', 'confidence', 'filter', 'parameter']

**Full text:**

```
When making a request to the SlideRule servers, the parameters of the request (i.e. what the user wants to process and how they want to process it) are supplied in the body of the request as a JSON structure. When using the SlideRule Python client, the parameters are captured and provided by the user in a Python dictionary, and the dictionary is automatically serialized into a JSON structure by the client when making the request. For example, to set the confidence filter on an ATL03 subsetting request, the parameter structure needed by the endpoint can be passed into the sliderule.run() function as a dictionary, like so: sliderule . run ( "atl03x" , { "cnf" : - 1 }, resources = [ "ATL03_20181019065445_03150111_007_01.h5" ])
```

#### r4 — score 0.311

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3.1 Quality Filter Parameters
- **category:** `user_guide`
- **matched_tokens:** ['filter']

**Full text:**

```
The ATL08 data can be filtered based on different quality filters. te_quality_score : terrain quality score threshold can_quality_score : canopy quality score threshold
```

#### r5 — score 0.237

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-04-00.html
- **title:** Release v4.4.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['confidence', 'parameter']

**Full text:**

```
v4.4.0 - Resources are queried from servers instead of client. If a processing request does not include a list of resources to process, the server processing the request will query CMR and populate the resources parameter. In addition, any sampling requests that need a populated catalog parameter will also be queried on the server side and have that parameter populated. v4.4.0 - 389 and 383 - updates to demo plotting and added support for downloading results v4.4.0 - Raster sampling support when the output is an Arrow generated format (Geo/Parquet, CSV, Feather). v4.4.0 - Added Feather output support v4.4.0 - 43d536b - Request parameters and record information added to metadata of generated Parquet files. v4.4.0 - 763e553 - max confidence in the signal_conf variable can be selected when filtering ATL03 photons based on confidence level v4.4.0 - 392 - GEBCO raster sampling support added v4.4.0 - 9d71b6e - Meta global canopy height raster support added
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.401

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 7
- **matched_tokens:** ['confidence', 'filter', 'parameter']

**Full text:**

```
This
new parameter allows users to easily identify photons that
are not likely true surface due to saturation conditions
and/or internal reflections within the ATLAS instrument. The
new parameter allows for identification of the potentially
problematic photons without changing the signal confidence
parameter, so users can filter photons at their discretion. Improved the saturation fraction computations for
near_sat_frac and full_sat_frac parameters.
vii Release Date: Fall 2022
```

#### r2 — score 0.314

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 3
- **matched_tokens:** ['confidence', 'filter', 'parameter']

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

#### r3 — score 0.360

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.2 Photon Weights
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 110
- **matched_tokens:** ['confidence', 'parameter']

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

#### r4 — score 0.341

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 108
- **matched_tokens:** ['confidence', 'parameter']

**Full text:**

```
Always set the confidence parameter to the
maximum of the previously defined value and the new value:
conf(i,isurf) = max(conf(i,isurf), 2) if SNRbin(l) < snrlow
conf(i) = max(conf(i), 3) if snrlow ≤ SNRbin(l) < snrmed
conf(i) = max(conf(i), 4) if SNRbin(l) > snrmed
(g) Save the number of photons selected from this process in
nphot_slant(time_n).
(h) If for any time_n, nphot_slant(time_n) is greater than nphot (time_n) then
update the integration parameters such that these parameters represent those
used to select the majority of the photon events at any time_n. That is, if
nphot_slant(time_n) is greater than nphot(time_n), then:
Nphot(time_n) = nphot_slant(time_n)
δzPC_out (time_n), δtPC_out (time_n), and tintbeg_out(time_n)
become the values used for slant histogramming. If μbg_δzBG_δtBG _out(time_n) and, σbg_δzBG_δtBG _out(time_n)
are undefined then set them equal to μBG_tn_δtBG_δzBG and
σBG_tn_δtBG_δzBG, respectively.
92 Release Date: Fall 2022
```

#### r5 — score 0.422

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 78
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 78
- **matched_tokens:** ['confidence', 'parameter']

**Full text:**

```
See
1409 Table 3-1 for values.
1410 signal_selection_status_confident: parameter indicating the success/failure of signal
1411 selection using low-or-better confidence PEs.
1412 signal_selection_status_all: parameter indicating the success/failure of signal selection
1413 using all flagged PEs.
1414 H_win: Height of the window around the best-fitting line used to select PE.
1415
1416 Procedure:
1417 1. If the inputs are empty (no PE are in the along-track window), set signal_selection_source to
1418 3, set signal_selection_status_confident to 3, set signal_selection_status_all to 3 set
1419 signal_selection_status_backup to 4, and return.
1420 2. Check if the confidently detected PE are adequate to define an initial segment.
1421 2a. Set PE_selection to true for all PE with Ice_confidence_flag>=2, to zero for all
1422 others
66
```

---

