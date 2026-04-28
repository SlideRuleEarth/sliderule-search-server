# Row 32 results: nsidc / algorithm

> Auto-generated. Open this file alongside `32-atl03-geophysical-corrections-ocean-tides-solid-earth-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 geophysical corrections ocean tides solid earth`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `geophysical correction`
- **expected_pages:** (none)
- **notes:** ATL03 ATBD geophysical corrections

---

## 📚 docsearch results (top 5)

#### r1 — score 0.423

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** References
- **category:** `background`
- **matched_tokens:** ['atl03', 'corrections']

**Full text:**

```
ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03
```

#### r2 — score 0.340

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['geophysical', 'ocean', 'tides']

**Full text:**

```
and the along-track segment fit meters (float) land_ice_segments/fit_statistics/h_robust_sprd w_surface_window_final Width of the surface window, top to bottom meters (float) land_ice_segments/fit_statistics/w_surface_window_final bsnow_conf Confidence flag for presence of blowing snow boolean land_ice_segments/geophysical/bsnow_conf bsnow_h Blowing snow layer top height meters (float) land_ice_segments/geophysical/bsnow_h r_eff Effective reflectance, uncorrected for atmospheric effects. (float) land_ice_segments/geophysical/r_eff tide_ocean Ocean tides meters (float) land_ice_segments/geophysical/tide_ocean n_fit_photons Number of PEs used in determining h_li count land_ice_segments/fit_statistics/n_fit_photons spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r3 — score 0.324

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-09-00.html
- **title:** Release v4.9.x
- **section:** Changes
- **category:** `release_notes`
- **matched_tokens:** ['atl03', 'corrections', 'geophysical']

**Full text:**

```
v4.9.2 - Optimized raster sampling code v4.9.2 - Fixed Python client to support output format specified as geoparquet with open_on_complete v4.9.2 - Changed default atl03 confidence flags to low, medium, and high v4.9.2 - Added separate geophysical corrections ancillary fields list in support of future ATL03 dataframe class v4.9.0 - Added ancillary field support to GEDI ( gedi01bp , gedi02ap , gedi04ap ) Bathy Version #15 - Separated out processing flags into their own variables in the h5 file: sensor depth exceeded, invalid kd, invalid wind speed, night flight Bathy Version #15 - Added low confidence flag to h5 Bathy Version #15 - Added ensemble confidence to h5 Bathy Version #15 - ISO.XML polygon is now taken directly from ATL03 Bathy Version #14 - Updated ensemble
```

#### r4 — score 0.379

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-03-00.html
- **title:** Release v5.3.x
- **section:** Release v5.3.x
- **category:** `release_notes`
- **matched_tokens:** ['earth']

**Full text:**

```
2025-03-12 Version description of the v5.3.0 release of SlideRule Earth.
```

#### r5 — score 0.356

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-09-00.html
- **title:** Release v4.9.x
- **section:** Release v4.9.x
- **category:** `release_notes`
- **matched_tokens:** ['earth']

**Full text:**

```
2025-02-04 Version description of the v4.9.3 release of SlideRule Earth. Sliderule Version Bathy Version v4.9.2 #14 v4.9.3 #15
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.654

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **title:** ATLAS/ICESat-2 L3A Land Ice Height
- **section:** 1.2.3 File Contents
- **category:** `user_guide`
- **source_product:** `ATL06` · **page:** 7
- **matched_tokens:** ['atl03', 'corrections', 'earth', 'geophysical', 'ocean', 'solid']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land Ice Height, Version 6
Table 1. Geophysical Corrections Applied to ICESat-2 Products
ICESat-2 Products by Surface Type Geophysical Corrections1
Photon-level product (ATL03) (i.e., corrections Ocean loading
applicable across all surface types) Solid Earth tide
Solid Earth pole tide
Ocean pole tide
Total column atmospheric range-delay
Land Ice, Land, and Inland Water (ATL06, No corrections beyond ATL03
ATL08, and ATL13)
Sea Ice (ATL07 and ATL10) Referenced to mean sea surface
Ocean tide
Long period equilibrium ocean tide
Inverted barometer (IB)
Ocean (ATL12) Ocean tide
Long period equilibrium ocean tide
1For details, see Section 5 of the ICESat-2 Data Comparison User's Guide for Rel006 available on the ATL03 data set
landing page.
1.2.3 File Contents
ATL06 data are provided as granules (files) that span about 1/14th of an orbit. Granule boundaries
are delineated by lines of latitude that define 14 regions, numbered from 01–14, as shown in Figure
3.
Figure 3. ATL06 region/granule boundaries.
Page 6 of 16National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.650

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.3 File Contents
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 7
- **matched_tokens:** ['atl03', 'corrections', 'earth', 'geophysical', 'ocean', 'solid']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
Table 1. Geophysical Corrections Applied to ICESat-2 Products
ICESat-2 Products by Surface Type Geophysical Corrections1
Photon-level product (ATL03) (i.e., corrections Ocean loading
applicable across all surface types) Solid Earth tide
Solid Earth pole tide
Ocean pole tide
Total column atmospheric range-delay
Land Ice, Land, and Inland Water (ATL06, No corrections beyond ATL03
ATL08, and ATL13)
Sea Ice (ATL07 and ATL10) Referenced to mean sea surface
Ocean tide
Long period equilibrium ocean tide
Inverted barometer (IB)
Ocean (ATL12) Ocean tide
Long period equilibrium ocean tide
1For details, see Section 5 of the ICESat-2 Data Comparison User's Guide for Rel006 available on the ATL03 data set
landing page.
1.2.3 File Contents
ATL03 data are segmented into granules (files) that span about 1/14th of an orbit. Granule
boundaries are delineated by lines of latitude that define 14 regions, numbered 01–14 as shown in
Figure :
Figure 3. ATL03 region/granule boundaries.
The following table lists the latitude bounds and region numbers for all 14 granule regions:
Page 6 of 22National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.619

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 2.3.2.2 Photon round-trip range correction
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 17
- **matched_tokens:** ['atl03', 'corrections', 'earth', 'geophysical', 'ocean', 'solid', 'tides']

**Full text:**

```
Over oceans, sea ice, and ice shelf surfaces, each photon
event typically requires corrections to account for temporal variability in atmospheric-oceanic
interactions (for example, inverted barometer and wind field effects) as well as tidal states and
other factors. Over land surfaces, each photon event requires corrections to account for
deformations induced by, for example, ocean loading and solid earth tides. The following sections list the time-dependent geophysical corrections. Geophysical corrections are
stored in the gt[x]/geophys_corr/ group and described in detail in Section 6 of the ATL03
ATBD.
2.3.2.1 Corrections applied due to variations in surface bounce point
• Solid Earth tides. Magnitude = ±40 cm (max).
• Ocean loading. Magnitude < 10 cm.
• Solid Earth pole tide. Magnitude = ±1.5 cm.
• Ocean pole tide. Magnitude = ±2 mm amplitude.
• Geocenter Motion (not applied to ATL03 but accounted for in POD). Magnitude = 3 to 5
mm amplitude in x, y, z.
2.3.2.2 Photon round-trip range correction
1 To meet the requirements of higher-level products, additional surrounding background photons are added as a
buffer if the identified signal photons for a Δtime do not meet a minimal height span requirement (at least 20 meters
vertically). See ATL03 ATBD | Section 5.1.2. Page 16 of 22National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.642

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.3 File Contents
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 7
- **matched_tokens:** ['atl03', 'corrections', 'earth', 'geophysical', 'ocean', 'solid']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Table 1. Geophysical Corrections Applied to ICESat-2 Products
ICESat-2 Products by Surface Type Geophysical Corrections1
Photon-level product (ATL03) (i.e., corrections Ocean loading
applicable across all surface types) Solid Earth tide
Solid Earth pole tide
Ocean pole tide
Total column atmospheric range-delay
Land Ice, Land, and Inland Water (ATL06, No corrections beyond ATL03
ATL08, and ATL13)
Sea Ice (ATL07 and ATL10) Referenced to mean sea surface
Ocean tide
Long period equilibrium ocean tide
Inverted barometer (IB)
Ocean (ATL12) Ocean tide
Long period equilibrium ocean tide
1For details, see Section 5 of the ICESat-2 Data Comparison User's Guide for Rel006 available on the ATL03 data set
landing page.
1.2.3 File Contents
ATL08 data are provided as granules (files) that span about 1/14th of an orbit. Granule boundaries
are delineated by lines of latitude that define 14 regions, numbered 01–14 as shown in Figure 3:
Figure 1. ATL08 region/granule boundaries.
Page 6 of 19National Snow and Ice Data Center
nsidc.org
```

#### r5 — score 0.645

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** Appendix A – ICEsat-2/atlas description
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 15
- **matched_tokens:** ['atl03', 'corrections', 'earth', 'geophysical', 'ocean', 'solid']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
Table A - 1. Geophysical Corrections Applied to ICESat-2 Products
ICESat-2 Products by Surface Type Geophysical Corrections1
Photon-level product (ATL03) (i.e., corrections Ocean loading
applicable across all surface types) Solid Earth tide
Solid Earth pole tide
Ocean pole tide
Total column atmospheric delay
Land Ice, Land, and Inland Water (ATL06, No geophysical corrections beyond ATL03
ATL08, and ATL13)
Sea Ice (ATL07 and ATL10) ATL03 corrections
Referenced to mean sea surface
Ocean tide
Long period equilibrium ocean tide
Dynamic atmosphere correction
Ocean (ATL12) ATL03 corrections
Ocean tide
Long period equilibrium ocean tide
1For details, see Section 5 of the ICESat-2 Data Comparison User's Guide for Rel006 available on the ATL03 data set
landing page.
Page 14 of 15National Snow and Ice Data Center
nsidc.org
```

---

