# Row 35 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `35-atl06-quality-flags-values-interpretation-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL06 quality flags values interpretation`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **expected_sections:**
  - `quality`
  - `data groups`
- **expected_pages:** (none)
- **notes:** ATL06 user guide quality flags

---

## 📚 docsearch results (top 5)

#### r1 — score 0.485

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['quality', 'values']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r2 — score 0.373

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-08-00.html
- **title:** Release v4.8.x
- **section:** General Changes
- **category:** `release_notes`
- **matched_tokens:** ['quality', 'values']

**Full text:**

```
The use of next and scroll-after has now been implemented. v4.8.0 - GEDI parameters updated to be more accurate an intuitive (the old parameter names are still functional but have been DEPRECATED, please switch to using the new ones in your code). degrade_flag changed to degrade_filter and instead of having to know what the flag values were; the user now just needs to set to True to filter out all degraded footprints. l2_quality_flag changed to l2_quality_filter and instead of having to know what the flag values were; the user now just needs to set to True to filter out anything that does not meet the L2 quality criteria. l4_quality_flag changed to l4_quality_filter and instead of having to know what the flag values were; the user now just needs to set to True to filter out anything that does not meet the L4 quality criteria. surface_flag changed to surface_filter and instead of having to know what the flag values were; the user now just needs to set to True to filter out anything that isnât a surface footprint. beam changed to beams to reflect that it is primarily a list of beams to process and not just a single beam (even though if the user only provides a single beam, the server side code will automatically promote it to a list of beams with only one element). v4.8.0 - Subsetting requests that use a rasterized geojson to perform the subsetting have been changed so that the geojson string is passed via a parameter named region_mask instead of raster .
```

#### r3 — score 0.527

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3.1 Quality Filter Parameters
- **category:** `user_guide`
- **matched_tokens:** ['quality']

**Full text:**

```
The ATL08 data can be filtered based on different quality filters. te_quality_score : terrain quality score threshold can_quality_score : canopy quality score threshold
```

#### r4 — score 0.454

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['flags']

**Full text:**

```
ed, the ATL03 extent records ( atl03rec ) are enhanced to include the following populated fields: relief : ATL08 normalized photon heights landcover : ATL08 landcover flags snowcover : ATL08 snowcover flags
```

#### r5 — score 0.347

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-00-00.html
- **title:** Release v4.0.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['atl06', 'flags']

**Full text:**

```
- Replace ânodataâ value with NaN as sampled value in GeoRaster v4.0.0 - #268 - Mismatch in pyH5Coro declarations v4.0.0 - #270 - Using H5Coro in stand alone mode v4.0.0 - #280 - Make default number of ATL06 iterations 6 v4.0.0 - #283 - feature request: report y_atc in ATL06-SR v4.0.0 - #284 - Feature idea : extract arbitrary fields from ATL03 to ATL06-SR v4.0.0 - #293 - Add ESA WorldCover plugin v4.0.0 - #295 - Requests to TNM for 3DEP 1m is timing out v4.0.0 - #299 - Errors reading ArcticDEM mosaic v4.0.0 - #300 - Put querying the catalog for raster datasets inside the API functions in the client v4.0.0 - #309 - GeoUserRaster causes use after free v4.0.0 - #312 - Bitmask/flags rasters should only be read when flags param is set
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.562

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['flags', 'quality', 'values']

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

#### r2 — score 0.527

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.7.5 Geolocation and Calibration Data Quality flag
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 155
- **matched_tokens:** ['flags', 'quality', 'values']

**Full text:**

```
A caution to end users is that these parameters refer only to the motion of the spacecraft and not
the beam angle.
7.7.5 Geolocation and Calibration Data Quality flag
The composite POD/PPD flag, /gtx/geolocation/podppd_flag, indicates the quality of input
geolocation products and the ATLAS calibration state at each ATL03 geolocation segment. The
calibration periods include regular ocean scans and round-the-world scans used to calibrate
pointing, ranging, and timing parameters where the spacecraft off-points from the reference
ground track for at least 8 minutes. Calibration flags are set with a 60-second buffer before and
after a scan period to account for spacecraft off-pointing slews. For more detail on calibration
scans, see Section 5.2 of the ICESat-2 POD ATBD. A POD/PPD flag value of zero is nominal, and considered the best available data. A non-zero
flag may suggest periods potentially impacting data quality, including degraded geolocation
and/or a calibration period. Flag values of 1-3 denote potentially degraded Precise Orbit
Determination (POD) or Precision Pointing Determination (PPD) solutions. A value of 4
indicates nominal data during an ATLAS calibration period. Flag values of 5-7 denote
potentially degraded geolocation solutions during an ATLAS calibration scan period. See Table
10.1 for details.
139 Release Date: Fall 2022
```

#### r3 — score 0.542

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Quality and Filtering Flags
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 48
- **matched_tokens:** ['flags', 'quality', 'values']

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

#### r4 — score 0.533

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Quality and Filtering Flags
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 48
- **matched_tokens:** ['flags', 'quality', 'values']

**Full text:**

```
The invalid_wind_speed is also a binary flag to indicate the
absence (=1) of a corresponding ATL09 wind speed. Absense of wind speed also impacts
the total propagated uncertainty estimation. Other useful flag of interest when considering
filtering for higher quality data is the sensor_depth_exceeded. This flag (=1) is for scenarios
when the photon depth exceeds any plausible ICESat-2 depth but remains (=0) when the
depth is reasonable. Finally, the night_flag is a binary flag to indicate when the photon was
detected in the absence of sunlight (=1). This was added with the knowledge that often the
presence of solar background noise degrades the classification accuracy. The combination
of uncertainty values, ensemble confidence scores, invalid_kd flags, and invalid_wind_speed
flags, and night_flags enables robust filtering of the data for specific use cases.
41
```

#### r5 — score 0.515

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 57
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 57
- **matched_tokens:** ['atl06', 'quality', 'values']

**Full text:**

```
A zero in this parameter implies that no data-quality
1029 tests have found a problem with the segment, a one implies that some potential problem has been
1030 found. Users who select only segments with zero values for this flag can be relatively certain of
1031 obtaining high-quality data, but will likely miss a significant fraction of usable data, particularly
1032 in cloudy, rough, or low-surface-reflectance conditions. Table 4-3 gives the parameter values
1033 needed for ATL06_quality_summary to be reported as zero. The last of these characteristics, the
1034 vertical density of photons, helps remove the effects of a common problem where the ATL03
1035 photon selection identifies a cloud top as a likely surface return. In these cases, ATL06 can
1036 converge to a large (10+ m) vertical window containing tens of signal photons. Requiring a
1037 minimum ratio between the number of photons and the height of the window eliminates most
1038 clouds, and eliminates only a few returns from rough or steep surfaces. Table 4-3 Segment characteristics for ATL06_quality_summary to be zero
Characteristic Threshold Description
h_li_sigma < 1 m Errors in surface
height are
moderate or better
snr_significance < 0.02 Surface detection
blunders are
unlikely
signal_selection_source <=1 Signal selection
must be based on
ATL03 photons
n_fit_photons / w_surface_window_final >1 PE /m for The vertical
weak beams, > density of photons
4 PE/m for in the final surface
strong beams window.
1039
45
```

---

