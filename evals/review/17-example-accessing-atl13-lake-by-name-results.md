# Row 17 results: docsearch / example

> Auto-generated. Open this file alongside `17-example-accessing-atl13-lake-by-name-review.md` —
> verdicts go there, this side is read-only.

**Query:** `example accessing atl13 lake by name`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/atl13_access.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl13 access tutorial

---

## 📚 docsearch results (top 5)

#### r1 — score 0.585

- **url:** https://docs.slideruleearth.io/assets/atl13_access.html
- **title:** Accessing ATL13 data using lake names, reference ids, and contained coordinates
- **section:** Accessing ATL13 data using lake names, reference ids, and contained coordinates
- **category:** `tutorial`
- **matched_tokens:** ['accessing', 'atl13', 'lake', 'name']

**Full text:**

```
SlideRule provides an Asset Metadata Service to lookup ATL13 granules using different variables: reference id lake name coordinate within the lake SlideRule can also be used to directly subset ATL13 using the above variables. [1]: # Imports from sliderule import sliderule # Setup sliderule . init ( verbose = True ) [1]: True
```

#### r2 — score 0.552

- **url:** https://docs.slideruleearth.io/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'example', 'lake', 'name']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r3 — score 0.738

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r4 — score 0.548

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'lake']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r5 — score 0.477

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-14-00.html
- **title:** Release v4.14.x
- **section:** New/Improved Functionality
- **category:** `release_notes`
- **matched_tokens:** ['atl13', 'lake', 'name']

**Full text:**

```
Arbitrary Code Execution - /source/ace API for executing user supplied lua scripts; only available on private clusters. Asset Metadata Service - /manager/ams API for querying metadata directly from SlideRule; only ATL13 currently supported. ATL13 - /source/atl13x API for subsetting the ATL13 standard data product; in addition to normal temporal/spatial subsetting requests, SlideRule also supports subsetting based on the ATL13 reference ID, lake name, and coordinate within a body of water.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.467

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

#### r2 — score 0.422

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

#### r3 — score 0.428

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 3.4.1 The ATL13 Inland Water Body Mask
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 49
- **matched_tokens:** ['atl13', 'example', 'lake']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
3.4.1 The ATL13 Inland Water Body Mask
The ATL13 Inland Water Body Shape Mask facilitates identification of ICESat-2 crossings over
individual water bodies. It delineates the shape and spatial distribution of contiguous individual
water bodies. These include a composite of lakes, reservoirs, rivers, and transitional waters
including estuaries and bays, and near shore coastal waters assembled by the inland water team
for use in the ATL13 algorithm. An ATL13 Inland Water Body Shape Mask is employed as a
shape-file (E.g. HydroLAKES, Messager et al. (2016); Lehner and Messager (2016 ), Global
River Width from Landsat (GRWL) (Allen and Pavelsky, 2018); Named Marine Water Bodies,
ESRI), unlike the ATL03 flag above which is a gridded product. The mask consists of polygons,
each representing either an entire single lake or reservoir, 7-km wide coast segment, bay, or river
segment including its tributaries. The ATL13 Inland Water Body Shape Mask includes an
approximately 100m buffer extended beyond the lake over the land to facilitate the identification
of the land/water interface. An example of ATL13 Inland Water Body Mask looks like for North
America (Jasinski, Stoll et al., 2019) is shown in Figure 3-3 below.
```

#### r4 — score 0.500

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

#### r5 — score 0.407

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

---

