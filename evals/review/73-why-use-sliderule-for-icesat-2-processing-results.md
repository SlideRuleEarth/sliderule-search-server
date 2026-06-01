# Row 73 results: docsearch / conceptual

> Auto-generated. Open this file alongside `73-why-use-sliderule-for-icesat-2-processing-review.md` —
> verdicts go there, this side is read-only.

**Query:** `why use SlideRule for ICESat-2 processing`
**Panel signature:** `ac411100c26f`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/why_sliderule.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** why_sliderule motivation page

---

## 📚 docsearch results (top 5)

#### r1 — score 0.605

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-01-00.html
- **title:** Release v4.1.x
- **section:** Release v4.1.x
- **category:** `release_notes`
- **matched_tokens:** ['icesat', 'processing', 'sliderule', 'use']

**Full text:**

```
2023-12-07 Version description of the v4.1.0 release of ICESat-2 SlideRule. * Important : This version requires an update of the Python client to use. The underlying mechanism used in support of including ancillary fields in processing requests was updated to support both the PhoREAL algorithm and the ATL06 subsetter. As a result, in order to include ancillary field requests in your code, you must have the latest client installed. No changes are needed to the code in your scripts.
```

#### r2 — score 0.625

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['icesat', 'sliderule', 'use']

**Full text:**

```
sliderule.icesat2. init ( url = 'slideruleearth.io' , verbose = False , max_resources = None , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 , rethrow = False ) [source] Initializes the Python client for use with SlideRule and should be called before other ICESat-2 API calls. This function is a wrapper for the sliderule.init(â¦) function . Parameters : max_resources ( int ) â maximum number of H5 granules to process in the request Examples >>> from sliderule import icesat2 >>> icesat2 . init ()
```

#### r3 — score 0.609

- **url:** https://docs.slideruleearth.io/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Issue the Processing Request
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'processing', 'sliderule', 'use']

**Full text:**

```
There are two general purpose routines provided in the SlideRule Python client for issuing processing requests. sliderule.source Implements the low-level protocol for making requests to SlideRule and processing the results. This can be used to issue a request to any SlideRule endpoint. sliderule.run Implements a standard SlideRule convention for making requests to SlideRule endpoints that return a dataframe. This uses the sliderule.source() routine. A user is always free to use one of the routines above for making requests to SlideRule, but many times it is more convenient to use one of the helper functions in the mission specific modules. For instance, when making processing requests for ICESat-2 data, the icesat2 module provides many routines that wrap calls to specific endpoints in an easy-to-use Python function. For instance, when making a request to the atl06p endpoint, a user should use the icesat2.atl06p() Python routine.
```

#### r4 — score 0.578

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'processing', 'sliderule', 'use']

**Full text:**

```
Its use on SlideRule removed critical performance barriers in accessing ICESat-2 datasets hosted in S3 and has enabled the project to cost effectively offer science processing services to the ICESat-2 science community. The demonstrated benefits of using the H5Coro library in SlideRule show that the approach of changing the library and not the data has merit, and that future efforts to utilize NASAâs HDF5 datasets could greatly benefit from a standardized subset of the HDF5 specification specifically suited for cloud environments.
```

#### r5 — score 0.547

- **url:** https://docs.slideruleearth.io/
- **title:** SlideRule v5.4.2
- **section:** Purpose of this Site
- **category:** `other`
- **matched_tokens:** ['icesat', 'processing', 'sliderule', 'use']

**Full text:**

```
This documentation is intended to explain how to use SlideRule and its accompanying Python client. SlideRule is a web service for on-demand science data processing, which provides researchers and other Earth science data systems low-latency access to customized data products using processing parameters supplied at the time of the request. SlideRule runs in AWS us-west-2 and has access to ICESat-2, GEDI, Landsat, ArcticDEM, REMA, and a growing list of other datasets stored in S3. While SlideRule can be accessed by any http client (e.g. curl) by making GET and POST requests to the SlideRule service, the python packages in this repository provide higher level access to SlideRule by hiding the GET and POST requests inside python function calls that accept basic python variable types (e.g. dictionaries, lists, numbers), and returns GeoDataFrames. âUsing SlideRuleâ typically means running a Python script youâve developed to analyze Earth science data, and in that script calling functions in the sliderule Python package to make processing requests to SlideRule web services to perform some of the data intensive parts of your analysis. Most of the documentation and examples we provide are focused on this use-case. We do provide other means of interacting with SlideRule, most notably the web client at https://client.slideruleearth.io , both those aspects of the project are less documented.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.625

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['icesat', 'processing', 'sliderule']

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

#### r2 — score 0.515

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['processing', 'sliderule', 'use']

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

#### r3 — score 0.514

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['icesat', 'processing', 'sliderule']

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

#### r4 — score 0.506

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** References
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 62
- **matched_tokens:** ['icesat', 'sliderule']

**Full text:**

```
Rice, Glen, Katrina Wyllie, Barry Gallagher, and Phuntsok Geleg (2023). “The National Bathymetric
Source”. OCEANS 2023-MTS/IEEE US Gulf Coast. IEEE, pp. 1–7. Schutz, B. E., H. J. Zwally, C. A. Shuman, D. Hancock, and J. P. DiMarzio (2005). “Overview of
the ICESat Mission”. Geophysical Research Letters 32.21, L21S01. doi: 10.1029/2005GL024009.
url: http://doi.wiley.com/10.1029/2005GL024009 (visited on 09/03/2022). Shean, David, J. P. Swinski, Ben Smith, Tyler Sutterley, Scott Henderson, Carlos Ugarte, Eric
Lidwa, and Thomas Neumann (Jan. 18, 2023). “SlideRule: Enabling rapid, scalable, open science
forthe NASA ICESat-2 mission and beyond”. Journal of Open Source Software 8.81, p. 4982.
doi: 10.21105/joss.04982. url: https://joss.theoj.org/papers/10.21105/joss.04982
(visited on 03/07/2023).
55
```

#### r5 — score 0.494

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['icesat', 'processing', 'sliderule']

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

