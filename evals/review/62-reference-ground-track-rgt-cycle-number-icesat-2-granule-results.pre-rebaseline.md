# Row 62 results: nsidc / cross_product

> Auto-generated. Open this file alongside `62-reference-ground-track-rgt-cycle-number-icesat-2-granule-review.md` —
> verdicts go there, this side is read-only.

**Query:** `reference ground track RGT cycle number ICESat-2 granule`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **expected_sections:**
  - `reference ground track`
  - `rgt`
  - `cycle`
- **expected_pages:** (none)
- **notes:** RGT/cycle concepts defined at ATL03 level, also in per-product user guides

---

## 📚 docsearch results (top 5)

#### r1 — score 0.587

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['cycle', 'granule', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r2 — score 0.564

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['cycle', 'granule', 'ground', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
pendent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r3 — score 0.539

- **url:** https://docs.slideruleearth.io/assets/boulder_watershed.html
- **title:** Using atl03x to get ICESat-2 data over the Boulder Watershed
- **section:** Execute ATL06 Algorithm using SlideRule
- **category:** `tutorial`
- **matched_tokens:** ['cycle', 'ground', 'reference', 'rgt']

**Full text:**

```
[3]: %%time # Build ATL06 Request parms = { "poly" : region , "srt" : icesat2 . SRT_LAND , "cnf" : icesat2 . CNF_SURFACE_HIGH , "ats" : 10.0 , "cnt" : 10 , "len" : 40.0 , "res" : 20.0 , "fit" : {} } # Request ATL06 Data gdf = sliderule . run ( "atl03x" , parms ) # Display Statistics print ( "Reference Ground Tracks: {} " . format ( gdf [ "rgt" ] . unique ())) print ( "Cycles: {} " . format ( gdf [ "cycle" ] . unique ())) print ( "Received {} elevations" . format ( len ( gdf ))) Exception <-1>: Failure on resource ATL03_20240321233614_00512302_006_01.h5 beam gt3r: H5Coro::Future read failure on gt3r/heights/dist_ph_along Reference Ground Tracks: [531 28 554 51 996 973] Cycles: [24 18 10 25 21 9 12 19 4 20 22 16 15 6 5 8 13 23 1 2 17 7 14 11 26 3] Received 398866 elevations CPU times: user 923 ms, sys: 303 ms, total: 1.23 s Wall time: 50.7 s
```

#### r4 — score 0.442

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['cycle', 'granule', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r5 — score 0.456

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['cycle', 'granule', 'ground', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
and the along-track segment fit meters (float) land_ice_segments/fit_statistics/h_robust_sprd w_surface_window_final Width of the surface window, top to bottom meters (float) land_ice_segments/fit_statistics/w_surface_window_final bsnow_conf Confidence flag for presence of blowing snow boolean land_ice_segments/geophysical/bsnow_conf bsnow_h Blowing snow layer top height meters (float) land_ice_segments/geophysical/bsnow_h r_eff Effective reflectance, uncorrected for atmospheric effects. (float) land_ice_segments/geophysical/r_eff tide_ocean Ocean tides meters (float) land_ice_segments/geophysical/tide_ocean n_fit_photons Number of PEs used in determining h_li count land_ice_segments/fit_statistics/n_fit_photons spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.729

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 4
- **matched_tokens:** ['cycle', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
Cycle
numbers track the number of 91-day periods that have elapsed since the ICESat-2 observatory
entered the science orbit. RGTs are uniquely identified, for example in ATL02 file names, by
appending the two-digit cycle number (cc) to the RGT number, e.g., 0001cc to 1387cc. Figure 1. Spot and ground track (GT) naming convention with
ATLAS oriented in the forward (instrument coordinate +x) direction
and backward (instrument coordinate -x) direction. NOTE: ICESat-2 reference ground tracks with dates and times can be downloaded as KMZ files from
NASA's ICESat-2 | Technical Specs page below the Orbit and Coverage table. Under normal operating conditions, data are not collected along the RGT; however, during
spacecraft slews, or off-pointing, some ground tracks may intersect the RGT. Off-pointing refers to
a series of plans over the mid-latitudes that have been designed to facilitate a global ground and
canopy height data product with approximately 2 km track spacing. Off-pointing began on 1 August
Page 3 of 22National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.690

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 71
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 71
- **matched_tokens:** ['cycle', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
1293 2.5.5 ATLAS_Pointing_Angle
1294 (parameter = atlas_pa). Off nadir pointing angle (in radians) of the satellite to
1295 increase spatial sampling in the non-polar regions.
1296 2.5.6 Reference_ground_track
1297 (parameter = rgt). The reference ground track (RGT) is the track on the earth
1298 at which the vector bisecting laser beams 3 and 4 (or GT2L and GT2R) is pointed
1299 during repeat operations. Each RGT spans the part of an orbit between two ascending
1300 equator crossings and are numbered sequentially. The ICESat-2 mission has 1387
1301 RGTs, numbered from 0001xx to 1387xx. The last two digits refer to the cycle number.
1302 2.5.7 Sigma_h
1303 (parameter = sigma_h). Total vertical uncertainty due to PPD (Precise Pointing
1304 Determination), POD (Precise Orbit Determination), and geolocation errors.
1305 Specifically, this parameter includes radial orbit error, 𝜎!"#$%, tropospheric errors,
1306 𝜎9"&' , forward scattering errors, 𝜎+&",-".(/-%%*"$01, instrument timing errors, 𝜎%$2$01,
1307 and off-nadir pointing geolocation errors. The component parameters are pulled
1308 from ATL03 and ATL09. Sigma_h is the root sum of squares of these terms as detailed
1309 in Equation 1.1. The sigma_h reported here is the mean of the sigma_h values reported
1310 within the five ATL03 geosegments that are used to create the 100 m ATL08 segment.
1311 2.5.8 Sigma_along
1312 (parameter = sigma_along). Total along-track uncertainty due to PPD and POD
1313 knowledge.
```

#### r3 — score 0.700

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** Appendix A – ICEsat-2/atlas description
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 18
- **matched_tokens:** ['cycle', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
Figure A - 1. Spot and Ground Track (GT) naming convention. The Reference Ground Track (RGT) is an imaginary track on Earth through the six-spot pattern
that is used to point the observatory. 1,387 RGTs are sampled over the course of 91 days, allowing
seasonal height changes to be detected. Onboard software aims the laser beams so that the RGT
is between GT2L and GT2R (i.e., coincident with Pair Track 2). Nominal RGT pointing occurs over
the oceans and polar regions and is periodically adjusted over vegetated land areas to broaden
global coverage. Cycle numbers track the number of 91-day periods that have elapsed since the
ICESat-2 observatory entered the science orbit. RGTs are uniquely identified by appending the
two-digit cycle number (cc) to the RGT number. Over lower latitudes, the satellite points slightly off the RGT during most cycles to measure canopy
and ground heights. Off-pointing began on 1 August 2019 with RGT 518 after the ATLAS/ICESat-2
Precision Pointing Determination (PPD) and Precision Orbit Determination (POD) solutions were
adequately resolved, and the instrument had pointed directly at the RGT for at least a full 91 days
(1,387 orbits). NOTE: ICESat-2 RGTs with dates and times can be downloaded as KML files from NASA's
ICESat-2 | Technical Specs page, below the Orbit and Coverage table.
```

#### r4 — score 0.639

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.5 ATL03 Granules
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 30
- **matched_tokens:** ['cycle', 'granule', 'ground', 'icesat', 'number', 'rgt', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
2.4.6 Group: /ancillary_data/gtx/signal_find_input
This group contains the setup parameters for the signal finding algorithm (Table 5-2 in section
5.1.3). Several parameters are common to all ground tracks, although the values for many of
these parameters are laser energy dependent (strong vs. weak) and surface-type dependent, and
so will be ground track-specific. They are provided once per granule to allow an unambiguous
connection between the output of the signal finding algorithm (captured in the group
/gtx/signal_find_output) and the parameters that were used for a given granule.
2.4.7 Group: /orbit_info
This group contains parameters that are constant for a granule, such as the RGT number and
cycle, the spacecraft orientation, and a handful of ATLAS parameters that are needed by higher-
level data products.
2.4.8 Group: /quality_assessment
This group contains quality assessment data.
```

#### r5 — score 0.645

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 97
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 97
- **matched_tokens:** ['cycle', 'ground', 'icesat', 'number', 'reference', 'rgt', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
1965 Photon Event. Some of the energy in a reflected pulse passes through the ATLAS receiver
1966 optics and electronics. ATLAS detects and time tags some fraction of the photons that make up
1967 the reflected pulse, as well as background photons due to sunlight or instrument noise. Any
1968 photon that is time tagged by the ATLAS instrument is called a photon event, regardless of
1969 source. Not: received photon, detected photon.
1970
1971 Reference Ground Track (RGT). The reference ground track (RGT) is the track on the earth at
1972 which a specified unit vector within the observatory is pointed. Under nominal operating
1973 conditions, there will be no data collected along the RGT, as the RGT is spanned by GT2L and
1974 GT2R (which are not shown in the figures, but are similar to the GTs that are shown). During
1975 spacecraft slews or off-pointing, it is possible that ground tracks may intersect the RGT. The
1976 precise unit vector has not yet been defined. The ICESat-2 mission has 1387 RGTs, numbered
1977 from 0001xx to 1387xx. The last two digits refer to the cycle number. Not: ground tracks, paths,
1978 sub-satellite track.
1979
1980 Cycle Number. Over 91 days, each of the 1387 RGTs will be targeted in the polar regions once.
1981 In subsequent 91-day periods, these RGTs will be targeted again.
```

---

