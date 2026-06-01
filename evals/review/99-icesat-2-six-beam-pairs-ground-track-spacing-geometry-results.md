# Row 99 results: nsidc / instrument

> Auto-generated. Open this file alongside `99-icesat-2-six-beam-pairs-ground-track-spacing-geometry-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ICESat-2 six beam pairs ground track spacing geometry`
**Panel signature:** `e70f9d757a48`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** beam-pair geometry in ATL03 docs

---

## 📚 docsearch results (top 5)

#### r1 — score 0.524

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['beam', 'ground', 'icesat', 'pairs', 'six', 'track']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r2 — score 0.448

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'geometry', 'ground', 'icesat', 'track']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude Fitted latitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude Fitted longitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Fitted along track distance meters (double) y_atc Fitted across track distance meters (float) photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags h_mean Fitted elevation of the segment meters (float) vertical datum controlled by parameters, default is ITRF2014 dh_fit_dx Fitted slope of the segment window_height Height of window used in final fit meters rms_misfit h_sigma spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation Using the Python client, this service is called via: parms = { "fit" : {} } sliderule . run ( 'atl03x' , parms )
```

#### r3 — score 0.432

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'geometry', 'ground', 'icesat', 'track']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) dist_ph_along + segment_distance y_atc Across track distance meters (float) dist_ph_across photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags ground_photon_count Number of photons classified as ground in the segment vegetation_photon_count Number of photons classified as canopy or top of canopy in the segment landcover ATL08 land cover flags snowcover ATL08 snow cover flags solar_elevation Sun elevation as provided in ATL03 degrees (float) h_te_median Median ellipsoidal height of the ground photons meters (float) vertical datum controlled by parameters, default is ITRF2014 h_max_canopy Maximum relief height for canopy photons meters (float) h_min_canopy Minimum relief height for canopy photons meters (float) h_mean_canopy Mean relief height for canopy photons meters (float) h_canopy 98th percentile relief height for canopy photons meters (float) canopy_openness Standard deviation of relief height for canopy photons canopy_h_metrics relief height at given percentile for canopy p
```

#### r4 — score 0.509

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['ground', 'icesat', 'track']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r5 — score 0.468

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['ground', 'icesat', 'track']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.716

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 15
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 15
- **matched_tokens:** ['beam', 'ground', 'icesat', 'pairs', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
77 track sampling and the multi-beam capability allow height products to be defined for segments
78 that are consistent in along-track position for repeated measurements along the same RPT.
79
Schematic drawing showing the pattern made by ATLAS’s 6-beam configuration on the
ground, for a track running from lower left to upper right. The RPTs (Reference Pair
Tracks, dashed lines) are defined in advance of launch; the central RPT follows the RGT
(Reference Ground Track, matching the nadir track of the predicted orbit). The Ground
Tracks are the tracks actually measured by ATLAS (GT1L, GT1R, etc, shown by green
footprints). Measured Pair Tracks (PTs) are defined by the centers of the pairs of GTs,
and deviate slightly from the RPTs because of inaccuracies in repeat-track pointing. The
separation of GTs in each pair in this figure is greatly exaggerated relative to the
separation of the PTs.
Figure 2-1. ICESat-2 repeat-track schematic
80
81 Further processing of ATL06 heights will produce heights corrected for surface slope and
82 curvature that give the estimated time-varying height for selected points on the RPTs and at
83 track-to-track crossover points (ATL11). These shape-corrected heights will be processed further
84 to give i) height maps for selected time intervals (semi-annual or annual, ATL14) and ii) annual
85 height-change maps for the Antarctic and Greenland ice sheets (ATL15)
86
3
```

#### r2 — score 0.653

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 62
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 62
- **matched_tokens:** ['beam', 'ground', 'icesat', 'pairs', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
1103 ground track number is associated with group names within the product: From left to right, they
1104 are gt1l, gt1r, gt2l, gt2r, gt3l, and gt3r. The laser beams are numbered from left to right relative
1105 to the spacecraft flight direction. When the spacecraft is flying with its x axis pointing forwards,
1106 the beam numbers are in the same order (beam numbers 1…6 correspond to tracks gt1l…gt3r),
1107 but when it is in the opposite orientation, the laser-beam numbers are reversed relative to the
1108 ground-track numbers (beam numbers 1…6 correspond to tracks gt3r…gt1l).
1109 This group is sparse, meaning that parameters are provided only for pairs of segments for which
1110 at least one beam has a valid surface-height measurement. Data-set attributes give:
1111 -the reference ground track number
1112 -the correspondence between laser beam numbers and ground tracks
1113 -the cycle number
1114 The RMS accuracy of the horizontal geolocation for the segment is described by the geolocation
1115 error ellipse, which is calculated based on the PE-medians of the ATL03 parameters
1116 sigma_geo_xt, sigma_geo_at and sigma_geo_r. The along-track and across-track coordinates of
1117 the segments are provided by parameters x_atc and y_atc.
```

#### r3 — score 0.595

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.3 ICESat-2 ATLAS Instrument
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 25
- **matched_tokens:** ['beam', 'ground', 'icesat', 'pairs', 'six', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
1.3 ICESat-2 ATLAS Instrument
NASA’s Ice, Cloud, and land Elevation Satellite-2 (ICESat-2) mission is the second of the
ICESat laser altimetry missions launch in September 2018. ICESat-2 carries an improved
Advanced Topographic Laser Altimeter System (ATLAS) consisting of a low energy,
micropulse, multibeam, high-resolution photon-counting laser altimeter possessing three pairs of
beams. Each pair, separated by about 90 m, consists of a high energy (~100 mJ) beam and a low
energy (25 mJ) beam each with an approximately 11 m footprint. Th pairs of beams are
separated by about 3 km. An instrument pulse rate of 10kHz and a nominal ground speed of
~7000m/s allow observations about every 70 cm. A schematic of the shot configuration is
shown in Figure 1-1. Figure 1-1 ICESat-2 ATLAS six-beam configuration. ICESat-2/ATLAS is thus significantly different than its predecessor, ICESat/GLAS that fired at a
much lower rate (40 Hz) but employed ~80 mJ lasers for full waveform detection (Abshire et al.
2005; Schutz et al., 2005). Each returned ATLAS photon is time-tagged with a vertical precision
of approximately 30 cm and a geolocation error ranging from 3.6 to 43 cm depending on off-
pointing angle (0 to 5 deg respectively, See Luthcke et al., 2019 ATL03g Received Photon
Geolocation), and surface and atmospheric characteristics.
```

#### r4 — score 0.600

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 19
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 19
- **matched_tokens:** ['ground', 'icesat', 'pairs', 'spacing', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
179 and 2 of the mission, ICESat-2 did not point at the RPTS, and ICESat2’s pairs are offset by up to
180 2 km from the RPT locations. The first cycle that was collected over the RPTS was the third.
181 We define ATL06 heights based on fits of a linear model to ATL03 height data from short
182 (40 m) segments of the ground track, centered on reference points spaced at 20-m intervals
183 along-track. We refer to height estimates for these short segments as “segment heights”, and
184 segment’s horizontal location is that of the reference point, displaced in a direction perpendicular
185 to the RGT to match the GT offset. The choice of 40 m for the segment length provides data
186 from slightly more than two independent (non-overlapping) ATL03 heights (based on 17-m
187 footprints) for the along-track slope estimate, so that this component of the slope can be
188 eliminated as a cause of vertical scatter in the PE height distribution. The spacing between
189 reference points is 20 m, so that each segment overlaps its neighbors by 50%.
```

#### r5 — score 0.651

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.4.1.3 Group: /gtx/geophys_corr
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 27
- **matched_tokens:** ['beam', 'ground', 'icesat', 'six', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
time, to the ground bounce point time of a reference photon. This number will usually be around
1.5 milliseconds (a result of the nominal ~500-km orbit altitude and the speed of light), and
allows the user to determine the time of day a photon bounced on the surface of the Earth to an
accuracy of less than 1 millisecond.
2.4.1 Group: /gtx
Each group contains the parameters for one of the six ATLAS ground tracks. As ICESat-2 orbits
the Earth during science operations, sequential transmitted laser pulses illuminate six ground
tracks on the surface of the Earth. All six of the ground tracks are associated with a single
reference ground track. The track width for each ground track is approximately 14 meters, equal
to the ATLAS footprint diameter. Each ground track is numbered according to the pattern of
tracks on the ground from left to right (GT1L, GT1R, GT2L, GT2R, GT3L, GT3R, abbreviated
as GTx). The labeling was chosen such that the beam names do not change when the observatory
orientation changes. Consequently, the relationship between beam energy (or ATLAS spot
number) and ground track name requires knowledge of the observatory orientation parameter as
described in section 7.5. See Appendix C, ATBD Lexicon, for further description of these terms. Owing to HDF convention, group and parameter names are not capitalized.
```

---

