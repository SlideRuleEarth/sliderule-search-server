# Row 59 results: docsearch / version_history

> Auto-generated. Open this file alongside `59-phoreal-added-sliderule-release-notes-version-review.md` —
> verdicts go there, this side is read-only.

**Query:** `phoreal added sliderule release notes version`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** phoreal first mentioned in v02-01-00 Major Changes

---

## 📚 docsearch results (top 5)

#### r1 — score 0.526

- **url:** https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `developer_guide`
- **matched_tokens:** ['notes', 'release', 'sliderule', 'version']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

#### r2 — score 0.565

- **url:** https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** Full release notes
- **category:** `developer_guide`
- **matched_tokens:** ['notes', 'release']

**Full text:**

```
https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
```

#### r3 — score 0.508

- **url:** https://docs.testsliderule.org/developer_guide/articles/private_clusters.html
- **title:** 2026-01-20: Private Clusters
- **section:** 2026-01-20: Private Clusters
- **category:** `developer_guide`
- **matched_tokens:** ['notes', 'release', 'sliderule']

**Full text:**

```
Note With release v5.0.2, SlideRule has transitioned the management of private clusters from the django-based SlideRule Provisioning System which was deployed in AWS ECS, to the pure Python-based SlideRule Authenticator and SlideRule Provisioner which are deployed via AWS Lambda. The main functions of the original system have been preserved, with a change in focus on clusters for individual users instead of organizations. See release notes for full details: https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
```

#### r4 — score 0.410

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/web-release-v04-00-03.html
- **title:** 2026-02-25: Web Client release v4.0.3
- **section:** Summary
- **category:** `release_notes`
- **matched_tokens:** ['added', 'notes', 'release', 'sliderule']

**Full text:**

```
ð SlideRule Web Client v4.0.3 Release Notes Changes since v3.8.0 Infrastructure CloudFront + Route 53 terraform modules added to support hosting the landing page at the root domain New Features Landing Page - The web client now serves as the SlideRule Earth landing page at slideruleearth.io, featuring a hero section with wallpaper image, About/Contact info panels, and a News tab that pulls articles directly from the SlideRule documentation site Home Button - A new Home button in the app bar navigates back to the landing page from anywhere in the app Docs Button - The old âAboutâ menu has been replaced with a streamlined âDocsâ button that links directly to the SlideRule documentation site Feedback Menu - The Feedback button now offers a dropdown with options to email support or open a GitHub issue directly Improvements Full-Width Analysis Map - The analysis map now uses the entire available width instead of a fixed 45vw, providing more room for map exploration Cleaner Analysis Layout - Removed unnecessary card wrapper and margins from the analysis view; the 3D panel is now hidden when not in use instead of taking up empty space Status Tooltips - All request statuses now show tooltip details on hover, including âpendingâ statuses that previously had no tooltip Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.569

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-09-00.html
- **title:** Release v4.9.x
- **section:** Release v4.9.x
- **category:** `release_notes`
- **matched_tokens:** ['release', 'sliderule', 'version']

**Full text:**

```
2025-02-04 Version description of the v4.9.3 release of SlideRule Earth. Sliderule Version Bathy Version v4.9.2 #14 v4.9.3 #15
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.381

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

#### r2 — score 0.287

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

#### r3 — score 0.358

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

#### r4 — score 0.264

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 52
- **matched_tokens:** ['sliderule']

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

#### r5 — score 0.233

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

