# Row 89 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `89-sliderule-toregion-polygon-helper-api-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sliderule toregion polygon helper api`
**Panel signature:** `fcb62227556a`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/sliderule.html
- **expected_sections:**
  - `toregion`
  - `sliderule`
- **expected_pages:** (none)
- **notes:** sliderule module helpers

---

## 📚 docsearch results (top 5)

#### r1 — score 0.631

- **url:** https://docs.slideruleearth.io/api_reference/sliderule.html
- **title:** sliderule
- **section:** run
- **category:** `api_reference`
- **matched_tokens:** ['api', 'polygon', 'sliderule', 'toregion']

**Full text:**

```
sliderule. run ( api , parms , aoi = None , resources = None , session = None ) [source] Execute the requested endpoint and return the results as a GeoDataFrame Parameters : api ( str ) â endpoint to run parms ( dict ) â parameter dictionary aoi ( dict ) â area of interest, passed to sliderule.toregion() function and polygon supplied in request resources ( list ) â list of resource names as strings Returns : result of executing the request endpoint Return type : GeoDataFrame Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r2 — score 0.617

- **url:** https://docs.slideruleearth.io/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Polygons
- **category:** `user_guide`
- **matched_tokens:** ['polygon', 'sliderule', 'toregion']

**Full text:**

```
All polygons provided to SlideRule must be provided as a list of dictionaries containing longitudes and latitudes in counter-clockwise order with the first and last point matching. The applicable parameters used to specify the polygon are: poly : polygon of region of interest proj : projection used when subsetting data (ânorth_polarâ, âsouth_polarâ, âplate_carreeâ). In most cases, do not specify and code will do the right thing. ignore_poly_for_cmr : boolean for whether to use the polygon as a part of the request to CMR for obtaining the list of resources to process. By default the polygon is used and this is only here for unusual cases where SlideRule is able to handle a polygon for subsetting that CMR cannot, and the list of resources to process is obtained some other way. For example: region = [ { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 }, { "lon" : - 107.7677425431139 , "lat" : 38.90611184543033 }, { "lon" : - 107.7818591266989 , "lat" : 39.26613714985466 }, { "lon" : - 108.3605610678553 , "lat" : 39.25086131372244 }, { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 } ] parms = { "poly" : region [ 'poly' ] } In order to facilitate other formats, the sliderule.toregion function can be used to convert polygons from the GeoJSON and Shapefile formats into this format accepted by SlideRule .
```

#### r3 — score 0.516

- **url:** https://docs.slideruleearth.io/getting_started/Getting-Started.html
- **title:** Getting Started
- **section:** Common Package Modules
- **category:** `getting_started`
- **matched_tokens:** ['api', 'helper', 'sliderule']

**Full text:**

```
In the SlideRule Python Package there are a few modules that are used more often than the others. Refer to the Userâs Guide and API Reference for further information. sliderule Core SlideRule services for initialization, configuration, processing requests, private cluster provisioning and access, area of interest processing icesat2 ICESat-2 specific services and definitions gedi GEDI specific services and definitions earthdata Interface to CMR and other STAC endpoints with helper functions for returning resources given a set of query parameters
```

#### r4 — score 0.604

- **url:** https://docs.slideruleearth.io/user_guide/overview.html
- **title:** Overview
- **section:** Area of Interest
- **category:** `user_guide`
- **matched_tokens:** ['polygon', 'sliderule', 'toregion']

**Full text:**

```
Python Client toregion - Raster Using the SlideRule Python Client toregion function, the user can provide a raster image which acts as a mask over the area of interest defining which latitude/longitude cells are âonâ and which cells are âoffâ. The source data is subsetted according to the mask. This is useful for very complicated areas of interest that represent coastlines or islands where a simple polygon is insufficient. Python Client toregion - GeoJson/Shapfile/GeoDataFrame Using the SlideRule Python Client, the user can define their area of interest using a geojson , shapefile , or GeoDataFrame , and still provide a properly formatted polygon in their request to SlideRule by converting the source definition using the toregion function. Python Client Earthdata Instead of letting the SlideRule server-side code handle querying the appropriate metadata repositories to obtain a list of resources to process, the SlideRule Python Client includes the earthdata module which provides functions for directly querying NASAâs Common Metadata Repository (CMR) and USGSâs The National Map (TNM). When the intended resources are supported by these metadata repositories, the user can query these repositories directly.
```

#### r5 — score 0.571

- **url:** https://docs.slideruleearth.io/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Rasterized Area of Interest
- **category:** `user_guide`
- **matched_tokens:** ['polygon', 'sliderule', 'toregion']

**Full text:**

```
There is no limit to the number of points in the polygon, but note that as the number of points grow, the amount of time it takes to perform the subsetting process also grows. Also, some regions cannot be expressed as a single polygon because they have holes in them or define discrete unconnected areas. Because of this, one of the outputs of the sliderule.toregion function is a GeoJSON object for describing complex geometries. It is available under the "raster" element of the returned dictionary. When the GeoJSON is supplied in the parameters sent in the request, the server side software forgoes using the polygon for subsetting operations, and instead builds a raster of the GeoJSON object using the specified cellsize, and then uses that raster image as a mask to determine which points in the source datasets are included in the region of interest.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.281

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['api', 'sliderule']

**Full text:**

```
includes long-running Python scripts. In addition to using the native runtime, the atl24g
endpoint will also use the SlideRule Container Runtime.
SlideRule Container Runtime
The container runtime environment for SlideRule services is a new runtime implemented
specifically to meet the needs of the atl24g endpoint. It uses the cluster management,
intelligent load balancing, and job orchestration components of SlideRule to kick-off and
communicate with Docker containers that are u
Figure 11: Top Container Schematic of SlideRule runtime environment
Applications written in Python will execute inside a Docker container running a Python
environment, and will use a provided Python API to retrieve a list of input files and return
a list of output files. Additional Docker container environments will be made available for
programs not written in Python.
6.3 Development Environment
The development of the atl24g, atl24s, and graphical web page will be done on local de-
velopment machines and coordinated through the GitHub ICESat-2 organization. This
includes training models, writing source code, compiling code, and deploying to both test
and production environments.
44
```

#### r2 — score 0.339

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['sliderule']

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

#### r3 — score 0.378

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['sliderule']

**Full text:**

```
6.2 Deployment Environment
ATL24 will use SlideRule to provide the compute infrastructure for all four project objectives:
• The atl24g gold standard product will be generated by a private instantiation of SlideRule
running in the AWS us-west-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to being transferred to the NSIDC.
• The atl24s and atl24p web services will be provided by the public instantiation of
SlideRule that runs in the AWS us-west-2 data center.
• The graphical web interface will be hosted in AWS S3 and served by Amazon’s CloudFront
at https://client.slideruleearth.io. Figure 10: Top Level SlideRule Architecture
SlideRule Native Runtime
The native runtime environment for SlideRule services is an extended Lua interpreter
where each request maps to a Lua script that instantiates custom classes written in C++ to
perform the processing needed to fulfill the request. The runtime is designed to quickly complete requests and return results back to users in
near real-time. To that end, all requests are expected to complete within 10 minutes, and
results are streamed back to the user as soon as they are available, over a TCP/IP connection
that remains open for the entire time of the request. (It is typical for the users that request
many granules to be processed at once to start receiving results for parts of their request
that have finished before other parts of their request have even begun to be processed).
```

#### r4 — score 0.269

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['sliderule']

**Full text:**

```
ATL24.g The gold standard product will be generated by a private instantiation of SlideRule
running in the AWS US-West-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to transfer to NSIDC. Moving forward, the ATL24.g option will
exist in SlideRule as a client facing product with subsetting capabilities. ATL24.s and ATL24.p Web-services will be provided by the public instantiation of Slid-
eRule. Includes interfacing to the client, and reading the ATL24 granules from S3. Graphical web interface The interface will be hosted in AWS S3 and served by Amazon’s
CloudFront at https://client.slieruleearth.io
The gold standard ATL24 product will be generated on a per-granule basis using SlideRule
and following the prescribed nearshore/coastal bathymetry mask to coordinate and execute
the full suite of contributing classification algorithms. This gold standard data product will
be a global resource using the most current algorithmic workflow and will be available to
users via sub-setting. Ultimately, the ATL24.g product provides the most robust algorithm
parameterization for global applications but does not provide the option for users to adjust
the input parameters. Figure 1 shows the execution flow from an incoming ATL24.g request
all the way to the output of a gold standard h5 granule.
3.3 ATL24 ATBD Sections
ATL24 primary input is ATL03, using the geolocated photon point cloud to determine
classifications of sea surface and seafloor.
```

#### r5 — score 0.368

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['sliderule']

**Full text:**

```
SlideRule runs in Amazon’s
cloud under GSFC Code 606’s Science Managed Cloud Environment (SMCE) and has access
to NASA’s Cumulus data archives. SlideRule provides web-services for researchers and other
data systems to generate custom data products in real-time using processing parameters
supplied at the time of the request. Scientists access SlideRule directly from any Python environment using a provided client;
a Javascript client is also provided for integrating SlideRule into other web-based systems. SlideRule is currently being used by glacier, snow, and bathymetry researchers to process
tens of thousands of ICESat-2 granules each month. SlideRule also supports private instantiations of its infrastructure that require authen-
ticated access. These instantiations, called private clusters, are managed by the SlideRule
Provisioning System at https://ps.slideruleearth.io. Private clusters are used for execut-
ing large processing runs, providing dedicated compute resources, and running proprietary
algorithms.
42
```

---

