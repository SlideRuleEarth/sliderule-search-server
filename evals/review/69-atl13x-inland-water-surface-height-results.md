# Row 69 results: docsearch / identifier

> Auto-generated. Open this file alongside `69-atl13x-inland-water-surface-height-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl13x inland water surface height`
**Panel signature:** `04e5570cdaa9`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `4. atl13`
  - `atl13x`
  - `4.1 inland lake`
- **expected_pages:** (none)
- **notes:** atl13x endpoint

---

## 📚 docsearch results (top 5)

#### r1 — score 0.547

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13x', 'height', 'inland', 'surface', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.510

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['inland', 'surface', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r3 — score 0.581

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['inland', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r4 — score 0.595

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['inland']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.425

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['height', 'surface']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.625

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.2 Data Product Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 19
- **matched_tokens:** ['height', 'inland', 'surface', 'water']

**Full text:**

```
These heights are corrected for several geophysical phenomena (e.g. atmospheric
refraction, tides) and are classified either as likely signal photon events or likely background
photon events. Atmospheric data products draw the raw atmospheric profiles for each strong beam from ATL02. ATL04 provides normalized relative backscatter profiles and ATL09 produces calibrated
backscatter profiles, atmospheric layer heights, and related atmospheric parameters. All Level 3A data products draw from the geolocated photon heights in ATL03 and the
atmospheric parameters from ATL09. Along-track land ice ellipsoidal heights are provided in
ATL06, along-track sea ice and polar ocean heights are provided in ATL07, and along-track
terrestrial ellipsoidal height and related metrics for vegetation heights are provided in ATL08. Sea ice freeboard for the Arctic and Antarctic seas and associated parameters are in ATL10. Ocean heights are provided in ATL12, while inland water heights are in ATL13. Level 3B data products are gridded products, drawing from the along-track products of Level
3A. ATL11, 14, and 15 are gridded land ice products corresponding to land ice height time
series, annually gridded land ice heights, and gridded land ice height change. Sea ice gridded
data for the Arctic and Antarctic are provided in ATL20 and 21. Gridded terrestrial data is
provided in ATL18 while the gridded mean sea surface heights are in ATL19.
```

#### r2 — score 0.605

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Abstract
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 2
- **matched_tokens:** ['height', 'inland', 'surface', 'water']

**Full text:**

```
In addition to ATL13 Level 3A, also co-produced as a separate product is the higher level L3B
mean values of the ATL13 along-track crossing values, which is described in the ATL22 ATBD
entitled ATL22 Mean Inland Surface Water Data (ATL22, Release 4). Citation for this ATL13 ATBD L3A Release 007 document:
M. Jasinski, J. Stoll, D. Hancock, J. Robbins, J. Nattala, J. Morrison, B. Jones, M. Ondrusek, C. Parrish, T. Pavelsky, Carabajal, C., and the ICESat-2 Science Team, January 2025: Algorithm
Theoretical Basis Document (ATBD) for Along Track Inland Surface Water Data, ATL13,
Release 7, January, 2025, NASA Goddard Space Flight Center, Greenbelt, MD, 190 pp. DOI: 10.5067/46BO943W5S2X
Citation when using ATL13 Inland Water data products from NSIDC:
M. Jasinski, J. Stoll, D. Hancock, J. Robbins, J. Nattala, T. Pavelsky, J. Morrison, B. Jones, M. Ondrusek, C. Parrish, and the ICESat-2 Science Team, 2025. ATLAS/ICESat-2 L3A Along Track
Inland Surface Water Data, Release 7. [Indicate subset used]. Boulder, Colorado USA. NASA
National Snow and Ice Data Center Distributed Active Archive Center. DOI:10.5067/ATLAS/ATL13.007
*Note: The name of the ATL13 product (including both the ATBD documentation and the
NSIDC data products) was changed to ATL13 Along Track Inland Surface Water Data beginning
with Version 4. This name change was necessary to more accurately reflect the expanded suite of
ATL13 products beyond just water height.
```

#### r3 — score 0.600

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 8
- **matched_tokens:** ['height', 'inland', 'surface', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 007
ATL13 Release 003 (Cont’d) March 1,
2020
- Added downscaled ATL09 input wind vector
components at 10m height (met_u10m, met_v10m).
-Included bottom in determining the minimum height to
calculate subsurface deconvolution.
-Updated threshold counts of photons within short
segment histogram multimode.
-Included max available ATL03 geolocation segments
outside of water mask edges, in height computation.
-Added water body transect parameters; transect_id,
sseg_start_lat, sseg_start_lon, sseg_end_lat,
sseg_end_lon and segment_azimuth.
-Corrected sign in EM bias (H_bias_EM) calculation.
-Updated expression for orthometric water surface height
and depth when H_bias_EM is designated as invalid and
H_bias_fit designated as valid, to omit invalid term.
-Implemented number of short segments to be designated
as anomalous due to near-shore influences (shore_buffer).
-Added surface (skin) temperature (met_ts_atl09)
interpolated from ATL09 inputs at 1 Hz and 25 Hz rate.
-Added NOAA snow/ice flag (snow_ice_atl09) from
interpolation of ATL09.
-Added writeup on MABEL Lake Mead bathymetry
viii
Release 007, January 31, 2025
```

#### r4 — score 0.591

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 20
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['height', 'inland', 'surface', 'water']

**Full text:**

```
259 1 INTRODUCTION
260 This document describes the theoretical basis and implementation of the
261 processing algorithms and data parameters for Level 3 land and vegetation heights
262 for the non-polar regions of the Earth. The ATL08 product contains heights for both
263 terrain and canopy in the along-track direction as well as other descriptive
264 parameters derived from the measurements. At the most basic level, a derived surface
265 height from the ATLAS instrument at a given time is provided relative to the WGS-84
266 ellipsoid. Height estimates from ATL08 can be compared with other geodetic data and
267 used as input to higher-level ICESat-2 products, namely ATL13 and ATL18. ATL13
268 will provide estimates of inland water-related heights and associated descriptive
269 parameters. ATL18 will consist of gridded maps for terrain and canopy features.
270 The ATL08 product will provide estimates of terrain heights, canopy heights,
271 and canopy cover at fine spatial scales in the along-track direction. Along-track is
272 defined as the direction of travel of the ICESat-2 satellite in the velocity vector.
273 Parameters for the terrain and canopy will be provided at a fixed step-size of 100 m
274 along the ground track referred to as a segment. A fixed segment size of 100 m was
275 chosen to provide continuity of data parameters on the ATL08 data product.
```

#### r5 — score 0.635

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 2.2.1 Water Light Reflection and Transmission in Open Water
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 39
- **matched_tokens:** ['height', 'inland', 'surface', 'water']

**Full text:**

```
However, initial MABEL studies indicate that the mean water surface
height correction may be small for inland water, on the order of several centimeters, due to fairly
turbid water. Typical attenuation coefficients of several US lakes are shown in Table 2-1.
16
Release 007, January 31, 2025
```

---

