# Row 6 results: docsearch / identifier

> Auto-generated. Open this file alongside `06-srt-surface-reference-type-parameter-review.md` —
> verdicts go there, this side is read-only.

**Query:** `srt surface reference type parameter`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
- **expected_sections:**
  - `native atl03`
  - `photon-selection`
  - `atl06p`
  - `atl03sp`
- **expected_pages:** (none)
- **notes:** srt parameter for surface type filter (user_guide/how_tos/ancillary_fields dropped after testsliderule.org rebaseline)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.337

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['reference', 'surface']

**Full text:**

```
and the along-track segment fit meters (float) land_ice_segments/fit_statistics/h_robust_sprd w_surface_window_final Width of the surface window, top to bottom meters (float) land_ice_segments/fit_statistics/w_surface_window_final bsnow_conf Confidence flag for presence of blowing snow boolean land_ice_segments/geophysical/bsnow_conf bsnow_h Blowing snow layer top height meters (float) land_ice_segments/geophysical/bsnow_h r_eff Effective reflectance, uncorrected for atmospheric effects. (float) land_ice_segments/geophysical/r_eff tide_ocean Ocean tides meters (float) land_ice_segments/geophysical/tide_ocean n_fit_photons Number of PEs used in determining h_li count land_ice_segments/fit_statistics/n_fit_photons spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.300

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['reference', 'surface']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r3 — score 0.294

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['reference', 'surface']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r4 — score 0.323

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['srt']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r5 — score 0.272

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['srt', 'surface', 'type']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.376

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.2 Land Ice
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 50
- **matched_tokens:** ['parameter', 'reference', 'surface', 'type']

**Full text:**

```
The
exception is the inland water mask, which is provided as a .tif file, and is stored and accessed by
SIPS as ANC12-02. These grids are under configuration management (CM) control and the
relevant document numbers are provided. For each surface type, the technical details and code used to generate the grid are also under CM
control and the relevant document numbers are provided. To the extent possible, the input data
used are also under CM control. As described above and in section 5.1.4.1.2, the surface type is determined at the major frame
rate, or at 50 Hz. We recommend using the latitude and longitude of the geolocated top of the
telemetry band as the basis for querying the surface type masks described below. On the output
ATL03 data product, the surf_type parameter is posted at the along-track segment rate at
reference photon locations. In order to map from one to the other, we use inclusive resampling,
where the value at the reference photon location is the combination of values at the major frame
locations before and after the reference photon location. If either end point indicates a particular
type (i.e. type=sea ice == true), then the value at the reference photon location is that type as
well.
```

#### r2 — score 0.402

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 98
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 98
- **matched_tokens:** ['reference', 'surface', 'type']

**Full text:**

```
RGT, as the RGT is spanned
by GT2L and GT2R. During
slews or off-pointing, it is
possible that ground tracks
may intersect the RGT. The
ICESat-2 mission has 1,387
RGTs.
sigma_along DOUBLE along-track meters Estimated Cartesian along- ATL03
geolocation track uncertainty (1-sigma)
uncertainty for the reference photon.
sigma_across DOUBLE across-track meters Estimated Cartesian across- ATL03
geolocation track uncertainty (1-sigma)
uncertainty for the reference photon.
surf_type INTEGER_ surface type unitless Flags describing which ATL03
1 surface types this interval is ,
associated with. 0=not type, Section
1=is type.
```

#### r3 — score 0.393

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 8.0 The Quality Assessment Group
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 156
- **matched_tokens:** ['reference', 'surface', 'type']

**Full text:**

```
Because reference photons are selected without considering
surface type, only one value is reported for each confidence level. The parameters and their
associated thresholds are:
qa_height_diff_DEM_ref_ph_high (> 50 m)
qa_height_diff_DEM_ref_ph_med (> 100 m)
qa_height_diff_DEM_ref_ph_low (> 200 m)
qa_height_diff_DEM_ref_ph_other (> 200 m)
140 Release Date: Fall 2022
```

#### r4 — score 0.358

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 166
- **matched_tokens:** ['parameter', 'reference', 'surface', 'type']

**Full text:**

```
This parameter is a 5xN array
where N is the number of
along-track geolocation
segments in the granule, and
the 5 rows indicate surface
type for each surface type (in
order: land, ocean, sea ice, land
ice and inland water).
velocity_sc FLOAT spacecraft meters Spacecraft velocity ATL03g, Step 3
velocity /second components (east component, in Section 3.1,
north component, up via POD ICD.
component) an observer on the
ground would measure. While
values are common to all
beams, this parameter is
naturally produced as part of
geolocation.
bounce_time_off FLOAT ground bounce seconds The difference between the ATL03, Section
set time offset transmit time and the ground 3.3
bounce time of the reference
photon.
150 Release Date: Fall 2022
```

#### r5 — score 0.406

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 189
- **matched_tokens:** ['parameter', 'surface', 'type']

**Full text:**

```
Surface-type dependent.
e_linfit_edit DOUBLE multiplier of unitless Multiplier of standard ATL03, Section
STD of linear fit deviation of linear fit to signal 5, e_linfit_edit
photons used to edit out noise
during running linear fit edit of
outliers.
e_linfit_slant DOUBLE multiplier of unitless Multiplier of sigma_linfit, the ATL03, Section
sigma_linfit standard deviation of the 5, e_linfit_edit
residuals between the actual
photon events used to
estimate the surface using a
linear fit; all photons with
height > e_linfit_slant
e_m FLOAT multiplier of unitless Multiplier of standard ATL03, Section
STD of deviation of the number of 5, em
background background photon events per
bin used in determining signal
photon threshold. Surface-type
dependent.
e_m_mult FLOAT multiplier of unitless Multiplier of e_m used to ATL03, Section
STD of e_m determine Thsig2, threshold for 5, em_mult
singular bins. Surface-type
dependent.
173 Release Date: Fall 2022
```

---

