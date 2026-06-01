# Row 76 results: docsearch / conceptual

> Auto-generated. Open this file alongside `76-what-is-sliderule-overview-on-demand-processing-review.md` —
> verdicts go there, this side is read-only.

**Query:** `what is SlideRule overview on-demand processing`
**Panel signature:** `175d1f78e23d`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/overview.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** overview / what-is page

---

## 📚 docsearch results (top 5)

#### r1 — score 0.647

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** SlideRule Project Goals
- **category:** `user_guide`
- **matched_tokens:** ['demand', 'processing', 'sliderule']

**Full text:**

```
The ultimate goal of the SlideRule project is to enable researchers to investigate questions they were hitherto unable to ask by providing them a scalable and dynamic science data distribution service. In the end, we hope SlideRule can be used as a model for future missions to change the way institutions release data products. For us to be successful, our service needs to have five characteristics: Cost effective Our system should have near zero costs when not in use, very small startup costs, and the ability to scale in a cost-controlled way to handle processing demand. Responsive For interactive sessions, the results for typical regions of interest should be returned quickly enough that the user does not go off and do something else while waiting for them. For integrated services (other software systems using our system as a service), we should be able to handle many small requests efficiently with minimal latency. Simple and well-documented The user interface for our system should be intuitive and require a very small learning curve. The methods for accessing our service should match current trends and be available through common packaging systems (for example, Python users should be able to install pip and/or conda packages to use our system).
```

#### r2 — score 0.573

- **url:** https://docs.slideruleearth.io/developer_guide/under_the_hood.html
- **title:** Under the Hood
- **section:** Components of a Processing Request
- **category:** `developer_guide`
- **matched_tokens:** ['demand', 'processing', 'sliderule']

**Full text:**

```
Web services provided by SlideRule can be accessed by any http client (e.g. curl); but different clients are provided by the project to make it easier to interact with SlideRule. These clients provide functional interfaces for making on-demand science data requests: processing parameters are populated, all the necessary requests to the SlideRule servers are performed and the responses from the servers are handled, and the results are collected into DataFrame-like structures and returned back to the calling code. Science Algorithms Science algorithms available to SlideRule are implemented in C++ and Lua code and run inside the SlideRule framework on each server. They are invoked by calls to the web services which kick off Lua scripts, and utilize the data access code to pull in the requested datasets for processing. On the public cluster, the customization of the algorithm processing is limited to predefined parameters made available by the code and exposed to the web service. On private clusters, users can run sandboxed Lua code provided at the time of the request. Data Interface At the start of every algorithm, the set of data needed by the algorithm is internally requested. SlideRule maintains a thread pool of data fetchers that receive those internal requests and perform the data reads asynchronously. The algorithms will do as much as they can with the data they have available and will block until notified by the data fetchers when they need more data to proceed.
```

#### r3 — score 0.610

- **url:** https://docs.slideruleearth.io/developer_guide/how_tos/amazon_linux_arm_setup.html
- **title:** Setting Up Amazon Linux Development Environment
- **section:** Overview
- **category:** `developer_guide`
- **matched_tokens:** ['overview', 'sliderule']

**Full text:**

```
These steps setup a development environment for SlideRule. The target platform is a Graviton3 processor running Amazon Linux 2023 in AWS.
```

#### r4 — score 0.547

- **url:** https://docs.slideruleearth.io/
- **title:** SlideRule v5.4.2
- **section:** Purpose of this Site
- **category:** `other`
- **matched_tokens:** ['demand', 'processing', 'sliderule']

**Full text:**

```
This documentation is intended to explain how to use SlideRule and its accompanying Python client. SlideRule is a web service for on-demand science data processing, which provides researchers and other Earth science data systems low-latency access to customized data products using processing parameters supplied at the time of the request. SlideRule runs in AWS us-west-2 and has access to ICESat-2, GEDI, Landsat, ArcticDEM, REMA, and a growing list of other datasets stored in S3. While SlideRule can be accessed by any http client (e.g. curl) by making GET and POST requests to the SlideRule service, the python packages in this repository provide higher level access to SlideRule by hiding the GET and POST requests inside python function calls that accept basic python variable types (e.g. dictionaries, lists, numbers), and returns GeoDataFrames. âUsing SlideRuleâ typically means running a Python script youâve developed to analyze Earth science data, and in that script calling functions in the sliderule Python package to make processing requests to SlideRule web services to perform some of the data intensive parts of your analysis. Most of the documentation and examples we provide are focused on this use-case. We do provide other means of interacting with SlideRule, most notably the web client at https://client.slideruleearth.io , both those aspects of the project are less documented.
```

#### r5 — score 0.547

- **url:** https://docs.slideruleearth.io/index.html
- **title:** SlideRule v5.4.2
- **section:** Purpose of this Site
- **category:** `other`
- **matched_tokens:** ['demand', 'processing', 'sliderule']

**Full text:**

```
This documentation is intended to explain how to use SlideRule and its accompanying Python client. SlideRule is a web service for on-demand science data processing, which provides researchers and other Earth science data systems low-latency access to customized data products using processing parameters supplied at the time of the request. SlideRule runs in AWS us-west-2 and has access to ICESat-2, GEDI, Landsat, ArcticDEM, REMA, and a growing list of other datasets stored in S3. While SlideRule can be accessed by any http client (e.g. curl) by making GET and POST requests to the SlideRule service, the python packages in this repository provide higher level access to SlideRule by hiding the GET and POST requests inside python function calls that accept basic python variable types (e.g. dictionaries, lists, numbers), and returns GeoDataFrames. âUsing SlideRuleâ typically means running a Python script youâve developed to analyze Earth science data, and in that script calling functions in the sliderule Python package to make processing requests to SlideRule web services to perform some of the data intensive parts of your analysis. Most of the documentation and examples we provide are focused on this use-case. We do provide other means of interacting with SlideRule, most notably the web client at https://client.slideruleearth.io , both those aspects of the project are less documented.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.466

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['demand', 'overview', 'processing', 'sliderule']

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

#### r2 — score 0.605

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['overview', 'processing', 'sliderule']

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

#### r3 — score 0.423

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['demand', 'processing', 'sliderule']

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

#### r4 — score 0.533

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['demand', 'sliderule']

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

#### r5 — score 0.600

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['processing', 'sliderule']

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

---

