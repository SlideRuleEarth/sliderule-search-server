# Retrieval POC — Label Audit

Per-query view of what the retriever returned + the actual chunk
text, so you can judge:

- Does the chunk at an `expected_url` actually answer the query?
- Are there chunks returned at top ranks that *also* legitimately
  answer the query but aren't in `expected_urls`?

Top 5 results per query. Chunk text truncated to
~400 characters for readability; full text is in the
chunk's source URL.

Legend:
- `[✓✓]` — full hit (URL match AND, if narrowing fields are set, section/page match)
- `[✓ ]` — URL match only (right doc, but section/page narrowing rejected this chunk)
- `[  ]` — URL not in `expected_urls`

For rows without `expected_sections` or `expected_pages`, URL match
alone is sufficient and shows as `[✓✓]` (no narrowing applied).

## docsearch

### docsearch #1 — `identifier` — ✓ rank 1

**Query:** `atl03x X-Series API photon processing`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html
- https://docs.slideruleearth.io/user_guide/xseries.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl03x`
- `1. atl03`

**Author's note:** identifier lookup; canonical page is user_guide/icesat2.html section on atl03x

**Top 5 returned:**

1. [✓✓] **score 0.625** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1. ATL03 - atl03x**  
    category=`user_guide`

    > The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track…

2. [✓ ] **score 0.629** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **A.1 Segmented Photon Data - atl03sp**  
    category=`user_guide`

    > The photon data is stored as along-track segments inside the ATL03 granules, which is then broken apart by SlideRule and re-segmented according to processing parameters supplied at the time of the request. The new segments are called extents . When the length of an extent is 40 meters, and the step size is 20 meters, the extent matches the ATL06 segments. Most of the time, the photon extents are…

3. [✓ ] **score 0.539** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.4 Ancillary Data**  
    category=`user_guide`

    > The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable…

4. [✓ ] **score 0.501** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **ICESat-2 Module**  
    category=`user_guide`

    > The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR…

5. [  ] **score 0.452** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-15-00.html  
    *section:* **Compatibility Changes**  
    category=`release_notes`

    > The h_mean value in the atl03x API when running the ATL06 surface fitting algorithm was changed from a double to a float. This was to make it consistent with the ATL06 standard data product and to normalize all DataFrames with z columns to floating point precision. The x-series APIs provide a different column for the sample time - time_ns instead of time . This is to reflect that the new time_ns…

---

### docsearch #2 — `identifier` — ✓ rank 3

**Query:** `atl06x surface fit elevation`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html
- https://docs.slideruleearth.io/user_guide/xseries.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl06x`
- `2. atl06`

**Author's note:** user_guide/icesat2.html has 'ATL06 - atl06x' section

**Top 5 returned:**

1. [  ] **score 0.507** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **ATL03 - Global Geolocated Photon Data**  
    category=`background`

    > Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high…

2. [✓ ] **score 0.431** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **A.2 Elevations - atl06p**  
    category=`user_guide`

    > The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from…

3. [✓✓] **score 0.453** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **2. ATL06 - atl06x**  
    category=`user_guide`

    > The SlideRule atl06x endpoint provides a service for ATL06 subsetting and custom processing. This endpoint queries ATL06 input granules for segment heights and locations based on geographic and temporal ranges. The resulting extents are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.

4. [  ] **score 0.419** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **ATL03 - Global Geolocated Photon Data**  
    category=`background`

    > The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of…

5. [  ] **score 0.455** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-15-00.html  
    *section:* **Compatibility Changes**  
    category=`release_notes`

    > The h_mean value in the atl03x API when running the ATL06 surface fitting algorithm was changed from a double to a float. This was to make it consistent with the ATL06 standard data product and to normalize all DataFrames with z columns to floating point precision. The x-series APIs provide a different column for the sample time - time_ns instead of time . This is to reflect that the new time_ns…

---

### docsearch #3 — `identifier` — ✓ rank 1

**Query:** `atl24x bathymetry subsetting`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl24x`
- `5. atl24`

**Author's note:** atl24x is documented in user_guide/icesat2.html section 5 (assets/atl24_access tutorial dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [✓✓] **score 0.691** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5. ATL24 - atl24x**  
    category=`user_guide`

    > The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster…

2. [  ] **score 0.616** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **Background**  
    category=`developer_guide`

    > The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of…

3. [  ] **score 0.555** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **Statistics**  
    category=`developer_guide`

    > 452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea…

4. [  ] **score 0.494** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **2025-03-28: ATL24 Processing Run**  
    category=`developer_guide`

    > Note SlideRule processed ICESat-2 cycles 1 through 25 to produce the first release of the Near-Shore Coastal Bathymetry Product (ATL24) for ICESat-2.

5. [  ] **score 0.578** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .

---

### docsearch #4 — `identifier` — ✓ rank 1

**Query:** `yapc photon classifier`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `yapc`

**Author's note:** yapc = Yet Another Photon Classifier; user_guide/icesat2.html has the section (assets/grandmesa tutorial dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [✓✓] **score 0.792** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.2 YAPC Classification**  
    category=`user_guide`

    > The experimental YAPC (Yet Another Photon Classifier) photon-classification scheme assigns each photon a score based on the number of adjacent photons. YAPC parameters are provided as a dictionary, with entries described below: yapc : settings for the yapc algorithm; if provided then SlideRule will execute the YAPC classification on all photons score : the minimum yapc classification score of a…

2. [✓ ] **score 0.656** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2 Photon-selection Parameters**  
    category=`user_guide`

    > Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements…

3. [✓ ] **score 0.457** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.6.1 PhoREAL Parameters**  
    category=`user_guide`

    > The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the…

4. [✓ ] **score 0.461** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1. ATL03 - atl03x**  
    category=`user_guide`

    > , 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident…

5. [✓ ] **score 0.418** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **A.1 Segmented Photon Data - atl03sp**  
    category=`user_guide`

    > The GeoDataFrame for each photon extent has the following columns: track : reference pair track number (1, 2, 3) sc_orient : spacecraft orientation (0: backwards, 1: forwards) rgt : reference ground track cycle : cycle segment_id : segment ID of first ATL03 segment in result segment_dist : along track distance from the equator to the center of the extent (in meters) count : the number of photons…

---

### docsearch #5 — `identifier` — ✓ rank 1

**Query:** `cnf confidence filter parameter`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/icesat2.html
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `native atl03`
- `photon-selection`
- `atl06p`
- `atl03sp`
- `atl06sp`

**Author's note:** cnf heavily in api_reference/icesat2.html atl06p section

**Top 5 returned:**

1. [✓✓] **score 0.315** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.1 Native ATL03 Photon Classification**  
    category=`user_guide`

    > ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence…

2. [✓ ] **score 0.331** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5.1 Query Parameters**  
    category=`user_guide`

    > The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid…

3. [  ] **score 0.227** — https://docs.testsliderule.org/user_guide/basic_usage.html  
    *section:* **Define the Request Parameters**  
    category=`user_guide`

    > When making a request to the SlideRule servers, the parameters of the request (i.e. what the user wants to process and how they want to process it) are supplied in the body of the request as a JSON structure. When using the SlideRule Python client, the parameters are captured and provided by the user in a Python dictionary, and the dictionary is automatically serialized into a JSON structure by…

4. [  ] **score 0.237** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-04-00.html  
    *section:* **New Features**  
    category=`release_notes`

    > v4.4.0 - Resources are queried from servers instead of client. If a processing request does not include a list of resources to process, the server processing the request will query CMR and populate the resources parameter. In addition, any sampling requests that need a populated catalog parameter will also be queried on the server side and have that parameter populated. v4.4.0 - 389 and 383 -…

5. [✓ ] **score 0.261** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **2. ATL06 - atl06x**  
    category=`user_guide`

    > and the along-track segment fit meters (float) land_ice_segments/fit_statistics/h_robust_sprd w_surface_window_final Width of the surface window, top to bottom meters (float) land_ice_segments/fit_statistics/w_surface_window_final bsnow_conf Confidence flag for presence of blowing snow boolean land_ice_segments/geophysical/bsnow_conf bsnow_h Blowing snow layer top height meters (float)…

---

### docsearch #6 — `identifier` — ✗ rank 17

**Query:** `srt surface reference type parameter`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `native atl03`
- `photon-selection`
- `atl06p`
- `atl03sp`

**Author's note:** srt parameter for surface type filter (user_guide/how_tos/ancillary_fields dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.337** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **2. ATL06 - atl06x**  
    category=`user_guide`

    > and the along-track segment fit meters (float) land_ice_segments/fit_statistics/h_robust_sprd w_surface_window_final Width of the surface window, top to bottom meters (float) land_ice_segments/fit_statistics/w_surface_window_final bsnow_conf Confidence flag for presence of blowing snow boolean land_ice_segments/geophysical/bsnow_conf bsnow_h Blowing snow layer top height meters (float)…

2. [  ] **score 0.300** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1. ATL03 - atl03x**  
    category=`user_guide`

    > , 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident…

3. [  ] **score 0.294** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **4. ATL13 - atl13x**  
    category=`user_guide`

    > The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via:…

4. [  ] **score 0.323** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.4 ATL24 Classification**  
    category=`user_guide`

    > If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph…

5. [  ] **score 0.272** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.1 Native ATL03 Photon Classification**  
    category=`user_guide`

    > ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence…

---

### docsearch #7 — `conceptual` — ✓ rank 2

**Query:** `how to filter ICESat-2 photons by confidence`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/icesat2.html
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `native atl03`
- `photon-selection`
- `atl06p`
- `atl03sp`

**Author's note:** photon confidence filtering via cnf

**Top 5 returned:**

1. [✓ ] **score 0.515** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **ICESat-2 Module**  
    category=`user_guide`

    > The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR…

2. [✓✓] **score 0.542** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.1 Native ATL03 Photon Classification**  
    category=`user_guide`

    > ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence…

3. [✓ ] **score 0.432** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5.1 Query Parameters**  
    category=`user_guide`

    > The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid…

4. [  ] **score 0.438** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **ATL03 - Global Geolocated Photon Data**  
    category=`background`

    > Some photons will be returns from the Transmit Echo Path (TEP) Some photons are from the ATLAS instrument that have reflected off the surface or vegetation (these are our signal photons). The ATLAS instrument receives a vast amount of data and decides on-board whether or not to telemeter packets of received photons back to Earth. ATLAS uses a digital elevation model (DEM) and a few simple rules…

5. [  ] **score 0.471** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **ATL03 - Global Geolocated Photon Data**  
    category=`background`

    > The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three…

---

### docsearch #8 — `conceptual` — ✓ rank 2

**Query:** `how to run atl06 with raster DEM sampling`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/raster_sampling.html

**Author's note:** pairing ATL06 with raster sampling (how_tos/arcticdem_request dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.461** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **2. ATL06 - atl06x**  
    category=`user_guide`

    > The SlideRule atl06x endpoint provides a service for ATL06 subsetting and custom processing. This endpoint queries ATL06 input granules for segment heights and locations based on geographic and temporal ranges. The resulting extents are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.

2. [✓✓] **score 0.414** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Overview**  
    category=`user_guide`

    > SlideRule supports sampling raster data at points of interest and including those sampled values alongside its customized data products. For instance, when performing an ATL06-SR processing run ( atl06p ), the returned GeoDataFrame has a row for each calculated elevation; that row can also include values from different raster datasets that have been sampled at the geolocation of the calculated…

3. [  ] **score 0.422** — https://docs.testsliderule.org/developer_guide/release_notes/release-v03-03-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > Sampling support added for the Merit DEM Added raster module to Python client - returns GeoDataFrame of sampled raster points of interest

4. [  ] **score 0.441** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks…

5. [  ] **score 0.449** — https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html  
    *section:* **SRWC-5.1: Raster Sampling**  
    category=`developer_guide`

    > The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land…

---

### docsearch #9 — `conceptual` — ✓ rank 1

**Query:** `how to use SlideRule Python client install`

**Expected URL(s):**
- https://docs.slideruleearth.io/getting_started/Install.html
- https://docs.slideruleearth.io/user_guide/basic_usage.html
- https://docs.slideruleearth.io/getting_started/Getting-Started.html

**Author's note:** Python client install + basic usage

**Top 5 returned:**

1. [✓✓] **score 0.897** — https://docs.testsliderule.org/getting_started/Install.html  
    *section:* **PyPI**  
    category=`getting_started`

    > Alternatively, you can use the PyPI package manager to install the SlideRule Python client. This is not the recommended way of installing, but is made available as an option for users who prefer to work with pip . pip install sliderule

2. [✓✓] **score 0.804** — https://docs.testsliderule.org/getting_started/Install.html  
    *section:* **Installation**  
    category=`getting_started`

    > The recommended way of installing the SlideRule Python client is to use the Conda Python package manager. conda install -c conda-forge sliderule In order to run the example notebooks , we provide an environment.yml that can be used to create an initial conda environment that has the SlideRule Python client installed along with all the dependencies necessary to run the examples. To install the…

3. [✓✓] **score 0.765** — https://docs.testsliderule.org/getting_started/Install.html  
    *section:* **Developer Install**  
    category=`getting_started`

    > For developers and contributors, to get the latest unreleased version of the Python client, the contents of the sliderule repository can be cloned or download as a zipped file . If cloning, please consider forking into your own account before cloning onto your system. Warning The main branch is used for the public cluster running at slideruleearth.io . Private clusters may be running versions of…

4. [  ] **score 0.630** — https://docs.testsliderule.org/developer_guide/release_notes/release-v01-04-00.html  
    *section:* **Required Updates**  
    category=`release_notes`

    > v1.4.0 - In order to use the latest SlideRule server deployments, the Python client must be updated. For conda users: $ conda update sliderule For developer installs: $ cd sliderule-python $ git checkout main $ git pull $ python3 setup.py install v1.4.0 - User scripts that use the Python client need to make the following updates: The track keyword argument of atl03sp , atl03s , atl06p , and atl06…

5. [  ] **score 0.707** — https://docs.testsliderule.org/api_reference/gedi.html  
    *section:* **init**  
    category=`api_reference`

    > sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()

---

### docsearch #10 — `conceptual` — ✓ rank 3

**Query:** `what is the X-Series API in SlideRule`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/xseries.html
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `icesat-2 module`
- `atl03x`
- `atl06x`
- `atl08x`
- `atl13x`
- `atl24x`

**Author's note:** X-Series concept page

**Top 5 returned:**

1. [✓ ] **score 0.654** — https://docs.testsliderule.org/user_guide/xseries.html  
    *section:* **X-Series APIs**  
    category=`user_guide`

    > Note This page documents the x-series APIs that are specifically geared for generating and processing DataFrames. These APIs were made public in early 2025 starting with version 4.11.0, and have a common methodology for processing the data which makes interfacing to them consistent across multiple datasets. Much of the functionality described here is duplicated in older-style p-series and…

2. [  ] **score 0.542** — https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html  
    *section:* **SRWC-4.3: Tutorial**  
    category=`developer_guide`

    > The UI shall provide a tutorial that guides a user through a series of steps necessary to make a basic SlideRule request and interact with the data.

3. [✓✓] **score 0.510** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **ICESat-2 Module**  
    category=`user_guide`

    > The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR…

4. [  ] **score 0.562** — https://docs.testsliderule.org/developer_guide/articles/plugins.html  
    *section:* **Components of a Plugin**  
    category=`developer_guide`

    > A SlideRule plugin consists of three components: (1) a shared object, (2) lua extension scripts, (3) lua api scripts.

5. [  ] **score 0.551** — https://docs.testsliderule.org/api_reference/sliderule.html  
    *section:* **sliderule**  
    category=`api_reference`

    > The SlideRule Python API sliderule.py is used to access the services provided by the base SlideRule server. From Python, the module can be imported via: import sliderule

---

### docsearch #11 — `conceptual` — ✓ rank 5

**Query:** `earthdata authentication credentials sliderule`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/earthdata.html
- https://docs.slideruleearth.io/background/NASA-Earthdata.html

**Author's note:** earthdata authentication setup

**Top 5 returned:**

1. [  ] **score 0.653** — https://docs.testsliderule.org/developer_guide/articles/security_model.html  
    *section:* **Overview**  
    category=`developer_guide`

    > SlideRule Earth leverages GitHub authentication and account membership status within the GitHub SlideRuleEarth organization to authorize access to SlideRule services. Credentials are provided by users using a JSON Web Token (JWT) issued by the SlideRule Earth login service ( login.slideruleearth.io ). A userâs JWT contains claims used and verified by SlideRule services to allow access.

2. [  ] **score 0.566** — https://docs.testsliderule.org/developer_guide/articles/private_clusters.html  
    *section:* **SlideRule Authenticator**  
    category=`developer_guide`

    > The SlideRule Authenticator is an AWS Lambdaâbased authentication service that delegates user authentication to GitHub. User login requests are redirected to GitHubâs authorization endpoint, where credentials are verified by GitHub. Upon successful authentication, GitHub returns an authorization grant that the service exchanges for an access token to establish the userâs identity. The…

3. [  ] **score 0.613** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Overview**  
    category=`user_guide`

    > The second step of obtaining credentials also requires some specialized code, but since most of our datasets are in AWS and authenticated through NASA DAACs, most of the authentication code is generic. But even still, because of this, each raster dataset supported by SlideRule needs to be registered with SlideRule ahead of time and provided in what we call an Asset Directory.

4. [  ] **score 0.492** — https://docs.testsliderule.org/developer_guide/how_tos/amazon_linux_arm_setup.html  
    *section:* **2-Factor Authentication**  
    category=`developer_guide`

    > Make sure to setup an initial .aws/credentials file so that it has the sliderule profile access key and secret access key. The credentials file will look something like: [ default ] aws_access_key_id = _ aws_secret_access_key = _ aws_session_token = _ [ sliderule ] aws_access_key_id = _ aws_secret_access_key = _ To populate the default keys and session token, run: aws --profile = sliderule sts…

5. [✓✓] **score 0.574** — https://docs.testsliderule.org/background/NASA-Earthdata.html  
    *section:* **Steps to Sync from NSIDC**  
    category=`background`

    > Register with NASA Earthdata Login system After registering, login to the system Add NSIDC_DATAPOOL_OPS and nsidc-daacdata applications to Earthdata Copy your NASA Earthdata credentials or create a .netrc file to store your credentials permanently echo "machine urs.earthdata.nasa.gov login <uid> password <password>" >> ~/.netrc chmod 0600 ~/.netrc

---

### docsearch #12 — `conceptual` — ✓ rank 2

**Query:** `output SlideRule results as GeoParquet format`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/arrow_output.html

**Author's note:** GeoParquet output format (how_tos/geoparquet_output dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.711** — https://docs.testsliderule.org/developer_guide/articles/geoparquet.html  
    *section:* **Overview**  
    category=`developer_guide`

    > SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters…

2. [✓✓] **score 0.632** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **Parameters**  
    category=`user_guide`

    > To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported,…

3. [✓✓] **score 0.638** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **Overview**  
    category=`user_guide`

    > By default, SlideRule returns all processing results in a native (i.e. custom to SlideRule) format as soon as they are generated. Those results are streamed back to the client and used by the client to construct a (Geo)DataFrame that is presented to the user. But sometimes it is desirable to have SlideRule build a (Geo)DataFrame on the server, and then stream that dataframe back to the client for…

4. [  ] **score 0.605** — https://docs.testsliderule.org/developer_guide/articles/geoparquet.html  
    *section:* **Constraints**  
    category=`developer_guide`

    > Currently, only support for the atl06 , atl08 , and flattened atl03 records is provided. This means that the ICESat-2 compact parameter being set is not supported when outputting to GeoParquet, and the atl03 results may look slightly different between native runs and runs that request the GeoParquet format. The results in the GeoParquet file are not sorted. The SlideRule server side version…

5. [  ] **score 0.710** — https://docs.testsliderule.org/developer_guide/articles/geoparquet.html  
    *section:* **2023-02-24: GeoParquet**  
    category=`developer_guide`

    > Warning SlideRule now supports returning results back to data users as GeoParquet files. The functionality described in this article has been improved with broad support for returning data via Apache Arrow based formats.

---

### docsearch #13 — `example` — ✗ rank 12

**Query:** `how to process atl06 elevations`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl06x`
- `2. atl06`

**Author's note:** rebaselined for testsliderule.org: assets/grandmesa.html removed; user_guide section on atl06 is closest substitute

**Top 5 returned:**

1. [  ] **score 0.569** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl06**  
    category=`api_reference`

    > sliderule.icesat2. atl06 ( parm , resource ) [source] Performs ATL06-SR processing on ATL03 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated elevations (see Elevations ) Return type : GeoDataFrame

2. [  ] **score 0.565** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl08**  
    category=`api_reference`

    > sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame

3. [  ] **score 0.475** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl06sp**  
    category=`api_reference`

    > Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges…

4. [  ] **score 0.517** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl06s**  
    category=`api_reference`

    > sliderule.icesat2. atl06s ( parm , resource ) [source] Subsets ATL06 data given the polygon and time range provided and returns elevations Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) resource ( str ) â ATL06 HDF5 filename Returns : ATL06 elevations Return type : GeoDataFrame

5. [  ] **score 0.521** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks…

---

### docsearch #14 — `example` — ✓ rank 1

**Query:** `how to use yapc photon classifier in atl03`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `yapc`
- `atl03`

**Author's note:** rebaselined for testsliderule.org: assets/grandmesa_atl03_classification.html removed; user_guide yapc/atl03 sections are closest substitute

**Top 5 returned:**

1. [✓✓] **score 0.733** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.2 YAPC Classification**  
    category=`user_guide`

    > The experimental YAPC (Yet Another Photon Classifier) photon-classification scheme assigns each photon a score based on the number of adjacent photons. YAPC parameters are provided as a dictionary, with entries described below: yapc : settings for the yapc algorithm; if provided then SlideRule will execute the YAPC classification on all photons score : the minimum yapc classification score of a…

2. [✓ ] **score 0.784** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2 Photon-selection Parameters**  
    category=`user_guide`

    > Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements…

3. [✓✓] **score 0.479** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1. ATL03 - atl03x**  
    category=`user_guide`

    > , 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident…

4. [  ] **score 0.496** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **References**  
    category=`background`

    > ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03

5. [✓ ] **score 0.424** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.6.1 PhoREAL Parameters**  
    category=`user_guide`

    > The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the…

---

### docsearch #15 — `example` — ✓ rank 2

**Query:** `how to sample ArcticDEM raster mosaic`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/raster_sampling.html

**Author's note:** rebaselined for testsliderule.org: assets/arcticdem_mosaic.html and how_tos/arcticdem_request.html both removed; raster_sampling page is closest substitute

**Top 5 returned:**

1. [  ] **score 0.522** — https://docs.testsliderule.org/developer_guide/articles/gdal_vrt_benchmark.html  
    *section:* **Overview**  
    category=`developer_guide`

    > Test reads elevation value from ArcticDem. POI is lon: -74.60 lat: 82.86 Method used vrt file created from mosaic rasters, version 3.0, 2m, hosted on AWS. The mosaic.vrt file is stored locally on aws dev server at /data/ArcticDem/mosaic.vrt The actual raster containing the elevation for POI is: /vsis3/pgc-opendata-dems/arcticdem/mosaics/v3.0/2m/34_37/34_37_1_1_2m_v3.0_reg_dem.tif The elevation…

2. [✓✓] **score 0.533** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Parameters**  
    category=`user_guide`

    > ds that should be treated as elevation bands which allows a 3D transform to be applied key_space : 64-bit integer defining the upper 32-bits of the file_id ; this in general should never be set as the server will typically do the right thing assigning a key space; but for users that are parallelizing requests on the client-side, this parameter can be usedful when constructing the resulting file…

3. [  ] **score 0.568** — https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html  
    *section:* **SRWC-5.1: Raster Sampling**  
    category=`developer_guide`

    > The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land…

4. [  ] **score 0.435** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks…

5. [  ] **score 0.517** — https://docs.testsliderule.org/developer_guide/articles/gdal_vrt_benchmark.html  
    *section:* **2022-11-10: VRT Performance Benchmarking**  
    category=`developer_guide`

    > Note GDAL VRT performance was benchmarked using the ArcticDEM mosaic dataset.

---

### docsearch #16 — `example` — ✓ rank 3

**Query:** `how to subset atl24 bathymetry data`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl24x`
- `5. atl24`

**Author's note:** rebaselined for testsliderule.org: assets/atl24_access.html removed; user_guide section on atl24x is closest substitute

**Top 5 returned:**

1. [  ] **score 0.689** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .

2. [  ] **score 0.580** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **Background**  
    category=`developer_guide`

    > The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of…

3. [✓✓] **score 0.675** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5. ATL24 - atl24x**  
    category=`user_guide`

    > The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster…

4. [✓ ] **score 0.602** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.4 ATL24 Classification**  
    category=`user_guide`

    > If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph…

5. [  ] **score 0.536** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **Statistics**  
    category=`developer_guide`

    > 452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea…

---

### docsearch #17 — `example` — ✗ rank 6

**Query:** `how to query atl13 lake by name`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl13x`
- `4. atl13`

**Author's note:** rebaselined for testsliderule.org: assets/atl13_access.html removed; user_guide section on atl13x is closest substitute

**Top 5 returned:**

1. [  ] **score 0.599** — https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html  
    *section:* **Example Use Case - ATL13 Lake ID Mapping**  
    category=`developer_guide`

    > The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13…

2. [✓ ] **score 0.762** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **4.1 Inland Lake Parameters**  
    category=`user_guide`

    > Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}

3. [  ] **score 0.669** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .

4. [  ] **score 0.422** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-14-00.html  
    *section:* **New/Improved Functionality**  
    category=`release_notes`

    > Arbitrary Code Execution - /source/ace API for executing user supplied lua scripts; only available on private clusters. Asset Metadata Service - /manager/ams API for querying metadata directly from SlideRule; only ATL13 currently supported. ATL13 - /source/atl13x API for subsetting the ATL13 standard data product; in addition to normal temporal/spatial subsetting requests, SlideRule also supports…

5. [  ] **score 0.373** — https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html  
    *section:* **Example Use Case - ATL13 Lake ID Mapping**  
    category=`developer_guide`

    > Given a user query, the ATL13 global database can be used to get a reference ID, and the reverse lookup table can be used to get all of the granules with data for that reference ID. The first option was the simplest but suffered from relying on CMR which is relatively slow and the possibility of having granules returned for other nearby bodies of water due to buffering on the along-track polygons…

---

### docsearch #18 — `version_history` — ✓ rank 1

**Query:** `when was atl24x added to sliderule release`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-11-00.html

**Author's note:** atl24x major change in v04-11-00

**Top 5 returned:**

1. [✓✓] **score 0.656** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-11-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > v4.11.0 - The official release of the SlideRule Web Client at https://client.slideruleearth.io v4.11.0 - The atl03x endpoint is being previewed. This implements a dataframe model for the data instead of a streaming model. v4.11.0 - The atl24x endpoint provides subsetting support for the ATL24 standard data product.

2. [  ] **score 0.638** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5. ATL24 - atl24x**  
    category=`user_guide`

    > The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster…

3. [  ] **score 0.586** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5.2 Ancillary Data**  
    category=`user_guide`

    > Ancillary data returned from the atl24x endpoint comes from the {beam} group of the ATL24 granules. anc_fields : fields in the beam group of the ATL24 granule, provided as a list of strings For example, parms = { "anc_fields" : [ "index_ph" ], } gdf = sliderule . run ( "atl24x" , parms )

4. [  ] **score 0.462** — https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html  
    *section:* **New Functionality**  
    category=`release_notes`

    > Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and…

5. [  ] **score 0.635** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **2025-12-08: Public Cluster Release v5**  
    category=`developer_guide`

    > Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.

---

### docsearch #19 — `version_history` — ✗ rank 9

**Query:** `yapc added to sliderule version release notes`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-03-00.html
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-04-00.html

**Author's note:** yapc introduced in v01.03-v01.04 range

**Top 5 returned:**

1. [  ] **score 0.537** — https://docs.testsliderule.org/developer_guide/articles/private_clusters.html  
    *section:* **2026-01-20: Private Clusters**  
    category=`developer_guide`

    > Note With release v5.0.2, SlideRule has transitioned the management of private clusters from the django-based SlideRule Provisioning System which was deployed in AWS ECS, to the pure Python-based SlideRule Authenticator and SlideRule Provisioner which are deployed via AWS Lambda. The main functions of the original system have been preserved, with a change in focus on clusters for individual users…

2. [  ] **score 0.502** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **2025-12-08: Public Cluster Release v5**  
    category=`developer_guide`

    > Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.

3. [  ] **score 0.492** — https://docs.testsliderule.org/developer_guide/release_notes/release-v03-05-00.html  
    *section:* **Release v3.5.x**  
    category=`release_notes`

    > 2023-06-09 Version description of the v3.5.0 release of ICESat-2 SlideRule. This document also captures functionality added in versions v3.4.0 and v3.4.1.

4. [  ] **score 0.447** — https://docs.testsliderule.org/developer_guide/release_notes/web-release-v04-00-03.html  
    *section:* **Summary**  
    category=`release_notes`

    > ð SlideRule Web Client v4.0.3 Release Notes Changes since v3.8.0 Infrastructure CloudFront + Route 53 terraform modules added to support hosting the landing page at the root domain New Features Landing Page - The web client now serves as the SlideRule Earth landing page at slideruleearth.io, featuring a hero section with wallpaper image, About/Contact info panels, and a News tab that pulls…

5. [  ] **score 0.526** — https://docs.testsliderule.org/developer_guide/release_notes/release-v01-01-00.html  
    *section:* **Release v1.1.x**  
    category=`release_notes`

    > 2021-10-13 Version description of the v1.1.5 release of ICESat-2 SlideRule.

---

### docsearch #20 — `version_history` — ✓ rank 3

**Query:** `sliderule version 5 breaking changes new functionality`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html

**Author's note:** v5.0.0 release notes

**Top 5 returned:**

1. [  ] **score 0.515** — https://docs.testsliderule.org/developer_guide/release_notes/release-v02-00-00.html  
    *section:* **New Features**  
    category=`release_notes`

    > Version 2.0.0 of SlideRule represents a major change to the SlideRule architecture and is NOT backward compatible with any of the previous releases. The following is a list of changes in this major release. New Domain : SlideRule has moved from http://icesat2sliderule.org to https://slideruleearth.io . This change was made to reflect the new scope of SlideRule which includes datasets (e.g.…

2. [  ] **score 0.454** — https://docs.testsliderule.org/user_guide/versioning.html  
    *section:* **Library Version ( version )**  
    category=`user_guide`

    > The SlideRule executable version (called the Library Version in the code) is the semantic version used by the SlideRule team to identify a release of SlideRule. It uses the following convention: vX.Y.Z where: X is the major version; when incremented it indicates a break in backward compatibility. Y is the minor version; when incremented it indicates new or significantly changed functionality Z is…

3. [✓✓] **score 0.394** — https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html  
    *section:* **Breaking Changes**  
    category=`release_notes`

    > All calls to session.manager should no longer be used as that functionality will cease in future releases. v5.0.3 - The main Python module sliderule no longer creates a default session on import but requires either sliderule.init() or sliderule.create_session() . The creation of a default session was confusing when users called sliderule.init() which then created a second session. This caused odd…

4. [  ] **score 0.526** — https://docs.testsliderule.org/user_guide/versioning.html  
    *section:* **Note on Reproducibility**  
    category=`user_guide`

    > It is the goal of the SlideRule development team to create a system where results are able to be reproduced; but this is often times either extremely difficult or impossible for reasons outside of the teams control. SlideRule relies on publicly hosted datasets. When those datasets are updated, older versions of the datasets are often removed. For instance, ICESat-2 Standard Data Products have a…

5. [  ] **score 0.525** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **2025-12-08: Public Cluster Release v5**  
    category=`developer_guide`

    > Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.

---

### docsearch #21 — `version_history` — ✓ rank 4

**Query:** `recent changes to atl06x release notes`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-03-00.html

**Author's note:** atl06x mentioned in v05-00-00 and v05-03-00

**Top 5 returned:**

1. [  ] **score 0.466** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **2025-12-08: Public Cluster Release v5**  
    category=`developer_guide`

    > Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.

2. [  ] **score 0.472** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **TL;DR**  
    category=`developer_guide`

    > ps.slideruleearth.io has been retired and replaced by provisioner.slideruleearth.io There are breaking changes (which will hopefully be minimal because they involved features that have been deprecated for some time) ATL24 release 002 is now the default The internal Asset Metadata Service is used for ATL24, ATL13, and 3DEP (only when specified) Earthdata error reporting was made more intuitive h5p…

3. [  ] **score 0.474** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-11-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > v4.11.0 - The official release of the SlideRule Web Client at https://client.slideruleearth.io v4.11.0 - The atl03x endpoint is being previewed. This implements a dataframe model for the data instead of a streaming model. v4.11.0 - The atl24x endpoint provides subsetting support for the ATL24 standard data product.

4. [✓✓] **score 0.398** — https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html  
    *section:* **New Functionality**  
    category=`release_notes`

    > Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and…

5. [  ] **score 0.465** — https://docs.testsliderule.org/developer_guide/release_notes/release-v05-02-00.html  
    *section:* **Issues Resolved**  
    category=`release_notes`

    > v5.2.0 - ATL09 and ATL13 supported release updated to 007 v5.2.1 - Various fixes/improvements for authenticator v5.2.1 - AMS update to support latest version of DuckDB (changes in spatial functionality)

---

### docsearch #22 — `api_lookup` — ✓ rank 1

**Query:** `GEDI L4A python API parameters`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/gedi.html

**Expected sections** (case-insensitive substring on chunk.section):
- `gedi04ap`
- `gedi04a`

**Author's note:** GEDI module api reference; query uses human-facing product name not the gedi04ap identifier

**Top 5 returned:**

1. [✓✓] **score 0.564** — https://docs.testsliderule.org/api_reference/gedi.html  
    *section:* **gedi04a**  
    category=`api_reference`

    > sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame

2. [  ] **score 0.538** — https://docs.testsliderule.org/developer_guide/release_notes/release-v03-01-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks:…

3. [  ] **score 0.459** — https://docs.testsliderule.org/user_guide/gedi.html  
    *section:* **1. Overview**  
    category=`user_guide`

    > The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be…

4. [✓ ] **score 0.532** — https://docs.testsliderule.org/api_reference/gedi.html  
    *section:* **gedi**  
    category=`api_reference`

    > The GEDI Python API gedi.py is used to access the services provided by the gedi plugin for SlideRule. From Python, the module can be imported via: from sliderule import gedi

5. [✓ ] **score 0.516** — https://docs.testsliderule.org/api_reference/gedi.html  
    *section:* **init**  
    category=`api_reference`

    > sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()

---

### docsearch #23 — `api_lookup` — ✓ rank 1

**Query:** `raster sampling API function parameters`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/raster.html
- https://docs.slideruleearth.io/user_guide/raster_sampling.html

**Author's note:** raster module api reference

**Top 5 returned:**

1. [✓✓] **score 0.497** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Parameters**  
    category=`user_guide`

    > losest_time : time used to filter rasters to be sampled; only the raster that is closest in time to the provided time will be sampled - can be multiple rasters if they all share the same time (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z) use_poi_time : overrides the âclosest_timeâ setting (or provides one if not set) with the time associated with the point of interest being sampled…

2. [✓✓] **score 0.701** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Parameters**  
    category=`user_guide`

    > To request raster sampling, the samples parameter must be populated as a dictionary in the request.

3. [  ] **score 0.442** — https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html  
    *section:* **SRWC-3.3: Advanced Mode**  
    category=`developer_guide`

    > In advanced mode, the control panel shall display the following controls All control elements present in basic mode Resource query parameter controls specific to the API that has been selected that allow a user to make a processing request without an area of interest A list of parameter controls specific to the API that has been selected; the parameter controls are grouped into exandable category…

4. [✓✓] **score 0.494** — https://docs.testsliderule.org/user_guide/raster_sampling.html  
    *section:* **Parameters**  
    category=`user_guide`

    > Each key in the dictionary is used to label the data returned for that raster in the returned DataFrame. samples : dictionary of rasters to sample <key> : user supplied name used to identify results returned from sampling this raster asset : name of the raster (as supplied in the Asset Directory) to be sampled algorithm : algorithm to use to sample the raster; the available algorithms for…

5. [  ] **score 0.414** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-00-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > v4.0.0 - Added new capability to subset rasters. The subsets endpoint subsets rasters and returns the data back to the user. It works in conjunction with the raster.subset Python API. v4.0.0 - Added new opendata plugin that supports sampling the ESA World Cover 10m dataset. v4.0.0 - The Python client supports returning a GeoDataFrame with 3D point geometry. The user must supply a âheightâ…

---

### docsearch #24 — `paraphrased` — ✓ rank 1

**Query:** `getting canopy height from atl03 photons using atl08`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl08 classification`
- `phoreal`
- `1.2.3 atl08`
- `1.6 phoreal`
- `3. atl08`

**Author's note:** phoreal / atl08_class usage (assets/phoreal + grandmesa_atl03_classification dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [✓✓] **score 0.688** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.3 ATL08 Classification**  
    category=`user_guide`

    > If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class…

2. [✓ ] **score 0.513** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **A.1 Segmented Photon Data - atl03sp**  
    category=`user_guide`

    > The GeoDataFrame for each photon extent has the following columns: track : reference pair track number (1, 2, 3) sc_orient : spacecraft orientation (0: backwards, 1: forwards) rgt : reference ground track cycle : cycle segment_id : segment ID of first ATL03 segment in result segment_dist : along track distance from the equator to the center of the extent (in meters) count : the number of photons…

3. [✓✓] **score 0.651** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.6 PhoREAL Algorithm**  
    category=`user_guide`

    > The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .

4. [✓ ] **score 0.627** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1. ATL03 - atl03x**  
    category=`user_guide`

    > The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track…

5. [✓✓] **score 0.449** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.6 PhoREAL Algorithm**  
    category=`user_guide`

    > This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) dist_ph_along +…

---

### docsearch #25 — `paraphrased` — ✓ rank 1

**Query:** `add ancillary fields to sliderule atl06 output`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/icesat2.html
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `anc_fields`
- `ancillary`
- `atl06p`

**Author's note:** rebaselined for testsliderule.org: how_tos/ancillary_fields removed; anc_fields parameter is documented in api_reference/icesat2.html atl06p signature

**Top 5 returned:**

1. [✓✓] **score 0.529** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **2.1 Ancillary Data**  
    category=`user_guide`

    > Ancillary data returned from the atl06x endpoint (as well as atl06 and atl06p endpoints) come from the land_ice_segments group of the ATL06 granules. The data is mostly returned as-is, with one exception. Double-precision and single-precision floating point variables are checked to see if they contain the maximum value of their respective encodings, and if so, a floating point NaN (not-a-number)…

2. [  ] **score 0.472** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-01-00.html  
    *section:* **Release v4.1.x**  
    category=`release_notes`

    > 2023-12-07 Version description of the v4.1.0 release of ICESat-2 SlideRule. * Important : This version requires an update of the Python client to use. The underlying mechanism used in support of including ancillary fields in processing requests was updated to support both the PhoREAL algorithm and the ATL06 subsetter. As a result, in order to include ancillary field requests in your code, you…

3. [✓✓] **score 0.681** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **3.2 Ancillary Data**  
    category=`user_guide`

    > Ancillary data returned from the atl08x endpoint (as well as atl08 and atl08p endpoints) come from the {beam} group of the ATL08 granules. atl08_fields : fields in the beam group of the ATL08 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "asr" ], } gdf = sliderule . run ( "atl08x" , parms )

4. [✓✓] **score 0.637** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **5.2 Ancillary Data**  
    category=`user_guide`

    > Ancillary data returned from the atl24x endpoint comes from the {beam} group of the ATL24 granules. anc_fields : fields in the beam group of the ATL24 granule, provided as a list of strings For example, parms = { "anc_fields" : [ "index_ph" ], } gdf = sliderule . run ( "atl24x" , parms )

5. [✓✓] **score 0.629** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **4.2 Ancillary Data**  
    category=`user_guide`

    > Ancillary data returned from the atl13x endpoint comes from the {beam} group of the ATL13 granules. atl13_fields : fields in the beam group of the ATL13 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "ice_flag" ], } gdf = sliderule . run ( "atl13x" , parms )

---

### docsearch #26 — `api_lookup` — ✓ rank 2

**Query:** `sliderule module initialization session setup`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/sliderule.html

**Expected sections** (case-insensitive substring on chunk.section):
- `init`
- `sliderule`
- `set_url`

**Author's note:** sliderule module api reference

**Top 5 returned:**

1. [  ] **score 0.564** — https://docs.testsliderule.org/developer_guide/release_notes/release-v05-00-00.html  
    *section:* **Breaking Changes**  
    category=`release_notes`

    > All calls to session.manager should no longer be used as that functionality will cease in future releases. v5.0.3 - The main Python module sliderule no longer creates a default session on import but requires either sliderule.init() or sliderule.create_session() . The creation of a default session was confusing when users called sliderule.init() which then created a second session. This caused odd…

2. [✓✓] **score 0.589** — https://docs.testsliderule.org/api_reference/sliderule.html  
    *section:* **set_url**  
    category=`api_reference`

    > sliderule. set_url ( domain , session = None ) [source] Configure sliderule package with URL of service Parameters : urls ( str ) â IP address or hostname of SlideRule service (note, there is a special case where the url is provided as a list of strings instead of just a string; when a list is provided, the client hardcodes the set of servers that are used to process requests to the exact set…

3. [  ] **score 0.487** — https://docs.testsliderule.org/user_guide/versioning.html  
    *section:* **Python Client**  
    category=`user_guide`

    > To get the version of the SlideRule Python Client: from sliderule import version version . version When the SlideRule Python Client init() function is called, it issues a get_version() request to the SlideRule cluster and then checks that the client version is compatible with the server version. If there is a major version difference, the initialization function will return an error. If there is…

4. [  ] **score 0.583** — https://docs.testsliderule.org/developer_guide/articles/private_clusters.html  
    *section:* **Access**  
    category=`developer_guide`

    > Users configure the SlideRule Python client to communicate with their private cluster when the client is initialized. For session based configuration, the following code initializes the client to talk to <my_cluster> : import sliderule session = sliderule . create_session ( cluster = "<my_cluster>" ) For functional configuration, the following code initializes the client to talk to <my_cluster> :…

5. [  ] **score 0.470** — https://docs.testsliderule.org/getting_started/Getting-Started.html  
    *section:* **Common Package Modules**  
    category=`getting_started`

    > In the SlideRule Python Package there are a few modules that are used more often than the others. Refer to the Userâs Guide and API Reference for further information. sliderule Core SlideRule services for initialization, configuration, processing requests, private cluster provisioning and access, area of interest processing icesat2 ICESat-2 specific services and definitions gedi GEDI specific…

---

### docsearch #27 — `api_lookup` — ✓ rank 2

**Query:** `h5 hdf5 read function parameters h5p h5x`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/h5.html

**Author's note:** h5 api reference; h5p and h5x are canonical read helpers

**Top 5 returned:**

1. [  ] **score 0.575** — https://docs.testsliderule.org/developer_guide/endpoints.html  
    *section:* **h5p**  
    category=`developer_guide`

    > POST /source/h5p <request payload> Reads a list of datasets from an HDF5 file and returns the values of the datasets in a dictionary of lists. See h5.h5p function for a convenient method for accessing HDF5 datasets. Request Payload (application/json) parameter description default asset data source asset (see Assets) required resource HDF5 filename required datasets list of datasets (see h5 for a…

2. [✓✓] **score 0.531** — https://docs.testsliderule.org/api_reference/h5.html  
    *section:* **h5**  
    category=`api_reference`

    > sliderule.h5. h5 ( dataset , resource , asset , datatype = 3 , col = 0 , startrow = 0 , numrows = -1 ) [source] Reads a dataset from an HDF5 file and returns the values of the dataset in a list This function provides an easy way for locally run scripts to get direct access to HDF5 data stored in a cloud environment. But it should be noted that this method is not the most efficient way to access…

3. [  ] **score 0.599** — https://docs.testsliderule.org/developer_guide/endpoints.html  
    *section:* **h5**  
    category=`developer_guide`

    > POST /source/h5 <request payload> Reads a dataset from an HDF5 file and return the values of the dataset in a list. See h5.h5 function for a convenient method for accessing HDF5 datasets.

4. [  ] **score 0.569** — https://docs.testsliderule.org/developer_guide/articles/h5coro.html  
    *section:* **H5Coro::read**  
    category=`developer_guide`

    > H5Coro :: Future * H5Coro :: readp ( const char * asset , const char * resource , const char * datasetname , RecordObject :: valType_t valtype , long col , long startrow , long numrows , Context * context = NULL ) {parameters} see H5Coro::read for parameter descriptions H5Coro::Future* a pointer to a structure that will contain the info_t information read from the H5 file when the read operation…

5. [✓✓] **score 0.374** — https://docs.testsliderule.org/api_reference/h5.html  
    *section:* **h5x**  
    category=`api_reference`

    > sliderule.h5. h5x ( variables , resource , asset , groups = None , col = None , startrow = None , numrows = None , index_column = None , time_column = None , x_column = None , y_column = None , z_column = None , crs = None , session = None ) [source] Builds a DataFrame from an HDF5 file where each variable in variables is a column. The groups parameter is used to create datasets from multiple…

---

### docsearch #28 — `api_lookup` — ✓ rank 1

**Query:** `icesat2 atl06p python function parameters`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl06p`

**Author's note:** icesat2 module atl06p api

**Top 5 returned:**

1. [✓✓] **score 0.616** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl06p**  
    category=`api_reference`

    > Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for…

2. [  ] **score 0.611** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-00-00.html  
    *section:* **Breaking Changes**  
    category=`release_notes`

    > This version contains a number of backward-incompatible changes, specifically to the names of the fields being returned by the atl03s and atl06 APIs, and the Python client function APIs. These changes were made to standardize the downstream processing of the photon and elevation data, and also to bring the names of the fields being returned by SlideRule closer to the ICESat-2 Standard Data…

3. [  ] **score 0.545** — https://docs.testsliderule.org/user_guide/basic_usage.html  
    *section:* **Issue the Processing Request**  
    category=`user_guide`

    > There are two general purpose routines provided in the SlideRule Python client for issuing processing requests. sliderule.source Implements the low-level protocol for making requests to SlideRule and processing the results. This can be used to issue a request to any SlideRule endpoint. sliderule.run Implements a standard SlideRule convention for making requests to SlideRule endpoints that return…

4. [✓ ] **score 0.572** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **init**  
    category=`api_reference`

    > sliderule.icesat2. init ( url = 'slideruleearth.io' , verbose = False , max_resources = None , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 , rethrow = False ) [source] Initializes the Python client for use with SlideRule and should be called before other ICESat-2 API calls. This function is a wrapper for the sliderule.init(â¦) function . Parameters :…

5. [✓ ] **score 0.573** — https://docs.testsliderule.org/api_reference/icesat2.html  
    *section:* **atl13sp**  
    category=`api_reference`

    > sliderule.icesat2. atl13sp ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs ATL13 subsetting in parallel on ATL13 data and returns measurement data. Unlike the atl13s function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch…

---

### docsearch #29 — `api_lookup` — ✓ rank 1

**Query:** `earthdata CMR search function signature`

**Expected URL(s):**
- https://docs.slideruleearth.io/api_reference/earthdata.html

**Expected sections** (case-insensitive substring on chunk.section):
- `cmr`
- `search`
- `earthdata`

**Author's note:** earthdata CMR search

**Top 5 returned:**

1. [✓✓] **score 0.511** — https://docs.testsliderule.org/api_reference/earthdata.html  
    *section:* **cmr**  
    category=`api_reference`

    > sliderule.earthdata. cmr ( short_name = None , version = None , polygon = None , time_start = '2018-01-01T00:00:00Z' , time_end = '2026-04-28T19:44:13Z' , return_metadata = False , name_filter = None ) [source] Query the NASA Common Metadata Repository (CMR) for a list of data within temporal and spatial parameters Parameters : short_name ( str ) â dataset short name as defined in the NASA CMR…

2. [✓✓] **score 0.401** — https://docs.testsliderule.org/api_reference/earthdata.html  
    *section:* **search**  
    category=`api_reference`

    > sliderule.earthdata. search ( parm , resources = None ) [source] This is the highest-level API call and attempts to automatically determine which service needs to be queried to return the resources being requested. Parameters : parm ( dict ) â request parameters Returns : list of resources to process Return type : list Notes The asset parameter must be supplied Examples >>> from sliderule…

3. [✓ ] **score 0.458** — https://docs.testsliderule.org/api_reference/earthdata.html  
    *section:* **stac**  
    category=`api_reference`

    > sliderule.earthdata. stac ( short_name = None , collections = None , polygon = None , time_start = '2018-01-01T00:00:00Z' , time_end = '2026-04-28T19:44:13Z' , as_str = True ) [source] Perform a STAC query of the NASA Common Metadata Repository (CMR) catalog for a list of data within temporal and spatial parameters Parameters : short_name ( str ) â dataset short name as defined in the NASA CMR…

4. [  ] **score 0.467** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-20-00.html  
    *section:* **Issues Resolved**  
    category=`release_notes`

    > 7d8c96c - Updated playwright version to address vulnerability Added ATL24 support to the Python client earthdata module faf1de0 - Fixed errant CMR failure status message 8856215 - fix for with_flags and bands in dataframe sampling

5. [✓✓] **score 0.419** — https://docs.testsliderule.org/api_reference/earthdata.html  
    *section:* **cmr**  
    category=`api_reference`

    > : - 108.3605610678553 , "lat" : 39.25086131372244 }, ... { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 } ] >>> granules = earthdata . cmr ( short_name = 'ATL06' , polygon = region ) >>> granules ['ATL03_20181017222812_02950102_003_01.h5', 'ATL03_20181110092841_06530106_003_01.h5', ... 'ATL03_20201111102237_07370902_003_01.h5']

---

### docsearch #30 — `paraphrased` — ✗ rank 12

**Query:** `generate a DEM from ICESat-2 data over my area of interest`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl06`
- `atl06-sr`
- `2. atl06`

**Author's note:** asking for ATL06 elevations without using ATL06 terminology (assets/grandmesa.html dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.540** — https://docs.testsliderule.org/developer_guide/why_sliderule.html  
    *section:* **Why Develop SlideRule?**  
    category=`developer_guide`

    > The tremendous growth in the size of Earth science datasets being produced by institutions over the past ten to fifteen years has broken the historical data archive model. When datasets changed from being a few hundred Gigabytes to hundreds of Terabytes (and now Petabytes), comprehensive analysis of those datasets using existing technology became impossible. For example, ICESat (the original…

2. [  ] **score 0.465** — https://docs.testsliderule.org/getting_started/Examples.html  
    *section:* **Examples**  
    category=`getting_started`

    > The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks…

3. [  ] **score 0.512** — https://docs.testsliderule.org/developer_guide/articles/h5coro.html  
    *section:* **SlideRule Project Background**  
    category=`developer_guide`

    > The NASA/ICESat-2 program is investing in a collaboration between Goddard Space Flight Center and the University of Washington to develop a cloud-based on-demand science data processing system called SlideRule to lower the barrier of entry to using the ICESat-2 data for scientific discovery and integration into other data services. SlideRule is a server-side framework implemented in C++/Lua that…

4. [  ] **score 0.449** — https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html  
    *section:* **Background**  
    category=`developer_guide`

    > The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of…

5. [  ] **score 0.444** — https://docs.testsliderule.org/developer_guide/release_notes/release-v03-03-00.html  
    *section:* **Major Changes**  
    category=`release_notes`

    > Sampling support added for the Merit DEM Added raster module to Python client - returns GeoDataFrame of sampled raster points of interest

---

### docsearch #31 — `paraphrased` — ✓ rank 5

**Query:** `combine multiple ATL products in one processing pipeline`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/xseries.html
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Author's note:** multi-product workflow (assets/atl24_access.html dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.274** — https://docs.testsliderule.org/developer_guide/why_sliderule.html  
    *section:* **Why Develop SlideRule?**  
    category=`developer_guide`

    > For example, one university could build a data service that leverages the public API of another universityâs data service to produce a combined data product without ever having to rehost the other universityâs data. From a technical implementation standpoint, the two universities remain distinct and decentralized entities, yet by providing their data as a service, they allow for combined data…

2. [  ] **score 0.214** — https://docs.testsliderule.org/developer_guide/why_sliderule.html  
    *section:* **Why Develop SlideRule?**  
    category=`developer_guide`

    > New algorithms can be added at any time Instead of institutions running multiple pipelines to produce data products that are released on fixed schedules, institutions run multiple services and new services can be added at any time and have access to all of the data (current and historic) immediately. Improvements and fixes are immediately available Instead of institutions having to replace old…

3. [  ] **score 0.260** — https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html  
    *section:* **User Lua Script**  
    category=`developer_guide`

    > -- 1. import modules local json = require ( "json" ) -- 2. create an h5coro object from the granule to be processed local asset = core . getbyname ( "icesat2-atl13" ) local h5obj = h5coro . file ( asset , "ATL13_20250302152414_11692601_007_01.h5" ) -- 3. read the reference id out of each of the 6 beams local column_gt1l = h5obj : readp ( "gt1l/atl13refid" ) local column_gt1r = h5obj : readp (…

4. [  ] **score 0.388** — https://docs.testsliderule.org/developer_guide/articles/arbitrary_code_execution.html  
    *section:* **User Python Script**  
    category=`developer_guide`

    > If the user provided script needs to only be run against a single granule, then no additional steps are necessary - the script can be set to the ace API as is and the results processed. But if a user wants to execute the script against multiple granules and take advantage of the cluster computing capabilities of SlideRule, then the user must also write a Python program that manages the…

5. [✓✓] **score 0.273** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.4 Ancillary Data**  
    category=`user_guide`

    > The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable…

---

### docsearch #32 — `paraphrased` — ✓ rank 2

**Query:** `filter only vegetation photons from ICESat-2 atl03`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/icesat2.html

**Expected sections** (case-insensitive substring on chunk.section):
- `atl08 classification`
- `atl08_class`
- `1.2.3 atl08`
- `phoreal`

**Author's note:** atl08_class with canopy label; user_guide/icesat2 has the class mapping (assets/grandmesa + phoreal dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [✓ ] **score 0.571** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **ICESat-2 Module**  
    category=`user_guide`

    > The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR…

2. [✓✓] **score 0.661** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2.3 ATL08 Classification**  
    category=`user_guide`

    > If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class…

3. [  ] **score 0.566** — https://docs.testsliderule.org/background/ICESat-2.html  
    *section:* **ATL03 - Global Geolocated Photon Data**  
    category=`background`

    > The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three…

4. [✓ ] **score 0.566** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **1.2 Photon-selection Parameters**  
    category=`user_guide`

    > Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements…

5. [✓ ] **score 0.533** — https://docs.testsliderule.org/user_guide/icesat2.html  
    *section:* **A.2 Elevations - atl06p**  
    category=`user_guide`

    > The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from…

---

### docsearch #33 — `paraphrased` — ✓ rank 2

**Query:** `save sliderule output to a parquet file for later analysis`

**Expected URL(s):**
- https://docs.slideruleearth.io/user_guide/arrow_output.html

**Author's note:** parquet/arrow output; phrased as save-for-later rather than 'return in format' (how_tos/geoparquet_output dropped after testsliderule.org rebaseline)

**Top 5 returned:**

1. [  ] **score 0.692** — https://docs.testsliderule.org/developer_guide/articles/geoparquet.html  
    *section:* **Overview**  
    category=`developer_guide`

    > SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters…

2. [✓✓] **score 0.642** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **S3 Staging**  
    category=`user_guide`

    > SlideRule also supports writing the output to its own S3 bucket for times when temporary storage is needed and the user does not have access to a bucket they own. To use this feature, the following parameters can be used: "output" : { "asset" : "sliderule-stage" , "path" : "myfile.parquet" , "open_on_complete" : False , } The sliderule-stage asset tells sliderule to stage the output in…

3. [✓✓] **score 0.646** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **Parameters**  
    category=`user_guide`

    > To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported,…

4. [✓✓] **score 0.511** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **S3 Output to User Bucket**  
    category=`user_guide`

    > SlideRule supports writing the output to an S3 bucket instead of streaming the output back to the client. In order to enable this behavior, the output.path field must start with âs3://â followed by the bucket name and object key. For example, if you wanted the result to be written to a file named âgrandmesa.parquetâ in your S3 bucket âmybucketâ, in the subfolder âmapsâ, then the…

5. [✓✓] **score 0.530** — https://docs.testsliderule.org/user_guide/arrow_output.html  
    *section:* **Parameters**  
    category=`user_guide`

    > ; this is only supported in x-series endpoints (e.g. atl03x, atl13x, atl24x, etc.) parms { "output" : { "path" : "grandmesa.parquet" , "format" : "parquet" , "open_on_complete" : True } }

---

### docsearch #34 — `version_history` — ✗ rank 48

**Query:** `phoreal added sliderule release notes version`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html

**Author's note:** phoreal first mentioned in v02-01-00 Major Changes

**Top 5 returned:**

1. [  ] **score 0.526** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **2025-12-08: Public Cluster Release v5**  
    category=`developer_guide`

    > Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.

2. [  ] **score 0.565** — https://docs.testsliderule.org/developer_guide/articles/v5_server_release.html  
    *section:* **Full release notes**  
    category=`developer_guide`

    > https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html

3. [  ] **score 0.508** — https://docs.testsliderule.org/developer_guide/articles/private_clusters.html  
    *section:* **2026-01-20: Private Clusters**  
    category=`developer_guide`

    > Note With release v5.0.2, SlideRule has transitioned the management of private clusters from the django-based SlideRule Provisioning System which was deployed in AWS ECS, to the pure Python-based SlideRule Authenticator and SlideRule Provisioner which are deployed via AWS Lambda. The main functions of the original system have been preserved, with a change in focus on clusters for individual users…

4. [  ] **score 0.410** — https://docs.testsliderule.org/developer_guide/release_notes/web-release-v04-00-03.html  
    *section:* **Summary**  
    category=`release_notes`

    > ð SlideRule Web Client v4.0.3 Release Notes Changes since v3.8.0 Infrastructure CloudFront + Route 53 terraform modules added to support hosting the landing page at the root domain New Features Landing Page - The web client now serves as the SlideRule Earth landing page at slideruleearth.io, featuring a hero section with wallpaper image, About/Contact info panels, and a News tab that pulls…

5. [  ] **score 0.569** — https://docs.testsliderule.org/developer_guide/release_notes/release-v04-09-00.html  
    *section:* **Release v4.9.x**  
    category=`release_notes`

    > 2025-02-04 Version description of the v4.9.3 release of SlideRule Earth. Sliderule Version Bathy Version v4.9.2 #14 v4.9.3 #15

---

### docsearch #35 — `version_history` — ✗ rank 7

**Query:** `sliderule api deprecation breaking removed old function`

**Expected URL(s):**
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-00-00.html
- https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html

**Author's note:** v04-00-00 and v05-00-00 are the major breaking-change releases

**Top 5 returned:**

1. [  ] **score 0.480** — https://docs.testsliderule.org/user_guide/versioning.html  
    *section:* **Note on Reproducibility**  
    category=`user_guide`

    > It is the goal of the SlideRule development team to create a system where results are able to be reproduced; but this is often times either extremely difficult or impossible for reasons outside of the teams control. SlideRule relies on publicly hosted datasets. When those datasets are updated, older versions of the datasets are often removed. For instance, ICESat-2 Standard Data Products have a…

2. [  ] **score 0.487** — https://docs.testsliderule.org/api_reference/gedi.html  
    *section:* **init**  
    category=`api_reference`

    > sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()

3. [  ] **score 0.455** — https://docs.testsliderule.org/developer_guide/release_notes/release-v01-04-00.html  
    *section:* **Required Updates**  
    category=`release_notes`

    > v1.4.0 - In order to use the latest SlideRule server deployments, the Python client must be updated. For conda users: $ conda update sliderule For developer installs: $ cd sliderule-python $ git checkout main $ git pull $ python3 setup.py install v1.4.0 - User scripts that use the Python client need to make the following updates: The track keyword argument of atl03sp , atl03s , atl06p , and atl06…

4. [  ] **score 0.491** — https://docs.testsliderule.org/api_reference/sliderule.html  
    *section:* **init**  
    category=`api_reference`

    > sliderule. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 20 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 , plugins = None , log_handler = None , github_token = None , rethrow = False , user_service = False ) [source] Initializes the Python client for use with SlideRule, and should be called before other ICESat-2 API calls. This function is a wrapper…

5. [  ] **score 0.495** — https://docs.testsliderule.org/developer_guide/articles/plugins.html  
    *section:* **Shared Object**  
    category=`developer_guide`

    > The pluginâs shared object must be named <plugin_name>.so and export two âCâ style functions: void init<plugin_name>(void) and void deinit<plugin_name>(void) . At startup, the SlideRule executable loads all plugins and calls their initialization function ( init ). When the SlideRule executable exits, the deinitialization ( deinit ) function for each loaded plugin is called. The init…

---

## nsidc

### nsidc #1 — `algorithm` — ✗ rank 23

**Query:** `how does ATL03 signal finding algorithm work`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `signal finding`
- `signal-finding`

**Author's note:** ATL03 ATBD Signal Finding chapter

**Top 5 returned:**

1. [✓ ] **score 0.462** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **List of Tables**  
    category=`atbd` · product=`ATL03` · page 16

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 List of Tables Table Page Table 5-1. Input Variables for Photon Classification Algorithm. ................................................. 55 Table 5-2. Parameters Needed to Drive the Algorithm; Input Parameters. .................................. 61 Table 5-3. Parameters Calculated Interally Within…

2. [  ] **score 0.581** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.1 Noise Filtering**  
    category=`user_guide` · product=`ATL08` · page 15

    > Once the signal photons have been identified by DRAGANN, they are combined with the coarse signal finding output from ATL03. This process is described in detail in "Section 3.1.1 | DRAGANN" in the ATDB for ATL08. Page 14 of 19National Snow and Ice Data Center nsidc.org

3. [  ] **score 0.503** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 30**  
    category=`atbd` · product=`ATL06` · page 30

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 393 Table 3-1 signal_selection_source values Value Meaning 0 Signal selection succeeded using ATL03 confident-or- better flagged PE 1 Signal selection failed using ATL03 confident-or- better flagged PE but succeeded using all flagged ATL03 PE 2 Signal selection failed using all flagged ATL03 PE, but succeeded…

4. [  ] **score 0.505** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 95**  
    category=`atbd` · product=`ATL08` · page 95

    > 1768 4 ALGORITHM IMPLEMENTATION 1769 Prior to running the surface finding algorithms used for ATL08 data products, the 1770 superset of output from the GSFC medium-high confidence classed photons (ATL03 1771 signal_conf_ph: flags 3-4) and the output from DRAGANN will be considered as the input 1772 data set. ATL03 input data requirements include the along-track time, latitude, longitude, 1773…

5. [✓ ] **score 0.477** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **10.1 Appendix A – ATL03 Output Parameter Table.**  
    category=`atbd` · product=`ATL03` · page 188

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 Parameter ATBD Name Data Type Long Name Units Description Source /ancillary_data/gtx/signal_find Group contains the setup parameters for the signal finding ATL03, Section _input algorithm. All parameters have dimension of 5,1 5, Table 5-2 corresponding with the 5 different surface types. alpha_max…

---

### nsidc #2 — `algorithm` — ✓ rank 4

**Query:** `how does ATL06 surface fit algorithm compute elevation`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf

**Expected pages** (inclusive ranges on chunk.source_page):
- 20–50

**Author's note:** ATL06 ATBD

**Top 5 returned:**

1. [  ] **score 0.570** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **5.1.4.2.5.2 Slant Histogram Along a Specified Surface Slope**  
    category=`atbd` · product=`ATL03` · page 107

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 Figure 5-7. Slant Histogram Geometry Over a Single Gap. 4. For each time, time_n, from time_n = Tbegcoef(m) + Δtime/2, to Tendcoef(m)_ - Δtime/2, the algorithm forms a histogram of the heights relative to the surface defined by the linear fit for that segmentor time interval, H(m). The histogram bin…

2. [✓ ] **score 0.588** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 73**  
    category=`atbd` · product=`ATL06` · page 73

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 1241 Figure 5-1. Flow chart for top-level ATL06 processing ATL03 PE Project to local lat, lon, h, coordinates, select by reference point RT, PT lat, h_mean lon, number Iterative linear fit and Background-rate surface-window w_surface_window_final, refinement dh_fit_dx, h_robust_sprd estimate ATL03 pulse shape…

3. [✓ ] **score 0.575** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 56**  
    category=`atbd` · product=`ATL06` · page 56

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 h_li_sigma Meters Propagated error due to Equation 48 sampling error and FPB correction from the land ice algorithm sigma_geo_h meters Total vertical geolocation 3.10 error due to PPD and POD, including the effects of horizontal geolocation error on the segment vertical error latitude degrees Latitude of segment…

4. [✓✓] **score 0.553** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 33**  
    category=`atbd` · product=`ATL06` · page 33

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 452 3.3.5.1 Least-squares fitting 453 For each segment, we first calculate a least-squares best-fitting segment to the initially selected 454 ATL03 PEs, then use an iterative procedure based on the least-squares fit to refine this window. 455 Each time we perform the least-squares fit, we construct a design…

5. [  ] **score 0.524** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **5.3.3 Compute signal photon histogram of long segments per ground track**  
    category=`atbd` · product=`ATL13` · page 134

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 7 Detrend as would be done with complete long segment and histogram results to determine L_surf_inc_mean2 and L_surf_inc_stdev2 via an 80% height gaussian fit. As in section 4.7.1.3, Ht_surf_inc_adjustment = 0 Calculate the standard deviation for each short segment as sigma_unit_fit = sqrt[(…

---

### nsidc #3 — `algorithm` — ✓ rank 3

**Query:** `how does ATL08 classify photons into ground canopy noise`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf

**Expected pages** (inclusive ranges on chunk.source_page):
- 10–80

**Author's note:** ATL08 ATBD photon classification

**Top 5 returned:**

1. [  ] **score 0.679** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.1 Noise Filtering**  
    category=`user_guide` · product=`ATL08` · page 15

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Processing To detect both the canopy surface and the underlying topography, the ATL08 software has been designed to accept multiple approaches to capture both the upper and lower surface signal photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best preserves signal photons returned…

2. [  ] **score 0.655** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **4.2 Date Last Updated**  
    category=`user_guide` · product=`ATL08` · page 20

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Table 5. Version History Summary Version Date Description V1 May 2019 Initial release V2 October 2019 Refer to V2 User Guide V3 May 2020 Refer to V3 User Guide V4 April 2021 Refer to V4 User Guide V5 November 2021 Refer to V5 User Guide • Added a quality check to reject segments for which the V6 May 2023 canopy photons fall more…

3. [✓✓] **score 0.623** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 76**  
    category=`atbd` · product=`ATL08` · page 76

    > 1410 3 ALGORITHM METHODOLOGY 1411 For the ecosystem community, identification of the ground and canopy surface 1412 is by far the most critical task, as meeting the science objective of determining global 1413 canopy heights hinges upon the ability to detect both the canopy surface and the 1414 underlying topography. Since a space-based photon counting laser mapping system 1415 is a relatively…

4. [  ] **score 0.713** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.5 Refining the Photon Classifications**  
    category=`user_guide` · product=`ATL08` · page 18

    > Signal photon classifications are stored in gt[x]/signal_photons/classed_pc_flag and use the following values: noise (0), ground (1), canopy (2), and top of canopy (3) (Section 3.4, ATBD for ATL08). 2.3.5 Refining the Photon Classifications During the first surface finding iteration, the algorithm may mislabel some photons (most likely classifying noise as canopy). After the first iteration, the…

5. [✓✓] **score 0.655** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 31**  
    category=`atbd` · product=`ATL08` · page 31

    > 520 1.6 Additional Potential Height Errors from ATLAS 521 Some additional potential height errors in the ATL08 terrain and vegetation 522 product can come from a variety of sources including: 523 a. Vertical sampling error. ATLAS height estimates are based on a 524 random sampling of the surface height distribution. Photons may 525 be reflected from anywhere within the PDF of the reflecting…

---

### nsidc #4 — `algorithm` — ✓ rank 4

**Query:** `how does ATL13 derive inland water surface height`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `inland`
- `water surface`
- `water body`

**Author's note:** ATL13 ATBD inland water

**Top 5 returned:**

1. [✓ ] **score 0.632** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **Abstract**  
    category=`atbd` · product=`ATL13` · page 2

    > In addition to ATL13 Level 3A, also co-produced as a separate product is the higher level L3B mean values of the ATL13 along-track crossing values, which is described in the ATL22 ATBD entitled ATL22 Mean Inland Surface Water Data (ATL22, Release 4). Citation for this ATL13 ATBD L3A Release 007 document: M. Jasinski, J. Stoll, D. Hancock, J. Robbins, J. Nattala, J. Morrison, B. Jones, M.…

2. [  ] **score 0.624** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **1.2 Data Product Overview**  
    category=`atbd` · product=`ATL03` · page 19

    > These heights are corrected for several geophysical phenomena (e.g. atmospheric refraction, tides) and are classified either as likely signal photon events or likely background photon events. Atmospheric data products draw the raw atmospheric profiles for each strong beam from ATL02. ATL04 provides normalized relative backscatter profiles and ATL09 produces calibrated backscatter profiles,…

3. [✓ ] **score 0.600** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **Change History Log**  
    category=`atbd` · product=`ATL13` · page 8

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 007 ATL13 Release 003 (Cont’d) March 1, 2020 - Added downscaled ATL09 input wind vector components at 10m height (met_u10m, met_v10m). -Included bottom in determining the minimum height to calculate subsurface deconvolution. -Updated threshold counts of photons within short segment histogram…

4. [✓✓] **score 0.637** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **1.5 Goals of ICESat-2 Inland Water Body Height Data Products**  
    category=`atbd` · product=`ATL13` · page 27

    > Also note that the ATL22 level L3B companion product containing the means of the ATL13 along-track products are co-developed developed and reported in a separate ATBD entitled “Mean Inland Surface Water Data (ATL22)”, with its own release versions, currently Release 4 as of 20. The difference between the along track ATL13 products and the mean ATL22 products is graphically illustrated in Figure…

5. [✓ ] **score 0.648** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **2.0 PHYSICS OF OPEN WATER**  
    category=`atbd` · product=`ATL13` · page 32

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 7 Table 1-2 Summary of Principal Features of the ATL13 and ATL22 Inland Surface Water Products 2.0 PHYSICS OF OPEN WATER The retrieval of the inland water height requires consideration of several key physical processes including: i) the generation, characterization and statistical representation…

---

### nsidc #5 — `algorithm` — ✗ rank 6

**Query:** `ATL24 PointNet++ bathymetric photon classification`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `pointnet`
- `ensemble classification`
- `classification algorithm`

**Author's note:** ATL24 ATBD PointNet++

**Top 5 returned:**

1. [  ] **score 0.572** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3.1.4 PointNet++ Classification**  
    category=`user_guide` · product=`ATL24` · page 8

    > A group of photons are then passed into the prediction model, and the output of the prediction model assigns each photon a classification value of “0” (non-bathymetric point) and “1” (bathymetric point). At this time, Page 7 of 15National Snow and Ice Data Center nsidc.org

2. [  ] **score 0.553** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3.1.8 Ensemble Classification**  
    category=`user_guide` · product=`ATL24` · page 9

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 the PointNet++ algorithm is not being used in the ensemble, but it may be activated at a future date. 2.3.1.5 Median Filter Classification Median Filter is a simple empirical method for extracting bathymetry profiles from ICESat-2 data. For ATL24, all ATL03 photon ellipsoid heights are converted to orthometric…

3. [  ] **score 0.540** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3.1.4 PointNet++ Classification**  
    category=`user_guide` · product=`ATL24` · page 8

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 2.3.1 Classification Models 2.3.1.1 CoastNet Classification CoastNet employs a convolutional neural network designed for network architectures with significant depth and can effectively extract spatial features from input images. Fixed-size samples are selected from a 2D raster of the along-track profile, then…

4. [✓ ] **score 0.585** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **ATL24 ATBD Sections**  
    category=`atbd` · product=`ATL24` · page 14

    > The many algorithms combined to provide a robust means to signal finding and photon labeling are presented in Section 4.1. This section describes 7 independent methods that each produce predictive classes within the granule and then describes an innovative ensemble machine learning model that provides the final label. Additional description in Section 4.1 is given for the specific input variables…

5. [  ] **score 0.551** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3.1.4 PointNet++ Classification**  
    category=`user_guide` · product=`ATL24` · page 8

    > The photons that connect the target and source photons are then extracted and classified as bathymetry. 2.3.1.3 OpenOceans Classification OpenOceans is designed to leverage physical processes and principles for sea surface, seafloor, and water column photon classifications. The approach involves first generating a histogram of photon return heights through vertical binning of photon returns…

---

### nsidc #6 — `algorithm` — ✗ rank 6

**Query:** `GEDI L4A biomass estimation from waveforms algorithm`

**Expected URL(s):**
- https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf

**Expected pages** (inclusive ranges on chunk.source_page):
- 5–30

**Author's note:** GEDI L4A ATBD

**Top 5 returned:**

1. [✓ ] **score 0.596** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 3**  
    category=`atbd` · product=`GEDI_L4A` · page 3

    > Foreword This document is the Algorithm Theoretical Basis Document for the GEDI Level-4A (L4A) Footprint Level Aboveground Biomass Density product. The GEDI Science Team assumes responsibility for this document and updates it, as required, as algorithms are refined. Reviews of this document are performed when appropriate and as needed updates to this document are made. This document is a GEDI…

2. [  ] **score 0.570** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 17**  
    category=`user_guide` · product=`GEDI_L4A` · page 17

    > If successful, this could facilitate the use of machine learning in a way that is compliant with GEDI04_B algorithms. 9. References Baskerville, G. L. (1972). Use of Logarithmic Regression in the Estimation of Plant Biomass. Canadian Journal of Forest Research. https://doi.org/10.1139/x72-009 Beck, J., Wirt, B., Luthcke, S., Hofton, M., & Armston, J. (2021). Global Ecosystem Dynamics…

3. [  ] **score 0.582** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 1**  
    category=`user_guide` · product=`GEDI_L4A` · page 1

    > Title: Algorithm theoretical basis document for GEDI footprint aboveground biomass density Authors and affiliations: James R. Kellner1,2, John Armston3, Laura Duncanson4 1. Institute at Brown for Environment and Society, Brown University, Providence RI, ORCID ID: 0000-0002-9861-4857 2. Department of Ecology, Evolution and Organismal Biology, Brown University, Providence RI 3. Department of…

4. [✓ ] **score 0.563** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 1**  
    category=`atbd` · product=`GEDI_L4A` · page 1

    > Algorithm Theoretical Basis Document (ATBD) for GEDI Level-4A (L4A) Footprint Level Aboveground Biomass Density James R. Kellner1,2, John Armston3, Laura Duncanson3 1 Institute at Brown for Environment and Society, Brown University, Providence RI 2 Department of Ecology, Evolution and Organismal Biology, Brown University, Providence RI 3 Department of Geographical Sciences, University of…

5. [✓ ] **score 0.534** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 2**  
    category=`atbd` · product=`GEDI_L4A` · page 2

    > Abstract The Global Ecosystem Dynamics Investigation (GEDI) lidar is a multibeam laser altimeter on the International Space Station. GEDI is the first spaceborne instrument designed specifically to measure vegetation structure and estimate aboveground carbon stocks in temperate and tropical forests and woodlands. This document describes the algorithm theoretical basis underpinning the development…

---

### nsidc #7 — `algorithm` — ✗ rank 7

**Query:** `ATL03 geophysical corrections ocean tides solid earth`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `geophysical correction`

**Author's note:** ATL03 ATBD geophysical corrections

**Top 5 returned:**

1. [  ] **score 0.654** — https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf  
    *section:* **1.2.3 File Contents**  
    category=`user_guide` · product=`ATL06` · page 7

    > USER GUIDE: ATLAS/ICESat-2 L3A Land Ice Height, Version 6 Table 1. Geophysical Corrections Applied to ICESat-2 Products ICESat-2 Products by Surface Type Geophysical Corrections1 Photon-level product (ATL03) (i.e., corrections Ocean loading applicable across all surface types) Solid Earth tide Solid Earth pole tide Ocean pole tide Total column atmospheric range-delay Land Ice, Land, and Inland…

2. [  ] **score 0.650** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.3 File Contents**  
    category=`user_guide` · product=`ATL03` · page 7

    > USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6 Table 1. Geophysical Corrections Applied to ICESat-2 Products ICESat-2 Products by Surface Type Geophysical Corrections1 Photon-level product (ATL03) (i.e., corrections Ocean loading applicable across all surface types) Solid Earth tide Solid Earth pole tide Ocean pole tide Total column atmospheric range-delay Land Ice, Land,…

3. [  ] **score 0.619** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **2.3.2.2 Photon round-trip range correction**  
    category=`user_guide` · product=`ATL03` · page 17

    > Over oceans, sea ice, and ice shelf surfaces, each photon event typically requires corrections to account for temporal variability in atmospheric-oceanic interactions (for example, inverted barometer and wind field effects) as well as tidal states and other factors. Over land surfaces, each photon event requires corrections to account for deformations induced by, for example, ocean loading and…

4. [  ] **score 0.642** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **1.2.3 File Contents**  
    category=`user_guide` · product=`ATL08` · page 7

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Table 1. Geophysical Corrections Applied to ICESat-2 Products ICESat-2 Products by Surface Type Geophysical Corrections1 Photon-level product (ATL03) (i.e., corrections Ocean loading applicable across all surface types) Solid Earth tide Solid Earth pole tide Ocean pole tide Total column atmospheric range-delay Land Ice, Land,…

5. [  ] **score 0.645** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **Appendix A – ICEsat-2/atlas description**  
    category=`user_guide` · product=`ATL24` · page 15

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 Table A - 1. Geophysical Corrections Applied to ICESat-2 Products ICESat-2 Products by Surface Type Geophysical Corrections1 Photon-level product (ATL03) (i.e., corrections Ocean loading applicable across all surface types) Solid Earth tide Solid Earth pole tide Ocean pole tide Total column atmospheric delay…

---

### nsidc #8 — `algorithm` — ✓ rank 3

**Query:** `ATL08 canopy height calculation method`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf

**Expected pages** (inclusive ranges on chunk.source_page):
- 40–130

**Author's note:** ATL08 ATBD canopy height

**Top 5 returned:**

1. [✓ ] **score 0.688** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 7**  
    category=`atbd` · product=`ATL08` · page 7

    > The saturation flag indicates that the ATL08 segment experienced some saturation which is often an indicator for water 2020 May 15 Canopy height metrics (relative and absolute heights) were expanded to every 5% ranging from 5 – 95%. 2020 May 15 The Landsat canopy cover check to determine whether the algorithm should search for both ground and canopy or just ground has been disabled. Now the ATL08…

2. [  ] **score 0.638** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.2.5 Ground-Finding Filter**  
    category=`user_guide` · product=`ATL08` · page 17

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 2.3.2.2 Canopy Determination The success of the surface finding algorithm relies heavily on correctly identifying the presence of canopy along any given L-km length segment. Due to the large volume of data ATLAS generates, this process is automated so that the correct methodology can be applied for surface extraction. In the…

3. [✓✓] **score 0.619** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 121**  
    category=`atbd` · product=`ATL08` · page 121

    > 2469 cutOff = median filter (ground, medianSpan) 2470 cutOff = smooth filter (cutOff, Window) 2471 ground = ground( (cutOff – ground) > -1 ) 2472 end 2473 15. Run the ground output once more through a median filter using window side 2474 medianSpan and a smoothing filter using window size Window, but this time 2475 with the Savitzky-Golay method. 2476 16. Finally, linearly interpolate a surface…

4. [✓✓] **score 0.732** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 49**  
    category=`atbd` · product=`ATL08` · page 49

    > 851 2.2.8 Absolute_segment_mean_canopy 852 (parameter = h_mean_canopy_abs). The absolute mean canopy height for the 853 segment. relative canopy heights are the photons heights for canopy photons (labels 854 2 and 3) above the estimated terrain surface. These relative heights are averaged and 855 then added to h_te_bestfit. 856 2.2.9 Segment_mean_canopy 857 (parameter = h_mean_canopy). The mean…

5. [✓✓] **score 0.710** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 44**  
    category=`atbd` · product=`ATL08` · page 44

    > 775 776 Figure 2.4. Illustration of canopy photons (red dots) interaction in a vegetated area. 777 Relative canopy heights, Hi, are computed by differencing the canopy photon height from 778 an interpolated terrain surface. 779 Table 2.2. Summary table of canopy parameters on ATL08. Group Data Type Description Source segment_id_beg Integer First along-track segment_id number ATL03 in 100-m…

---

### nsidc #9 — `variable_lookup` — ✗ not found

**Query:** `ATL03 HDF5 file structure data groups photon fields`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `data groups`
- `file contents`
- `file structure`

**Author's note:** ATL03 user guide HDF5 structure

**Top 5 returned:**

1. [  ] **score 0.516** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **10.2.5 HDF5 Dataset Information**  
    category=`atbd` · product=`ATL03` · page 197

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 possible that the resulting TEP histogram will have non-zero bin counts between the primary and secondary TEP return regions. We therefore suggest the following checks before a higher-level algorithm uses the TEP: (a) If the TEP histogram is to be used as a proxy for the system impulse response…

2. [  ] **score 0.552** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.4 ATL03 Data Structure for Each Ground Track**  
    category=`atbd` · product=`ATL03` · page 26

    > The smaller downlinked photon bandwidth (telemetry bandwidth) is generally not sufficient to generate a robust estimate of the background count rate, but can be used if the atmospheric histograms are not available. Section 8.0 describes data quality and browse products. Section 9.0 summarizes the metadata groups in the ATL03 data product. The appendices contain the table of inputs and outputs for…

3. [  ] **score 0.522** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **9.0 METADATA**  
    category=`atbd` · product=`ATL03` · page 159

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 9.0 METADATA The following metadata structure is planned for the ATLAS data within this product: 1) HDF structure overview 2) Each of the six ATLAS ground tracks (GT) have common data • reference ground track and cycle number • instrument performance / status parameters • background photon counts •…

4. [✓ ] **score 0.525** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.4.1 METADATA**  
    category=`user_guide` · product=`ATL03` · page 8

    > USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6 Table 2. ATLAS/ICESat-2 Granule Boundaries and Region Numbers Region Latitude Bounds Region Latitude Bounds # # 01 Equator → 27° N (ascending) 08 Equator → 27° S (descending) 02 27° N → 59.5° N (ascending) 09 27° S → 50° S (descending) 03 59.5° N → 80° N (ascending) 10 50° S → 79° S (descending) 04 80° N (ascending) → 80° N…

5. [✓ ] **score 0.510** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.4.5 gt1l–gt3r**  
    category=`user_guide` · product=`ATL03` · page 9

    > USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6 ISO19115 structured metadata with sufficient content to generate the required geospatial metadata (ATL03 ATBD | Section 2.4.9). 1.2.4.2 ancillary_data Parameters related to ATLAS that provide insight about the instrument transmit pulse, optics, receiver sensitivity, etc. These parameters are needed by higher level products…

---

### nsidc #10 — `variable_lookup` — ✗ rank 35

**Query:** `ATL06 quality flags values interpretation`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `quality`
- `data groups`

**Author's note:** ATL06 user guide quality flags

**Top 5 returned:**

1. [  ] **score 0.562** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 96**  
    category=`atbd` · product=`ATL08` · page 96

    > 1793 For this release of the software, we want to mention that there are cases of after-pulsing 1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20. 1795 For this release of the software, we have determined that we will include saturated photons. 1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to 1797 a value of 0 when…

2. [  ] **score 0.527** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **7.7.5 Geolocation and Calibration Data Quality flag**  
    category=`atbd` · product=`ATL03` · page 155

    > A caution to end users is that these parameters refer only to the motion of the spacecraft and not the beam angle. 7.7.5 Geolocation and Calibration Data Quality flag The composite POD/PPD flag, /gtx/geolocation/podppd_flag, indicates the quality of input geolocation products and the ATLAS calibration state at each ATL03 geolocation segment. The calibration periods include regular ocean scans and…

3. [  ] **score 0.542** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Data Quality and Filtering Flags**  
    category=`atbd` · product=`ATL24` · page 48

    > 5.3 Data Quality and Filtering Flags For the initial release of ATL24 the product provides some parameter values and binary flags to assist users with filtering data that meets certain criteria or requirements. One of the most useful parameters for filtering on the general quality of the classification accuracy is the confidence variable. The confidence value is a per photon value determined by…

4. [  ] **score 0.533** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Data Quality and Filtering Flags**  
    category=`atbd` · product=`ATL24` · page 48

    > The invalid_wind_speed is also a binary flag to indicate the absence (=1) of a corresponding ATL09 wind speed. Absense of wind speed also impacts the total propagated uncertainty estimation. Other useful flag of interest when considering filtering for higher quality data is the sensor_depth_exceeded. This flag (=1) is for scenarios when the photon depth exceeds any plausible ICESat-2 depth but…

5. [  ] **score 0.515** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 57**  
    category=`atbd` · product=`ATL06` · page 57

    > A zero in this parameter implies that no data-quality 1029 tests have found a problem with the segment, a one implies that some potential problem has been 1030 found. Users who select only segments with zero values for this flag can be relatively certain of 1031 obtaining high-quality data, but will likely miss a significant fraction of usable data, particularly 1032 in cloudy, rough, or…

---

### nsidc #11 — `variable_lookup` — ✗ not found

**Query:** `ATL08 terrain classification output variables HDF5`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `classification`
- `data groups`
- `ground`

**Author's note:** ATL08 user guide terrain variables

**Top 5 returned:**

1. [✓ ] **score 0.603** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **1.2.5 Naming Convention**  
    category=`user_guide` · product=`ATL08` · page 10

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Three HDF5 dimension scales are stored at the top level alongside the data groups— ds_geosegments, ds_metrics, and ds_surf_type—which index the within-land geosegments, surface type, and metrics arrays. For details about how the parameters are organized in the ATL08 product, see "Section 2 | ATL08: Data Product" in the ATBD for…

2. [✓ ] **score 0.540** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **1.2.2 ATLAS/ICESat-2 Description**  
    category=`user_guide` · product=`ATL08` · page 3

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 1 DATA DESCRIPTION Parameters Along-track terrain and canopy height above the WGS 84 ellipsoid (ITRF2014 reference frame). File Information 1.2.1 Format Data are provided as HDF5 formatted files. 1.2.2 ATLAS/ICESat-2 Description The following brief description of the Ice, Cloud and land Elevation Satellite-2 (ICESat-2)…

3. [  ] **score 0.525** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 34**  
    category=`atbd` · product=`ATL08` · page 34

    > 582 583 Figure 2.1. HDF5 data structure for ATL08 products 584 585 For each data parameter, terrain surface elevation and canopy heights will be 586 provided at a fixed segment size of 100 meters along the ground track. Based on the 587 satellite velocity and the expected number of reflected photons for land surfaces, each 588 segment should have more than 100 signal photons, but in some…

4. [  ] **score 0.546** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 7**  
    category=`atbd` · product=`ATL08` · page 7

    > The saturation flag indicates that the ATL08 segment experienced some saturation which is often an indicator for water 2020 May 15 Canopy height metrics (relative and absolute heights) were expanded to every 5% ranging from 5 – 95%. 2020 May 15 The Landsat canopy cover check to determine whether the algorithm should search for both ground and canopy or just ground has been disabled. Now the ATL08…

5. [  ] **score 0.523** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Classification Algorithms**  
    category=`atbd` · product=`ATL24` · page 22

    > 4.3.1 ATL24 Data Structure and Naming Conventions The naming and internal organization of the final HDF5 file for each ATL24 granule will match the conventions used on the rest of the project. Each granule will also have the naming convention similar to the other ICESat-2 data products. Each variable within the name (place holders) are described in Table 5. Please note that there are two sets of…

---

### nsidc #12 — `variable_lookup` — ✓ rank 1

**Query:** `ATL13 file naming convention granule filename`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `file naming`
- `naming convention`

**Author's note:** ATL13 user guide file naming

**Top 5 returned:**

1. [✓✓] **score 0.582** — https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf  
    *section:* **1.2.3 File Naming Convention**  
    category=`user_guide` · product=`ATL13` · page 5

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7 1.2.2.4 orbit_info Orbit parameters that are constant for a granule, such as the Reference Ground Track (RGT) number and cycle and the spacecraft orientation (sc_orient). 1.2.2.5 quality_assessment Quality assessment data for the granule as a whole, including a pass/fail flag and a failure reason indicator. 1.2.3 File…

2. [✓✓] **score 0.552** — https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf  
    *section:* **1.2.3 File Naming Convention**  
    category=`user_guide` · product=`ATL13` · page 5

    > Because ATL13 data files span four full orbits, the region number is always set to 01. 2Occasionally, NSIDC receives reprocessed granules from our data provider. These granules have the same file name as the original (i.e., date, time, ground track, cycle, and region number), but the revision number has been incremented. Although NSIDC deletes the superseded granule, the process can take several…

3. [  ] **score 0.464** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 35**  
    category=`atbd` · product=`ATL08` · page 35

    > 592 all height fields. In the event that there are more than 50 classed photons, but a terrain 593 height cannot be determined due to an insufficient number of ground photons, (e.g. 594 lack of photons penetrating through dense canopy), the only reported terrain height 595 will be the interpolated surface height. 596 The ATL08 product will be produced per granule based on the ATL03 defined 597…

4. [  ] **score 0.518** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Classification Algorithms**  
    category=`atbd` · product=`ATL24` · page 22

    > 4.3.1 ATL24 Data Structure and Naming Conventions The naming and internal organization of the final HDF5 file for each ATL24 granule will match the conventions used on the rest of the project. Each granule will also have the naming convention similar to the other ICESat-2 data products. Each variable within the name (place holders) are described in Table 5. Please note that there are two sets of…

5. [  ] **score 0.462** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **1.2.3 Naming Convention**  
    category=`user_guide` · product=`ATL24` · page 5

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 • x_atc: along-track distance (m) in a segment projected to the ellipsoid of the received photon • y_atc: across-track distance (m) projected to the ellipsoid of the received photon from the reference ground track (RGT) 1.2.2.3 metadata Query metadata (geospatial and temporal extents), algorithm run times,…

---

### nsidc #13 — `variable_lookup` — ✓ rank 3

**Query:** `ATL24 file contents and spatial coverage`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `file contents`
- `coverage`

**Author's note:** ATL24 user guide

**Top 5 returned:**

1. [  ] **score 0.482** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **1.3.2 Resolution**  
    category=`user_guide` · product=`ATL08` · page 11

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 1.2.6 Browse Files Browse files are provided as JPGs that contain images designed to quickly assess the location and quality of each granule's data. Images include track location, canopy heights, and terrain and canopy photon count for each ground track. Browse files utilize the same naming convention as their corresponding data…

2. [  ] **score 0.512** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Page 4**  
    category=`atbd` · product=`ATL24` · page 4

    > Contents 1 Introduction 1 2 Context/Background 4 2.1 Historical Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 3 ATL24 Overview 5 3.1 ATL24 Data Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 3.2 Data Dissemination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 3.3 ATL24 ATBD Sections . . . . . . . . . . . . . . . . . . . . .…

3. [✓✓] **score 0.382** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **1.2.2 File Contents**  
    category=`user_guide` · product=`ATL24` · page 3

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 1 DATA DESCRIPTION This user guide refers to the ICESat-2 Project Algorithm Theoretical Basis Document (ATBD) for Coastal and Nearshore Along-Track Bathymetry Product (ATL24) (ATBD for ATL24, V1 | https://doi.org/10.5067/PXJMCZD0MYLN). 1.1 Summary ATL24 provides global along-track coastal and nearshore…

4. [  ] **score 0.375** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Performance Assessment and Validation**  
    category=`atbd` · product=`ATL24` · page 41

    > Figure 8: NOAA BlueTopo data set, which will be used as the reference data set in testing the accuracy of ATL24. 5 Performance Assessment and Validation The accuracy of ATL24 will be tested using the NOAA BlueTopo data set, which is a compilation of best-available bathymetric data for U.S. waters, maintained and distributed by NOAA’s Office of Coast Survey (OCS) through the National Bathymetric…

5. [✓ ] **score 0.466** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **1.2.3 Naming Convention**  
    category=`user_guide` · product=`ATL24` · page 5

    > VVV_RR Version and revision number of the input ATL03 files*. vvv_rr Version and revision number of the ATL24 product*. *Occasionally, NSIDC receives reprocessed granules from our data provider. These granules have the same file name as the original (i.e., date, time, ground track, cycle, and region number), but the revision Page 4 of 15National Snow and Ice Data Center nsidc.org

---

### nsidc #14 — `variable_lookup` — ✗ rank 11

**Query:** `GEDI L4A footprint geolocation variables AGBD`

**Expected URL(s):**
- https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html

**Expected pages** (inclusive ranges on chunk.source_page):
- 10–30

**Author's note:** GEDI L4A user guide

**Top 5 returned:**

1. [✓ ] **score 0.563** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 3**  
    category=`user_guide` · product=`GEDI_L4A` · page 3

    > 1. Introduction The Global Ecosystem Dynamics Investigation (GEDI) is a multibeam waveform lidar on the International Space Station (Dubayah et al., 2020). Two objectives of the mission are to quantify the distribution of aboveground carbon in woody vegetation, and to use these estimates to determine the impact of land use and land cover changes on aboveground carbon stocks. Both of these…

2. [  ] **score 0.605** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 10**  
    category=`atbd` · product=`GEDI_L4A` · page 10

    > with the best performance in comparison to other technologies (Saatchi et al., 2011; Zolkos et al., 2013). Most previous efforts have developed site-specific or regional relationships between AGBD and remote sensing measurements (Zolkos et al., 2013). GEDI faces a different challenge: it needs to develop models and algorithms that perform well throughout the entire observation domain of the ISS.…

3. [  ] **score 0.597** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 9**  
    category=`atbd` · product=`GEDI_L4A` · page 9

    > This uncertainty propagates through GEDI level-2A (GEDI02_A) RH metrics that are used to predict AGBD (Dubayah et al., 2020b). The first release of the GEDI level-4A (GEDI04_A) data product is based on Version 1 of GEDI02_A (Dubayah et al., 2020b), and uses one of six algorithm setting groups to interpret the received waveform and identify the elevation of the lowest mode (Hofton and Blair,…

4. [✓ ] **score 0.532** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 2**  
    category=`user_guide` · product=`GEDI_L4A` · page 2

    > biomass density (AGBD) data product. The GEDI04_A data product contains estimates of AGBD for individual GEDI footprints and associated prediction intervals. The algorithm uses GEDI02_A relative height (RH) metrics and 13 linear models to predict AGBD in 32 combinations of plant functional type (PFT) and world region within the observation limits of the ISS. GEDI04_A models for the release 1 and…

5. [  ] **score 0.504** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 1**  
    category=`atbd` · product=`GEDI_L4A` · page 1

    > Algorithm Theoretical Basis Document (ATBD) for GEDI Level-4A (L4A) Footprint Level Aboveground Biomass Density James R. Kellner1,2, John Armston3, Laura Duncanson3 1 Institute at Brown for Environment and Society, Brown University, Providence RI 2 Department of Ecology, Evolution and Organismal Biology, Brown University, Providence RI 3 Department of Geographical Sciences, University of…

---

### nsidc #15 — `variable_lookup` — ✗ rank 45

**Query:** `ATL03 h_ph photon height variable description`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `heights`
- `photon`
- `data groups`

**Author's note:** ATL03 h_ph variable

**Top 5 returned:**

1. [  ] **score 0.654** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 96**  
    category=`atbd` · product=`ATL08` · page 96

    > ATL03 photon Computed from the ECEF Cartesian coordinates of the bounce point. lon_ph FLOAT longitude degrees Longitude of each received photon. ATL03 of photon Computed from the ECEF Cartesian coordinates of the bounce point. h_ph FLOAT height of meters Height of each received photon, ATL03 photon relative to the WGS-84 ellipsoid. sigma_h FLOAT height m Estimated height uncertainty (1- ATL03…

2. [✓ ] **score 0.628** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **4 Version History**  
    category=`user_guide` · product=`ATL03` · page 22

    > This update represents the best estimates of height uncertainty for a reference photon in on-orbit data. • Changed data type for ph_id_count to an unsigned 1-byte integer (bug fix). Prior releases of ATL03 stored the value as a signed datatype, limiting the reported value to 127. • Changed the geographic extent metadata from a predicted orbit path to a geodetic polygon, providing better…

3. [  ] **score 0.676** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **6.3.9 Atmospheric Delay Correction**  
    category=`atbd` · product=`ATL03` · page 130

    > Each non-reference photon height is then corrected as: h_ph = h_phuncorr + neutat _delay_total + neutat_delay_derivative * (h_phuncorr - neutat_ht) 114 Release Date: Fall 2022

4. [  ] **score 0.555** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **6.2 List of Geophysical Corrections**  
    category=`atbd` · product=`ATL03` · page 116

    > The photon event heights on the ATL03 output product, /gtx/heights/h_ph, are the geophysically-corrected photon event heights (Hgc), referenced to the WGS-84 ellipsoid. The values of the geophysical corrections and reference values, described below, are determined using the reference photons, nominally spaced at twenty meters along-track for each ground track. The reference photons are determined…

5. [  ] **score 0.539** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **ATL24 Input Variables**  
    category=`atbd` · product=`ATL24` · page 16

    > Roughly following the procedures used in airborne bathymetric lidar, we start with return photon coordinates that assume topograpy, rather than bathymetry, and then apply refraction correction. The initial coordinates are from ATL03: specifically, the lat_ph, lon_ph, and h_ph in the /gtx/heights group. 4.2 ATL24 Input Variables Table 2 captures each stage of the processing phase in the production…

---

### nsidc #16 — `product_disambiguation` — ✓ rank 2

**Query:** `ATL06 data groups structure for land ice`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf

**Author's note:** ATL06-specific; must not return ATL03 chunks

**Top 5 returned:**

1. [  ] **score 0.727** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 53**  
    category=`atbd` · product=`ATL06` · page 53

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 929 4 ATL06 DATA PRODUCT DESCRIPTION 930 Here we describe how the parameters appear in the ATL06 product. The ATL06 parameters are 931 arranged by beam, and within each beam in a number of groups and subgroups. Where 932 parameter descriptions in the ATL06 data dictionary are considered adequate, they are not…

2. [✓✓] **score 0.704** — https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf  
    *section:* **1.2.4.5 quality_assessment**  
    category=`user_guide` · product=`ATL06` · page 9

    > USER GUIDE: ATLAS/ICESat-2 L3A Land Ice Height, Version 6 The following sections summarize the contents of the data groups and certain parameters of interest. Data groups are described in detail in "Section 4 | ATL06 Data Product Description" in the ATBD for ATL06. A complete list of parameters is available in the ATL06 Data Dictionary. 1.2.4.1 METADATA ISO19115 structured metadata with…

3. [  ] **score 0.713** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **1.2.4.6 Dimension Scales**  
    category=`user_guide` · product=`ATL08` · page 9

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 The following sections summarize the structure and primary variables of interest in ATL08 data files. Additional details are available in "Section 2 | ATL08 Data Product" of the ATBD for ATL08. A complete list of parameters is available in the ATL08 Data Dictionary. 1.2.4.1 METADATA ISO19115 structured metadata with sufficient…

4. [  ] **score 0.706** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 55**  
    category=`atbd` · product=`ATL06` · page 55

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 A value of 3 indicates that all algorithms failed. 984 985 4.2.1 Signal_selection_status subgroup 986 This subgroup includes the Signal_selection_status_confident, Signal_selection_status_all, and 987 Signal_selection_status_backup parameters. Their values are described in Table 3-2. Its density 988 structure…

5. [  ] **score 0.634** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 53**  
    category=`atbd` · product=`ATL06` · page 53

    > Datasets in this group can be used to check 945 the geographic distribution of data gaps in the ATL06 record. 946 In the land_ice_segments group, data are sparse, meaning that values are reported only for those 947 pairs for which adequate signal levels (i.e. more than 10 PE, snr_significance > 0.05) were found 948 for at least one segment: This means that within each pair, every dataset has the…

---

### nsidc #17 — `product_disambiguation` — ✓ rank 1

**Query:** `ATL08 DRAGANN noise filtering algorithm`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf

**Author's note:** DRAGANN is ATL08-specific

**Top 5 returned:**

1. [✓✓] **score 0.624** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 15**  
    category=`atbd` · product=`ATL08` · page 15

    > 169 4.2 Preparing ATL03 data for input to ATL08 algorithm ......................................... 101 170 4.3 Noise filtering via DRAGANN ........................................................................................ 102 171 4.3.1 DRAGANN Quality Assurance .............................................................................. 105 172 4.3.2 Preprocessing to dynamically…

2. [✓✓] **score 0.551** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 95**  
    category=`atbd` · product=`ATL08` · page 95

    > 1768 4 ALGORITHM IMPLEMENTATION 1769 Prior to running the surface finding algorithms used for ATL08 data products, the 1770 superset of output from the GSFC medium-high confidence classed photons (ATL03 1771 signal_conf_ph: flags 3-4) and the output from DRAGANN will be considered as the input 1772 data set. ATL03 input data requirements include the along-track time, latitude, longitude, 1773…

3. [✓✓] **score 0.588** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 2**  
    category=`atbd` · product=`ATL08` · page 2

    > Reference source not found.) 2017 July Revised alternative DRAGANN methodology (see bolded text in Sec 4.3.1) 2017 July Added post-DRAGANN filtering methodology (Sec 4.9) 2017 July Updated SNR to be estimated from superset of ATL03 and DRAGANN found signal used for processing ATL08 (Sec 2.5.18) 2017 September More details added to DRAGANN description (Sec 4.3), and corrections to DRAGANN…

4. [✓✓] **score 0.486** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 57**  
    category=`atbd` · product=`ATL08` · page 57

    > 1047 2.3.5 DRAGANN_flag 1048 (parameter = d_flag). Flag indicating the labeling of DRAGANN noise filtering for 1049 a given photon. 0 = noise, 1=signal. 1050 1051 2.4 Subgroup: Reference data 1052 The reference data subgroup contains parameters and information that are 1053 useful for determining the terrain and canopy heights that are reported on the 1054 product. In addition to position and…

5. [✓✓] **score 0.458** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 102**  
    category=`atbd` · product=`ATL08` · page 102

    > 1903 c. All other segments that are not extended will report a last_seg_extend 1904 value of 0. 1905 4. Add a buffer of 200 m (or 10 segment_id's) to both ends of each L-km 1906 segment. The total processing segment length is (L-km + 2*buffer), but will 1907 be referred to as L-km segments for simplicity. 1908 a. The first L-km segment from an ATL03 granule would only have a 1909 buffer at the…

---

### nsidc #18 — `product_disambiguation` — ✓ rank 1

**Query:** `ATL24 ensemble classification bathymetry`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf

**Author's note:** ATL24 ensemble classification

**Top 5 returned:**

1. [✓✓] **score 0.640** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **ATL24 Data Workflow**  
    category=`atbd` · product=`ATL24` · page 12

    > The specific classifications in ATL24 are are sea surface (41), and bathymetry (40), all other photons, not classified as 40 or 41 are considered unclassified (0). These point class designations are from the American Society for Photogrammetry and Remote Sensing (ASPRS) LAS Domain Profile for Topo-Bathy Lidar (ASPRS 2013). In many regards, the classification step in the workflow is the most…

2. [  ] **score 0.693** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3 Processing**  
    category=`user_guide` · product=`ATL24` · page 7

    > On-demand and customizable, science-ready bathymetry is also available via SlideRule, a public web application programming interface for processing of science data in the cloud. 2.2 Acquisition ATL03 provides heights above the WGS84 ellipsoid, the latitude and longitude, and time for every ATLAS photon detection. These values and data quality flags are the primary input to ATL24. 2.3 Processing…

3. [✓✓] **score 0.629** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Known Issues**  
    category=`atbd` · product=`ATL24` · page 55

    > 6.5 Known Issues ATL24 product known issues can be categorized as data quality issues, user utility issues, or product parameterization. Each of these categories has several different facets that range in complexity of the problems and the possibility of a solution. • Data Quality 1. Classification performance: The most notable issue with data quality will likely be the photon-classification…

4. [✓✓] **score 0.620** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Data Quality and Filtering Flags**  
    category=`atbd` · product=`ATL24` · page 48

    > Removing these lower confidence photons (=1) will certainly eliminate many bathymetry false positives but could be at the cost of removing true positives in the case where fewer of the base algorithm inputs to the ensemble agreed. The threshold is determined by comparing the photon elevations and geolocations to a reference data set. A direct comparison between the provided the vertical…

5. [  ] **score 0.564** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **2.3.1.8 Ensemble Classification**  
    category=`user_guide` · product=`ATL24` · page 9

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1 the PointNet++ algorithm is not being used in the ensemble, but it may be activated at a future date. 2.3.1.5 Median Filter Classification Median Filter is a simple empirical method for extracting bathymetry profiles from ICESat-2 data. For ATL24, all ATL03 photon ellipsoid heights are converted to orthometric…

---

### nsidc #19 — `product_disambiguation` — ✗ rank 19

**Query:** `ATL13 processing workflow and goals`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf

**Author's note:** ATL13-specific; must not return ATL03 chunks

**Top 5 returned:**

1. [  ] **score 0.519** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **ATL24 Input Variables**  
    category=`atbd` · product=`ATL24` · page 17

    > will be used), the latitude, longitude, and time tag for every ATLAS photon detection. These values are the primary input to ATL24 but many ATL03 specific parameters are passed through the processing workflow and attached to the ATL24 product for user utility and convenience. ATL03 parameters are all defined in the dedicated Algorithm Theoretical Basis Document and the Neumann et al., 2019…

2. [  ] **score 0.475** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **1.5 Goals of ICESat-2 Inland Water Body Height Data Products**  
    category=`atbd` · product=`ATL13` · page 27

    > Also note that the ATL22 level L3B companion product containing the means of the ATL13 along-track products are co-developed developed and reported in a separate ATBD entitled “Mean Inland Surface Water Data (ATL22)”, with its own release versions, currently Release 4 as of 20. The difference between the along track ATL13 products and the mean ATL22 products is graphically illustrated in Figure…

3. [  ] **score 0.428** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **ATL24 Data Workflow**  
    category=`atbd` · product=`ATL24` · page 12

    > 3 ATL24 Overview 3.1 ATL24 Data Workflow Similar to other ICESat-2 Level 3a products, the input to the ATL24 pipeline is Level 2a, Global geolocated point cloud data; ATL03 (T. A. Neumann et al. 2019b). ATL03 provides every detected photon (signal and noise), with the calculated geolocation (geodetic latitude and longitude) and associated parameters (operational) for each of ATLAS’s six beams.…

4. [  ] **score 0.466** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Data Dissemination**  
    category=`atbd` · product=`ATL24` · page 13

    > Subsequent versions, ATL24.s and ATL24.p will leverage the full capabilities of SlideRule to provide a subsetting service and on-demand product generation service using a Python client, Javascript client, or web map GUI. This functionality will enable users to optimize the output data product for their particular science need, resulting in truly ”science-ready” data. The descriptions of each…

5. [  ] **score 0.506** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Page 4**  
    category=`atbd` · product=`ATL24` · page 4

    > Contents 1 Introduction 1 2 Context/Background 4 2.1 Historical Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 3 ATL24 Overview 5 3.1 ATL24 Data Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 3.2 Data Dissemination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 3.3 ATL24 ATBD Sections . . . . . . . . . . . . . . . . . . . . .…

---

### nsidc #20 — `cross_product` — ✓ rank 5

**Query:** `strong versus weak beams ICESat-2 ATLAS`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `beam`
- `atlas`

**Author's note:** beam geometry is ATL03-defined but referenced across products

**Top 5 returned:**

1. [✓ ] **score 0.677** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **1.1 Background**  
    category=`atbd` · product=`ATL03` · page 17

    > The beam pairs are separated by ~3.3 kilometers in the across-track direction, and the strong and weak beams are separated by ~2.5 kilometers in the along-track direction. Figure 1-1 shows the idealized beam and footprint pattern for ICESat-2. Figure 1-1. ATLAS Idealized Beam and Footprint Pattern. The left panel (Figure 1-1) shows the beam pattern for ICESat-2, while the right panel shows the…

2. [✓ ] **score 0.666** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **7.5 The Spacecraft Orientation Parameter**  
    category=`atbd` · product=`ATL03` · page 147

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 the pce_mframe_cnt roll-over every 2.7 years, this framework establishes a unique identification for every photon in the ICESat-2 data products. 7.5 The Spacecraft Orientation Parameter The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. ATL03…

3. [✓ ] **score 0.626** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **5.1.4 Algorithm Implementation**  
    category=`atbd` · product=`ATL03` · page 86

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 beam strength, have been derived based on MABEL data. Of the parameters in Table 5-2, those that are associated with time (i.e. Δtime and δtmax) have been scaled for use with ATLAS data. For example, most MABEL data have 1,000 laser pulses fired every 40 meters along-track (MABEL’s laser pulse rate was…

4. [✓ ] **score 0.701** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **2.2 Acquisition**  
    category=`user_guide` · product=`ATL03` · page 14

    > USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6 Figure 5. ICESat-2 data processing flow. ATL02 processing converts ATL01 data to science units and applies instrument corrections. The Precision Pointing Determination (PPD) and Precision Orbit Determination (POD) solutions compute the pointing vector and position of the ICESat-2 observatory. Acquisition The ATLAS instrument…

5. [✓✓] **score 0.677** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.2 ATLAS/ICESat-2 Description**  
    category=`user_guide` · product=`ATL03` · page 3

    > Each ground track is numbered according to the laser spot number that generates it, with ground track 1L (GT1L) on the far left and ground track 3R (GT3R) on the far right. Left/right spots within each pair are approximately 90 m apart in the across-track direction and 2.5 km in the along-track direction. Higher level ATLAS/ICESat-2 data products (ATL03 and above) are organized by ground track,…

---

### nsidc #21 — `cross_product` — ✓ rank 1

**Query:** `how ATL08 uses ATL03 photons for classification`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `classification`
- `noise filtering`
- `input`

**Expected pages** (inclusive ranges on chunk.source_page):
- 6–30

**Author's note:** cross-product: ATL08 ingests ATL03

**Top 5 returned:**

1. [✓✓] **score 0.598** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.1 Noise Filtering**  
    category=`user_guide` · product=`ATL08` · page 15

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Processing To detect both the canopy surface and the underlying topography, the ATL08 software has been designed to accept multiple approaches to capture both the upper and lower surface signal photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best preserves signal photons returned…

2. [  ] **score 0.590** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **3 SOFTWARE AND TOOLS**  
    category=`user_guide` · product=`ATL03` · page 21

    > Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03 data product have provided guidance regarding the fidelity to which the ATL03 algorithm needs to discriminate signal and background photon events. In general, each higher-level data product requires ATL03 to identify likely signal photon events within ±10 meters of the surface. Because the signal-finding…

3. [✓✓] **score 0.603** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 28**  
    category=`atbd` · product=`ATL08` · page 28

    > In addition to 459 recording photons from the reflected signal, the ATLAS instrument will detect 460 background photons from sunlight which are continually entering the telescope. A 461 primary objective of the ICESat-2 data processing software is to correctly 462 discriminate between signal photons and background photons. Some of this 463 processing occurs at the ATL03 level and some of it also…

4. [✓ ] **score 0.581** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 96**  
    category=`atbd` · product=`ATL08` · page 96

    > 1793 For this release of the software, we want to mention that there are cases of after-pulsing 1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20. 1795 For this release of the software, we have determined that we will include saturated photons. 1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to 1797 a value of 0 when…

5. [  ] **score 0.614** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **5.1.1 Introduction**  
    category=`atbd` · product=`ATL03` · page 64

    > The ground tracks of a strong and weak beam pair are essentially parallel to each other, and separated by ~90 meters in the across-track direction, so the slopes of the resultant surface profiles should be very similar. Therefore for the weak beam of each pair, the algorithm uses the surface profile found in the strong beam to guide slant histogramming in the weak beam. Authors of each of the…

---

### nsidc #22 — `cross_product` — ✗ rank 31

**Query:** `photon classification confidence values ATL03`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `photon classification`
- `confidence`

**Author's note:** confidence is ATL03 concept, also used by ATL08/ATL24

**Top 5 returned:**

1. [✓ ] **score 0.666** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.3 ATL03 ATBD Sections**  
    category=`atbd` · product=`ATL03` · page 25

    > This designation provides guidance to some aspects of the photon classification algorithm (section 5.0) and guides high-level data products to the ATL03 data of interest. There is an overlap of approximately ten kilometers between adjacent surface classifications, and therefore some regions on the Earth have multiple surface classifications. For example, areas along the edges of the Arctic Ocean…

2. [  ] **score 0.684** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **Data Quality and Filtering Flags**  
    category=`atbd` · product=`ATL24` · page 48

    > 5.3 Data Quality and Filtering Flags For the initial release of ATL24 the product provides some parameter values and binary flags to assist users with filtering data that meets certain criteria or requirements. One of the most useful parameters for filtering on the general quality of the classification accuracy is the confidence variable. The confidence value is a per photon value determined by…

3. [  ] **score 0.658** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 96**  
    category=`atbd` · product=`ATL08` · page 96

    > 1793 For this release of the software, we want to mention that there are cases of after-pulsing 1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20. 1795 For this release of the software, we have determined that we will include saturated photons. 1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to 1797 a value of 0 when…

4. [  ] **score 0.675** — https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf  
    *section:* **1.2.2.2 gt1l–gt3r**  
    category=`user_guide` · product=`ATL24` · page 4

    > This may include product and instrument characteristics and/or processing constants. 1.2.2.2 gt1l–gt3r Six ground track groups (gt1l–gt3r) that contain the per-beam data parameters for the specified ATLAS ground track, as follows: • class_ph: classification of photon (0 = unclassified, 1 = other, 40 = bathymetry, 41 = sea surface) • confidence: floating point value in the range 0 to 1 indicating…

5. [✓ ] **score 0.597** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **5.1.2 Overview**  
    category=`atbd` · product=`ATL03` · page 69

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 Figure 5-4. Final Classified Likely Signal Photons. Confidence level - high (blue, 29153 photons), medium (green, 12587 photons), low (red, 4292), padding (black, 3393 photons). The figures above illustrate the algorithm performance on a segment of MABEL data over land ice. As the algorithm development…

---

### nsidc #23 — `instrument` — ✓ rank 5

**Query:** `ATLAS laser altimeter instrument specifications`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `atlas`
- `instrument`

**Author's note:** ATLAS instrument canonically described in ATL03 docs

**Top 5 returned:**

1. [  ] **score 0.640** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 24**  
    category=`atbd` · product=`ATL08` · page 24

    > 375 to canopy structure and vegetation physiology. For example, the PDF of a conifer tree 376 will look different than broadleaf trees. 377 378 Figure 1.1. Various modalities of lidar detection. Adapted from Harding, 2009. 379 A cautionary note, the photon counting PDF that is illustrated in Figure 1.1 is 380 merely an illustration if enough photons (i.e. hundreds of photons or more) were to 381…

2. [✓ ] **score 0.567** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **1.1 Background**  
    category=`atbd` · product=`ATL03` · page 17

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 1.0 INTRODUCTION This section introduces the ICESat-2 mission, the measurement concept of its sole instrument (ATLAS, the Advanced Topographic Laser Altimeter System), and the family of ICESat-2 data products. 1.1 Background The ICESat-2 observatory and ATLAS instrument use a photon-counting lidar and…

3. [  ] **score 0.586** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **1.3 ICESat-2 ATLAS Instrument**  
    category=`atbd` · product=`ATL13` · page 25

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 7 1.3 ICESat-2 ATLAS Instrument NASA’s Ice, Cloud, and land Elevation Satellite-2 (ICESat-2) mission is the second of the ICESat laser altimetry missions launch in September 2018. ICESat-2 carries an improved Advanced Topographic Laser Altimeter System (ATLAS) consisting of a low energy,…

4. [  ] **score 0.605** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 104**  
    category=`atbd` · product=`ATL06` · page 104

    > Geoscience Laser Altimeter System waveform simulation and 2100 its applications. Annals of Glaciology, Vol 29, 1999, 29: 279-285. 2101 92

5. [✓✓] **score 0.519** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.2 ATLAS/ICESat-2 Description**  
    category=`user_guide` · product=`ATL03` · page 3

    > USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6 1 DATA DESCRIPTION Parameters Height above the ellipsoid, time, and geodetic latitude and longitude for individual photons. Heights are provided in the ITRF2014 reference frame; geographic coordinates are referenced to the WGS84 ellipsoid. File Information 1.2.1 Format Data are provided as HDF5 formatted files. 1.2.2…

---

### nsidc #24 — `instrument` — ✓ rank 2

**Query:** `ATL03 photon geolocation algorithm method`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `geolocation`

**Author's note:** ATL03 ATBD geolocation

**Top 5 returned:**

1. [✓ ] **score 0.751** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.3 ATL03 ATBD Sections**  
    category=`atbd` · product=`ATL03` · page 25

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 2.3 ATL03 ATBD Sections Calculation of the latitude, longitude, and ellipsoidal height of each returned photon requires an algorithm for geolocation – the location of a given photon with respect to the surface of the Earth. The atmospheric path delay and the geolocation algorithms are described in…

2. [✓✓] **score 0.714** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **3.1 The ICESat-2 Geolocation Along-Track Segments**  
    category=`atbd` · product=`ATL03` · page 34

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 3.0 GEOLOCATION Analysis of altimetry data to meet the ICESat-2 science requirements demands an accurate determination of the laser spot location on the Earth’s surface. The geolocation of the laser spot with respect to the Earth’s center of mass (or geocenter) is determined by both the orbital…

3. [✓ ] **score 0.673** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.3 ATL03 ATBD Sections**  
    category=`atbd` · product=`ATL03` · page 25

    > The algorithm calculates a weight for each photon based on the mean inverse vertical distance between a given photon and its number of neighbors within a predefined selection window. Section 6.0 describes the geophysical corrections applied to and supplied as reference values on the ATL03 data product, such as solid earth tides or dynamic ocean topographic corrections. The atmospheric refraction…

4. [✓✓] **score 0.684** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **3.1 The ICESat-2 Geolocation Along-Track Segments**  
    category=`atbd` · product=`ATL03` · page 34

    > The algorithm description for the direct and crossover altimeter measurement models, and residual analysis for geolocation parameter estimation (calibration and validation), is provided in the POD and geolocation calibration documents. 3.1 The ICESat-2 Geolocation Along-Track Segments The photon event data in ATL03 is ultimately presented in geodetic spherical coordinates as geodetic latitude,…

5. [✓ ] **score 0.647** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **Change History Log**  
    category=`atbd` · product=`ATL03` · page 9

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 Revision Date Description of Change Level Approved 5.0 Updated the default uncertainties to sigma_h = 0.17 m, 11/1/2021 sigma_along = 5 m, sigma_across = 5 m, sigma_lat = 0.000063 deg, and sigma_lon ~= 0.000063 deg. Updated the reference photon selection algorithm to more 11/1/2021 accurately follow…

---

### nsidc #25 — `instrument` — ✓ rank 1

**Query:** `GEDI shot footprint size geometry`

**Expected URL(s):**
- https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html

**Expected pages** (inclusive ranges on chunk.source_page):
- 1–20

**Author's note:** GEDI L4A footprint geometry

**Top 5 returned:**

1. [✓✓] **score 0.498** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 6**  
    category=`user_guide` · product=`GEDI_L4A` · page 6

    > Some of the allometric scaling models used to predict 𝑀𝑖 have a reported tree size domain over which predictions are valid. These tree size domains are defined by the data used to develop the equations (Chave et al., 2014; Forrester et al., 2017; Jenkins et al., 2003; Paul et al., 2016; Roxburgh et al., 2019; Ung et al., 2008). If a footprint contained at least one tree with a diameter, height,…

2. [✓✓] **score 0.492** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 11**  
    category=`user_guide` · product=`GEDI_L4A` · page 11

    > When mapped individual stems are available and the coordinates of a given stem are within the extent of the footprint, 𝑀𝑖, as defined by a given allometric model, is assigned to the footprint. When stem positions are unavailable, the mean AGBD in the square subplot is assigned to the footprint. Four assumptions underpin this approach. First, across-beam laser intensity follows a Gaussian…

3. [  ] **score 0.458** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 19**  
    category=`atbd` · product=`GEDI_L4A` · page 19

    > For example, assuming the across-beam σ is 5.5 m (Hancock et al., 2019), about 2.3% of the returned laser energy on a uniform reflectance target with constant elevation is received from surfaces beyond the 12.5 m threshold. The third and fourth assumptions address the size of GEDI footprints relative to the trees within them. A tree whose stem is outside the 12.5 m radius used to assign 𝑀! to…

4. [  ] **score 0.438** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 14**  
    category=`atbd` · product=`GEDI_L4A` · page 14

    > specific gravity outside the range defined by the original authors, the footprint was excluded (640 footprints, or 5.27%). 3.2.5. Overlap between simulated footprints and field data Some simulated GEDI footprints are not completely contained within the boundaries of field-inventory plots. When this occurs, information about AGBD within the footprint is incomplete. Previous work has demonstrated…

5. [✓ ] **score 0.476** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 42**  
    category=`user_guide` · product=`GEDI_L4A` · page 42

    > Figure S1. GEDI04_A algorithm flow. The GEDI04_A algorithm assimilates external data from GEDI02_A and other sources. A prediction is generated for every GEDI shot where algorithm_run_flag = 1. The algorithm looks up the GEDI04_A model using a world region grid and error-corrected and infilled MODIS MCD12Q1 PFT (see Fig. 2, main text). xvar is the transformed and scaled predictor data (GEDI02_A…

---

### nsidc #26 — `cross_product` — ✗ not found

**Query:** `ICESat-2 ground track beam naming GT1L GT1R GT2L convention`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `beam`
- `ground track`
- `naming`

**Author's note:** beam naming convention defined in ATL03 docs but referenced across products

**Top 5 returned:**

1. [✓ ] **score 0.664** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **10.3 Appendix D - Lexicon for ATBD Writing**  
    category=`atbd` · product=`ATL03` · page 204

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 direction of travel Reference Ground Track Ground Track 3L GT1L (ATLAS Spot 6, GT3L on GT 3L weak) (ATLAS Spot 2, weak) GT2L (ATLAS Spot 4, Ground Track 3R Sub-satellite track weak) (during an offpoint) GT3R on GT 3R GT1R GT2R (ATLAS Spot 1, (ATLAS Spot 5, (ATLAS Spot 3, strong) strong) strong)…

2. [✓ ] **score 0.667** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **10.3 Appendix D - Lexicon for ATBD Writing**  
    category=`atbd` · product=`ATL03` · page 205

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 direction of travel Reference Ground Track Ground Track 3L GT1L (ATLAS Spot 1, GT3L on GT 3L strong) (ATLAS Spot 5, strong) GT2L (ATLAS Spot 3, Ground Track 3R Sub-satellite track strong) (during an offpoint) GT1R GT2R GT3R on GT 3R (ATLAS Spot 2, (ATLAS Spot 4, (ATLAS Spot 6, weak) weak) weak)…

3. [  ] **score 0.691** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 62**  
    category=`atbd` · product=`ATL06` · page 62

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 1103 ground track number is associated with group names within the product: From left to right, they 1104 are gt1l, gt1r, gt2l, gt2r, gt3l, and gt3r. The laser beams are numbered from left to right relative 1105 to the spacecraft flight direction. When the spacecraft is flying with its x axis pointing forwards,…

4. [✓ ] **score 0.624** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.4.1.3 Group: /gtx/geophys_corr**  
    category=`atbd` · product=`ATL03` · page 27

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 time, to the ground bounce point time of a reference photon. This number will usually be around 1.5 milliseconds (a result of the nominal ~500-km orbit altitude and the speed of light), and allows the user to determine the time of day a photon bounced on the surface of the Earth to an accuracy of less…

5. [  ] **score 0.634** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 98**  
    category=`atbd` · product=`ATL06` · page 98

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 2006 2007 Pair Track (PT). The pair track is the imaginary line half way between the actual locations of 2008 the strong and weak ground tracks that make up a pair. There are three PTs: PT1 is spanned by 2009 GT1L and GT1R, PT2 is spanned by GT2L and GT2R (and may be coincident with the RGT at 2010 times), PT3…

---

### nsidc #27 — `cross_product` — ✗ not found

**Query:** `reference ground track RGT cycle number ICESat-2 granule`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `reference ground track`
- `rgt`
- `cycle`

**Author's note:** RGT/cycle concepts defined at ATL03 level, also in per-product user guides

**Top 5 returned:**

1. [✓ ] **score 0.729** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **1.2.2 ATLAS/ICESat-2 Description**  
    category=`user_guide` · product=`ATL03` · page 4

    > Cycle numbers track the number of 91-day periods that have elapsed since the ICESat-2 observatory entered the science orbit. RGTs are uniquely identified, for example in ATL02 file names, by appending the two-digit cycle number (cc) to the RGT number, e.g., 0001cc to 1387cc. Figure 1. Spot and ground track (GT) naming convention with ATLAS oriented in the forward (instrument coordinate +x)…

2. [  ] **score 0.690** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 71**  
    category=`atbd` · product=`ATL08` · page 71

    > 1293 2.5.5 ATLAS_Pointing_Angle 1294 (parameter = atlas_pa). Off nadir pointing angle (in radians) of the satellite to 1295 increase spatial sampling in the non-polar regions. 1296 2.5.6 Reference_ground_track 1297 (parameter = rgt). The reference ground track (RGT) is the track on the earth 1298 at which the vector bisecting laser beams 3 and 4 (or GT2L and GT2R) is pointed 1299 during repeat…

3. [  ] **score 0.700** — https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf  
    *section:* **Appendix A – ICEsat-2/atlas description**  
    category=`user_guide` · product=`ATL13` · page 18

    > USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7 Figure A - 1. Spot and Ground Track (GT) naming convention. The Reference Ground Track (RGT) is an imaginary track on Earth through the six-spot pattern that is used to point the observatory. 1,387 RGTs are sampled over the course of 91 days, allowing seasonal height changes to be detected. Onboard software aims the…

4. [  ] **score 0.639** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.5 ATL03 Granules**  
    category=`atbd` · product=`ATL03` · page 30

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 2.4.6 Group: /ancillary_data/gtx/signal_find_input This group contains the setup parameters for the signal finding algorithm (Table 5-2 in section 5.1.3). Several parameters are common to all ground tracks, although the values for many of these parameters are laser energy dependent (strong vs. weak)…

5. [  ] **score 0.645** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 97**  
    category=`atbd` · product=`ATL06` · page 97

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 1965 Photon Event. Some of the energy in a reflected pulse passes through the ATLAS receiver 1966 optics and electronics. ATLAS detects and time tags some fraction of the photons that make up 1967 the reflected pulse, as well as background photons due to sunlight or instrument noise. Any 1968 photon that is time…

---

### nsidc #28 — `cross_product` — ✗ rank 18

**Query:** `ATL06 uses ATL03 photons to compute surface elevations algorithm`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `surface`
- `elevations`
- `data groups`

**Expected pages** (inclusive ranges on chunk.source_page):
- 20–50

**Author's note:** cross-product: ATL06 ingests ATL03

**Top 5 returned:**

1. [  ] **score 0.689** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf  
    *section:* **OpenOceans++ Classification**  
    category=`atbd` · product=`ATL24` · page 28

    > Algorithm 3 OO++ General Algorithm Input: ATL03 track consisting of a list of photons. Each photon contains an along-track distance, x, and an elevation, z. Output: ATL24 track, where each photon has an associated classification (unclassified, sea surface, or bathymetry), an estimate of the sea surface elevation at that photon’s along-track distance, and an estimate of the bathymetry elevation at…

2. [  ] **score 0.668** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **5.1.1 Introduction**  
    category=`atbd` · product=`ATL03` · page 64

    > The ground tracks of a strong and weak beam pair are essentially parallel to each other, and separated by ~90 meters in the across-track direction, so the slopes of the resultant surface profiles should be very similar. Therefore for the weak beam of each pair, the algorithm uses the surface profile found in the strong beam to guide slant histogramming in the weak beam. Authors of each of the…

3. [  ] **score 0.661** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **3 SOFTWARE AND TOOLS**  
    category=`user_guide` · product=`ATL03` · page 21

    > Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03 data product have provided guidance regarding the fidelity to which the ATL03 algorithm needs to discriminate signal and background photon events. In general, each higher-level data product requires ATL03 to identify likely signal photon events within ±10 meters of the surface. Because the signal-finding…

4. [  ] **score 0.634** — https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf  
    *section:* **2.3.1 Noise Filtering**  
    category=`user_guide` · product=`ATL08` · page 15

    > USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6 Processing To detect both the canopy surface and the underlying topography, the ATL08 software has been designed to accept multiple approaches to capture both the upper and lower surface signal photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best preserves signal photons returned…

5. [  ] **score 0.623** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **10.1 Appendix A – ATL03 Output Parameter Table.**  
    category=`atbd` · product=`ATL03` · page 188

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 Parameter ATBD Name Data Type Long Name Units Description Source /ancillary_data/gtx/signal_find Group contains the setup parameters for the signal finding ATL03, Section _input algorithm. All parameters have dimension of 5,1 5, Table 5-2 corresponding with the 5 different surface types. alpha_max…

---

### nsidc #29 — `instrument` — ✗ rank 40

**Query:** `ICESat-2 orbit altitude inclination mission specifications`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `orbit`
- `mission`
- `atlas`

**Author's note:** mission-level specs in ATL03 docs

**Top 5 returned:**

1. [  ] **score 0.612** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **1.3 ICESat-2 ATLAS Instrument**  
    category=`atbd` · product=`ATL13` · page 26

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 7 Parameter ATLAS MABEL Operational altitude 500 km 20 km Wavelength 532 nm 532 and 1064 nm Telescope diameter 0.8 m 0.127 m Laser pulse repetition 10 kHz Variable 5-25 kHz frequency Strong beam: 121 µJ Variable, nominal Laser pulse energy Week beam: 30 µJ 5-7 µJ per beam Mean Pulse Width < 1.5…

2. [  ] **score 0.616** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 26**  
    category=`atbd` · product=`ATL08` · page 26

    > 409 Weak (1) Weak (1) Weak (1) 2.5 km* 3.305 km* Strong (4) Strong (4) Strong (4) 410 411 Figure 1.2. Schematic of 6-beam configuration for ICESat-2 mission. The laser energy will 412 be split into 3 laser beam pairs – each pair having a weak spot (1X) and a strong spot (4X). 413 The motivation behind this multi-beam design is its capability to compute 414 cross-track slopes on a per-orbit basis,…

3. [✓ ] **score 0.575** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **3.3.1 Range bias determination**  
    category=`atbd` · product=`ATL03` · page 43

    > ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03) Release 006 2. If exactly two photons are equidistant from the center, and their distance is the closest to the center, the reference photon is the equidistant photon with the higher ellipsoidal height. 3. If more than two photons are equidistant from the center, and their distance is the closest to the center,…

4. [  ] **score 0.589** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 71**  
    category=`atbd` · product=`ATL08` · page 71

    > 1293 2.5.5 ATLAS_Pointing_Angle 1294 (parameter = atlas_pa). Off nadir pointing angle (in radians) of the satellite to 1295 increase spatial sampling in the non-polar regions. 1296 2.5.6 Reference_ground_track 1297 (parameter = rgt). The reference ground track (RGT) is the track on the earth 1298 at which the vector bisecting laser beams 3 and 4 (or GT2L and GT2R) is pointed 1299 during repeat…

5. [  ] **score 0.622** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 2**  
    category=`atbd` · product=`ATL06` · page 2

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 Abstract This document describes the theoretical basis of the land ice height processing algorithms and the products that are produced by the ICESat-2 mission. It includes descriptions of the parameters that are provided with each product as well as ancillary geophysical parameters used in the derivation of the…

---

### nsidc #30 — `instrument` — ✓ rank 1

**Query:** `GEDI laser channels power modes beam configuration`

**Expected URL(s):**
- https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf

**Expected pages** (inclusive ranges on chunk.source_page):
- 1–20

**Author's note:** GEDI instrument basics

**Top 5 returned:**

1. [✓✓] **score 0.444** — https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf  
    *section:* **Page 19**  
    category=`atbd` · product=`GEDI_L4A` · page 19

    > For example, assuming the across-beam σ is 5.5 m (Hancock et al., 2019), about 2.3% of the returned laser energy on a uniform reflectance target with constant elevation is received from surfaces beyond the 12.5 m threshold. The third and fourth assumptions address the size of GEDI footprints relative to the trees within them. A tree whose stem is outside the 12.5 m radius used to assign 𝑀! to…

2. [✓✓] **score 0.417** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 11**  
    category=`user_guide` · product=`GEDI_L4A` · page 11

    > When mapped individual stems are available and the coordinates of a given stem are within the extent of the footprint, 𝑀𝑖, as defined by a given allometric model, is assigned to the footprint. When stem positions are unavailable, the mean AGBD in the square subplot is assigned to the footprint. Four assumptions underpin this approach. First, across-beam laser intensity follows a Gaussian…

3. [✓✓] **score 0.389** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 16**  
    category=`user_guide` · product=`GEDI_L4A` · page 16

    > Algorithm sensitivity to GEDI data waveform properties Training data must also be representative of GEDI waveform properties. The release 1 and release 2 GEDI04_A models were developed using simulated noiseless waveforms, where ground elevation was known from discrete-return ALS. In practice, identifying the ground- return in recorded GEDI data can be challenging under conditions of dense canopy…

4. [  ] **score 0.325** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf  
    *section:* **1.3 ICESat-2 ATLAS Instrument**  
    category=`atbd` · product=`ATL13` · page 25

    > ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data ATL13 Release 7 1.3 ICESat-2 ATLAS Instrument NASA’s Ice, Cloud, and land Elevation Satellite-2 (ICESat-2) mission is the second of the ICESat laser altimetry missions launch in September 2018. ICESat-2 carries an improved Advanced Topographic Laser Altimeter System (ATLAS) consisting of a low energy,…

5. [✓✓] **score 0.373** — https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html  
    *section:* **Page 15**  
    category=`user_guide` · product=`GEDI_L4A` · page 15

    > The GEDI04_A algorithms were developed for prediction of AGBD using GEDI data. Although the approach developed here could be replicated for other sensors, the GEDI04_A models should not be directly applied to alternative sensor data. For example, Duncanson et al. (2020) applied the GEDI04_A model framework to simulated ICEsat-2 data. This required the development of alternative statistical…

---

### nsidc #31 — `instrument` — ✓ rank 2

**Query:** `ATL03 pointing biases beam geolocation error model`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf

**Expected sections** (case-insensitive substring on chunk.section):
- `pointing`
- `bias`
- `geolocation`

**Author's note:** pointing bias + error model is ATBD territory

**Top 5 returned:**

1. [✓ ] **score 0.673** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **2.2 Data Flow Within ATL03**  
    category=`atbd` · product=`ATL03` · page 23

    > ATL03g uses these inputs and determines a preliminary latitude, longitude, and height above the ellipsoid for each photon in steps 1 through 7 in section 3.1 of the ATL03g document. In addition, ATL03g estimates the range bias for each beam, which is stored for additional analysis. The range bias estimates are used to potentially update the beam-specific time of flight biases applied in ATL02.…

2. [✓✓] **score 0.568** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **3.3.2 Range bias uncertainty**  
    category=`atbd` · product=`ATL03` · page 46

    > The atmospheric delay (combining wet and dry tropospheric effects) is described in ATL03a. This range correction is based on imperfect atmospheric models of temperature and humidity and has a residual error that is determined in the ATL03a processing. From a data flow standpoint, the ISF produces TEP for each realization of the TEP along with the TEP-based bias correction. The POD/PPD facility…

3. [✓✓] **score 0.537** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf  
    *section:* **3.3.1 Range bias determination**  
    category=`atbd` · product=`ATL03` · page 44

    > In post-launch operations, the surface return times of flight are passed from ATL02 to the geolocation algorithm (ATL03g), converted to range, and then eventually to photon height. In parallel, the TEP times of flight of the likely TEP photons are passed to the Instrument Support Facility (ISF). The ISF uses the TEP photons, and changes in their time of flight, to generate the TEP-based range…

4. [  ] **score 0.556** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 62**  
    category=`atbd` · product=`ATL06` · page 62

    > Table 4-5 ground_track subgroup Parameter Units Description Derived ref_azimuth degrees The direction, eastwards from north, ATL03 of the laser beam vector as seen by an observer at the laser ground spot viewing toward the spacecraft (i.e., the vector from the ground to the spacecraft). ref_coelv degrees Coelevation (CE) is direction from ATL03 vertical of the laser beam as seen by an observer…

5. [  ] **score 0.574** — https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf  
    *section:* **2.3.6 Surface Masks**  
    category=`user_guide` · product=`ATL03` · page 19

    > The ATLAS zero-range distance was measured before launch to account for optical and electrical path lengths within the instrument for many permutations of ATLAS settings and configurations (documented in the ATLAS pre-launch calibration product CAL-08). The TEP provides an option to internally calibrate ATLAS in orbit. Range bias uncertainty is due to (1) uncertainty in the TEP-based bias…

---

### nsidc #32 — `product_disambiguation` — ✓ rank 1

**Query:** `ATL06 land ice along-track segment elevation`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf

**Author's note:** ATL06-specific segment elevation

**Top 5 returned:**

1. [✓✓] **score 0.751** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 19**  
    category=`atbd` · product=`ATL06` · page 19

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 179 and 2 of the mission, ICESat-2 did not point at the RPTS, and ICESat2’s pairs are offset by up to 180 2 km from the RPT locations. The first cycle that was collected over the RPTS was the third. 181 We define ATL06 heights based on fits of a linear model to ATL03 height data from short 182 (40 m) segments of…

2. [✓✓] **score 0.743** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 27**  
    category=`atbd` · product=`ATL06` · page 27

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 338 Figure 3-5. RGT coordinates N azimuth Seg PRGT y x P RGT RPT Along-track coordinates for point P relative to its RGT. The track drawn is ascending, in the northern hemisphere, so x is increasing from south to north. Y at P is negative. 339 340 The AL06 along-track coordinate for each segment is given by the…

3. [✓✓] **score 0.712** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 25**  
    category=`atbd` · product=`ATL06` · page 25

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 312 same. Each cycle, i, contributes measurements from two beams, with different l values, to the 313 repeat; these different measurements allow the across-track slope to be constrained 314 independently from the height change, and the along-track segment fitting procedure allows us to 315 correct for the…

4. [✓✓] **score 0.662** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 1**  
    category=`atbd` · product=`ATL06` · page 1

    > Ice, Cloud, and land Elevation Satellite-2 (ICESat-2) Project Algorithm Theoretical Basis Document (ATBD) for Land Ice Along-Track Height Product (ATL06) Prepared by: Benjamin Smith, University of Washington Applied Physics Lab with David Hancock, Kaitlin Harbeck, LeeAnne Roberts, Thomas Neumann, Kelly Brunt, Helen Fricker, Alex Gardner, Matthew Siegfried, Susheel Adusumilli, Beata Csathó,…

5. [✓✓] **score 0.690** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf  
    *section:* **Page 23**  
    category=`atbd` · product=`ATL06` · page 23

    > ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06) Release 006 274 3.2 Outline of processing 275 The outline of the process is as follows for each cycle for each along-track point. First, heights 276 and along-track slopes are calculated for each beam in each pair: 277 1. PEs from the current cycle falling into the along-track bin for the along-track point are 278 collected…

---

### nsidc #33 — `product_disambiguation` — ✓ rank 1

**Query:** `ATL08 100-meter segment terrain canopy height`

**Expected URL(s):**
- https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf

**Author's note:** ATL08 100m segment is its signature; must not return ATL06 (which also uses segments)

**Top 5 returned:**

1. [✓✓] **score 0.648** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 44**  
    category=`atbd` · product=`ATL08` · page 44

    > 775 776 Figure 2.4. Illustration of canopy photons (red dots) interaction in a vegetated area. 777 Relative canopy heights, Hi, are computed by differencing the canopy photon height from 778 an interpolated terrain surface. 779 Table 2.2. Summary table of canopy parameters on ATL08. Group Data Type Description Source segment_id_beg Integer First along-track segment_id number ATL03 in 100-m…

2. [✓✓] **score 0.631** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 94**  
    category=`atbd` · product=`ATL08` · page 94

    > 1751 Canopy photons (shown as blue) are considered as photons lying between the terrain 1752 surface and top of canopy. 1753 1754 3.6 Canopy Height Determination 1755 Once a final ground surface is determined, canopy heights for individual 1756 photons are computed by removing the ground surface height for that photon’s 1757 latitude/longitude. These relative canopy height values will be used to…

3. [✓✓] **score 0.573** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 20**  
    category=`atbd` · product=`ATL08` · page 20

    > 259 1 INTRODUCTION 260 This document describes the theoretical basis and implementation of the 261 processing algorithms and data parameters for Level 3 land and vegetation heights 262 for the non-polar regions of the Earth. The ATL08 product contains heights for both 263 terrain and canopy in the along-track direction as well as other descriptive 264 parameters derived from the measurements. At…

4. [✓✓] **score 0.704** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 49**  
    category=`atbd` · product=`ATL08` · page 49

    > 851 2.2.8 Absolute_segment_mean_canopy 852 (parameter = h_mean_canopy_abs). The absolute mean canopy height for the 853 segment. relative canopy heights are the photons heights for canopy photons (labels 854 2 and 3) above the estimated terrain surface. These relative heights are averaged and 855 then added to h_te_bestfit. 856 2.2.9 Segment_mean_canopy 857 (parameter = h_mean_canopy). The mean…

5. [✓✓] **score 0.654** — https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf  
    *section:* **Page 48**  
    category=`atbd` · product=`ATL08` · page 48

    > 826 2.2.5 Absolute_segment_canopy_height 827 (parameter = h_canopy_abs). The absolute 98% height of classified canopy 828 photon heights (labels 2 and 3) above the ellipsoid. The relative height from classified 829 canopy photons are sorted into a cumulative distribution, and the height associated 830 with the 98% height above the h_te_bestfit for that segment is reported. For cases 831 where the…

---
