# Row 13 results: docsearch / example

> Auto-generated. Open this file alongside `13-example-custom-atl06-processing-grand-mesa-review.md` —
> verdicts go there, this side is read-only.

**Query:** `example custom atl06 processing Grand Mesa`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/grandmesa.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** grandmesa tutorial

---

## 📚 docsearch results (top 5)

#### r1 — score 0.726

- **url:** https://docs.slideruleearth.io/assets/grandmesa.html
- **title:** Generating a Custom ATL06 over Grand Mesa, CO
- **section:** Generating a Custom ATL06 over Grand Mesa, CO
- **category:** `tutorial`
- **matched_tokens:** ['atl06', 'custom', 'grand', 'mesa']

**Full text:**

```
Process ATL03 data from the Grand Mesa, CO region and produce a customized ATL06 dataset.
```

#### r2 — score 0.531

- **url:** https://docs.slideruleearth.io/assets/grandmesa.html
- **title:** Generating a Custom ATL06 over Grand Mesa, CO
- **section:** What is demonstrated
- **category:** `tutorial`
- **matched_tokens:** ['atl06', 'grand', 'mesa', 'processing']

**Full text:**

```
The icesat2.atl06p API is used to perform a SlideRule parallel processing request of the Grand Mesa region The icesat2.cmr and icesat2.h5p APIâs are used to manually retrieve specific ATL06 datasets corresponding to the Grand Mesa region The pyproj and shapely packages are used to subset ATL06 data that was manually retrieved The matplotlib package is used to plot the data processed by SlideRule alongside the manually retrieved and subsetted data
```

#### r3 — score 0.567

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Retrieve ATL03 elevations with ATL08 classifications
- **category:** `tutorial`
- **matched_tokens:** ['grand', 'mesa', 'processing']

**Full text:**

```
define a polygon to encompass Grand Mesa, and pick an ATL03 granule that has good coverage over the top of the mesa. Note that this granule was captured at night, under clear-sky conditions. Other granules are unlikely to have results as clear s these. [4]: %%time # build sliderule parameters for ATL03 subsetting request parms = { # processing parameters "srt" : icesat2 .
```

#### r4 — score 0.563

- **url:** https://docs.slideruleearth.io/assets/grandmesa.html
- **title:** Generating a Custom ATL06 over Grand Mesa, CO
- **section:** Points of interest
- **category:** `tutorial`
- **matched_tokens:** ['atl06', 'grand', 'mesa']

**Full text:**

```
The resulting datasets plotted at the bottom of the notebook show that existing ATL06 data is not available for the entire Grand Mesa region. By using the SlideRule API to process ATL03 data and produce a customized ATL06 dataset, elevation data can be returned for the entire region of interest. [1]: import concurrent.futures import time from datetime import datetime import geopandas as gpd import matplotlib.pyplot as plt from pyproj import Transformer from shapely.geometry import Polygon , Point from sliderule import sliderule , icesat2 , earthdata , h5
```

#### r5 — score 0.413

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl06', 'custom', 'example', 'grand', 'mesa', 'processing']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib. ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.441

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 73
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 73
- **matched_tokens:** ['atl06', 'processing']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
1241
Figure 5-1. Flow chart for top-level ATL06 processing
ATL03 PE Project to local
lat, lon, h, coordinates, select
by reference point
RT, PT lat,
h_mean
lon, number Iterative linear fit
and
Background-rate surface-window w_surface_window_final,
refinement dh_fit_dx, h_robust_sprd estimate
ATL03 pulse
shape segment residual
Transmit-pulse histogram
shape
correction
TX_shape
mean, median
Dead-time corrections
estimates
First-photon
bias correction FPB mean,
median Sum
corrections
h_li from
Across-track h_li
other
slope
beam in
calculation
pair dh_fit_dy
Processing chain showing inputs and outputs for ATL06 fitting routine.
1242
1243 5.4 Top-Level Fitting Routine
1244 This routine calls the other routines in the processing chain to derive the final heights and
1245 corrections. It corresponds to all the steps described in 3.2.
1246
1247 Inputs, for each beam, for ATL03 segments m-1 and m:
61
```

#### r2 — score 0.359

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['custom', 'processing']

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

#### r3 — score 0.351

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 2.1 Background
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 13
- **matched_tokens:** ['atl06', 'example', 'processing']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
Temporal Information
1.3.4 Coverage
13 October 2018 to 3 March 2025
Note that satellite maneuvers, data downlink issues, and other events can introduce data gaps into
the ATL03 product. An ongoing list of ATL03 data gaps (.xlsx) can be downloaded from the data
set landing page under Documentation.
1.3.5 Resolution
Each of ICESat-2's 1,387 RGTs is targeted in the polar regions once every 91 days (i.e., the
satellite has a 91-day repeat cycle).
2 DATA ACQUISITION AND PROCESSING
Background
The simplest description of ATL03 is that it provides height, time, latitude, and longitude for all
photon events that ICESat-2 downlinks. It acts as the bridge between the lower level,
instrumentation-specific products and the higher-level, surface-specific products (ATL06 and
above). By design, ATL03 is a single source for all photon data and ancillary information that the
higher-level products need, including spacecraft and instrument parameters. For example, stored
within ATL03 is the ATLAS impulse-response function utilized by the sea ice height and ocean
height algorithms, as well as land ice, sea ice, ocean, land, and inland water surface masks.
Although this information is not explicitly required to generate ATL03, it is included to facilitate
subsequent data products.
The following figure illustrates the suite of ICESat-2 data products and their connections:
Page 12 of 22National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.383

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 23
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 23
- **matched_tokens:** ['atl06', 'processing']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
274 3.2 Outline of processing
275 The outline of the process is as follows for each cycle for each along-track point. First, heights
276 and along-track slopes are calculated for each beam in each pair:
277 1. PEs from the current cycle falling into the along-track bin for the along-track point are
278 collected (3.3)
279 2. The heights and surface windows are iteratively refined (3.3.5.2)
280 3. Corrections and error estimates are calculated based on the edited PEs. ( 3.4, 3.5, 3.6 )
281 Once these steps are complete, based on the height values for the two beams,
282 4. The across-track slope is calculated (3.7)
283 Each of these steps is described in turn below.
284 3.3 PE selection
285 ATL03 provides PE locations and timings for each beam. The first step in ATL06 processing is
286 to select groups of PEs that determine the segment height at each along-track point. Processing
287 is only carried out if the ATL03 podppd_flag indicates that the PE geolocation was of high
288 quality for all pulses in the segment, otherwise the segment is skipped.
289 3.3.1 Along-track segments
290 Our height- and height-change schemes rely on dividing the data into repeatable along-track
291 segments.
```

#### r5 — score 0.381

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 18
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 18
- **matched_tokens:** ['atl06', 'processing']

**Full text:**

```
5 1) and 2) are treated as random errors, and their effects are quantified in the error estimates
166 associated with the products.
167 3) and 4) will produce relatively large errors, and will need to be addressed with consistency
168 checks on the data during the generation of higher-level products.
169 5) will be corrected routinely during ATL06 processing (see Section 3.0).
170 6) and 7) require information about cloud structure and ice-surface conditions that will not be
171 available at the time of processing of ATL06.
```

---

