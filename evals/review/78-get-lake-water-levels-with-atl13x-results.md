# Row 78 results: docsearch / example

> Auto-generated. Open this file alongside `78-get-lake-water-levels-with-atl13x-review.md` —
> verdicts go there, this side is read-only.

**Query:** `get lake water levels with atl13x`
**Panel signature:** `ed7fa111e41f`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `4. atl13`
  - `4.1 inland lake`
- **expected_pages:** (none)
- **notes:** ATL13 lake query

---

## 📚 docsearch results (top 5)

#### r1 — score 0.686

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13x', 'lake', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.741

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['lake']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.711

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['lake', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r4 — score 0.591

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['lake', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r5 — score 0.475

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-14-00.html
- **title:** Release v4.14.x
- **section:** New/Improved Functionality
- **category:** `release_notes`
- **matched_tokens:** ['atl13x', 'lake', 'water']

**Full text:**

```
Arbitrary Code Execution - /source/ace API for executing user supplied lua scripts; only available on private clusters. Asset Metadata Service - /manager/ams API for querying metadata directly from SlideRule; only ATL13 currently supported. ATL13 - /source/atl13x API for subsetting the ATL13 standard data product; in addition to normal temporal/spatial subsetting requests, SlideRule also supports subsetting based on the ATL13 reference ID, lake name, and coordinate within a body of water.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.592

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.9.2.2 Assessment and Validation Activities
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 89
- **matched_tokens:** ['lake', 'levels', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Figure 4-10 Examples of potential collaborative calibration/validation sites (red circles) in Alaska.
c) Mid-Latitude Lakes and Reservoirs
Assessment sites include collaboration a several sites with various groups including the Great
Lakes (JALBTCX, Illinois State geological Survey), Lakes Mead (US Bureau of Reclamation),
Lake Fort Peck (USACE), Lake Tahoe and Western Lake Erie (Kent State). For the Great
Lakes, ATL13 is collaborating with efforts to measure Great Lakes surface water conditions at
the locations shown below.
Figure 4-11 Lake level gauge and monitoring stations on the Great Lakes.
https://www.glerl.noaa.gov/data/wlevels/levels.html#monitoringNetwork
d) Transitional Water Bodies (Estuaries, Bays, Near Shore Coasts)
Principal areas would include the Chesapeake Bay, and the estuaries of the
Mississippi/Atchafalaya River deltas, Everglades, Mackenzie River, and Yukon River, together
66
Release 007, January 31, 2025
```

#### r2 — score 0.651

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 3.4.1 The ATL13 Inland Water Body Mask
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 49
- **matched_tokens:** ['lake', 'water']

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

#### r3 — score 0.605

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.7.1.2 Water Body Reference Identification Scheme:
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 72
- **matched_tokens:** ['lake', 'water']

**Full text:**

```
ATL13 water body types are defined as: Type 1 = lake; Type 2 =
known reservoir; Type 3 = Reserved for future use; Type 4 = Ephemeral water; Type 5 = river;
Type 6 = transitional water (estuary or bay); Type 7 = transitional water (coastal); Type 8 =
49
Release 007, January 31, 2025
```

#### r4 — score 0.545

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 5.4 ATL13 Inland Surface Water Output Variables
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 165
- **matched_tokens:** ['get', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Name Units Description ATBD
Source
segment_geoi meters Value to convert segment geoid heights from the 5.3.5 (A)
d_free2mean mean-tide system to the tide-free system. Subtract
this value from mean-tide system segment_geoid (on
ATL13) to get geoid heights in the tide-free system. Applicable value at reporting location for all short
segment statistics.
segment_tide_ meters Segment rate value to convert solid earth tide from 5.3.5 (A)
earth_free2me the tide-free system that was applied in ATL03 to
an photon heights to the ht_water_surf to the mean-tide
system. Subtract value from ht_water_surf to
reference it in the mean-tide system.
```

#### r5 — score 0.561

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.9.2.1 External Products Available for Monitoring ATL13 Data
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 86
- **matched_tokens:** ['levels', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
organizations. Data product quality is achieved through monitoring, assessment and validation at
various levels of effort depending on available resources. The overall approach is i) to compare
ATL13 data products with in situ data and satellite radar altimetry where available, ii) evaluate
several components of the ATL13 algorithm through threshold monitoring with model
diagnostics, and iii) conduct in situ validation and calibration when resources are available or
synergistic field opportunities arise. Evaluation can be conducted over all ATL13 Inland Water
Body types including lakes, reservoirs, rivers, estuaries and near shore coasts. Sites are located
primarily in the US and North America, but also at several international sites. Every effort is
made to be aware of, and participate in, other sponsored field programs by NASA and other
agencies including satellite mission CAL/VAL plan.
4.9.2.1 External Products Available for Monitoring ATL13 Data
Monitoring refers to active and continuous evaluation of ICESat-2 data-product parameters,
primarily through data visualizations and threshold monitoring. Monitoring can occur through
comparison of ATL13 time series data plots with other independent data.
```

---

