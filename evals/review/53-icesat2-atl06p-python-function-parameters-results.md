# Row 53 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `53-icesat2-atl06p-python-function-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `icesat2 atl06p python function parameters`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
- **expected_sections:**
  - `atl06p`
- **expected_pages:** (none)
- **notes:** icesat2 module atl06p api

---

## 📚 docsearch results (top 5)

#### r1 — score 0.616

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06p
- **category:** `api_reference`
- **matched_tokens:** ['atl06p', 'function', 'icesat2', 'parameters']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : geolocated elevations (see Elevations ) Return type : GeoDataFrame Examples >>> from sliderule import icesat2 >>> icesat2 . init ( "slideruleearth.io" , True ) >>> parms = { "cnf" : 4 , "ats" : 20.0 , "cnt" : 10 , "len" : 40.0 , "res" : 20.0 } >>> resources = [ "ATL03_20181019065445_03150111_003_01.h5" ] >>> atl03_asset = "atlas-local" >>> rsps = icesat2 . atl06p ( parms , asset = atl03_asset , resources = resources ) >>> rsps dh_fit_dx w_surface_window_final ... time geometry 0 0.000042 61.157661 ... 2018-10-19 06:54:46.104937 POINT (-63.82088 -79.00266) 1 0.002019 61.157683 ... 2018-10-19 06:54:46.467038 POINT (-63.82591 -79.00247) 2 0.001783 61.157678 ... 2018-10-19 06:54:46.107756 POINT (-63.82106 -79.00283) 3 0.000969 61.157666 ... 2018-10-19 06:54:46.469867 POINT (-63.82610 -79.00264) 4 -0.000801 61.157665 ... 2018-10-19 06:54:46.110574 POINT (
```

#### r2 — score 0.611

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-00-00.html
- **title:** Release v4.0.x
- **section:** Breaking Changes
- **category:** `release_notes`
- **matched_tokens:** ['atl06p', 'function', 'parameters', 'python']

**Full text:**

```
This version contains a number of backward-incompatible changes, specifically to the names of the fields being returned by the atl03s and atl06 APIs, and the Python client function APIs. These changes were made to standardize the downstream processing of the photon and elevation data, and also to bring the names of the fields being returned by SlideRule closer to the ICESat-2 Standard Data Products. v4.0.0 - For atl03s and atl03sp APIs: distance is now x_atc Across track distance is now y_atc v4.0.0 - For atl06 and atl06p APIs: distance is now x_atc Across track distance is now y_atc dh_fit_dy has been removed lon is now longitude lat is now latitude v4.0.0 - The compact ATL06 record atl06rec-compact has been removed entirely and is no longer supported. v4.0.0 - The asset parameter has been removed from the Python client functions and is now managed internally by the client. Users can still override the asset by supplying an asset key in the request parameters; but going forward users should not generally need to worry about which assets the servers are using.
```

#### r3 — score 0.545

- **url:** https://docs.testsliderule.org/user_guide/basic_usage.html
- **title:** Basic Usage
- **section:** Issue the Processing Request
- **category:** `user_guide`
- **matched_tokens:** ['atl06p', 'function', 'icesat2', 'python']

**Full text:**

```
There are two general purpose routines provided in the SlideRule Python client for issuing processing requests. sliderule.source Implements the low-level protocol for making requests to SlideRule and processing the results. This can be used to issue a request to any SlideRule endpoint. sliderule.run Implements a standard SlideRule convention for making requests to SlideRule endpoints that return a dataframe. This uses the sliderule.source() routine. A user is always free to use one of the routines above for making requests to SlideRule, but many times it is more convenient to use one of the helper functions in the mission specific modules. For instance, when making processing requests for ICESat-2 data, the icesat2 module provides many routines that wrap calls to specific endpoints in an easy-to-use Python function. For instance, when making a request to the atl06p endpoint, a user should use the icesat2.atl06p() Python routine.
```

#### r4 — score 0.572

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['function', 'icesat2', 'parameters', 'python']

**Full text:**

```
sliderule.icesat2. init ( url = 'slideruleearth.io' , verbose = False , max_resources = None , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 , rethrow = False ) [source] Initializes the Python client for use with SlideRule and should be called before other ICESat-2 API calls. This function is a wrapper for the sliderule.init(â¦) function . Parameters : max_resources ( int ) â maximum number of H5 granules to process in the request Examples >>> from sliderule import icesat2 >>> icesat2 . init ()
```

#### r5 — score 0.573

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl13sp
- **category:** `api_reference`
- **matched_tokens:** ['function', 'icesat2', 'parameters']

**Full text:**

```
sliderule.icesat2. atl13sp ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs ATL13 subsetting in parallel on ATL13 data and returns measurement data. Unlike the atl13s function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. Parameters : parms ( dict ) â parameters used to configure ATL13 subsetting (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL13_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : ATL13 water measurements Return type : GeoDataFrame
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.533

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

#### r2 — score 0.493

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 2.0 PHYSICS OF OPEN WATER
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 32
- **matched_tokens:** ['icesat2']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Table 1-2 Summary of Principal Features of the ATL13 and ATL22 Inland Surface Water Products
2.0 PHYSICS OF OPEN WATER
The retrieval of the inland water height requires consideration of several key physical processes
including: i) the generation, characterization and statistical representation of surface waves, ii)
the propagation and scattering of light, from both ICESat2 and sun sources, especially at the
water surface and within the subsurface, and iii) an understanding of the characteristics of the
9
Release 007, January 31, 2025
```

#### r3 — score 0.520

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.4.5 gt1l–gt3r
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 9
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
ISO19115 structured metadata with sufficient content to generate the required geospatial metadata
(ATL03 ATBD | Section 2.4.9).
1.2.4.2 ancillary_data
Parameters related to ATLAS that provide insight about the instrument transmit pulse, optics,
receiver sensitivity, etc. These parameters are needed by higher level products and are generally
passed to ATL03 from the ICESat-2 Science Unit Converted Telemetry product, ATL02 (ATL02
and ATL03 ATBDs Sections 2.4.3–2.4.6).
1.2.4.3 atlas_impulse_response
Parameters needed by higher level data products that require knowledge of the ATLAS system
impulse-response function to account for how the ATLAS system impacts ground return statistics
(ATL03 ATBD | Section 2.4.2).
1.2.4.4 Dimension Scales
Two HDF5 dimension scales are stored at the top level alongside the data groups:
• ds_surf_type: dimension scale indexing the surface type array
(gt[x]/geolocation/surf_type)
• ds_xyz: dimension scale indexing the X-Y-Z components of the spacecraft velocity (east
component, north component, up component) an observer on the ground would measure
(gt[x]/geolocation/velocity_sc)
1.2.4.5 gt1l–gt3r
Six gt[x] groups, each of which contains the parameters for one of the six ATLAS ground tracks
including height above the WGS 84 ellipsoid, time, latitude, and longitude for individual photons
(ATL03 ATBD | Section 2.4.1).
```

#### r4 — score 0.656

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.1 ATL03 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['parameters']

**Full text:**

```
The primary output from ATL03 is described in this document, and is listed as Appendix A. A
complete listing and description of the parameters are available through the NSIDC website
(https://nsidc.org/data/icesat-2).
5 Release Date: Fall 2022
```

#### r5 — score 0.491

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.2.2 ATLAS Transmitter Echo Path
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 135
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
and conversely for negative values of tx_pulse_skew_est. Note that this parameter is not the
same as the pulse skew; it is an indication of pulse skew and variations of the actual pulse skew. This parameter is aligned with tx_pulse_width_lower and tx_pulse_width_upper, uses the same
threshold crossings, and can be found in the /gtx/geolocation group. The parameters related to the transmit pulse provided at the geolocation segment (~20 meter)
basis therefore are:
Parameter Description Units Source / Input
tx_pulse_width_lower difference between the lower threshold seconds ATL02, Section 3.4.6
crossing times
tx_pulse_width_upper difference between the upper threshold seconds ATL02, Section 3.4.6
crossing times
tx_pulse_thresh_lower lower threshold setting of the SPD volts ATL02, Section 5.2
tx_pulse_thresh_upper upper threshold setting of the SPD volts ATL02, Section 5.2
tx_pulse_distribution fraction of transmit pulse energy per unitless ATL02, Section 3.4.6
beam
tx_pulse_skew_est difference between the means of the seconds ATL02, Section 3.5
lower and upper threshold crossing
times
Table 7-2. Transmit Pulse Parameters.
7.2.2 ATLAS Transmitter Echo Path
An estimate of the ATLAS impulse-response function is derived from the transmitter echo path
(TEP) photon events.
```

---

