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

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06p
- **category:** `api_reference`
- **matched_tokens:** ['atl06p', 'function', 'icesat2', 'parameters']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : geolocated elevations (see Elevations ) Return type : GeoDataFrame Examples >>> from sliderule import icesat2 >>> icesat2 . init ( "slideruleearth.io" , True ) >>> parms = { "cnf" : 4 , "ats" : 20.0 , "cnt" : 10 , "len" : 40.0 , "res" : 20.0 } >>> resources = [ "ATL03_20181019065445_03150111_003_01.h5" ] >>> atl03_asset = "atlas-local" >>> rsps = icesat2 . atl06p ( parms , asset = atl03_asset , resources = resources ) >>> rsps dh_fit_dx w_surface_window_final ... time geometry 0 0.000042 61.157661 ... 2018-10-19 06:54:46.104937 POINT (-63.82088 -79.00266) 1 0.002019 61.157683 ... 2018-10-19 06:54:46.467038 POINT (-63.82591 -79.00247) 2 0.001783 61.157678 ... 2018-10-19 06:54:46.107756 POINT (-63.82106 -79.00283) 3 0.000969 61.157666 ... 2018-10-19 06:54:46.469867 POINT (-63.82610 -79.00264) 4 -0.000801 61.157665 ... 2018-10-19 06:54:46.110574 POINT (
```

#### r2 — score 0.658

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/arcticdem_request.html
- **title:** Including ArcticDEM Samples
- **section:** Sampling the ArcticDEM mosaic in an atl06p request
- **category:** `user_guide`
- **matched_tokens:** ['atl06p', 'icesat2', 'parameters', 'python']

**Full text:**

```
The âsamplesâ parameter is used to request ArcticDEM samples be included in atl06p responses. For the ArcticDEM, there are two possible values that can be provided: âarcticdem-mosaicâ and âarcticdem-stripsâ . Step 1 : Import and initialize the SlideRule Python package for ICESat-2. >>> from sliderule import sliderule , icesat2 >>> icesat2 . init ( "slideruleearth.io" ) Step 2 : Create parameters for a typical atl06p processing request. >>> grand_mesa = sliderule . toregion ( 'dicksonfjord.geojson' ) >>> parms = { "poly": grand_mesa["poly"], "srt": icesat2.SRT_LAND, "cnf": icesat2.CNF_SURFACE_HIGH, "len": 40.0, "res": 20.0 } The dicksonfjord.geojson file used in this example can be downloaded by navigating to our downloads page; alternatively, you can create your own GeoJSON file at geojson.io . Be sure that your region of interest is in the arctic, otherwise there will be no data in the ArcticDEM for it.
```

#### r3 — score 0.611

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-00-00.html
- **title:** Release v4.0.x
- **section:** Breaking Changes
- **category:** `release_notes`
- **matched_tokens:** ['atl06p', 'function', 'parameters', 'python']

**Full text:**

```
This version contains a number of backward-incompatible changes, specifically to the names of the fields being returned by the atl03s and atl06 APIs, and the Python client function APIs. These changes were made to standardize the downstream processing of the photon and elevation data, and also to bring the names of the fields being returned by SlideRule closer to the ICESat-2 Standard Data Products. v4.0.0 - For atl03s and atl03sp APIs: distance is now x_atc Across track distance is now y_atc v4.0.0 - For atl06 and atl06p APIs: distance is now x_atc Across track distance is now y_atc dh_fit_dy has been removed lon is now longitude lat is now latitude v4.0.0 - The compact ATL06 record atl06rec-compact has been removed entirely and is no longer supported. v4.0.0 - The asset parameter has been removed from the Python client functions and is now managed internally by the client. Users can still override the asset by supplying an asset key in the request parameters; but going forward users should not generally need to worry about which assets the servers are using.
```

#### r4 — score 0.610

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/ancillary_fields.html
- **title:** Including Ancillary Fields
- **section:** Including an Ancillary Field in an atl06p request
- **category:** `user_guide`
- **matched_tokens:** ['atl06p', 'icesat2', 'parameters', 'python']

**Full text:**

```
The âatl03_geo_fieldsâ and âatl03_corr_fieldsâ parameters are used to request ancillary fields be included in atl06p responses. These fields must come from either the âgtxx/geolocationâ or âgtxx/geophys_corrâ subgroups respectively. Step 1 : Import and initialize the SlideRule Python package for ICESat-2. >>> from sliderule import sliderule , icesat2 >>> icesat2 . init ( "slideruleearth.io" , verbose = True ) Step 2 : Create parameters for a typical atl06p processing request. >>> grand_mesa = sliderule . toregion ( 'grandmesa.geojson' ) >>> parms = { "poly": grand_mesa["poly"], "srt": icesat2.SRT_LAND, "cnf": icesat2.CNF_SURFACE_HIGH, "len": 40.0, "res": 20.0 } The grandmesa.geojson file used in this example can be downloaded by navigating to our downloads page; alternatively, you can create your own GeoJSON file at geojson.io . Step 3 : Add ancillary fields to the request. >>> parms [ "atl03_geo_fields" ] = [ "ref_azimuth" , "ref_elev" ] Step 4 : Issue the processing request to SlideRule. >>> gdf = icesat2 . atl06p ( parms ) When this completes (~45 seconds), the gdf variable should now contain all of the results of the elevations calculated by SlideRule with corresponding columns for the âref_azimuthâ and âref_elevâ fields.
```

#### r5 — score 0.574

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/ancillary_fields.html
- **title:** Including Ancillary Fields
- **section:** Including an Ancillary Field in an atl03sp request
- **category:** `user_guide`
- **matched_tokens:** ['atl06p', 'icesat2', 'parameters', 'python']

**Full text:**

```
The âatl03_ph_fieldsâ parameter can be used to request ancillary fields be included in atl03sp responses. These fields must come from the âgtxx/heightsâ subgroup. The âatl03_geo_fieldsâ parameter can also be used - but note that when it is used, the resulting data will expand so that each photon row in the GeoDataFrame will have the value of the ancillary field corresponding to the segment that the photon is in. Step 1 : Import and initialize the SlideRule Python package for ICESat-2. >>> from sliderule import sliderule , icesat2 >>> icesat2 . init ( "slideruleearth.io" , verbose = True ) Step 2 : Create parameters for a typical atl06p processing request. >>> grand_mesa = sliderule . toregion ( 'grandmesa.geojson' ) >>> parms = { "poly": grand_mesa["poly"], "srt": icesat2.SRT_LAND, "cnf": icesat2.CNF_SURFACE_HIGH, "len": 40.0, "res": 20.0 } The grandmesa.geojson file used in this example can be downloaded by navigating to our downloads page; alternatively, you can create your own GeoJSON file at geojson.io .
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

