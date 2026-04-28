# Row 20 results: docsearch / version_history

> Auto-generated. Open this file alongside `20-sliderule-version-5-breaking-changes-new-functionality-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sliderule version 5 breaking changes new functionality`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** v5.0.0 release notes

---

## 📚 docsearch results (top 5)

#### r1 — score 0.515

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-00-00.html
- **title:** Release v2.0.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['changes', 'functionality', 'new', 'sliderule', 'version']

**Full text:**

```
Version 2.0.0 of SlideRule represents a major change to the SlideRule architecture and is NOT backward compatible with any of the previous releases. The following is a list of changes in this major release. New Domain : SlideRule has moved from http://icesat2sliderule.org to https://slideruleearth.io . This change was made to reflect the new scope of SlideRule which includes datasets (e.g. ArcticDEM and LandSat) beyond the ICESat-2 mission, and was necessary due to enhanced security measures and support for authenticated access. The icesat2sliderule.org domain will continue to run v1.4.6 until all existing users have transitioned over to the new domain, at which point we will make icesat2sliderule.org an alias for slideruleearth.io . The following are a list of the subdomains associated with our new domain: slideruleearth.io and www.slideruleearth.io : the static website for the SlideRule project (documentation, links, tutorials, etc) ps.slideruleearth.io : the SlideRule Provisioning system demo.slideruleearth.io : the graphical demo of SlideRule functionality sliderule.slideruleearth.io : the public SlideRule cluster {organization}.slideruleearthio.io : the private SlideRule cluster associated with {organization} Versioning : with the v2.0.0 release, the SlideRule project will adhere to strict versioning guidelines which are checked during client initialization in the icesat2.init function.
```

#### r2 — score 0.454

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Library Version ( version )
- **category:** `user_guide`
- **matched_tokens:** ['changes', 'functionality', 'new', 'sliderule', 'version']

**Full text:**

```
The SlideRule executable version (called the Library Version in the code) is the semantic version used by the SlideRule team to identify a release of SlideRule. It uses the following convention: vX.Y.Z where: X is the major version; when incremented it indicates a break in backward compatibility. Y is the minor version; when incremented it indicates new or significantly changed functionality Z is the patch version; when incremented it indicates a bug fix with no changes in the intended functionality of the system The SlideRule executable is packaged into a Docker container, tagged with the semantic version, which is built at the same time the library and executable is built. For all practical purposes, the building of the SlideRule executable and the building of the SlideRule Docker container image can be thought of as the same thing; the same code base and build information applies to both. In other words, the Docker container image is the final output of, and method of packaging for, the SlideRule executable.
```

#### r3 — score 0.526

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Note on Reproducibility
- **category:** `user_guide`
- **matched_tokens:** ['functionality', 'sliderule', 'version']

**Full text:**

```
It is the goal of the SlideRule development team to create a system where results are able to be reproduced; but this is often times either extremely difficult or impossible for reasons outside of the teams control. SlideRule relies on publicly hosted datasets. When those datasets are updated, older versions of the datasets are often removed. For instance, ICESat-2 Standard Data Products have a 6-month to 1-year release cycle and EarthData Cloud only stores the last two releases. Production systems must stay up-to-date with all security patches. This means libraries used by older versions of SlideRule may not be able to be deployed if newer versions of those libraries contain security patches. While we make every effort to keep backward compatibility for as long as possible, our development time is a limited resource and we are unable to maintain very old architectures of SlideRule. Once we increment a major version number, we often remove deprecated functionality and internal configurations needed to deploy those older system designs. That does not mean it would not be impossible to recreate the environment needed to run the older design - it does mean it becomes more and more impractical to do so. Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.394

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** Breaking Changes
- **category:** `release_notes`
- **matched_tokens:** ['breaking', 'changes', 'functionality', 'sliderule']

**Full text:**

```
All calls to session.manager should no longer be used as that functionality will cease in future releases. v5.0.3 - The main Python module sliderule no longer creates a default session on import but requires either sliderule.init() or sliderule.create_session() . The creation of a default session was confusing when users called sliderule.init() which then created a second session. This caused odd behavior with logging because at that point two loggers exist. Moving forward, users are encouraged to use sliderule.create_session() which returns a session object that can then unambiguously be used to communicate with a SlideRule cluster.. v5.0.3 - Raster sampling support has been optimized for x-series APIs at the cost of legacy p-series API performance. All users are strongly encouraged to switch to x-series APIs when performing raster sampling as the old p-series APIs will take much longer now. v5.0.3 - Removed the sliderule.authenticate function as authentication must now occur when a SlideRule session is created. v5.0.2 - Polygons used for earthdata.stac requests no longer need to be nested lists, but are supplied in the same format as all other requests: poly = [ { "lat" : lat1 , "lon" : lon1 }, { "lat" : lat2 , "lon" : lon2 }, ... { "lat" : lat1 , "lon" : lon1 } ] v5.0.2 - The raster field which was replaced by region_mask and has been deprecated is now no longer supported. v5.0.2 - The nsidc-s3 asset which was replaced by the icesat2 asset, is no longer supported.
```

#### r5 — score 0.525

- **url:** https://docs.slideruleearth.io/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `developer_guide`
- **matched_tokens:** ['changes', 'sliderule', 'version']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.285

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['functionality', 'sliderule']

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

#### r2 — score 0.191

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['new', 'sliderule']

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

#### r3 — score 0.359

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

#### r4 — score 0.316

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

#### r5 — score 0.206

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

