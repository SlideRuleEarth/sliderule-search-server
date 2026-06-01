# Row 82 results: docsearch / version_history

> Auto-generated. Open this file alongside `82-atl13x-added-to-sliderule-release-notes-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl13x added to sliderule release notes`
**Panel signature:** `384e77dd098c`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-14-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl13x first appears in v04-14-00

---

## 📚 docsearch results (top 5)

#### r1 — score 0.624

- **url:** https://docs.slideruleearth.io/user_guide/articles/251208_v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `user_guide`
- **matched_tokens:** ['notes', 'release', 'sliderule']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

#### r2 — score 0.600

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl13x', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl13x endpoint comes from the {beam} group of the ATL13 granules. atl13_fields : fields in the beam group of the ATL13 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "ice_flag" ], } gdf = sliderule . run ( "atl13x" , parms )
```

#### r3 — score 0.516

- **url:** https://docs.slideruleearth.io/user_guide/articles/251208_v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** Full release notes
- **category:** `user_guide`
- **matched_tokens:** ['notes', 'release']

**Full text:**

```
https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
```

#### r4 — score 0.489

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-14-00.html
- **title:** Release v4.14.x
- **section:** New/Improved Functionality
- **category:** `release_notes`
- **matched_tokens:** ['atl13x', 'sliderule']

**Full text:**

```
Arbitrary Code Execution - /source/ace API for executing user supplied lua scripts; only available on private clusters. Asset Metadata Service - /manager/ams API for querying metadata directly from SlideRule; only ATL13 currently supported. ATL13 - /source/atl13x API for subsetting the ATL13 standard data product; in addition to normal temporal/spatial subsetting requests, SlideRule also supports subsetting based on the ATL13 reference ID, lake name, and coordinate within a body of water.
```

#### r5 — score 0.428

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/web-release-v04-00-03.html
- **title:** 2026-02-25: Web Client release v4.0.3
- **section:** Summary
- **category:** `release_notes`
- **matched_tokens:** ['added', 'notes', 'release', 'sliderule']

**Full text:**

```
ð SlideRule Web Client v4.0.3 Release Notes Changes since v3.8.0 Infrastructure CloudFront + Route 53 terraform modules added to support hosting the landing page at the root domain New Features Landing Page - The web client now serves as the SlideRule Earth landing page at slideruleearth.io, featuring a hero section with wallpaper image, About/Contact info panels, and a News tab that pulls articles directly from the SlideRule documentation site Home Button - A new Home button in the app bar navigates back to the landing page from anywhere in the app Docs Button - The old âAboutâ menu has been replaced with a streamlined âDocsâ button that links directly to the SlideRule documentation site Feedback Menu - The Feedback button now offers a dropdown with options to email support or open a GitHub issue directly Improvements Full-Width Analysis Map - The analysis map now uses the entire available width instead of a fixed 45vw, providing more room for map exploration Cleaner Analysis Layout - Removed unnecessary card wrapper and margins from the analysis view; the 3D panel is now hidden when not in use instead of taking up empty space Status Tooltips - All request statuses now show tooltip details on hover, including âpendingâ statuses that previously had no tooltip Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.527

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

#### r2 — score 0.523

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

#### r3 — score 0.429

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

#### r4 — score 0.360

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

#### r5 — score 0.354

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

