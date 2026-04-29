# Row 40 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `40-atl03-h-ph-photon-height-variable-description-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 h_ph photon height variable description`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **expected_sections:**
  - `heights`
  - `photon`
  - `data groups`
- **expected_pages:** (none)
- **notes:** ATL03 h_ph variable

---

## 📚 docsearch results (top 5)

#### r1 — score 0.628

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'height', 'photon']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r2 — score 0.538

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.3 Photon-extent Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'photon', 'variable']

**Full text:**

```
Selected photons are divided and aggregated using along-track samples (âextentsâ) with user-specified length. These extends may or may not align with the original 20-m segments of ATL03 photons. The len parameter specifies the length of each extent, and the _res_parameter specifies the distance between subsequent extent centers. If res is less than len , subsequent segments will contain duplicate photons. The API may also select photons based on their along-track distance, or based on the segment-id parameters in the ATL03 product (see the dist_in_seg parameter). len : length of each extent in meters res : step distance for successive extents in meters dist_in_seg : true|false flag indicating that the units of the len and res are in ATL03 segments (e.g. if true then a len=2 is exactly 2 ATL03 segments which is approximately 40 meters) Extents are optionally filtered based on the number of photons in each extent and the distribution of those photons. If the pass_invalid parameter is set to False , only those extents fulfilling these criteria will be returned. pass_invalid : true|false flag indicating whether or not extents that fail validation checks are still used and returned in the results ats : minimum along track spread, which is the distance in meters between the outermost valid photons in the variable length segment cnt : minimum photon count in segment
```

#### r3 — score 0.614

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5.1 ATL06-SR Parameters
- **category:** `user_guide`
- **matched_tokens:** ['height', 'photon']

**Full text:**

```
The ATL06-SR parameters are supplied in user requests under the fit key and include: fit : maxi : maximum iterations, not including initial least-squares-fit selection H_min_win : minimum height to which the refined photon-selection window is allowed to shrink, in meters sigma_r_max : maximum robust dispersion in meters
```

#### r4 — score 0.496

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['description', 'height', 'photon']

**Full text:**

```
This endpoint is called via: sliderule . run ( 'atl24x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame lat_ph EPSG:7912 degrees (double) refraction corrected, replaced by geometry column when GeoDataFrame lon_ph EPSG:7912 degrees (double) refraction corrected, replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) not refraction corrected, dist_ph_along + segment_distance y_atc Across track distance meters (float) not refraction corrected, dist_ph_across ortho_h Orthometric height of photon (elevation above geoid) meters (float) EGM08 surface_h Orthometric height of calculated sea surface meters (float) EGM08 class_ph Photon classification 0:unclassified, 40: bathymetry, 41:sea surface confidence Bathymetry confidence 0 to 1.0, higher is more confident (float) ellipse_h Elliptical height of photon (elevation above ellipse) meters (float) ITRF2014, Optional: compact set to false invalid_kd Kd was not able to be retrieved for time and location of photon 0:valid, 1:invalid used in uncertainty calculation, Optional: compact set to false invalid_wind_speed wind speed was not able to be retrieved for time and location of photon 0:valid, 1:invalid used in uncertainty calculation, Optional: compact set to false low_confidence_Flag Bathymetry confidence is less than 0.6 0:high confidence, 1:low confidence Optional: compact set
```

#### r5 — score 0.487

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.4 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'photon', 'variable']

**Full text:**

```
The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable (atl03_ph_fields), a per-segment variable (atl03_geo_fields, atl03_corr_fields), or a rate variable (atl03_bckgrd_fields). Ancillary fields are used to specify additional fields in the ATL03, ATL08, and ATL09 granules to be returned with the photon extent and dowstream customized products. Each field provided by the user will result in a corresponding column added to the returned GeoDataFrame. Note: if a field is requested that is already present in the default GeoDataFrame, then the name of both fields will be changed to include a _x suffix for the default incusion of the field, and a _y for the ancillary inclusion of the field.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.654

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

#### r2 — score 0.628

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 4 Version History
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 22
- **matched_tokens:** ['atl03', 'h_ph', 'height', 'photon']

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

#### r3 — score 0.676

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 6.3.9 Atmospheric Delay Correction
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 130
- **matched_tokens:** ['h_ph', 'height', 'photon']

**Full text:**

```
Each non-reference photon height is then corrected as:
h_ph = h_phuncorr + neutat _delay_total + neutat_delay_derivative * (h_phuncorr - neutat_ht)
114 Release Date: Fall 2022
```

#### r4 — score 0.555

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 6.2 List of Geophysical Corrections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 116
- **matched_tokens:** ['atl03', 'h_ph', 'height', 'photon']

**Full text:**

```
The photon event heights on the ATL03 output product, /gtx/heights/h_ph, are the
geophysically-corrected photon event heights (Hgc), referenced to the WGS-84 ellipsoid. The values of the geophysical corrections and reference values, described below, are determined
using the reference photons, nominally spaced at twenty meters along-track for each ground
track. The reference photons are determined in section 3.2 and have a corresponding latitude,
longitude, time, and ellipsoidal height. The interpolating functions to determine geophysical
corrections at a specific point (i.e. the reference photon locations) are described below in the
Implementation Plan for each correction. In the event that an along-track segment has no
reference photon (i.e. there are no photons in a given segment) the geophysical corrections for
that segment are given the maximum value a data type can accommodate to represent an invalid
value of that parameter. While the models (those applied and those provided for reference) offer state-of-the-art values,
for use with the photon ellipsoidal heights, users are cautioned that small-scale features (such as
bays or peninsulas) or edges of surface-specific corrections (such as ocean tides) require
particular attention. Despite of the best efforts of the geodetic community to produce global
models that retain fidelity at small spatial or temporal scales, such regions remain challenging to
model at the fine spatial and temporal scales of interest to some users.
```

#### r5 — score 0.539

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 16
- **matched_tokens:** ['atl03', 'h_ph', 'photon']

**Full text:**

```
Roughly following the procedures used in airborne bathymetric lidar,
we start with return photon coordinates that assume topograpy, rather than bathymetry, and
then apply refraction correction. The initial coordinates are from ATL03: specifically, the
lat_ph, lon_ph, and h_ph in the /gtx/heights group.
4.2 ATL24 Input Variables
Table 2 captures each stage of the processing phase in the production of the ATL24 granule
and explains the significance of each step. Table 2 also lists the required inputs for that stage
with brief explanation. ATL03, the primary input, provides the heights above the WGS84
ellipsoid (ITRF2014 reference frame, through Release 06 of ATL03, after which ITRF2020
9
```

---

