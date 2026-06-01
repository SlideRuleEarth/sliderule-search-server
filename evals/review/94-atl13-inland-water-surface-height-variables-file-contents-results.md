# Row 94 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `94-atl13-inland-water-surface-height-variables-file-contents-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL13 inland water surface height variables file contents`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 6–12
- **notes:** ATL13 user guide file contents

---

## 📚 docsearch results (top 5)

#### r1 — score 0.640

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.582

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'inland', 'surface', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r3 — score 0.619

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'inland', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r4 — score 0.667

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl13', 'inland']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.561

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

#### r1 — score 0.713

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.2.2 File Contents
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 3
- **matched_tokens:** ['atl13', 'contents', 'file', 'height', 'inland', 'surface', 'variables', 'water']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
1 DATA DESCRIPTION
The ATL13 data product is described in detail in the ICESat-2 Algorithm Theoretical Basis Document for
Along Track Inland Surface Water Data (Jasinski et al., 2025). Summary
ATL13 provides along-track surface water products for inland water bodies, defined as lakes,
reservoirs, bays, estuaries, rivers, and a 7 km near-shore buffer. Data parameters include surface
water height statistics and related parameters including significant wave height, transect slope,
subsurface signal attenuation, and shallow water bathymetry. Water surface heights are provided
as both orthometric height and height referencing the WGS84 ellipsoid. ATL13 is also used to
produce the ATLAS/ICESat-2 L3B Mean Inland Surface Water Data product (ATL22). File Information
1.2.1 File Format
Data are provided as HDF5-formatted files.
1.2.2 File Contents
A complete list of all ATL13 parameters is available in the ATL13 Data Dictionary. Each data file (granule) contains inland water body and near-shore coastal water surface heights
acquired during four of ATLAS's 1,387 orbits. Within data files, similar variables such as science
data, instrument parameters, altimetry data, and metadata are grouped together according to the
HDF model. ATL13 data files contain the top-level groups and variables shown in the following
figure:
Figure 1. ATL13 top-level data groups and variables.
```

#### r2 — score 0.597

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 5.4 ATL13 Inland Surface Water Output Variables
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 159
- **matched_tokens:** ['atl13', 'height', 'inland', 'surface', 'variables', 'water']

**Full text:**

```
Science. https://doi.org/10.1126/science.aat0636),
6=Reserved, 7=Reserved,
8=Reserved, 9=Reserved
iw_bdy_regio N/A ATL13-created shapefile representing relevant bodies of 5.3.1 (A)
n water over which to implement the ATL13 water surface
finding algorithm only within a region of processing
interest
segment_appa meters Standard deviation of short segment photon height in 5.3.2(C)
rent_stdev the short segment with signal classification >
sig_threshold.
ht_water_surf meters Water surface height, reported for each short segment 5.3.5 (A)
(default length = approximately 100 signal photons)
with reference to WGS84 ellipsoid
segment_lat degrees Latitude of reporting location for all short segment 5.3.5 (A)
statistics
segment_lon degrees Longitude of reporting location for all short segment 5.3.5 (A)
statistics.
136
Release 007, January 31, 2025
```

#### r3 — score 0.557

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.2 File Contents
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 3
- **matched_tokens:** ['contents', 'file', 'surface', 'variables']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
1 DATA DESCRIPTION
This user guide refers to the ICESat-2 Project Algorithm Theoretical Basis Document (ATBD) for Coastal
and Nearshore Along-Track Bathymetry Product (ATL24) (ATBD for ATL24, V1 |
https://doi.org/10.5067/PXJMCZD0MYLN).
1.1 Summary
ATL24 provides global along-track coastal and nearshore bathymetry, consisting of refraction-
corrected seafloor and sea surface heights (orthometric and ellipsoidal heights and instantaneous
depths), as well as associated uncertainties. The data are derived from ATLAS/ICESat-2 L2A
Global Geolocated Photon Data (ATL03).
1.2 File Information
1.2.1 Format
The data are provided as HDF5-formatted files.
1.2.2 File Contents
A complete list of ATL24 parameters is available in the ATL24 Data Dictionary.
Within data files, similar variables such as science data, instrument parameters, and ancillary data
are grouped together. Figure 1 shows data groups stored at the top level in ATL24 data files.
Figure 1. ATL24 top-level data groups and variables.
The following sections describe the data groups and their contents stored at the top level in ATL24
data files.
Page 2 of 15National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.543

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.2.3 File Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 5
- **matched_tokens:** ['atl13', 'file', 'inland', 'surface', 'variables', 'water']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
1.2.2.4 orbit_info
Orbit parameters that are constant for a granule, such as the Reference Ground Track (RGT)
number and cycle and the spacecraft orientation (sc_orient).
1.2.2.5 quality_assessment
Quality assessment data for the granule as a whole, including a pass/fail flag and a failure reason
indicator.
1.2.3 File Naming Convention
Data files utilize the following naming convention:
ATL13_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr].h5
Example:
ATL13_20230607174704_11971901_007_01.h5
The following table describes the file naming convention variables:
Table 1. File Naming Convention Variables and Descriptions
Variable Description
ATL13 ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit RGT number of the first of four tracks in the granule. The ICESat-2
mission has 1,387 RGTs, numbered from 0001 to 1387.
cc Cycle number. The cycle number tracks the number of 91-day periods that have
elapsed since ICESat-2 entered the science orbit.
ss Region number. Not used for ATL13. Always 01.1
vvv_rr Version and revision number2
1Some ATLAS/ICESat-2 products (e.g., ATL03) are provided as files that span 1/14th of an orbit. As such,
these products' file names specify a region number that ranges from 01 to 14.
```

#### r5 — score 0.563

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.3.2 Resolution
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 6
- **matched_tokens:** ['atl13', 'file', 'height', 'inland', 'surface', 'water']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
Each data file has a corresponding XML file that contains additional file level metadata. XML
metadata files have the same name as their corresponding .h5 file, but with .xml appended.
1.2.4 Browse Files
Browse files are provided as JPGs designed to quickly assess the location and quality of each
granule's data. Browse files utilize the same naming convention as their corresponding data file but
with "_BRW" and descriptive keywords appended.
ATL13 includes two browse images per beam: water surface orthometric height (ht_ortho) and
granule ground track location and coverage (groundtrack). An example is shown below.
Figure 2. Example browse image for ht_ortho.
Spatial Information
1.3.1 Coverage
Spatial coverage is nearly global (approximately 88° N to 88° S); however, the focus of ATL13 is
high-latitude terrestrial regions where the convergence of the ICESat-2 orbits provides spatially
dense observations in the pan-Arctic region. Water surface height processing is constrained by an
inland water mask (see Section 2.3.1 Water Masks).
1.3.2 Resolution
The ATLAS instrument transmits laser pulses at 10 kHz. At the nominal ICESat-2 orbit altitude of
500 km, this yields approximately one transmitted laser pulse every 0.7 meters along ground
Page 5 of 20National Snow and Ice Data Center
nsidc.org
```

---

