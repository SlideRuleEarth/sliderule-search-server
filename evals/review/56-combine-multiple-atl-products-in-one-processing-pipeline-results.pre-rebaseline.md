# Row 56 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `56-combine-multiple-atl-products-in-one-processing-pipeline-review.md` —
> verdicts go there, this side is read-only.

**Query:** `combine multiple ATL products in one processing pipeline`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/xseries.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
  - https://docs.slideruleearth.io/assets/atl24_access.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** multi-product workflow; atl24 tutorial shows combining ATL03 + ATL24

---

## 📚 docsearch results (top 5)

#### r1 — score 0.320

- **url:** https://docs.slideruleearth.io/assets/atl24_access.html
- **title:** Subsetting and filtering ATL24 data
- **section:** (5) Combine ATL03 Filters with ATL24 Classification
- **category:** `tutorial`
- **matched_tokens:** ['combine', 'processing']

**Full text:**

```
[21]: parms = { "atl24" : { "class_ph" : [ "unclassified" , "sea_surface" , "bathymetry" ] }, "cnf" : 2 , "yapc" : { "version" : 0 , "score" : 100 }, "beams" : "gt3r" , "rgt" : 202 , "cycle" : 12 } gdf5 = sliderule . run ( "atl03x" , parms , aoi = aoi ) request <AppServer.64297> retrieved 1 resources Starting proxy for atl03x to process 1 resource(s) with 1 thread(s) request <AppServer.65199> on ATL03_20210706203010_02021201_006_01.h5 generated dataframe [gt3r] with 20773 rows and 15 columns Successfully completed processing resource [1 out of 1]: ATL03_20210706203010_02021201_006_01.h5 Writing arrow file: /tmp/tmphli10s8z Closing arrow file: /tmp/tmphli10s8z [22]: gdf5 [22]: region gt spacecraft_velocity atl24_class solar_elevation atl24_confidence yapc_score rgt ph_index height spot x_atc y_atc srcid cycle atl03_cnf background_rate quality_ph geometry time_ns 2021-07-06 20:35:11.530663168 1 60 7118.208496 0 36.057114 0.000000 63 202 12915866 -22.051737 1 2.146466e+06 -3246.126465 0 12 4 1202043.625 0 POINT (-69.53821 19.31118) 2021-07-06 20:35:11.530963200 1 60 7118.208496 0 36.057114 0.000000 153 202 12915888 -25.586315 1 2.146468e+06 -3246.155029 0 12 4 1202043.625 0 POINT (-69.53821 19.31120) 2021-07-06 20:35:11.531063040 1 60 7118.208496 0 36.057114 0.000000 138 202 12915897 -25.111528 1 2.146469e+06 -3246.154785 0 12 4 1202043.625 0 POINT (-69.53821 19.31120) 2021-07-06 20:35:11.531163136 1 60 7118.208496 0 36.057114 0.000000 78 202 12915898 -14.752754 1 2.146469e+06 -
```

#### r2 — score 0.274

- **url:** https://docs.slideruleearth.io/developer_guide/why_sliderule.html
- **title:** Why SlideRule
- **section:** Why Develop SlideRule?
- **category:** `developer_guide`
- **matched_tokens:** ['one', 'products']

**Full text:**

```
For example, one university could build a data service that leverages the public API of another universityâs data service to produce a combined data product without ever having to rehost the other universityâs data. From a technical implementation standpoint, the two universities remain distinct and decentralized entities, yet by providing their data as a service, they allow for combined data products.
```

#### r3 — score 0.388

- **url:** https://docs.slideruleearth.io/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** User Python Script
- **category:** `developer_guide`
- **matched_tokens:** ['multiple']

**Full text:**

```
If the user provided script needs to only be run against a single granule, then no additional steps are necessary - the script can be set to the ace API as is and the results processed. But if a user wants to execute the script against multiple granules and take advantage of the cluster computing capabilities of SlideRule, then the user must also write a Python program that manages the orchestration of those requests to SlideRule. For the ATL13 use case, the Python program used to manage the execution of the above script against all ATL13 granules can be found here: clients/python/utils/atl13_utils.py . This script queries CMR for a complete list of ATL13 granules and then creates a thread pool for workers that go through that list and issue ace API calls for each granule. The default concurrency is set to 8 in the script, but could easily be set to 100 for a private cluster of 10 nodes. As can be seen in the script, the results of each API call are added to a master lookup table (a dictionary of sets in Python) to produce the final lookup table that uses a reference ID to return a list of granules containing data with that ID.
```

#### r4 — score 0.214

- **url:** https://docs.slideruleearth.io/developer_guide/why_sliderule.html
- **title:** Why SlideRule
- **section:** Why Develop SlideRule?
- **category:** `developer_guide`
- **matched_tokens:** ['combine', 'multiple', 'processing', 'products']

**Full text:**

```
New algorithms can be added at any time Instead of institutions running multiple pipelines to produce data products that are released on fixed schedules, institutions run multiple services and new services can be added at any time and have access to all of the data (current and historic) immediately. Improvements and fixes are immediately available Instead of institutions having to replace old versions of data products when processing improvements and fixes are made, and then requiring data users to redownload those data products, institutions deploy improvements and fixes to their services and it immediately becomes available to data users. Multiple science applications benefit from a single investment By parameterizing algorithms, the resources spent developing an algorithm can serve different science applications. Services integrate with other services When institutions move to a service-based model for data distribution, those services can be integrated into other systems and produce synergetic benefits. A data archive stands alone, and the only way to avoid duplicating efforts between different archives is to combine and centralize the functionality. On the other hand, a data service can be integrated with and leverage other data services while still remaining decentralized.
```

#### r5 — score 0.260

- **url:** https://docs.slideruleearth.io/developer_guide/articles/arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** User Lua Script
- **category:** `developer_guide`
- **matched_tokens:** ['combine']

**Full text:**

```
-- 1. import modules local json = require ( "json" ) -- 2. create an h5coro object from the granule to be processed local asset = core . getbyname ( "icesat2-atl13" ) local h5obj = h5coro . file ( asset , "ATL13_20250302152414_11692601_007_01.h5" ) -- 3. read the reference id out of each of the 6 beams local column_gt1l = h5obj : readp ( "gt1l/atl13refid" ) local column_gt1r = h5obj : readp ( "gt1r/atl13refid" ) local column_gt2l = h5obj : readp ( "gt2l/atl13refid" ) local column_gt2r = h5obj : readp ( "gt2r/atl13refid" ) local column_gt3l = h5obj : readp ( "gt3l/atl13refid" ) local column_gt3r = h5obj : readp ( "gt3r/atl13refid" ) -- 4. helper function that puts reference ids into a table local function count ( results , column ) local values = column : unique () for k , _ in pairs ( values ) do results [ tostring ( k )] = true end end -- 5. combine the reference ids into a single table local results = {} count ( results , column_gt1l ) count ( results , column_gt1r ) count ( results , column_gt2l ) count ( results , column_gt2r ) count ( results , column_gt3l ) count ( results , column_gt3r ) -- 6. return the results as json return json . encode ( results ) The above user provided script was sent to the SlideRule ace api to execute on a private cluster (in this case, the cluster was the developers cluster). For the purposes of this article, Iâve annotated the script with comments to assist in the explanation below.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.368

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 17
- **matched_tokens:** ['pipeline', 'processing', 'products']

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

#### r2 — score 0.406

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 6
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 6
- **matched_tokens:** ['pipeline', 'processing']

**Full text:**

```
List of Tables
1 History of changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
2 ATL24 input variables and processing details within each stage of the product
production . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 ATL24 component input for processing pipeline . . . . . . . . . . . . . . . . 12
4 ATL24 output variables for each stage of the product production . . . . . . . 12
5 ATL24 naming convention . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 Sea Surface cross validation results from 180 labeled datasets. . . . . . . . . 39
7 Bathymetry cross validation results from 180 labeled datasets. . . . . . . . . 39
8 Cross validation results from 180 labeled datasets. . . . . . . . . . . . . . . . 39
9 Known issues, reasons and possible solutions to ATL24 classification accuracy 48
vi
```

#### r3 — score 0.291

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['pipeline', 'processing', 'products']

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

#### r4 — score 0.294

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Abstract
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 2
- **matched_tokens:** ['multiple', 'processing', 'products']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 007
Abstract
This document describes the theoretical basis of the algorithms employed in deriving and
processing the ATL13 Along Track Inland Surface Water Data products for ICESat-2, Release 7. These level L3A data products are reported for each ICESat-2 water body crossing using a
flexible mask at a continuous, along track, short segment rate defined by 100 signal photons. The principal products reported for each water body under relatively clear skies are water surface
height, crossing slope, significant wave height, wind speed, beam subsurface attenuation, and
bathymetry. Multiple intermediate products and 12 quality flags associated with the fidelity of
the specific product are also reported. The ATL13 ATBD includes descriptions of the data
products and product parameters, detailed algorithm steps required for the retrieval of those
products, a summary of other ancillary ICESat-2 products required in the processing, product
calibration and validation, and a plain language summary of the code. A brief summary of the
principal product updates for each subsequent version including Release 7 is provided in Table
1-1 and the Change History Log. .
```

#### r5 — score 0.244

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['multiple', 'one', 'pipeline', 'processing', 'products']

**Full text:**

```
6 ATL24 Implementation Architecture and Product Accessibility
6.1 SlideRule Overview
The current user experience with ICESat-2 data is associated with downloading large volumes
of standard data products from NSIDC and then developing independent routines if the goal
is to explore new parameterizations or data resolutions for their own research. This paradigm
is the case for ICESat-2 but it is also the scenario for many NASA satellite missions and the
supporting NASA DAACs. Often the only data tools made available to users are those for
geographical and/or temporal subsetting and although extremely useful in data downloads
the requests can take hours depending on the size of the area. State-of-the-art solutions
to length and voluminous data downloads seem to be leveraging on-demand, cloud-based
processing. One example of this is the Alaska Satellite Facility’s Hybrid Pluggable Processing
Pipeline (ASFHyP3) for customized processing of SAR images across multiple missions. The
OpenTopography Project provides another example through its support of web-based services
for scalable capabilities in processing and analysis of Earth science-oriented topography data
(Shean et al. 2023). These more modern approaches to data production and dissemination
inspired SlideRule, with specific applications for ICESat-2. SlideRule is an on-demand data processing system for rapid, scalable, open science, which
is open to the public and accessible at https://slideruleearth.io.
```

---

