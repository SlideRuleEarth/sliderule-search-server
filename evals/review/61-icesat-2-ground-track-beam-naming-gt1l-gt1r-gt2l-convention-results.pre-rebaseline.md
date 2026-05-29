# Row 61 results: nsidc / cross_product

> Auto-generated. Open this file alongside `61-icesat-2-ground-track-beam-naming-gt1l-gt1r-gt2l-convention-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ICESat-2 ground track beam naming GT1L GT1R GT2L convention`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `beam`
  - `ground track`
  - `naming`
- **expected_pages:** (none)
- **notes:** beam naming convention defined in ATL03 docs but referenced across products

---

## 📚 docsearch results (top 5)

#### r1 — score 0.515

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'track']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r2 — score 0.470

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['beam', 'ground', 'gt1l', 'gt1r', 'gt2l', 'track']

**Full text:**

```
This is reversed in the backward orientation, and the strong beams lead the weak beams with a strong beam on the left edge of the beam pattern. ATLAS beam mapping when in the forward orientation ATLAS Spot Number Ground track Designation Beam Strength 1 gt3r Strong 2 gt3l Weak 3 gt2r Strong 4 gt2l Weak 5 gt1r Strong 6 gt1l Weak
```

#### r3 — score 0.441

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'ground', 'gt1l', 'gt1r', 'gt2l', 'track']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r4 — score 0.423

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'track']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude Fitted latitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude Fitted longitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Fitted along track distance meters (double) y_atc Fitted across track distance meters (float) photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags h_mean Fitted elevation of the segment meters (float) vertical datum controlled by parameters, default is ITRF2014 dh_fit_dx Fitted slope of the segment window_height Height of window used in final fit meters rms_misfit h_sigma spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation Using the Python client, this service is called via: parms = { "fit" : {} } sliderule . run ( 'atl03x' , parms )
```

#### r5 — score 0.457

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'ground', 'gt1l', 'gt1r', 'gt2l', 'track']

**Full text:**

```
pendent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.664

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.3 Appendix D - Lexicon for ATBD Writing
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 204
- **matched_tokens:** ['convention', 'ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'naming', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
direction of travel Reference Ground Track Ground Track 3L
GT1L
(ATLAS Spot 6, GT3L on GT 3L
weak) (ATLAS Spot 2,
weak)
GT2L
(ATLAS Spot 4, Ground Track 3R Sub-satellite track weak)
(during an offpoint)
GT3R on GT 3R
GT1R GT2R
(ATLAS Spot 1,
(ATLAS Spot 5, (ATLAS Spot 3,
strong)
strong) strong)
Reference Pair
Reference Pair Track 1 Track 3
Pair Track 2
Pair Track 1 Pair 2 Pair Track 3
Pair 1 Pair 3
+x, along track +x, along track
+y, across track ATLAS oriented forward+y, across track
Figure 10-1. Spot and track naming convention with ATLAS oriented in the forward (instrument coordinate
+x) direction.
188 Release Date: Fall 2022
```

#### r2 — score 0.667

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.3 Appendix D - Lexicon for ATBD Writing
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 205
- **matched_tokens:** ['convention', 'ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'naming', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
direction of travel Reference Ground Track Ground Track 3L
GT1L
(ATLAS Spot 1,
GT3L on GT 3L
strong)
(ATLAS Spot 5,
strong) GT2L
(ATLAS Spot 3,
Ground Track 3R Sub-satellite track strong)
(during an offpoint)
GT1R GT2R GT3R on GT 3R
(ATLAS Spot 2, (ATLAS Spot 4, (ATLAS Spot 6,
weak) weak) weak)
Reference Pair Reference Pair Track 1
Track 3
Pair Track 2
Pair Track 1 Pair 2 Pair Track 3
Pair 1 Pair 3
+x, along track +x, along track
+y, across track ATLAS oriented backward+y, across track
Figure 10-2. Spot and track naming convention with ATLAS oriented in the backward (instrument
coordinate -x) direction.
189 Release Date: Fall 2022
```

#### r3 — score 0.691

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 62
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 62
- **matched_tokens:** ['beam', 'ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'track']

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

#### r4 — score 0.624

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.4.1.3 Group: /gtx/geophys_corr
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 27
- **matched_tokens:** ['beam', 'convention', 'ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'track']

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

#### r5 — score 0.634

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 98
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 98
- **matched_tokens:** ['ground', 'gt1l', 'gt1r', 'gt2l', 'icesat', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
2006
2007 Pair Track (PT). The pair track is the imaginary line half way between the actual locations of
2008 the strong and weak ground tracks that make up a pair. There are three PTs: PT1 is spanned by
2009 GT1L and GT1R, PT2 is spanned by GT2L and GT2R (and may be coincident with the RGT at
2010 times), PT3 is spanned by GT3L and GT3R. Note that this is the actual location of the midway
2011 point between GTs, and will be defined by the actual location of the GTs. Not: tracks, paths,
2012 reference ground tracks, footpaths, reference pair tracks.
2013
2014 Pairs. When considered together, individual strong and weak ground tracks form a pair. For
2015 example, GT2L and GT2R form the central pair of the array. The pairs are numbered 1 through
2016 3: Pair 1 is comprised of GT1L and GT1R, pair 2 is comprised of GT2L and GT2R, and pair 3 is
2017 comprised of GT3L and 3R.
2018
2019 Along-track. The direction of travel of the ICESat-2 observatory in the orbit frame is defined as
2020 the along-track coordinate, and is denoted as the +x direction. The positive x direction is
2021 therefore along the Earth-Centered Earth-Fixed velocity vector of the observatory. Each pair has
2022 a unique coordinate system, with the +x direction aligned with the Reference Pair Tracks.
2023
2024 Across-track.
```

---

