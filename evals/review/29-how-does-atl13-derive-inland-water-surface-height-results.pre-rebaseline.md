# Row 29 results: nsidc / algorithm

> Auto-generated. Open this file alongside `29-how-does-atl13-derive-inland-water-surface-height-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does ATL13 derive inland water surface height`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **expected_sections:**
  - `inland`
  - `water surface`
  - `water body`
- **expected_pages:** (none)
- **notes:** ATL13 ATBD inland water

---

## 📚 docsearch results (top 5)

#### r1 — score 0.567

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.577

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'inland', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r3 — score 0.529

- **url:** https://docs.slideruleearth.io/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'inland', 'surface', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r4 — score 0.441

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['height', 'surface']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.416

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl13s
- **category:** `api_reference`
- **matched_tokens:** ['atl13', 'water']

**Full text:**

```
sliderule.icesat2. atl13s ( parm , resource ) [source] Subsets ATL13 data given the polygon and time range provided and returns measurements Parameters : parms ( dict ) â parameters used to configure ATL13 subsetting (see Parameters ) resource ( str ) â ATL13 HDF5 filename Returns : ATL13 water measurements Return type : GeoDataFrame
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.632

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Abstract
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 2
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

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

#### r2 — score 0.624

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.2 Data Product Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 19
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

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

#### r3 — score 0.600

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 8
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

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

#### r4 — score 0.637

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.5 Goals of ICESat-2 Inland Water Body Height Data Products
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 27
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

**Full text:**

```
Also note that the ATL22 level L3B companion product containing the means of the ATL13
along-track products are co-developed developed and reported in a separate ATBD entitled
“Mean Inland Surface Water Data (ATL22)”, with its own release versions, currently Release 4
as of 20. The difference between the along track ATL13 products and the mean ATL22 products
is graphically illustrated in Figure 1-1 below. This ATL13 ATBD includes background (Chapter 2), details of the theoretical underpinnings of
the algorithms together with their testing on ATLAS or ATLAS prototype data (Chapters 3 and
4), a list of the specific ATL13 output product tables (Chapter 5), and several calibration and
validation background and opportunities (Chapter 6). Since this ATBD is refined over time due
to improvement to the algorithms, a summary of the principal updates to each version or release
is also provided in the Change Log and in Chapter 1. The complete documentation of the ATL13 product including the most recent version of this
ATL13 ATBD, Data Product Known Issues, and data acquisition, are available at link
https://nsidc.org/data/atl13.
1.5 Goals of ICESat-2 Inland Water Body Height Data Products
The Inland Water Body Height Data Product is computed as part of an integrated set of six
ICESat-2 geophysical products that also include ice sheets, sea ice, atmosphere, vegetation
structure and oceans.
```

#### r5 — score 0.648

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 2.0 PHYSICS OF OPEN WATER
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 32
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Table 1-2 Summary of Principal Features of the ATL13 and ATL22 Inland Surface Water Products
2.0 PHYSICS OF OPEN WATER
The retrieval of the inland water height requires consideration of several key physical processes
including: i) the generation, characterization and statistical representation of surface waves, ii)
the propagation and scattering of light, from both ICESat2 and sun sources, especially at the
water surface and within the subsurface, and iii) an understanding of the characteristics of the
9
Release 007, January 31, 2025
```

---

