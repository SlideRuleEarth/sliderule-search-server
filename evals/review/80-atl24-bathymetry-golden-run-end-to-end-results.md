# Row 80 results: docsearch / example

> Auto-generated. Open this file alongside `80-atl24-bathymetry-golden-run-end-to-end-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL24 bathymetry golden run end to end`
**Panel signature:** `b6c3dac74219`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL24 golden-run worked example article

---

## 📚 docsearch results (top 5)

#### r1 — score 0.471

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** 2025-03-28: ATL24 Processing Run
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'run']

**Full text:**

```
Note SlideRule processed ICESat-2 cycles 1 through 25 to produce the first release of the Near-Shore Coastal Bathymetry Product (ATL24) for ICESat-2.
```

#### r2 — score 0.517

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'run']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r3 — score 0.525

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r4 — score 0.450

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.450

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Statistics
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea surface 0.73% of classified photons were bathymetry
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.486

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Introduction
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 10
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
This new product, ATL24, will provide
automated bathymetry extraction, sea surface/wave parameters, and water column statistics
in all regions that provide adequate conditions for probable measurements. In contrast to
other ATLAS data products that were designed pre-launch, a great benefit to the ATL24
development effort is the opportunity to learn from and leverage the great wealth of ICESat-2
bathymetry studies that have been published over the past six years.
3
```

#### r2 — score 0.399

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['atl24', 'end']

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

#### r3 — score 0.421

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['atl24', 'bathymetry']

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

#### r4 — score 0.405

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 6
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 6
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
List of Tables
1 History of changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
2 ATL24 input variables and processing details within each stage of the product
production . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 ATL24 component input for processing pipeline . . . . . . . . . . . . . . . . 12
4 ATL24 output variables for each stage of the product production . . . . . . . 12
5 ATL24 naming convention . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 Sea Surface cross validation results from 180 labeled datasets. . . . . . . . . 39
7 Bathymetry cross validation results from 180 labeled datasets. . . . . . . . . 39
8 Cross validation results from 180 labeled datasets. . . . . . . . . . . . . . . . 39
9 Known issues, reasons and possible solutions to ATL24 classification accuracy 48
vi
```

#### r5 — score 0.411

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 16
- **matched_tokens:** ['atl24', 'bathymetry']

**Full text:**

```
Roughly following the procedures used in airborne bathymetric lidar,
we start with return photon coordinates that assume topograpy, rather than bathymetry, and
then apply refraction correction. The initial coordinates are from ATL03: specifically, the
lat_ph, lon_ph, and h_ph in the /gtx/heights group.
4.2 ATL24 Input Variables
Table 2 captures each stage of the processing phase in the production of the ATL24 granule
and explains the significance of each step. Table 2 also lists the required inputs for that stage
with brief explanation. ATL03, the primary input, provides the heights above the WGS84
ellipsoid (ITRF2014 reference frame, through Release 06 of ATL03, after which ITRF2020
9
```

---

