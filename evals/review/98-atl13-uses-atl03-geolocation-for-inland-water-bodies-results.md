# Row 98 results: nsidc / cross_product

> Auto-generated. Open this file alongside `98-atl13-uses-atl03-geolocation-for-inland-water-bodies-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL13 uses ATL03 geolocation for inland water bodies`
**Panel signature:** `03345191b5ad`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL13 builds on ATL03 geolocation

---

## 📚 docsearch results (top 5)

#### r1 — score 0.547

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'bodies', 'inland', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r2 — score 0.702

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl13', 'inland']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.675

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'inland', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r4 — score 0.586

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'inland', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r5 — score 0.449

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'bodies', 'uses', 'water']

**Full text:**

```
Given a user query, the ATL13 global database can be used to get a reference ID, and the reverse lookup table can be used to get all of the granules with data for that reference ID. The first option was the simplest but suffered from relying on CMR which is relatively slow and the possibility of having granules returned for other nearby bodies of water due to buffering on the along-track polygons CMR uses for their spatial queries. The second option would result in the best performance, but required every ATL13 granule to be read in order to build the reverse lookup table. The second option was chosen, and the Arbitrary Code Execution functionality in SlideRule was used to build the lookup table. Note SlideRule still supports temporal/spatial queries of CMR for ATL13; it is only when a user wants to use the reference ID, name, or containing coordinate that the lookup table option is used.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.646

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 2.4 Quality, Errors, and Limitations
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 11
- **matched_tokens:** ['atl03', 'atl13', 'bodies', 'inland', 'water']

**Full text:**

```
The algorithm provides an estimate of the along-track bottom topography and
water depth over the telemetry range, assuming favorable water clarity and relatively cloudless
skies.
2.3.2.4 Output
The overall method processes global inland water body height products and associated products
based on the ATL03 processing interval. The algorithm loops through the global inland water body
database organized within regional basins during each processing period, analyzing all ground
tracks of one water body before proceeding to the next. Along- and across-track data products are
computed for all new ground tracks observed for that water body since the previous processing
period. Inland water bodies are delineated by shapefiles defined in the ATL13 Inland Water Body
Shape mask. Quality, Errors, and Limitations
Data quality in this product depends largely on the precision of the georeferenced photons input
from ATL03 and associated products evaluated prior to use by the ATL13 algorithm. The overall
Page 10 of 20National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.627

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 2.3.1 Water Masks
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 9
- **matched_tokens:** ['atl03', 'atl13', 'bodies', 'inland', 'water']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
Figure 3. ATL03 Inland Water Processing Mask. The ATL13 algorithm that flags observations as water bodies
is only applied in the blue shaded areas (Jasinski et al., 2025).
This 0.1 km2 gridded mask was developed from a number of coastline and inland water databases
including the Global Self-consistent, Hierarchical, High-resolution Geography (GSHHG) coastlines
database and various lake shapefiles, including ephemeral lakes, permafrost extent, and custom
shapes created to close larger bays in locations not otherwise addressed.
The ATL13 Regional Basin Mask comprises polygons that represent principally the outline of
entire large river basins plus some adjacent intervening area. Each polygon contains all the lakes
and rivers within that river basin and logically organizes the ATLAS data used to produce the
hydrologic products (see figure below).
1 = Northern North America
2 = Southern North America
3 = Greenland
4 = South America
5 = Africa
6 = Europe
7 = Northern Asia
8 = Southern Asia
9 = Australia & Oceania
10 = Antarctica
Figure 4. ATL13 Regional Basin Mask (Jasinski et al., 2025).
Page 8 of 20National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.626

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 2.3.1 Water Masks
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 8
- **matched_tokens:** ['atl03', 'atl13', 'bodies', 'inland', 'water']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
2 DATA ACQUISITION AND PROCESSING
Background
ATLAS data have enabled understanding of high-latitude hydrology and the pan-Arctic water
balance. The ATL13 product helps determine impacts on freshwater fluxes into the Arctic Ocean,
melting snow, ocean salinity and circulation, methane distribution, ecosystem dynamics, and
geomorphology. The data has been widely used for scientific and application studies. Acquisition
ATL13 is primarily derived from geolocated, time-tagged photon heights and other parameters
passed from the ATLAS/ICESat-2 L2A Global Geolocated Photon Data (ATL03) product. Inputs
include precise latitude, longitude, and height for every received photon, plus applied geophysical
corrections such as Earth tides and atmospheric delays. Each photon is classified as signal or
background and by surface type (land ice, sea ice, land, ocean, and inland water). Processing
2.3.1 Water Masks
Water masks help organize the inland water data and constrain processing to only those land and
coastal regions that possess water bodies. See Section 3.4 of the ATBD (Jasinski et al.,
2025). ATL13 relies on three types of hydrologic masks:
• ATL03 Inland Water Processing Mask (applied to input data)
• ATL13 Regional Basin Mask
• ATL13 Inland Water Body Mask
The ATL03 Inland Water Processing Mask, shown in Figure, extracts data for analysis only from
those areas required for inland water analysis.
```

#### r4 — score 0.608

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 2.3.2.1 Inland Water Backscatter
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 10
- **matched_tokens:** ['atl03', 'atl13', 'bodies', 'inland', 'water']

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

#### r5 — score 0.579

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 3.4.1 The ATL13 Inland Water Body Mask
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 49
- **matched_tokens:** ['atl03', 'atl13', 'bodies', 'inland', 'water']

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

---

