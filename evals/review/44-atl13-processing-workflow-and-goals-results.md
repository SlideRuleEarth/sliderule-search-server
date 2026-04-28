# Row 44 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `44-atl13-processing-workflow-and-goals-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL13 processing workflow and goals`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL13-specific; must not return ATL03 chunks

---

## 📚 docsearch results (top 5)

#### r1 — score 0.503

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl13sp
- **category:** `api_reference`
- **matched_tokens:** ['atl13']

**Full text:**

```
sliderule.icesat2. atl13sp ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs ATL13 subsetting in parallel on ATL13 data and returns measurement data. Unlike the atl13s function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. Parameters : parms ( dict ) â parameters used to configure ATL13 subsetting (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL13_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : ATL13 water measurements Return type : GeoDataFrame
```

#### r2 — score 0.416

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13', 'processing']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r3 — score 0.437

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['atl13', 'processing']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r4 — score 0.527

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** User Python Script
- **category:** `developer_guide`
- **matched_tokens:** ['atl13']

**Full text:**

```
If the user provided script needs to only be run against a single granule, then no additional steps are necessary - the script can be set to the ace API as is and the results processed. But if a user wants to execute the script against multiple granules and take advantage of the cluster computing capabilities of SlideRule, then the user must also write a Python program that manages the orchestration of those requests to SlideRule. For the ATL13 use case, the Python program used to manage the execution of the above script against all ATL13 granules can be found here: clients/python/utils/atl13_utils.py . This script queries CMR for a complete list of ATL13 granules and then creates a thread pool for workers that go through that list and issue ace API calls for each granule. The default concurrency is set to 8 in the script, but could easily be set to 100 for a private cluster of 10 nodes. As can be seen in the script, the results of each API call are added to a master lookup table (a dictionary of sets in Python) to produce the final lookup table that uses a reference ID to return a list of granules containing data with that ID.
```

#### r5 — score 0.443

- **url:** https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `developer_guide`
- **matched_tokens:** ['atl13']

**Full text:**

```
Given a user query, the ATL13 global database can be used to get a reference ID, and the reverse lookup table can be used to get all of the granules with data for that reference ID. The first option was the simplest but suffered from relying on CMR which is relatively slow and the possibility of having granules returned for other nearby bodies of water due to buffering on the along-track polygons CMR uses for their spatial queries. The second option would result in the best performance, but required every ATL13 granule to be read in order to build the reverse lookup table. The second option was chosen, and the Arbitrary Code Execution functionality in SlideRule was used to build the lookup table. Note SlideRule still supports temporal/spatial queries of CMR for ATL13; it is only when a user wants to use the reference ID, name, or containing coordinate that the lookup table option is used.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.519

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 17
- **matched_tokens:** ['processing', 'workflow']

**Full text:**

```
will be used), the latitude, longitude, and time tag for every ATLAS photon detection. These
values are the primary input to ATL24 but many ATL03 specific parameters are passed
through the processing workflow and attached to the ATL24 product for user utility and
convenience. ATL03 parameters are all defined in the dedicated Algorithm Theoretical
Basis Document and the Neumann et al., 2019 publication on the product (T. A. Neumann
et al. 2019b). Table 2 provides a broad look at independent processing stages within the
ATL24 workflow with the associated input data required to provide an understanding of
the interdependencies of the algorithm on initial data products and intermediate products
produced within the computational pipeline.
```

#### r2 — score 0.475

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.5 Goals of ICESat-2 Inland Water Body Height Data Products
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 27
- **matched_tokens:** ['atl13', 'goals']

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

#### r3 — score 0.428

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['processing', 'workflow']

**Full text:**

```
3 ATL24 Overview
3.1 ATL24 Data Workflow
Similar to other ICESat-2 Level 3a products, the input to the ATL24 pipeline is Level 2a,
Global geolocated point cloud data; ATL03 (T. A. Neumann et al. 2019b). ATL03 provides
every detected photon (signal and noise), with the calculated geolocation (geodetic latitude
and longitude) and associated parameters (operational) for each of ATLAS’s six beams. The
ATL03 product also provides signal confidence flags and estimated uncertainties at the photon
level. Gridded surface masks for land ice, sea ice, land, ocean and inland water products are
used within the L3b processing workflows to reduce the volume of data processed and guide
the production of these surface-specific, higher-level ICESat-2 data products. The ATL24
workflow requires a similar search approach to limit data processing to coastal and nearshore
environments that present a reasonable opportunity for capturing bathymetry. As such, a
gridded bathymetry mask based on possible retrievability was created to guide the processing
extents and is discussed in detail in section subsection 6.4. Figure 1 provides the overarching processing pipeline for ATL24, including the search
mask step to identify relevant ATL03 granules. The ATL24 algorithm’s main goal is to
provide a solution for robust, global bathymetric and sea surface signal extraction and
classification.
```

#### r4 — score 0.466

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['goals']

**Full text:**

```
Subsequent versions, ATL24.s and ATL24.p
will leverage the full capabilities of SlideRule to provide a subsetting service and on-demand
product generation service using a Python client, Javascript client, or web map GUI. This
functionality will enable users to optimize the output data product for their particular science
need, resulting in truly ”science-ready” data. The descriptions of each planned ATL24.x
product goals and client service plans are listed below:
6
```

#### r5 — score 0.506

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 4
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 4
- **matched_tokens:** ['workflow']

**Full text:**

```
Contents
1 Introduction 1
2 Context/Background 4
2.1 Historical Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3 ATL24 Overview 5
3.1 ATL24 Data Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2 Data Dissemination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.3 ATL24 ATBD Sections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4 Technical Considerations 8
4.1 Scientific Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.2 ATL24 Input Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.3 ATL24 Output Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.3.1 ATL24 Data Structure and Naming Conventions . . . . . . . . . . . 15
4.4 Classification Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.4.1 CoastNet Classification . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.4.2 BathyPathFinder Classification . . . . . . . . . . . . . . . . . . . . . 19
4.4.3 OpenOceans++ Classification . . . . . . . . . . . . . . . . . . . . . . 20
4.4.4 Median Filter Classification . . . . . . . . . . . . . . . . . . . . . . . 23
4.4.5 C-SHELPh Classification . . . . . . . . . . . . . . . . . . . . . . . . 24
4.4.6 Quantile Trees Classification . . . . . . . . . . . . . . . . . . . . . . . 26
4.4.7 Ensemble Classification . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.8 Blunder Detection . . . . . . . . 
```

---

