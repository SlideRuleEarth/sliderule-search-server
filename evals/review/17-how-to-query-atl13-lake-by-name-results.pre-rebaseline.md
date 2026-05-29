# Row 17 results: docsearch / example

> Auto-generated. Open this file alongside `17-how-to-query-atl13-lake-by-name-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to query atl13 lake by name`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl13x`
  - `4. atl13`
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: assets/atl13_access.html removed; user_guide section on atl13x is closest substitute

---

## 📚 docsearch results (top 5)

#### r1 — score 0.599

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'lake', 'name', 'query']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r2 — score 0.762

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r3 — score 0.669

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.422

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-14-00.html
- **title:** Release v4.14.x
- **section:** New/Improved Functionality
- **category:** `release_notes`
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
Arbitrary Code Execution - /source/ace API for executing user supplied lua scripts; only available on private clusters. Asset Metadata Service - /manager/ams API for querying metadata directly from SlideRule; only ATL13 currently supported. ATL13 - /source/atl13x API for subsetting the ATL13 standard data product; in addition to normal temporal/spatial subsetting requests, SlideRule also supports subsetting based on the ATL13 reference ID, lake name, and coordinate within a body of water.
```

#### r5 — score 0.373

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'lake', 'name', 'query']

**Full text:**

```
Given a user query, the ATL13 global database can be used to get a reference ID, and the reverse lookup table can be used to get all of the granules with data for that reference ID. The first option was the simplest but suffered from relying on CMR which is relatively slow and the possibility of having granules returned for other nearby bodies of water due to buffering on the along-track polygons CMR uses for their spatial queries. The second option would result in the best performance, but required every ATL13 granule to be read in order to build the reverse lookup table. The second option was chosen, and the Arbitrary Code Execution functionality in SlideRule was used to build the lookup table. Note SlideRule still supports temporal/spatial queries of CMR for ATL13; it is only when a user wants to use the reference ID, name, or containing coordinate that the lookup table option is used.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.464

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 3.4.1 The ATL13 Inland Water Body Mask
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 49
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
Figure 3-3 ATL13 Inland Water Body Shape Mask for North America Shape file (Jasinski Stoll et al., 2019)
Each lake is identified by number, lat/long, and local name if available from the HydroLAKES
database. It is estimated that the multi-beam ATL13 ICESat-2 coverage contains over 1.4 M
water bodies, allowing the overpass of about 650 lakes ≥ 100km2, of which 50% are in Canada,
and 25% in Eurasia. For lakes ≥ 0.1km2, the estimate is about 1.42M lakes. With 100 photon
along-track aggregation there is the potential to record heights of the more numerous smaller
26
Release 007, January 31, 2025
```

#### r2 — score 0.411

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 1.2.2.3 METADATA
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 4
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
See "4.7.1.2
| Water Body Reference Identification Scheme" in the ATL13 ATBD (Jasinski et al., 2025):
• inland_water_body_type: water body type (1 = lake, 2 = known reservoir, 4 = ephemeral
water, 5 = river, 6 = estuary or bay, 7 = coastal water)
• inland_water_body_size: water body size; A = area in km2 (0 = not assigned, 1 =
A>10,000, 2 = 10,000>A≥1,000, 3 = 1,000>A≥100, 4 = 100>A≥10, 5 = 10>A≥1, 6 =
1>A≥0.1, 7 = 0.01>A)
• inland_water_body_source: source of inland water body shape (1 = HydroLAKES, 2 =
Global Lakes and Wetlands Database, 3 = Named Marine Water Bodies, 4 = GSHHG
Shoreline, 5 = Global River Widths from Landsat)
• inland_water_body_id: identifying signature of an individual inland water body
The gt[x] groups also contain standard deviation, subsurface signal (532 nm) attenuation,
significant wave height, wind speed, and coarse depth to bottom topography.
1.2.2.3 METADATA
ISO19115 structured summary metadata for the granule, including content that describes the
required geospatial information. The version(s) of the input files are included in the file name
attribute under the Lineage group. Page 3 of 20National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.447

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.7.1.2 Water Body Reference Identification Scheme:
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 72
- **matched_tokens:** ['atl13', 'lake']

**Full text:**

```
ATL13 water body types are defined as: Type 1 = lake; Type 2 =
known reservoir; Type 3 = Reserved for future use; Type 4 = Ephemeral water; Type 5 = river;
Type 6 = transitional water (estuary or bay); Type 7 = transitional water (coastal); Type 8 =
49
Release 007, January 31, 2025
```

#### r4 — score 0.428

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.1 Overall Approach
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 51
- **matched_tokens:** ['atl13', 'lake']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
shaded regions in Fig 3-5 below, is one of efficiency. The implementation of ATL13 algorithm
draws only on ICESat-2 observations that have been flagged as falling within an ATL03 Inland
Water Mask. The data base of the ATL03 Inland Water Mask does not identify the type of water
body, only that one exists.
Figure 3-5 ATL03 Inland Water Mask (gridded, non-contiguous).
The ATL03 Inland Water Mask is a high resolution gridded mask developed to extract data for
analysis from only those areas required for inland water analysis. The ATL03 mask was created
by overlaying the ATL13 inland water body shape file mask, developed by the ATL13 team,
onto the global grid. It has been developed from a number of coastline and inland water
databases including the Global Self-consistent, Hierarchical, High-resolution Geography
(GSHHG) coastlines, various lake database shapefiles including ephemeral lakes, permafrost
extent, and a custom set of shapes to close gaps in larger bays where not otherwise included. (ref:
ATL03 ATBD).
4.0 ALGORITHM THEORY
4.1 Overall Approach
ATLAS observations provide information on both the altimetry and the backscatter of the water
surface and subsurface. Of principal interest for ATL13 is the altimetry that will provide
information on along track height statistics. However, knowledge of backscatter also will
28
Release 007, January 31, 2025
```

#### r5 — score 0.383

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 2.3.2.1 Inland Water Backscatter
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 10
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
The ATL13 Inland Water Body Mask identifies ICESat-2 crossings over individual water bodies. It
was designed to delineate the shape and spatial distribution of contiguous individual water bodies,
such as lakes, reservoirs, and rivers, and is applied as a shapefile—unlike the gridded ATL03 mask
flag described above. The shape mask consists of polygon shapefiles that each represent an entire
single lake, reservoir, river segment and tributaries, bay, or 7 km wide coast segment. An
approximately 100 m buffer is extended over land to clearly distinguish the land/water
interface. Each water body is identified by a unique number, latitude and longitude, and local name
if available.
2.3.2 Surface Height Algorithm
The goal of ATL13 is to estimate the mean water surface height in short, statistically
representative segments (75–100 signal photons) for each ATLAS beam that crosses a water body
in the along-track direction. Thus, computing inland water heights requires distances of about 50 to
100 m, depending on atmospheric, solar, and water conditions. In addition, although the majority of
the signal photons that return to ATLAS from a given water body are reflected from the surface,
typically a percentage comprise subsurface backscatter.
```

---

