# Row 1 results: docsearch / identifier

> Auto-generated. Open this file alongside `01-atl03x-x-series-api-photon-processing-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl03x X-Series API photon processing`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
  - https://docs.slideruleearth.io/user_guide/xseries.html
- **expected_sections:**
  - `atl03x`
  - `1. atl03`
- **expected_pages:** (none)
- **notes:** identifier lookup; canonical page is user_guide/icesat2.html section on atl03x

---

## 📚 docsearch results (top 5)

#### r1 — score 0.625

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03x', 'photon', 'processing']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r2 — score 0.629

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['api', 'photon', 'processing']

**Full text:**

```
The photon data is stored as along-track segments inside the ATL03 granules, which is then broken apart by SlideRule and re-segmented according to processing parameters supplied at the time of the request. The new segments are called extents . When the length of an extent is 40 meters, and the step size is 20 meters, the extent matches the ATL06 segments. Most of the time, the photon extents are kept internal to SlideRule and not returned to the user. But there are some APIs that do return raw photon extents for the user to process on their own. Even though this offloads processing on the server, the API calls can take longer since more data needs to be returned to the user, which can bottleneck over the network. Photon extents are returned as GeoDataFrames where each row is a photon. Each extent represents the data that the ATL06 algorithm uses to generate a single ATL06 elevation. When the step size is shorter than the length of the extent, the extents returned overlap each other which means that each photon is being returned multiple times and will be duplicated in the resulting GeoDataFrame.
```

#### r3 — score 0.539

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.4 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl03x', 'photon', 'processing']

**Full text:**

```
The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable (atl03_ph_fields), a per-segment variable (atl03_geo_fields, atl03_corr_fields), or a rate variable (atl03_bckgrd_fields). Ancillary fields are used to specify additional fields in the ATL03, ATL08, and ATL09 granules to be returned with the photon extent and dowstream customized products. Each field provided by the user will result in a corresponding column added to the returned GeoDataFrame. Note: if a field is requested that is already present in the default GeoDataFrame, then the name of both fields will be changed to include a _x suffix for the default incusion of the field, and a _y for the ancillary inclusion of the field.
```

#### r4 — score 0.515

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.2 ATL08-PhoREAL Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['photon', 'processing', 'series']

**Full text:**

```
Ancillary data returned from the atl08 and atl08p APIs come from the land_segments group of the ATL08 granules. The data goes through a series of processing steps before being returned back to the user as per-extent (i.e. variable-length segment) result values. When a user requests an ATL08 ancillary field, the ATL08 classifications are automatically enabled with all unclassified photons filtered out (i.e. noise, ground, canopy, and top of canopy are included; unclassified photons are excluded). If the user is also requesting PhoREAL processing, then noise photons are automatically filtered out as well. Lastly, if the user manually specifies which ATL08 photon classifications to use, then that manual specification takes precedence and is used. If a user manually specifies that unclassified photons are to be included, the value used for an ancillary field for that photon has all 1âs in the binary encoding of that value. For example, if it is an 8-bit unsigned integer, the value would be 255. If it is a double-precision floating point, the value would be -nan. Since the ATL08 APIs return per-extent values and not per-photon values, the set of per-photon ancillary field values must be reduced in some way to a single per-extent value to be returned back to the user. There are currently two options available for how this reduction occurs. Nearest Neighbor (Mode): the value that appears most often in the extent is selected. This is the default method.
```

#### r5 — score 0.501

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['photon', 'processing', 'series']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.531

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 28
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 28
- **matched_tokens:** ['processing', 'series']

**Full text:**

```
In addition to
459 recording photons from the reflected signal, the ATLAS instrument will detect
460 background photons from sunlight which are continually entering the telescope. A
461 primary objective of the ICESat-2 data processing software is to correctly
462 discriminate between signal photons and background photons. Some of this
463 processing occurs at the ATL03 level and some of it also occurs within the software
464 for ATL08. At ATL03, this discrimination is done through a series of three steps of
465 progressively finer resolution with some processing occurring onboard the satellite
466 prior to downlink of the raw data. The ATL03 data product produces a classification
467 between signal and background (i.e. noise) photons, and further discussion on that
468 classification process can be read in the ATL03 ATBD. In addition, not all geophysical
469 corrections (e.g. ocean tide) are applied to the position of the individual geolocated
470 photons at the ATL03 level, but they are provided on the ATL03 data product if there
28
```

#### r2 — score 0.573

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.3.1 Range bias determination
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 45
- **matched_tokens:** ['photon', 'processing']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
TEP-based corrections from the ISF, pre-launch data analysis of the zero-range point for each
beam (based on ATLAS Cal-08), and a model for how the TEP varies around an orbit. When the
Start Pulse Coefficient Table is used, the TEP-based range bias is combined with the TOF-flag-
based correction in quadrature to produce a single range bias value for each beam at the 1-second
rate. These corrections are included in the ANC04 ancillary data product that is passed from the
POD/PPD facility to the SIPS where ATL03 is produced. For the rapid processing of ATL03, the ANC04 file contains static values of the range-bias
correction for each beam, based on lower fidelity models. The higher fidelity model described
above requires additional processing time and is only included on the final ATL03 product. The complete ATL03 processing flow is described above in Section 2. For the purposes of the
range bias correction, ATL03 ingests the photon time of flight data from ATL02 and the range-
bias corrections from ANC04 to produce our best estimate of photon range in the geolocation
processing. The value of the range bias correction is provided on the ATL03 data product as
/gtx/geolocation/range_bias_corr. In releases 001-004, the range bias for each spot was calculated from pre-launch analysis and
calibration. The range bias correction for these releases is beam-specific and constant over time.
```

#### r3 — score 0.564

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.2 Data Flow Within ATL03
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 23
- **matched_tokens:** ['photon', 'processing']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
ATLAS is operating nominally and collecting science data. At all other times, ATL02 is the final
data product produced. There are time periods when ATLAS is conducting one of several calibration procedures. In
order to avoid contaminating science data with calibration data, ATL02 contains a "use_flag"
that indicates those periods when ATLAS is collecting normal science data or is collecting
calibration data. ATL03 and subsequent data products contain only those data where the use_flag indicates
normal science data. In some cases, this will cause an entire ATL03 granule to be skipped; in
other cases, only a portion of an ATL03 granule is skipped. In the case of a fully-skipped
ATL03, ATL02 is the final data product produced. The SIPS data processing generates an empty
ATL03 file in these cases: the metadata and orbit related parameters are correct, but the granule
contains no photon-rate data. Strictly speaking, ATL03 is generated only for those periods where ATLAS is in normal science
mode and laser transmit time information is available in these same periods of
time. Additionally, ATL03 is generated only when all necessary pieces (ATL02, POD, PPD, and
related ANC files) are available, and if there are at least 1000 photons present per beam to avoid
processing problems. If any of these are missing, ATL03 and higher-level products are not
generated.
```

#### r4 — score 0.593

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['photon', 'processing']

**Full text:**

```
1793 For this release of the software, we want to mention that there are cases of after-pulsing
1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20.
1795 For this release of the software, we have determined that we will include saturated photons.
1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to
1797 a value of 0 when ATL03 quality_ph flags photons with values other than 0, 10, or 20 such
1798 that they are ignored in the ATL08 algorithm.
1799 A third quality check pertains to the signal photons (DRAGANN + ATL03 signal
1800 confidence photons) and whether those heights are near the surface heights. To pass this
1801 check, signal photons that lie 120 m above the reference DEM will be disregarded. Signal
1802 photons lying below the reference DEM will be allowed to continue for additional ATL08
1803 processing. The motivation for this quality check is to eliminate ICESat-2 photons that are
1804 reflecting from clouds rather than the true surface.
1805 Table 4.1. Input parameters to ATL08 classification algorithm. Name Data Type Long Units Description Source
Name
delta_time DOUBLE GPS seconds Elapsed GPS seconds since start of ATL03
elapsed the granule for a given photon. Use
time the metadata attribute
granule_start_seconds to compute
full gps time.
lat_ph FLOAT latitude of degrees Latitude of each received photon.
```

#### r5 — score 0.631

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 17
- **matched_tokens:** ['photon', 'processing']

**Full text:**

```
will be used), the latitude, longitude, and time tag for every ATLAS photon detection. These
values are the primary input to ATL24 but many ATL03 specific parameters are passed
through the processing workflow and attached to the ATL24 product for user utility and
convenience. ATL03 parameters are all defined in the dedicated Algorithm Theoretical
Basis Document and the Neumann et al., 2019 publication on the product (T. A. Neumann
et al. 2019b). Table 2 provides a broad look at independent processing stages within the
ATL24 workflow with the associated input data required to provide an understanding of
the interdependencies of the algorithm on initial data products and intermediate products
produced within the computational pipeline.
```

---

