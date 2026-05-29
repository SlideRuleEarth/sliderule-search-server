# Row 40 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `40-atl03-atbd-output-parameter-table-photon-height-h-ph-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 ATBD output parameter table photon height h_ph`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 185–205
- **notes:** ATL03 ATBD Appendix A output parameter table lists photon-level variables (h_ph etc.), ~pp.188-200

---

## 📚 docsearch results (top 5)

#### r1 — score 0.608

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** References
- **category:** `background`
- **matched_tokens:** ['atbd', 'atl03', 'photon']

**Full text:**

```
ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03
```

#### r2 — score 0.588

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'height', 'photon']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r3 — score 0.607

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5.1 ATL06-SR Parameters
- **category:** `user_guide`
- **matched_tokens:** ['height', 'photon']

**Full text:**

```
The ATL06-SR parameters are supplied in user requests under the fit key and include: fit : maxi : maximum iterations, not including initial least-squares-fit selection H_min_win : minimum height to which the refined photon-selection window is allowed to shrink, in meters sigma_r_max : maximum robust dispersion in meters
```

#### r4 — score 0.493

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.3 Photon-extent Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'parameter', 'photon']

**Full text:**

```
Selected photons are divided and aggregated using along-track samples (âextentsâ) with user-specified length. These extends may or may not align with the original 20-m segments of ATL03 photons. The len parameter specifies the length of each extent, and the _res_parameter specifies the distance between subsequent extent centers. If res is less than len , subsequent segments will contain duplicate photons. The API may also select photons based on their along-track distance, or based on the segment-id parameters in the ATL03 product (see the dist_in_seg parameter). len : length of each extent in meters res : step distance for successive extents in meters dist_in_seg : true|false flag indicating that the units of the len and res are in ATL03 segments (e.g. if true then a len=2 is exactly 2 ATL03 segments which is approximately 40 meters) Extents are optionally filtered based on the number of photons in each extent and the distribution of those photons. If the pass_invalid parameter is set to False , only those extents fulfilling these criteria will be returned. pass_invalid : true|false flag indicating whether or not extents that fail validation checks are still used and returned in the results ats : minimum along track spread, which is the distance in meters between the outermost valid photons in the variable length segment cnt : minimum photon count in segment
```

#### r5 — score 0.404

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'height', 'photon']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.617

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 4 Version History
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 22
- **matched_tokens:** ['atl03', 'h_ph', 'height', 'photon', 'table']

**Full text:**

```
This update represents the best estimates of height uncertainty for
a reference photon in on-orbit data.
• Changed data type for ph_id_count to an unsigned 1-byte integer (bug fix). Prior releases
of ATL03 stored the value as a signed datatype, limiting the reported value to 127.
• Changed the geographic extent metadata from a predicted orbit path to a geodetic
polygon, providing better information on where ATL03 data exist for spatial queries.
• Updated the ANC42 TEP reference file to reflect changes in the ATL02 time-of-flight (TOF)
calculations stemming from calibration file updates. The updated reference TEPs allow the
appropriate TEPs passing QA to be written from ANC41 to ATL03 files.
• ATL03 V6 encompasses several updates affecting photon heights (h_ph), particularly
changes in the TOF calibrations, zero-range point, and range bias correction. The time and
temperature dependent range bias correction was first introduced in V5 but applied with an
incorrect sign. This was fixed in V6. The mean offset between the pre-launch (V5) and
post-launch (V6) zero range point is about -4 cm (V6 is ~4 cm lower than V5) and varies by
spot and strength. Table 6 below shows spot-specific mean offsets and standard
deviations. Page 21 of 22National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.554

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 183
- **matched_tokens:** ['atbd', 'atl03', 'height', 'output', 'parameter', 'table']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
ph_uncorrelated FLOAT uncorrelated meters The estimate of uncorrelated ATL03 Section
_error error height error.
```

#### r3 — score 0.510

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 190
- **matched_tokens:** ['atbd', 'atl03', 'height', 'output', 'parameter', 'photon', 'table']

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

#### r4 — score 0.592

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['atl03', 'h_ph', 'height', 'photon']

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

#### r5 — score 0.495

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 182
- **matched_tokens:** ['atbd', 'atl03', 'height', 'output', 'parameter', 'photon', 'table']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
min_full_sat INTEGER minimum full n/a The minimum number of
saturation photons within a single
photons transmit pulse that determines
if the pulse is fully saturated
(strong, weak).
min_near_sat INTEGER minimum near n/a The minimum number of
saturation photons within a single
photons transmit pulse that determines
if the pulse is nearly saturated
(strong, weak).
min_sat_h FLOAT minimum meters The height, in meters, used for
saturation determining a saturated
height transmit pulse.
min_scan_s FLOAT Minimum scan seconds Minimum number of seconds
time in an alternate knobs setting
that shall be considered an
ocean or around-the-world
scan.
min_knn INTEGER Minimum KNN n/a The minimum number of ATL03 Section
value neighbors to consider when 5.2.1
calculating photon weights.
ph_sat_flag INTEGER Saturation n/a Indicates if identification of
identification possibly saturated photons
flag (using quality_ph) is enabled.
ph_sat_lb FLOAT Saturation meters Lower bound of window used
identification in saturation identification.
lower bound
ph_sat_up FLOAT Saturation meters Upper bound of window used
identification in saturation identification.
upper bound
podppd_pad DOUBLE padding for seconds Seconds of padding data
POD/PPD needed for POD/PPD
interpolation interpolation.
scan_settle_s FLOAT Scan settle time seconds Number of second
```

---

