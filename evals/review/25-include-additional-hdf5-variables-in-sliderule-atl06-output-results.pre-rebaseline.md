# Row 25 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `25-include-additional-hdf5-variables-in-sliderule-atl06-output-review.md` —
> verdicts go there, this side is read-only.

**Query:** `include additional HDF5 variables in sliderule atl06 output`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/how_tos/ancillary_fields.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ancillary fields how-to

---

## 📚 docsearch results (top 5)

#### r1 — score 0.562

- **url:** https://docs.slideruleearth.io/api_reference/h5.html
- **title:** h5
- **section:** h5x
- **category:** `api_reference`
- **matched_tokens:** ['hdf5', 'sliderule', 'variables']

**Full text:**

```
sliderule.h5. h5x ( variables , resource , asset , groups = None , col = None , startrow = None , numrows = None , index_column = None , time_column = None , x_column = None , y_column = None , z_column = None , crs = None , session = None ) [source] Builds a DataFrame from an HDF5 file where each variable in variables is a column. The groups parameter is used to create datasets from multiple groups within the file. For example, if groups = ["/data/r1", "/data/r2", "/data/r3"] and datasets = ["x", "y"] then the dataframe will have two columns: âxâ and âyâ that are populated from six datasets within the file: â/data/r1/xâ, â/data/r2/xâ, âdata/r3/xâ, and â/data/r1/yâ, â/data/r2/yâ, âdata/r3/yâ Parameters : variables ( list ) â list of variables to read from each group resource ( str ) â HDF5 filename asset ( str ) â data source asset groups ( list ) â list of full paths to the groups to read from the file Returns : A pandas dataframe of the data read from the file Return type : DataFrame Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r2 — score 0.557

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/ancillary_fields.html
- **title:** Including Ancillary Fields
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['hdf5', 'include', 'sliderule']

**Full text:**

```
The ATL03 granules include data associated with the photons in different subgroups inside the HDF5 file. SlideRule currently supports including ancillary fields from three subgroups inside those granules: gtxx/geolocation gtxx/geophys_corr gtxx/heights When an atl03sp or at06p processing request specifies ancillary fields, SlideRule reads those fields from the ATL03 granules, subsets them to the region of interest, and correlates them to the dynamically generated photon segment (called and âextentâ in the code) they belong to. The result is a GeoDataFrame with a column for each ancillary field populated by the value associated with each photon for atl03sp requests, and elevation for atl06p requests. Note, including ancillary fields in a processing request will increase the amount of time it takes for the request to be processed, and also the amount of data returned, so it should only be used when the fields are needed by the end user.
```

#### r3 — score 0.448

- **url:** https://docs.slideruleearth.io/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Import the client package
- **category:** `user_guide`
- **matched_tokens:** ['additional', 'hdf5', 'include', 'output', 'sliderule', 'variables']

**Full text:**

```
The majority of the SlideRule Python client functionality is found in the sliderule module; but there are other modules as well that include additional features and mission specific functions and variables. To import the client and start using Sliderule, you can use the following code: from sliderule import sliderule Here is a list of modules in the SlideRule Python client. sliderule Core functionality: initialization and configuration, making requests, processing an area of interest. earthdata Query for resources using CMR, CMR-STAC, TNM, and other services. h5 Directly read HDF5 data from the cloud using the server-side H5Coro implementation. raster Sample and subset supported raster datasets icesat2 Issue processing requests for ICESat-2 standard and custom data products gedi Issue processing requests for GEDI standard and custom data products io Read and write SlideRule output in different formats ipysliderule Widgets and routines for building interactive interfaces to SlideRule in a Jupyter notebook If you wanted to use multiple modules from the SlideRule Python client, you could use the following code as an example: from sliderule import sliderule , earthdata , icesat2
```

#### r4 — score 0.535

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06s
- **category:** `api_reference`
- **matched_tokens:** ['atl06', 'hdf5', 'sliderule']

**Full text:**

```
sliderule.icesat2. atl06s ( parm , resource ) [source] Subsets ATL06 data given the polygon and time range provided and returns elevations Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) resource ( str ) â ATL06 HDF5 filename Returns : ATL06 elevations Return type : GeoDataFrame
```

#### r5 — score 0.546

- **url:** https://docs.slideruleearth.io/assets/atl13_access.html
- **title:** Accessing ATL13 data using lake names, reference ids, and contained coordinates
- **section:** Accessing ATL13 data using lake names, reference ids, and contained coordinates
- **category:** `tutorial`
- **matched_tokens:** ['sliderule', 'variables']

**Full text:**

```
SlideRule provides an Asset Metadata Service to lookup ATL13 granules using different variables: reference id lake name coordinate within the lake SlideRule can also be used to directly subset ATL13 using the above variables. [1]: # Imports from sliderule import sliderule # Setup sliderule . init ( verbose = True ) [1]: True
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.479

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['output', 'sliderule']

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

#### r2 — score 0.367

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 53
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 53
- **matched_tokens:** ['atl06', 'hdf5']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
929 4 ATL06 DATA PRODUCT DESCRIPTION
930 Here we describe how the parameters appear in the ATL06 product. The ATL06 parameters are
931 arranged by beam, and within each beam in a number of groups and subgroups. Where
932 parameter descriptions in the ATL06 data dictionary are considered adequate, they are not
933 repeated in this document.
934 4.1 Data Granules
935 ATL06 data are provided as HDF5 files. The HDF format allows several datasets of different
936 spatial and temporal resolutions to be included in a file. ATL06 files contain data primarily at the
937 single-segment resolution, divided into different groups to improve the conceptual organization
938 of the files. Each file contains data from a single cycle and a single RGT.
939 Within each file there are six top-level groups, each corresponding to data from GT: gt1l, gt1r,
940 gt2l, etc. The subgroups within these gtxx groups are segment_quality, land_ice_segments, and
941 residual_histogram.
942 In the segment_quality group, the data are nearly dense, providing signal-selection and location
943 information for every segment attempted (i.e. those that contain at least one ATL03 PE) in the
944 granule, at the 20-meter along-track segment spacing.
```

#### r3 — score 0.363

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.5 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 10
- **matched_tokens:** ['hdf5', 'variables']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Three HDF5 dimension scales are stored at the top level alongside the data groups—
ds_geosegments, ds_metrics, and ds_surf_type—which index the within-land geosegments,
surface type, and metrics arrays. For details about how the parameters are organized in the ATL08 product, see "Section 2 | ATL08:
Data Product" in the ATBD for ATL08.
1.2.5 Naming Convention
Data files utilize the following naming convention:
ATL08_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr].h5
Example:
ATL08_20181014001049_02350102_006_01.h5
The following table describes the file naming convention variables:
Table 3. File Naming Convention Variables and Descriptions
Variable Description
ATL08 ATLAS/ICESat-2 L3A Land and Vegetation Height product
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit Reference Ground Track number. The ICESat-2 mission has 1,387
RGTs, numbered from 0001 to 1387.
cc Cycle Number. Each of the 1,387 RGTs is targeted in the polar regions once every
91 days. The cycle number tracks the number of 91-day periods that have elapsed
since ICESat-2 entered the science orbit.
ss Orbital segment (region) number (see Figure 3). ATL08 data files cover
approximately 1/14th of an orbit. Orbital segment numbers range from 01–14.
vvv_rr Version and revision number.*
From time to time, NSIDC receives reprocessed granules from our data provider.
```

#### r4 — score 0.350

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 32
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 32
- **matched_tokens:** ['additional', 'atl06']

**Full text:**

```
The
427 subset of segments with ATL06_quality_summary = 0 are unlikely to contain blunders due to
428 signal-finding errors. This choice of parameters may reject useful elevations collected over
429 rough, strongly sloping, or low-reflectivity surfaces and under clouds so obtain more height
430 estimates, users may need to examine additional parameters in ATL06, or regenerate a similar
431 flag for themselves based on a less-stringent set of parameters.
432 A variety of data flags are available to indicate why a particular segment does not have a
433 reported height parameter. In many cases, the strong-beam segment in a pair will have a
434 reported height, and the weak beam will not; in these cases, a full record is available for the
435 weak-beam segment, providing all parameters up to the step where the fitting process failed. In
436 cases where neither the strong nor the weak beam returned a surface height, the segment_quality
437 group provides the signal_selection_source parameter, which will show a value of 3 if all signal-
438 selection strategies failed.
```

#### r5 — score 0.274

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['additional', 'sliderule']

**Full text:**

```
used alone or in combination with total propagated uncertainty (TPU) values to filter the
data. Figure 1: ATL24 flow diagram of computational architecture
3.2 Data Dissemination
The implementation architecture chosen for ATL24 r001 will follow the standard approach for
the dissemination of the ICESat-2 mission products through the National Snow and Ice Data
Center (NSIDC). However, in the last few years NSIDC has pushed the products to the cloud
for modernized access to the data, which will be an additional pathway to ATL24 data access
for the scientific community. Both means of access will provide capabilities for geographical
and temporal sub-setting to the user. Additionally, for ATL24 specifically, there is also a
planned, parallel capacity for allowing on-demand and customized, science-ready bathymetry
product from ATL03 granules via SlideRule, a public web application programming interface
(API) for processing of science data in the cloud (Shean et al. 2023). ATL24 will eventually
present a family of data products, which collectively will be referred to as ATL24.x. This
ATBD describes the version referred to as the ”gold standard” version, ATL24.g, hosted by
NSIDC and available in Earthdata cloud, with the metadata for the granules registered in
NASA’s Common Metadata Repository (CMR).
```

---

