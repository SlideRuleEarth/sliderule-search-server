# Row 2 results: docsearch / identifier

> Auto-generated. Open this file alongside `02-atl06x-surface-fit-elevation-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl06x surface fit elevation`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
  - https://docs.slideruleearth.io/user_guide/xseries.html
- **expected_sections:**
  - `atl06x`
  - `2. atl06`
- **expected_pages:** (none)
- **notes:** user_guide/icesat2.html has 'ATL06 - atl06x' section

---

## 📚 docsearch results (top 5)

#### r1 — score 0.507

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['fit', 'surface']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r2 — score 0.431

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['elevation', 'fit', 'surface']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r3 — score 0.453

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['atl06x']

**Full text:**

```
The SlideRule atl06x endpoint provides a service for ATL06 subsetting and custom processing. This endpoint queries ATL06 input granules for segment heights and locations based on geographic and temporal ranges. The resulting extents are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r4 — score 0.419

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['elevation', 'surface']

**Full text:**

```
The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of segments for each beam. In SlideRule the average segment elevations will not be corrected for transmit pulse shape biases or first photon biases as compared to the higher level data products.
```

#### r5 — score 0.455

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-15-00.html
- **title:** Release v4.15.x
- **section:** Compatibility Changes
- **category:** `release_notes`
- **matched_tokens:** ['surface']

**Full text:**

```
The h_mean value in the atl03x API when running the ATL06 surface fitting algorithm was changed from a double to a float. This was to make it consistent with the ATL06 standard data product and to normalize all DataFrames with z columns to floating point precision. The x-series APIs provide a different column for the sample time - time_ns instead of time . This is to reflect that the new time_ns is provided as a Unix(ns) time, whereas the old time was provided as a GPS seconds time. The Unix(ns) time makes it compatible with Pandas and easier to display for human readability.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.447

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 107
- **matched_tokens:** ['elevation', 'fit', 'surface']

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

#### r2 — score 0.446

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 19
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 19
- **matched_tokens:** ['elevation', 'fit']

**Full text:**

```
Defining
190 overlapping segments in this way increases the chances that a segment will overlap a locally
191 smooth area within a crevasse field, potentially improving elevation-rate recovery in these areas.
192 We use the same along-track sampling for both beams in each beam pair, and, for each cycle, use
193 the same reference point each time we calculate a segment height. This allows for direct
194 comparison between segment heights from the same RPT, without the need to interpolate in the
195 along-track direction. The ATL03 PE used for each segment can be determined by associating
196 the /gtxx/land_ice_segments/segment_id parameter in ATL06 with the
197 /gtxx/geolocation/segment_id parameter in ATL03: segment m in ATL06 includes PEs from
198 ATL03 segments m-1 and m (here xx represents the ATLAS beam, with gt1l and gt1r providing
199 the left and right beams for pair 1).
200 A minimal representation of the data is given in datasets in the ATL06 product in the
201 /gtxx/land_ice_segments groups. In these groups, we give the latitude, longitude, height, slope,
202 vertical error estimate, and a quality flag for each segment. This represents the minimum set of
203 parameters needed by most users; a wide variety of parameters describing the segment fit, the
204 input data, and the environmental conditions for the data are available in the subgroups within
205 the gtxx groups.
7
```

#### r3 — score 0.440

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 41
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 41
- **matched_tokens:** ['elevation', 'fit']

**Full text:**

```
699 over each segment [100 m]; e.g., if the slope value is 0.04, there is a 4 m rise over the
700 100 m segment. Required input data are the classified terrain photons.
701 2.1.14 Segment_terrain_height_best_fit
702 (parameter = h_te_best_fit). The best fit terrain elevation at the mid-point
703 location of each 100 m segment. The mid-segment terrain elevation is determined by
704 selecting the best of three fits – linear, 3rd order and 4th order polynomials – to the
705 terrain photons and interpolating the elevation at the mid-point location of the 100
706 m segment. For the linear fit, a slope correction and weighting is applied to each
707 ground photon based on the distance to the slope height at the center of the segment.
708 2.1.15 Segment_terrain_height_25
709 (parameter = h_te_rh25). The terrain elevation from the 25% height. The
710 classified ground photons are sorted into a cumulative distribution and the height
711 associated with the 25% height for that segment is reported.
712 2.1.16 Subset_te_flag {1:5}
713 (parameter = subset_te_flag). This flag indicates the quality distribution of
714 identified terrain photons within each 100 m on a geosegment basis. The purpose of
715 this flag is to provide the user with an indication whether the photons contributing to
716 the terrain estimate are evenly distributed or only partially distributed (i.e. due to
717 cloud cover or signal attenuation).
```

#### r4 — score 0.437

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 130
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 130
- **matched_tokens:** ['elevation', 'fit', 'surface']

**Full text:**

```
2718 f. Compute the residuals of the ground photon Z heights about the
2719 interpolated terrain surface, FINALGROUND. The product is the root
2720 sum of squares of the ground photon residuals combined with the
2721 sigma_atlas_land term in Table 2.5 as described in Equation 1.4. This
2722 parameter reported as h_te_uncertainty in Table 2.1.
2723 g. Compute a linear fit on the ground photons and report the slope. This
2724 parameter is terrain_slope in Table 2.1.
2725 h. Calculate a best fit terrain elevation at the mid-point location of the
2726 100 m segment:
2727 i. Calculate each terrain photon’s distance along-track into the
2728 100 m segment using the corresponding ATL03 20 m products
2729 segment_length and dist_ph_along, and determine the mid-
2730 segment distance (expected to be 50 m ± 0.5 m).
2731 1. Use the mid-segment distance to linearly interpolate a
2732 mid-segment time (delta_time in Table 2.4). Use the
2733 mid-segment time to linearly interpolate other mid-
2734 segment parameters: interpolated terrain surface,
2735 FINALGROUND, as h_te_interp (Table 2.1); latitude
2736 and longitude (Table 2.4).
2737 ii. Calculate a linear fit, as well as 3rd and 4th order polynomial fits
2738 to the terrain photons in the segment.
2739 iii.
```

#### r5 — score 0.492

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.8 Quality and classification flags throughout flow of analysis
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 80
- **matched_tokens:** ['elevation', 'surface']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Segment_fpb_correction = 0.00015 * ffb_corr [m] 4.24e
Note: The user should subtract the_fpb_correction from the mean height products such as
ht_ortho (EGM2008) and ht_water_surf (WGS84). The above correction is not applied when all
detectors are saturated. A future ATL03 correction for such severely biased returns is will be
applied to future ATL13 Releases.
4.7.3.7 Inclusion of best publicly available DEM. As indicated in the ATL13 output table, also included is the best publicly available Digital
Elevation Model) DEM (based on resolution and quality) at the ATL13 short segment rate
together with the source of the DEM. DEM location is assigned to the short segment index
photon. DEM selection sources include all available from ATL03. The currently available
selection source and hierarchy among those are:
1) ArcticDEM
2) DTU13 Mean Sea Surface (MSS).
3) Reference Elevation Model of Antarctica (REMA)
4) Multi-Error-Removed Improved-Terrain (MERIT) DEM. Inclusion of additional future ATL03 DEM products may alter the above hierarchy.
4.7.4 Dynamic Atmospheric Correction and Ocean Tides
Three fields associated with dynamic atmospheric correction and ocean tides were added to the
output table.
```

---

