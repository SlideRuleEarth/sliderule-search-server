# Row 75 results: docsearch / conceptual

> Auto-generated. Open this file alongside `75-how-does-sliderule-version-its-server-and-client-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does SlideRule version its server and client`
**Panel signature:** `9db83f4b800b`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/versioning.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** versioning policy page

---

## 📚 docsearch results (top 5)

#### r1 — score 0.848

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Client Version
- **category:** `user_guide`
- **matched_tokens:** ['client', 'server', 'sliderule', 'version']

**Full text:**

```
In addition to the version information needed to identify the version of the SlideRule server executable running, SlideRule clients provide their own version information.
```

#### r2 — score 0.832

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Web Client
- **category:** `user_guide`
- **matched_tokens:** ['client', 'server', 'sliderule', 'version']

**Full text:**

```
The SlideRule Web Client identifies its version next to the server version in the upper left corner of the browser window.
```

#### r3 — score 0.607

- **url:** https://docs.slideruleearth.io/api_reference/sliderule.html
- **title:** sliderule
- **section:** check_version
- **category:** `api_reference`
- **matched_tokens:** ['client', 'server', 'sliderule', 'version']

**Full text:**

```
sliderule. check_version ( plugins = None , session = None ) [source] Check that the version of the client matches the version of the server and any additionally requested plugins Parameters : plugins ( list ) â list of package names (as strings) to check the version on Returns : True (always; kept for backward compatibility) Return type : bool
```

#### r4 — score 0.671

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Python Client
- **category:** `user_guide`
- **matched_tokens:** ['client', 'server', 'sliderule', 'version']

**Full text:**

```
To get the version of the SlideRule Python Client: from sliderule import version version . version When the SlideRule Python Client init() function is called, it issues a get_version() request to the SlideRule cluster and then checks that the client version is compatible with the server version. If there is a major version difference, the initialization function will return an error. If there is a minor version difference, the initialization function will return a warning.
```

#### r5 — score 0.637

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Web API
- **category:** `user_guide`
- **matched_tokens:** ['client', 'server', 'sliderule', 'version']

**Full text:**

```
Using any client able to speak HTTP, the version endpoint can be hit to retrieve the current version of SlideRule that is running. For example: $ curl -sS https://sliderule.slideruleearth.io/source/version | jq has the following output: { "server" : { "launch" : "2025-09-02T06:05:11Z" , "build" : "v4.19.0-0-g79275b17, 6.1.147-172.266.amzn2023.aarch64, Thu Aug 28 19:04:14 UTC 2025" , "duration" : 645587997 , "organization" : "sliderule" , "cluster" : "sliderule-blue" , "packages" : [ "core" , "arrow" , "aws" , "cre" , "geo" , "h5" , "streaming" , "bathy" , "bluetopo" , "gebco" , "gedi" , "icesat2" , "landsat" , "opendata" , "pgc" , "swot" , "usgs3dep" , "gedtm" , "nisar" , "atl24" ], "version" : "v4.19.0" , "environment" : "v4.19.0-0-g79275b17" } }
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.463

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['client', 'sliderule']

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

#### r2 — score 0.567

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['client', 'sliderule']

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

#### r3 — score 0.559

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['client', 'sliderule']

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

#### r4 — score 0.361

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 52
- **matched_tokens:** ['server', 'sliderule']

**Full text:**

```
Both compute and storage services in AWS are available through the SlideRule SMCE
account and will be used on an as-needed basis.
The following data resources will be stored in the SlideRule SMCE account S3 bucket:
• Labeled photon data
• Global bathymetry mask
• Refractive index
• Uncertainty lookup table
The following Docker images will be stored in the SlideRule SMCE account container registry:
• SlideRule server, intelligent load balancer, and monitor
• Python runtime environment
The following applications will be hosted in the SlideRule SMCE S3 bucket:
• Graphic web interface
• Documentation webpage
45
```

#### r5 — score 0.400

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['client', 'sliderule']

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

