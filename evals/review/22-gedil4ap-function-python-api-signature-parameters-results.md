# Row 22 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `22-gedil4ap-function-python-api-signature-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `gedil4ap function python API signature parameters`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/gedi.html
- **expected_sections:**
  - `gedi04ap`
  - `gedi04a`
- **expected_pages:** (none)
- **notes:** GEDI module api reference

---

## 📚 docsearch results (top 5)

#### r1 — score 0.434

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['api', 'function', 'python']

**Full text:**

```
sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()
```

#### r2 — score 0.396

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 4. Callbacks
- **category:** `user_guide`
- **matched_tokens:** ['api', 'function', 'parameters', 'python']

**Full text:**

```
For large processing requests, it is possible that the data returned from the API is too large or impractical to fit in the local memory of the Python interpreter making the request. In these cases, certain APIs in the SlideRule Python client allow the calling application to provide a callback function that is called for every result that is returned by the servers. If a callback is supplied, the API will not return back to the calling application anything associated with the supplied record types, but assumes the callback fully handles processing the data. The callback function takes the following form: callback ( record , session ) Callback that handles the results of a processing request for the given record. Parameters : record ( dict ) â the record object, usually a dictionary containing data session ( class ) â the session object, containing settings for the current connection to the sliderule servers Here is an example of a callback being used for the gedi01bp function: rec_cnt = 0 def gedi01bp_cb ( rec , session ): global rec_cnt rec_cnt += 1 print ( " {} {} " . format ( rec_cnt , rec [ "shot_number" ]), end = ' \r ' ) gdf = gedi . gedi01bp ({}, callbacks = { "gedi01brec" : gedi01bp_cb }) Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.411

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi01bp
- **category:** `api_reference`
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure subsetting process asset ( str ) â data source asset callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âGEDI04_A_2019229131935_O03846_02_T03642_02_002_02_V002.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : geolocated footprints Return type : GeoDataFrame Examples >>> from sliderule import gedi >>> gedi . init () >>> region = [ { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 } ] >>> parms = { "poly" : region } >>> resources = [ "GEDI01_B_2019229131935_O03846_02_T03642_02_002_02_V002.h5" ] >>> asset = "gedi-local" >>> rsps = gedi . gedi01bp ( parms , asset = asset , resources = resources ) Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.411

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi02ap
- **category:** `api_reference`
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure subsetting process asset ( str ) â data source asset callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âGEDI04_A_2019229131935_O03846_02_T03642_02_002_02_V002.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : geolocated footprints Return type : GeoDataFrame Examples >>> from sliderule import gedi >>> gedi . init () >>> region = [ { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 } ] >>> parms = { "poly" : region } >>> resources = [ "GEDI02_A_2019229131935_O03846_02_T03642_02_002_02_V002.h5" ] >>> asset = "gedi-local" >>> rsps = gedi . gedi02ap ( parms , asset = asset , resources = resources )
```

#### r5 — score 0.411

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04ap
- **category:** `api_reference`
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure subsetting process asset ( str ) â data source asset callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âGEDI04_A_2019229131935_O03846_02_T03642_02_002_02_V002.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : geolocated footprints Return type : GeoDataFrame Examples >>> from sliderule import gedi >>> gedi . init () >>> region = [ { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 39.81983728534918 }, ... { "lon" : - 105.30742121965137 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 40.164048017973755 }, ... { "lon" : - 105.82971551223244 , "lat" : 39.81983728534918 } ] >>> parms = { "poly" : region } >>> resources = [ "GEDI04_A_2019229131935_O03846_02_T03642_02_002_02_V002.h5" ] >>> asset = "ornldaac-s3" >>> rsps = gedi . gedi04ap ( parms , asset = asset , resources = resources )
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.318

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 9
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 9
- **matched_tokens:** ['function']

**Full text:**

```
This uncertainty propagates
through GEDI level-2A (GEDI02_A) RH metrics that are used to predict AGBD (Dubayah et al.,
2020b). The first release of the GEDI level-4A (GEDI04_A) data product is based on Version 1
of GEDI02_A (Dubayah et al., 2020b), and uses one of six algorithm setting groups to interpret
the received waveform and identify the elevation of the lowest mode (Hofton and Blair, 2020). The Version 1 of GEDI04_A uses linear statistical models selected from an ensemble of
candidates that predict AGBD as a function of one or more RH metrics. GEDI04_A models are a
required input to the 1 km GEDI level-4B (GEDI04_B) AGBD data product (Patterson et al.,
2019).
2. HISTORICAL PERSPECTIVE
Estimating AGBD using remote sensing requires aboveground biomass, 𝑀!, for a sample
of trees that has been computed using an allometric model in a fixed area, such as a field-
inventory plot or lidar footprint. Summing the 𝑀! over all individuals in the plot or footprint and
expressing it per unit ground area produces an estimate of AGBD. Coincident remote sensing
data are used to develop an empirical relationship between AGBD and a remotely sensed
measurement. This relationship can then be used to predict AGBD using remotely sensed data
(Drake et al., 2002; Lefsky et al., 2002).
```

#### r2 — score 0.155

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['api', 'python']

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

#### r3 — score 0.149

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 102
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 102
- **matched_tokens:** ['function', 'signature']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
2079 Glossary/Acronyms
ASAS ATLAS Science Algorithm Software
ATBD Algorithm Theoretical Basis Document
ATLAS ATLAS Advance Topographic Laser Altimeter System
CDF Cumulative Distribution Function
DEM Digital Elevation Model
GSFC Goddard Space Flight Center
GTs Ground Tracks
ICESat-2 Ice, Cloud, and land Elevation Satellite-2
MABEL Multiple altimeter Beam Experimental Lidar
MIS Management Information System
NASA National Aeronautics and Space Administration
PE Photon Event
POD Precision Orbit Determination
PPD Precision Pointing Determination
PRD Precise Range Determination
PSO ICESat-2 Project Science Office
PTs Pair Tracks
RDE Robust Dispersion Estimate
RGT Reference Ground Track
RMS Root Mean Square
RPTs Reference Pair Tracks
RT Real Time
SCoRe Signature Controlled Request
90
```

#### r4 — score 0.242

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 58
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 58
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
1040 4.3.1 geophysical subgroup
1041 The geophysical group (Table 4-4) contains tidal and atmospheric corrections that may be added
1042 to or removed from h_li, and inferred atmospheric properties that may be used to determine
1043 whether the elevation of a given segment might be affected by atmospheric forward scattering.
1044 Note that the neutat_delay parameter and all tide_ parameters in this group are applied by default
1045 except for tide_ocean and dac (dynamic atmosphere correction).. The sign of the parameters is
1046 such that adding the parameter value to h_IS removes the correction (for applied corrections) and
1047 subtracting the parameter includes the correction (for tide_ocean). These parameters are
1048 interpolated from the corresponding ATL03 parameters for the ‘nominal photons’, interpolated
1049 as a piecewise linear function of along-track distance to the segment centers.
```

#### r5 — score 0.148

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['python']

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

