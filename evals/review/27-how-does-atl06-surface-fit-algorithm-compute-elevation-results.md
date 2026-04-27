# Row 27 results: nsidc / algorithm

> Auto-generated. Open this file alongside `27-how-does-atl06-surface-fit-algorithm-compute-elevation-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does ATL06 surface fit algorithm compute elevation`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 20–50
- **notes:** ATL06 ATBD

---

## 📚 docsearch results (top 5)

#### r1 — score 0.501

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['atl06', 'elevation', 'fit', 'surface']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r2 — score 0.555

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5.2 ATL06-SR Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl06', 'fit']

**Full text:**

```
Ancillary data returned from the fit algorithm (as well as atl06 and atl06p APIs) come from the ancillary fields specified for ATL03, but instead of being returned as-is, they are processed using the ATL06 least-squares-fit algorithm, and only the result is returned. In other words, ancillary data points from ATL03 to be included in an ATL06-SR result are treated just like the h_mean, latitude, and longitude variables, and returned as a fitted double-precision floating point value.
```

#### r3 — score 0.520

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-15-00.html
- **title:** Release v4.15.x
- **section:** Compatibility Changes
- **category:** `release_notes`
- **matched_tokens:** ['algorithm', 'atl06', 'surface']

**Full text:**

```
The h_mean value in the atl03x API when running the ATL06 surface fitting algorithm was changed from a double to a float. This was to make it consistent with the ATL06 standard data product and to normalize all DataFrames with z columns to floating point precision. The x-series APIs provide a different column for the sample time - time_ns instead of time . This is to reflect that the new time_ns is provided as a Unix(ns) time, whereas the old time was provided as a GPS seconds time. The Unix(ns) time makes it compatible with Pandas and easier to display for human readability.
```

#### r4 — score 0.550

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['fit', 'surface']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.445

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl06', 'elevation', 'fit']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude Fitted latitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude Fitted longitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Fitted along track distance meters (double) y_atc Fitted across track distance meters (float) photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags h_mean Fitted elevation of the segment meters (float) vertical datum controlled by parameters, default is ITRF2014 dh_fit_dx Fitted slope of the segment window_height Height of window used in final fit meters rms_misfit h_sigma spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation Using the Python client, this service is called via: parms = { "fit" : {} } sliderule . run ( 'atl03x' , parms )
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.570

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 107
- **matched_tokens:** ['algorithm', 'elevation', 'fit', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Figure 5-7. Slant Histogram Geometry Over a Single Gap.
4. For each time, time_n, from time_n = Tbegcoef(m) + Δtime/2, to Tendcoef(m)_ -
Δtime/2, the algorithm forms a histogram of the heights relative to the surface
defined by the linear fit for that segmentor time interval, H(m). The histogram bin
size, δzpc, and integration time, δtpc, are set in the same manner as in section
5.1.4.2.4.
(a) Calculate the beginning and end values of the elevation of the mth linear fit,
noting that although this corresponds to the mth entry in the Tbegcoeff array,
not all m intervals had valid linear fits:
Zbeg = c0(m) + c1(m) × time_hb
Zend = c0(m) + c1(m) × time_he
where:
time_hb = time_n - δtpc/2
time_he = min(time_n + δtpc/2, Tendcoef(m))
(b) Rotate Zbeg, Zend and the bin size δzpc into the slant reference frame defined by
α to obtain heights, Zslbeg, Zslend and the corresponding times, Tslbeg(m),
Tslend(m). Again note that photon times along track are not adjusted, but carry
over from the ellipsoidal-reference frame times:
Zslbeg = Zbeg× cos(α(m)) - Time_hb × sin(α(m))
Zslend = Zend× cos(α(m)) - Time_he × sin(α(m))
Tslbeg = Time_hb
Tslend = Time_he
δzpcsl = δz x cos(α(m))
91 Release Date: Fall 2022
```

#### r2 — score 0.588

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 73
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 73
- **matched_tokens:** ['algorithm', 'atl06', 'fit', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
1241
Figure 5-1. Flow chart for top-level ATL06 processing
ATL03 PE Project to local
lat, lon, h, coordinates, select
by reference point
RT, PT lat,
h_mean
lon, number Iterative linear fit
and
Background-rate surface-window w_surface_window_final,
refinement dh_fit_dx, h_robust_sprd estimate
ATL03 pulse
shape segment residual
Transmit-pulse histogram
shape
correction
TX_shape
mean, median
Dead-time corrections
estimates
First-photon
bias correction FPB mean,
median Sum
corrections
h_li from
Across-track h_li
other
slope
beam in
calculation
pair dh_fit_dy
Processing chain showing inputs and outputs for ATL06 fitting routine.
1242
1243 5.4 Top-Level Fitting Routine
1244 This routine calls the other routines in the processing chain to derive the final heights and
1245 corrections. It corresponds to all the steps described in 3.2.
1246
1247 Inputs, for each beam, for ATL03 segments m-1 and m:
61
```

#### r3 — score 0.575

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 56
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 56
- **matched_tokens:** ['algorithm', 'atl06', 'fit', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
h_li_sigma Meters Propagated error due to Equation 48
sampling error and FPB
correction from the land
ice algorithm
sigma_geo_h meters Total vertical geolocation 3.10
error due to PPD and
POD, including the effects
of horizontal geolocation
error on the segment
vertical error
latitude degrees Latitude of segment 3.10
north center, WGS84, North=+
longitude degrees Longitude of segment 3.10
east center, WGS84, East=+
segment_id counts Segment number, ATL03
counting from the equator. Equal to the segment_id
for the second of the two
20-m ATL03 segments
included in the 40-m
ATL06 segment
999
1000 The standard surface height will be given on the ATL06 product as h_li. This height is the
1001 segment-center height obtained from the along-track slope fit, with the mean-median correction
1002 applied so that it represents the median surface height for the segment. By default, h_li will be
1003 corrected for all height increments in the geophysical parameter group except for the ocean tide,
1004 the equilibrium tide, and the dynamic atmosphere correction (dac); this includes earth, load, and
1005 pole tides, and troposphere corrections. Since these parameters are included in the standard
1006 ATL03 PE height, no correction is applied at the ATL06 stage.
```

#### r4 — score 0.553

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 33
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 33
- **matched_tokens:** ['algorithm', 'atl06', 'fit', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
452 3.3.5.1 Least-squares fitting
453 For each segment, we first calculate a least-squares best-fitting segment to the initially selected
454 ATL03 PEs, then use an iterative procedure based on the least-squares fit to refine this window.
455 Each time we perform the least-squares fit, we construct a design matrix, G0, from the vector x,
456 of along-track coordinates for the selected PEs:
2
𝐆4 = [1 𝒙]
457 The segment height and along-track slope are calculated based on G0 and the vector of ATL03
458 heights, h, as:
𝑑ℎ 3
[ℎ52", 𝑑𝑥] = (𝐆46𝐆4)7(𝑮46𝒉
459 The residuals to this model are then calculated:
𝑑ℎ 4
𝑟8 = ℎ−𝐆𝟎[ℎ52", 𝑑𝑥]
460
461 3.3.5.2 Iterative ground-window refinement
462 The initial surface window height may be as large as 20 meters from top to bottom, larger in
463 rough terrain or when the signal-to-noise ratio is small. This means that it may include many
464 noise PEs mixed with the signal PEs. If included in the calculation, these will lead to large
465 random errors in the surface slope and height. We can increase the proportion of signal PEs by
466 shrinking the surface window, but need to avoid shrinking it so much that we lose signal PEs.
467 To do this, we seek to find a window centered on the median height of the surface-return PEs,
468 whose height is three times the spread of the surface PE height residuals.
```

#### r5 — score 0.524

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 5.3.3 Compute signal photon histogram of long segments per ground track
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 134
- **matched_tokens:** ['algorithm', 'compute', 'fit', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Detrend as would be done with complete long segment and histogram results to determine
L_surf_inc_mean2 and L_surf_inc_stdev2 via an 80% height gaussian fit. As in section 4.7.1.3,
Ht_surf_inc_adjustment = 0
Calculate the standard deviation for each short segment as sigma_unit_fit = sqrt[(
L_surf_inc_stdev2)2 – (irf_sigma)2]. If ABS[( L_surf_inc_stdev2)2 – (irf_sigma)2] < 0.000025, then sigma_unit_fit = 0.005. If [(
L_surf_inc_stdev2)2 – (irf_sigma)2] < - 0.000025, then sigma_unit_fit is invalid.. Use values for H_bias_fit and H_bias_em equal to those of the preceeding long segment. If no
preceeding long segment exists, H_bias_fit = H_bias_em = invalid. The height adjustment value (Ht_surf_inc_adjustment) and is applied to each short segment
S_Seg1_modes within the incomplete long segment, in conjuction with valid values of
H_bias_fit and H_bias_EM, to produce ht_water_surface and the program then advances to
5.3.5(C).
```

---

