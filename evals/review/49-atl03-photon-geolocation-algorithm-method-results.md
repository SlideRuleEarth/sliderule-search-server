# Row 49 results: nsidc / instrument

> Auto-generated. Open this file alongside `49-atl03-photon-geolocation-algorithm-method-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 photon geolocation algorithm method`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `geolocation`
- **expected_pages:** (none)
- **notes:** ATL03 ATBD geolocation

---

## 📚 docsearch results (top 5)

#### r1 — score 0.530

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.1 PhoREAL Parameters
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'geolocation', 'photon']

**Full text:**

```
The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the median value across all photons in the segment; âcenterâ - takes the halfway value calculated by the average of the first and last photon in the segment use_abs_h : boolean whether the absolute photon heights are used instead of the normalized heights send_waveform : boolean whether to send to the client the photon height histograms in addition to the vegetation statistics above_classifier : boolean whether to use the ABoVE photon classifier when determining top of canopy photons
```

#### r2 — score 0.709

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** References
- **category:** `background`
- **matched_tokens:** ['atl03', 'geolocation', 'photon']

**Full text:**

```
ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03
```

#### r3 — score 0.582

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03', 'photon']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r4 — score 0.529

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03', 'photon']

**Full text:**

```
The photon data is stored as along-track segments inside the ATL03 granules, which is then broken apart by SlideRule and re-segmented according to processing parameters supplied at the time of the request. The new segments are called extents . When the length of an extent is 40 meters, and the step size is 20 meters, the extent matches the ATL06 segments. Most of the time, the photon extents are kept internal to SlideRule and not returned to the user. But there are some APIs that do return raw photon extents for the user to process on their own. Even though this offloads processing on the server, the API calls can take longer since more data needs to be returned to the user, which can bottleneck over the network. Photon extents are returned as GeoDataFrames where each row is a photon. Each extent represents the data that the ATL06 algorithm uses to generate a single ATL06 elevation. When the step size is shorter than the length of the extent, the extents returned overlap each other which means that each photon is being returned multiple times and will be duplicated in the resulting GeoDataFrame.
```

#### r5 — score 0.447

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl03sp
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'geolocation', 'photon']

**Full text:**

```
sliderule.icesat2. atl03sp ( parm , callbacks = {} , resources = None , keep_id = False , height_key = None ) [source] Performs ATL03 subsetting in parallel on ATL03 data and returns photon segment data. Unlike the atl03s function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. Warning Note, it is often the case that the list of resources (i.e. granules) returned by the CMR system includes granules that come close, but do not actually intersect the region of interest. This is due to geolocation margin added to all CMR ICESat-2 resources in order to account for the spacecraft off-pointing. The consequence is that SlideRule will return no data for some of the resources and issue a warning statement to that effect; this can be ignored and indicates no issue with the data processing.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.751

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.3 ATL03 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 25
- **matched_tokens:** ['algorithm', 'atl03', 'geolocation', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
2.3 ATL03 ATBD Sections
Calculation of the latitude, longitude, and ellipsoidal height of each returned photon requires an
algorithm for geolocation – the location of a given photon with respect to the surface of the
Earth. The atmospheric path delay and the geolocation algorithms are described in separate
ATBD documents. Atmospheric path delay includes tropospheric refraction, as discussed in
ATL03a. The geolocation algorithm, discussed in ATL03g, draws from three sources: the
ATL02 data product, the PPD pointing vector of the ATLAS boresite, and the spacecraft position
relative to the Earth from the POD process. Section 3.0 describes other issues related to geolocation, but not included in ATL03g. Namely,
the ICESat-2 Geolocation along-track segments (sometimes called geolocation bins, or
geolocation segments) is discussed in section 3.1 along with the algorithm to assign each photon
to a segment. Section 3.2 describes how reference photons for each along-track segment that
contains photons are selected, and section 3.3 describes other parameters that are also geolocated
(namely, the top of the photon downlink or telemetry band). Section 4.0 describes the surface masks used to assign each photon to one or more surface types. ATL03 defines five surface types (land, ocean, sea ice, land ice, and inland water) that
collectively cover the surface of the Earth.
```

#### r2 — score 0.714

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.1 The ICESat-2 Geolocation Along-Track Segments
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 34
- **matched_tokens:** ['algorithm', 'atl03', 'geolocation', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
3.0 GEOLOCATION
Analysis of altimetry data to meet the ICESat-2 science requirements demands an accurate
determination of the laser spot location on the Earth’s surface. The geolocation of the laser spot
with respect to the Earth’s center of mass (or geocenter) is determined by both the orbital
location of ATLAS in an appropriate reference frame and the direction of the laser beams
described in the same reference frame. With these position and direction vectors and the photon
path range, the location of each measured photon event can be calculated in geodetic coordinates
(geodetic latitude, longitude, and height above the WGS-84 ellipsoid) along with associated
measurement uncertainties. The geolocation procedure is documented in a separate ATBD (ATL03g, Geolocation). That
document provides: 1) a general theoretical overview of the algorithms, processing steps, and
procedures required to geolocate the ATLAS received photons, 2) a detailed geolocation
algorithm and processing flow specifically designed for the ICESat-2 mission, and 3) a
description of the application of the atmospheric path delay correction. The details of the
atmospheric path delay computation are provided in ATL03a.
```

#### r3 — score 0.673

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.3 ATL03 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 25
- **matched_tokens:** ['algorithm', 'atl03', 'geolocation', 'photon']

**Full text:**

```
The algorithm calculates a weight for each photon based on the mean inverse vertical
distance between a given photon and its number of neighbors within a predefined selection
window. Section 6.0 describes the geophysical corrections applied to and supplied as reference values on
the ATL03 data product, such as solid earth tides or dynamic ocean topographic corrections. The
atmospheric refraction correction, being an integral aspect of the geolocation process, is
9 Release Date: Fall 2022
```

#### r4 — score 0.684

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.1 The ICESat-2 Geolocation Along-Track Segments
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 34
- **matched_tokens:** ['algorithm', 'atl03', 'geolocation', 'photon']

**Full text:**

```
The algorithm description for the
direct and crossover altimeter measurement models, and residual analysis for geolocation
parameter estimation (calibration and validation), is provided in the POD and geolocation
calibration documents.
3.1 The ICESat-2 Geolocation Along-Track Segments
The photon event data in ATL03 is ultimately presented in geodetic spherical coordinates as
geodetic latitude, longitude and photon event height above the WGS-84 ellipsoid (or ellipsoidal
height). ATL03g provides the details of the geolocation algorithm, which we briefly summarize
here. Each individual photon event is initially geolocated without the correction for atmospheric
path delay. These geolocated photons are then provided to the signal finding algorithm (described
in section 5.0). The signal characterized photons are then binned in ~20 m along-track segments
that are fixed to the Reference Ground Track (RGT) in predetermined locations. A reference
photon is selected (section 3.2, below) from the photon events classified as likely signal photons. These segments are referred to as the along-track geolocation segments, also known as geolocation
segments or geosegs in this and related documents. The atmospheric path delay (described in
ATL03a) and its derivatives with respect to ellipsoid height are computed for the reference photon.
```

#### r5 — score 0.647

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 9
- **matched_tokens:** ['algorithm', 'atl03', 'geolocation', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Revision Date
Description of Change
Level Approved
5.0 Updated the default uncertainties to sigma_h = 0.17 m, 11/1/2021
sigma_along = 5 m, sigma_across = 5 m, sigma_lat =
0.000063 deg, and sigma_lon ~= 0.000063 deg. Updated the reference photon selection algorithm to more 11/1/2021
accurately follow the logic described in the ATBD. Fixed the calculation and application of the neutral 11/1/2021
atmosphere delay derivative to non-reference photons in a
geolocation segment. Improved TEP flagging to better identify TEP photons, and 11/1/2021
fixed TEP detection to function only in ATLAS spots 1 and
3. The improved TEP flagging captures more TEP photons,
particularly in low signal cases. Improved the quality_ph flagging. 11/1/2021
Updated ATL03 photon heights to include time-dependent 11/1/2021
range bias.
```

---

