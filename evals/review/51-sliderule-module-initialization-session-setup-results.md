# Row 51 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `51-sliderule-module-initialization-session-setup-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sliderule module initialization session setup`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/sliderule.html
- **expected_sections:**
  - `init`
  - `sliderule`
  - `set_url`
- **expected_pages:** (none)
- **notes:** sliderule module api reference

---

## 📚 docsearch results (top 5)

#### r1 — score 0.564

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** Breaking Changes
- **category:** `release_notes`
- **matched_tokens:** ['module', 'session', 'sliderule']

**Full text:**

```
All calls to session.manager should no longer be used as that functionality will cease in future releases. v5.0.3 - The main Python module sliderule no longer creates a default session on import but requires either sliderule.init() or sliderule.create_session() . The creation of a default session was confusing when users called sliderule.init() which then created a second session. This caused odd behavior with logging because at that point two loggers exist. Moving forward, users are encouraged to use sliderule.create_session() which returns a session object that can then unambiguously be used to communicate with a SlideRule cluster.. v5.0.3 - Raster sampling support has been optimized for x-series APIs at the cost of legacy p-series API performance. All users are strongly encouraged to switch to x-series APIs when performing raster sampling as the old p-series APIs will take much longer now. v5.0.3 - Removed the sliderule.authenticate function as authentication must now occur when a SlideRule session is created. v5.0.2 - Polygons used for earthdata.stac requests no longer need to be nested lists, but are supplied in the same format as all other requests: poly = [ { "lat" : lat1 , "lon" : lon1 }, { "lat" : lat2 , "lon" : lon2 }, ... { "lat" : lat1 , "lon" : lon1 } ] v5.0.2 - The raster field which was replaced by region_mask and has been deprecated is now no longer supported. v5.0.2 - The nsidc-s3 asset which was replaced by the icesat2 asset, is no longer supported.
```

#### r2 — score 0.589

- **url:** https://docs.testsliderule.org/api_reference/sliderule.html
- **title:** sliderule
- **section:** set_url
- **category:** `api_reference`
- **matched_tokens:** ['session', 'sliderule']

**Full text:**

```
sliderule. set_url ( domain , session = None ) [source] Configure sliderule package with URL of service Parameters : urls ( str ) â IP address or hostname of SlideRule service (note, there is a special case where the url is provided as a list of strings instead of just a string; when a list is provided, the client hardcodes the set of servers that are used to process requests to the exact set provided; this is used for testing and for local installations and can be ignored by most users) Examples >>> import sliderule >>> sliderule . set_url ( "service.my-sliderule-server.org" )
```

#### r3 — score 0.487

- **url:** https://docs.testsliderule.org/user_guide/versioning.html
- **title:** Versioning
- **section:** Python Client
- **category:** `user_guide`
- **matched_tokens:** ['initialization', 'sliderule']

**Full text:**

```
To get the version of the SlideRule Python Client: from sliderule import version version . version When the SlideRule Python Client init() function is called, it issues a get_version() request to the SlideRule cluster and then checks that the client version is compatible with the server version. If there is a major version difference, the initialization function will return an error. If there is a minor version difference, the initialization function will return a warning.
```

#### r4 — score 0.583

- **url:** https://docs.testsliderule.org/developer_guide/articles/private_clusters.html
- **title:** 2026-01-20: Private Clusters
- **section:** Access
- **category:** `developer_guide`
- **matched_tokens:** ['session', 'sliderule']

**Full text:**

```
Users configure the SlideRule Python client to communicate with their private cluster when the client is initialized. For session based configuration, the following code initializes the client to talk to <my_cluster> : import sliderule session = sliderule . create_session ( cluster = "<my_cluster>" ) For functional configuration, the following code initializes the client to talk to <my_cluster> : import sliderule sliderule . init ( organization = "<my_cluster>" ) Note that behind the scenes, the sliderule.init call and sliderule.create_session call makes a call to session.authenticate to automatically authenticate the caller as a user of the cluster. It will first look in the environment for SLIDERULE_GITHUB_TOKEN , and then if not found, will initiate the device flow authentication process.
```

#### r5 — score 0.470

- **url:** https://docs.testsliderule.org/getting_started/Getting-Started.html
- **title:** Getting Started
- **section:** Common Package Modules
- **category:** `getting_started`
- **matched_tokens:** ['initialization', 'sliderule']

**Full text:**

```
In the SlideRule Python Package there are a few modules that are used more often than the others. Refer to the Userâs Guide and API Reference for further information. sliderule Core SlideRule services for initialization, configuration, processing requests, private cluster provisioning and access, area of interest processing icesat2 ICESat-2 specific services and definitions gedi GEDI specific services and definitions earthdata Interface to CMR and other STAC endpoints with helper functions for returning resources given a set of query parameters
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.306

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

#### r2 — score 0.387

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

#### r3 — score 0.365

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

#### r4 — score 0.312

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

#### r5 — score 0.209

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

---

