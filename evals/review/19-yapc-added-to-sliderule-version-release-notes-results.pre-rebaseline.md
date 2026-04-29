# Row 19 results: docsearch / version_history

> Auto-generated. Open this file alongside `19-yapc-added-to-sliderule-version-release-notes-review.md` —
> verdicts go there, this side is read-only.

**Query:** `yapc added to sliderule version release notes`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-03-00.html
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-04-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** yapc introduced in v01.03-v01.04 range

---

## 📚 docsearch results (top 5)

#### r1 — score 0.537

- **url:** https://docs.slideruleearth.io/developer_guide/articles/private_clusters.html
- **title:** 2026-01-20: Private Clusters
- **section:** 2026-01-20: Private Clusters
- **category:** `developer_guide`
- **matched_tokens:** ['notes', 'release', 'sliderule']

**Full text:**

```
Note With release v5.0.2, SlideRule has transitioned the management of private clusters from the django-based SlideRule Provisioning System which was deployed in AWS ECS, to the pure Python-based SlideRule Authenticator and SlideRule Provisioner which are deployed via AWS Lambda. The main functions of the original system have been preserved, with a change in focus on clusters for individual users instead of organizations. See release notes for full details: https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
```

#### r2 — score 0.502

- **url:** https://docs.slideruleearth.io/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `developer_guide`
- **matched_tokens:** ['notes', 'release', 'sliderule', 'version']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

#### r3 — score 0.447

- **url:** https://docs.slideruleearth.io/developer_guide/articles/web_client_release_notes_4_0_3.html
- **title:** 2026-02-25: Web Client release v4.0.3
- **section:** Summary
- **category:** `developer_guide`
- **matched_tokens:** ['added', 'notes', 'release', 'sliderule']

**Full text:**

```
ð SlideRule Web Client v4.0.3 Release Notes Changes since v3.8.0 Infrastructure CloudFront + Route 53 terraform modules added to support hosting the landing page at the root domain New Features Landing Page - The web client now serves as the SlideRule Earth landing page at slideruleearth.io, featuring a hero section with wallpaper image, About/Contact info panels, and a News tab that pulls articles directly from the SlideRule documentation site Home Button - A new Home button in the app bar navigates back to the landing page from anywhere in the app Docs Button - The old âAboutâ menu has been replaced with a streamlined âDocsâ button that links directly to the SlideRule documentation site Feedback Menu - The Feedback button now offers a dropdown with options to email support or open a GitHub issue directly Improvements Full-Width Analysis Map - The analysis map now uses the entire available width instead of a fixed 45vw, providing more room for map exploration Cleaner Analysis Layout - Removed unnecessary card wrapper and margins from the analysis view; the 3D panel is now hidden when not in use instead of taking up empty space Status Tooltips - All request statuses now show tooltip details on hover, including âpendingâ statuses that previously had no tooltip Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.492

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-05-00.html
- **title:** Release v3.5.x
- **section:** Release v3.5.x
- **category:** `release_notes`
- **matched_tokens:** ['added', 'release', 'sliderule', 'version']

**Full text:**

```
2023-06-09 Version description of the v3.5.0 release of ICESat-2 SlideRule. This document also captures functionality added in versions v3.4.0 and v3.4.1.
```

#### r5 — score 0.526

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-01-00.html
- **title:** Release v1.1.x
- **section:** Release v1.1.x
- **category:** `release_notes`
- **matched_tokens:** ['release', 'sliderule', 'version']

**Full text:**

```
2021-10-13 Version description of the v1.1.5 release of ICESat-2 SlideRule.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.438

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

#### r2 — score 0.437

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

#### r3 — score 0.229

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['sliderule', 'version']

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

#### r4 — score 0.231

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.3 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 5
- **matched_tokens:** ['sliderule', 'version']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
• x_atc: along-track distance (m) in a segment projected to the ellipsoid of the received
photon
• y_atc: across-track distance (m) projected to the ellipsoid of the received photon from the
reference ground track (RGT)
1.2.2.3 metadata
Query metadata (geospatial and temporal extents), algorithm run times, SlideRule metadata, and
granule-level statistics.
1.2.2.4 orbit_info
Orbit parameters that are constant for a granule, such as the RGT number, cycle, and spacecraft
orientation.
1.2.3 Naming Convention
Data files utilize the following naming convention:
ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[VVV_RR]_[vvv_rr].h5
Example:
ATL24_20230704193540_02232008_006_02_001_01.h5
The following table describes the file naming convention variables:
Table 1. File Naming Convention Variables and Descriptions
Variable Description
ATL24 ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit RGT number. The ICESat-2 mission has 1,387 RGTs, numbered from
0001 to 1387.
cc Cycle number. The cycle number tracks the number of 91-day periods that have
elapsed since ICESat-2 entered the science orbit.
ss Region number. ATL03 data files are segmented into approximately 1/14th of an
orbit. Region numbers range from 01 to 14. Note that some regions may not be
available.
```

#### r5 — score 0.322

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

---

