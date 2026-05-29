# Row 18 results: docsearch / version_history

> Auto-generated. Open this file alongside `18-when-was-atl24x-added-to-sliderule-release-review.md` —
> verdicts go there, this side is read-only.

**Query:** `when was atl24x added to sliderule release`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-11-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl24x major change in v04-11-00

---

## 📚 docsearch results (top 5)

#### r1 — score 0.656

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-11-00.html
- **title:** Release v4.11.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['atl24x', 'release', 'sliderule']

**Full text:**

```
v4.11.0 - The official release of the SlideRule Web Client at https://client.slideruleearth.io v4.11.0 - The atl03x endpoint is being previewed. This implements a dataframe model for the data instead of a streaming model. v4.11.0 - The atl24x endpoint provides subsetting support for the ATL24 standard data product.
```

#### r2 — score 0.638

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl24x', 'sliderule']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r3 — score 0.586

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl24x', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl24x endpoint comes from the {beam} group of the ATL24 granules. anc_fields : fields in the beam group of the ATL24 granule, provided as a list of strings For example, parms = { "anc_fields" : [ "index_ph" ], } gdf = sliderule . run ( "atl24x" , parms )
```

#### r4 — score 0.462

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** New Functionality
- **category:** `release_notes`
- **matched_tokens:** ['added', 'release', 'sliderule']

**Full text:**

```
Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and GEDI01B ( gedi01bx ) v5.0.2 - ATL24 uses release 002 by default, which uses the internal Asset Metadata Service (AMS). v5.0.2 - #549 - h5p now supports slices. v5.0.2 - earthdata.py is no longer a standalone implementation of an interface to CMR and TNM, but instead makes a request to the SlideRule cluster to execute the server-side implementations in earth_data_query.lua . This consolidates the interface to these services in one place, and also provides a consistent interface between the web and Python clients. v5.0.2 - Added the 3dep1m asset which accesses the same USGS 3DEP data product but uses the internal AMS service for STAC queries. This is an attempt to alleviate issues with inconsistent availability and functionality in The National Map (TNM) service which made using 3DEP difficult.
```

#### r5 — score 0.635

- **url:** https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `developer_guide`
- **matched_tokens:** ['release', 'sliderule']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.664

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

#### r2 — score 0.533

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['sliderule']

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

#### r3 — score 0.538

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

#### r4 — score 0.600

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

#### r5 — score 0.498

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['sliderule']

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

---

