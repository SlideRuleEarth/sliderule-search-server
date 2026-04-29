# Row 37 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `37-atl13-file-naming-convention-granule-filename-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL13 file naming convention granule filename`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **expected_sections:**
  - `file naming`
  - `naming convention`
- **expected_pages:** (none)
- **notes:** ATL13 user guide file naming

---

## 📚 docsearch results (top 5)

#### r1 — score 0.422

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl13s
- **category:** `api_reference`
- **matched_tokens:** ['atl13', 'filename']

**Full text:**

```
sliderule.icesat2. atl13s ( parm , resource ) [source] Subsets ATL13 data given the polygon and time range provided and returns measurements Parameters : parms ( dict ) â parameters used to configure ATL13 subsetting (see Parameters ) resource ( str ) â ATL13 HDF5 filename Returns : ATL13 water measurements Return type : GeoDataFrame
```

#### r2 — score 0.437

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'granule']

**Full text:**

```
Ancillary data returned from the atl13x endpoint comes from the {beam} group of the ATL13 granules. atl13_fields : fields in the beam group of the ATL13 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "ice_flag" ], } gdf = sliderule . run ( "atl13x" , parms )
```

#### r3 — score 0.381

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** User Lua Script
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'file', 'granule']

**Full text:**

```
-- 1. import modules local json = require ( "json" ) -- 2. create an h5coro object from the granule to be processed local asset = core . getbyname ( "icesat2-atl13" ) local h5obj = h5coro . file ( asset , "ATL13_20250302152414_11692601_007_01.h5" ) -- 3. read the reference id out of each of the 6 beams local column_gt1l = h5obj : readp ( "gt1l/atl13refid" ) local column_gt1r = h5obj : readp ( "gt1r/atl13refid" ) local column_gt2l = h5obj : readp ( "gt2l/atl13refid" ) local column_gt2r = h5obj : readp ( "gt2r/atl13refid" ) local column_gt3l = h5obj : readp ( "gt3l/atl13refid" ) local column_gt3r = h5obj : readp ( "gt3r/atl13refid" ) -- 4. helper function that puts reference ids into a table local function count ( results , column ) local values = column : unique () for k , _ in pairs ( values ) do results [ tostring ( k )] = true end end -- 5. combine the reference ids into a single table local results = {} count ( results , column_gt1l ) count ( results , column_gt1r ) count ( results , column_gt2l ) count ( results , column_gt2r ) count ( results , column_gt3l ) count ( results , column_gt3r ) -- 6. return the results as json return json . encode ( results ) The above user provided script was sent to the SlideRule ace api to execute on a private cluster (in this case, the cluster was the developers cluster). For the purposes of this article, Iâve annotated the script with comments to assist in the explanation below.
```

#### r4 — score 0.391

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'granule']

**Full text:**

```
Given a user query, the ATL13 global database can be used to get a reference ID, and the reverse lookup table can be used to get all of the granules with data for that reference ID. The first option was the simplest but suffered from relying on CMR which is relatively slow and the possibility of having granules returned for other nearby bodies of water due to buffering on the along-track polygons CMR uses for their spatial queries. The second option would result in the best performance, but required every ATL13 granule to be read in order to build the reverse lookup table. The second option was chosen, and the Arbitrary Code Execution functionality in SlideRule was used to build the lookup table. Note SlideRule still supports temporal/spatial queries of CMR for ATL13; it is only when a user wants to use the reference ID, name, or containing coordinate that the lookup table option is used.
```

#### r5 — score 0.455

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v05-01-00.html
- **title:** Release v5.1.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['atl13']

**Full text:**

```
v5.1.0 - Fixed atl13 and atl24 access example notebooks to use latest earthdata endpoint. v5.1.0 - b486378 - Fixed name filter support in AMS
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.582

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.2.3 File Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 5
- **matched_tokens:** ['atl13', 'convention', 'file', 'granule', 'naming']

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

#### r2 — score 0.552

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.2.3 File Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 5
- **matched_tokens:** ['atl13', 'convention', 'file', 'granule', 'naming']

**Full text:**

```
Because ATL13 data files
span four full orbits, the region number is always set to 01.
2Occasionally, NSIDC receives reprocessed granules from our data provider. These granules have the
same file name as the original (i.e., date, time, ground track, cycle, and region number), but the revision
number has been incremented. Although NSIDC deletes the superseded granule, the process can take
several days. If you encounter multiple granules with the same file name, please use the granule with the
highest revision number. Page 4 of 20National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.464

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 35
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 35
- **matched_tokens:** ['convention', 'file', 'granule', 'naming']

**Full text:**

```
592 all height fields. In the event that there are more than 50 classed photons, but a terrain
593 height cannot be determined due to an insufficient number of ground photons, (e.g.
594 lack of photons penetrating through dense canopy), the only reported terrain height
595 will be the interpolated surface height.
596 The ATL08 product will be produced per granule based on the ATL03 defined
597 regions (see Figure 2.2). Thus, the ATL08 file/name convention scheme will match
598 the file/naming convention for ATL03 –in attempt for reducing complexity to allow
599 users to examine both data products.
600
601 Figure 2.2. ATL03 granule regions; graphic from ATL03 ATBD (Neumann et al.).
602 The ATL08 product additionally has its own internal regions, which are
603 roughly assigned by continent, as shown by Figure 2.3. For the regions covering
604 Antarctica (regions 7, 8, 9, 10) and Greenland (region 11), the ATL08 algorithm will
605 assume that no canopy is present. These internal ATL08 regions will be noted in the
606 ATL08 product (see parameter atl08_region in Section 2.4.24). Note that the regions
607 for each ICESat-2 product are not the same.
35
```

#### r4 — score 0.518

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Classification Algorithms
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 22
- **matched_tokens:** ['convention', 'file', 'granule', 'naming']

**Full text:**

```
4.3.1 ATL24 Data Structure and Naming Conventions
The naming and internal organization of the final HDF5 file for each ATL24 granule will
match the conventions used on the rest of the project. Each granule will also have the naming
convention similar to the other ICESat-2 data products. Each variable within the name
(place holders) are described in Table 5. Please note that there are two sets of version and
revision numbers that represent both ATL03 input version and revision and then the version
and revision of ATL24. ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr]_[vvv_rr].h5
Table 5: ATL24 naming convention
Variable Description
ATL24 ICESat-2 Level 3 Global nearshore and coastal bathymetry
ATLAS/ICESat-2 Level 3a calibrated backscatter profiles and at- ATL09 mopsheric layer characteristics
yyyymmdd Year, month and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC). Four digit Reference Ground Track number. The ICESat-2 mission tttt has 1,387 RGTs, numbered from 0001 to 1387. Cycle Number. Each of the 1387 RGTs is targeted in the polar
regions once every 91 days. The cycle number tracks the number of cc 91-day periods that have elapsed since ICESat-2 entered the science
orbit. Segment number. ATL03 data files are segmented into approxi-
ss mately 1/14th of an orbit. Segment numbers range from 01-14.
```

#### r5 — score 0.462

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.3 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 5
- **matched_tokens:** ['convention', 'file', 'granule', 'naming']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
• x_atc: along-track distance (m) in a segment projected to the ellipsoid of the received
photon
• y_atc: across-track distance (m) projected to the ellipsoid of the received photon from the
reference ground track (RGT)
1.2.2.3 metadata
Query metadata (geospatial and temporal extents), algorithm run times, SlideRule metadata, and
granule-level statistics.
1.2.2.4 orbit_info
Orbit parameters that are constant for a granule, such as the RGT number, cycle, and spacecraft
orientation.
1.2.3 Naming Convention
Data files utilize the following naming convention:
ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[VVV_RR]_[vvv_rr].h5
Example:
ATL24_20230704193540_02232008_006_02_001_01.h5
The following table describes the file naming convention variables:
Table 1. File Naming Convention Variables and Descriptions
Variable Description
ATL24 ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit RGT number. The ICESat-2 mission has 1,387 RGTs, numbered from
0001 to 1387.
cc Cycle number. The cycle number tracks the number of 91-day periods that have
elapsed since ICESat-2 entered the science orbit.
ss Region number. ATL03 data files are segmented into approximately 1/14th of an
orbit. Region numbers range from 01 to 14. Note that some regions may not be
available.
```

---

