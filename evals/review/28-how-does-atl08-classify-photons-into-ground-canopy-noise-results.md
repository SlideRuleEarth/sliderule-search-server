# Row 28 results: nsidc / algorithm

> Auto-generated. Open this file alongside `28-how-does-atl08-classify-photons-into-ground-canopy-noise-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does ATL08 classify photons into ground canopy noise`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 10–80
- **notes:** ATL08 ATBD photon classification

---

## 📚 docsearch results (top 5)

#### r1 — score 0.638

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.2 ATL08-PhoREAL Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'noise', 'photons']

**Full text:**

```
Ancillary data returned from the atl08 and atl08p APIs come from the land_segments group of the ATL08 granules. The data goes through a series of processing steps before being returned back to the user as per-extent (i.e. variable-length segment) result values. When a user requests an ATL08 ancillary field, the ATL08 classifications are automatically enabled with all unclassified photons filtered out (i.e. noise, ground, canopy, and top of canopy are included; unclassified photons are excluded). If the user is also requesting PhoREAL processing, then noise photons are automatically filtered out as well. Lastly, if the user manually specifies which ATL08 photon classifications to use, then that manual specification takes precedence and is used. If a user manually specifies that unclassified photons are to be included, the value used for an ancillary field for that photon has all 1âs in the binary encoding of that value. For example, if it is an 8-bit unsigned integer, the value would be 255. If it is a double-precision floating point, the value would be -nan. Since the ATL08 APIs return per-extent values and not per-photon values, the set of per-photon ancillary field values must be reduced in some way to a single per-extent value to be returned back to the user. There are currently two options available for how this reduction occurs. Nearest Neighbor (Mode): the value that appears most often in the extent is selected. This is the default method.
```

#### r2 — score 0.514

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v01-01-00.html
- **title:** Release v1.1.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'noise', 'photons']

**Full text:**

```
Time is also used as the index. (APIs affected: atl06 , atl06p , atl03s , atl03sp ). v1.1.0 - ATL08 classifications are now supported in the atl06 , atl06p , atl03s , atl03sp APIs: sliderule#71 when the request parameters supply a list of ATL08 classifications to use, the server code will read the corresponding ATL08 data and only use the supplied classifications in the calculation the following classifications are supported: noise, ground, canopy, top of canopy, unclassified for the atl03s , atl03sp , the presence of the ATL08 classification list also enables the returned photon data to include each photons classification v1.1.0 - The following APIs now return GeoDataFrames instead of dictionaries: atl06 , atl06p , atl03s , atl03sp . this standardizes the return structure at no cost to performance each GeoDataFrame has a âtimeâ column which is a Python datetime value each GeoDataFrame uses the geometry.x and geometry.y to represent the âlongitudeâ and âlatitudeâ fields respectively. the âdelta_timeâ column now represents the time from the ATLAS Standard Data Product (SDP) epoch (January 1, 2018) The GeoDataFrames returned by atl03s and atl03sp contain a row for each photon that is returned v1.1.0 - All APIs default to using version 004 of the data products. v1.1.0 - Added the ground track field ( âgtâ ) to the atl06 and atl06p elevation returns. added the following constants to the icesat2.py module: GT1L, GT1R, GT2L, GT2R, GT3L, GT3R you can now do thing
```

#### r3 — score 0.490

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'noise', 'photons']

**Full text:**

```
The GeoDataFrame for each photon extent has the following columns: track : reference pair track number (1, 2, 3) sc_orient : spacecraft orientation (0: backwards, 1: forwards) rgt : reference ground track cycle : cycle segment_id : segment ID of first ATL03 segment in result segment_dist : along track distance from the equator to the center of the extent (in meters) count : the number of photons in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds latitude : latitude (-90.0 to 90.0) longitude : longitude (-180.0 to 180.0) x_atc : along track distance of the photon in meters (with respect to the center of the segment) y_atc : across track distance of the photon in meters across : across track distance of the photon in meters height : height of the photon in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees background_rate : background photon counts per second atl08_class : the photonâs ATL08 classification (0: noise, 1: ground, 2: canopy, 3: top of canopy, 4: unclassified) atl03_cnf : the photonâs ATL03 confidence level (-2: TEP, -1: not considered, 0: background, 1: within 10m, 2: low, 3: medium, 4: high) quality_ph : the photonâs quality classification (0: nominal, 1: possible after pulse, 2: possible impulse responpse effect, 3: possible tep) yapc_score : the photonâs YAPC classification (0 - 255, the larger the number the higher the confidence in surface reflection) Note: when PhoREAL is enabl
```

#### r4 — score 0.528

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'photons']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

#### r5 — score 0.595

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['noise', 'photons']

**Full text:**

```
The ATL06-SR algorithm fits a line segment to the photons in each extent, using an iterative selection refinement to eliminate noise photons not correctly identified by the photon classification. The results are then checked against three parameters : sigma_r_max , which eliminates segments for which the robust dispersion of the residuals is too large, and the ats and cnt parameters described above, which eliminate segments for which the iterative fitting has eliminated too many photons. The algorithm is run by supplying the fit parameter in the processing request, but can also be run via the legacy atl06 and atl06p endpoints.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.679

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['atl08', 'canopy', 'into', 'noise', 'photons']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Processing
To detect both the canopy surface and the underlying topography, the ATL08 software has been
designed to accept multiple approaches to capture both the upper and lower surface signal
photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best
preserves signal photons returned from the canopy and topography while rejecting noise photons. The following sections outline the approach implemented by the algorithm. More detailed
descriptions are available in "Section 3 | Algorithm Methodology" and "Section 4 | Algorithm
Implementation" of the ATBD for ATL08.
2.3.1 Noise Filtering
Removing solar background photons represents one of the biggest challenges with photon
counting lidar data. The ATL03 signal finding approach uses a histogramming strategy that places
photons into vertical bins along a consistent horizontal span and then assumes the signal lies
within the bins that contain the highest number of photons. This method works well over simple
surfaces such as ice sheets; however, photons that are reflected from the top of the canopy in
vegetated areas are not always flagged as signal.
```

#### r2 — score 0.655

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 4.2 Date Last Updated
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'into', 'noise', 'photons']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Table 5. Version History Summary
Version Date Description
V1 May 2019 Initial release
V2 October 2019 Refer to V2 User Guide
V3 May 2020 Refer to V3 User Guide
V4 April 2021 Refer to V4 User Guide
V5 November 2021 Refer to V5 User Guide
• Added a quality check to reject segments for which the V6 May 2023
canopy photons fall more than 150 m below the reference
DEM.
• Calculated the background noise rate and number of noise
photons within a canopy segment and adjusted the canopy
radiometric rate accordingly.
• For segments with a solar elevation angle > 20°, if the
background noise rate is < 0.98 of the canopy rate, then
reassign the canopy photons as noise photons.
• Incorporated the YAPC photon weights from the ATL03
data product into the ground-finding approach.
• Reduced the number of labeled photons required to report
the canopy or terrain heights within each segment for the
strong and weak beams, resulting in more ATL08 reported
values.
V6.1 May 2024 Data from 13 November 2022 to 26 October 2023 were
reprocessed using ITRF2014 (replacing ITRF2020) for
consistency across the entire data set.
V6.1 March 2026 Data access was removed for v6.1. Data coverage was 14 Oct
2018 to 2 Mar 2025.
Publication Date
May 2023
Date Last Updated
March 2026
Page 19 of 19National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.623

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 76
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 76
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'into', 'noise', 'photons']

**Full text:**

```
1410 3 ALGORITHM METHODOLOGY
1411 For the ecosystem community, identification of the ground and canopy surface
1412 is by far the most critical task, as meeting the science objective of determining global
1413 canopy heights hinges upon the ability to detect both the canopy surface and the
1414 underlying topography. Since a space-based photon counting laser mapping system
1415 is a relatively new instrument technology for mapping the Earth’s surface, the
1416 software to accurately identify and extract both the canopy surface and ground
1417 surface is described here. The methodology adopted for ATL08 establishes a
1418 framework to potentially accept multiple approaches for capturing both the upper
1419 and lower surface of signal photons. One method used is an iterative filtering of
1420 photons in the along-track direction. This method has been found to preserve the
1421 topography and capture canopy photons, while rejecting noise photons. An advantage
1422 of this methodology is that it is self-parameterizing, robust, and works in all
1423 ecosystems if sufficient photons from both the canopy and ground are available. For
1424 processing purposes, along-track data signal photons are parsed into L-km segment
1425 of the orbit which is recommended to be 10 km in length.
1426
1427 3.1 Noise Filtering
1428 Solar background noise is a significant challenge in the analysis of photon
1429 counting laser data.
```

#### r4 — score 0.713

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.5 Refining the Photon Classifications
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 18
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'noise', 'photons']

**Full text:**

```
Signal
photon classifications are stored in gt[x]/signal_photons/classed_pc_flag and use the
following values: noise (0), ground (1), canopy (2), and top of canopy (3) (Section 3.4, ATBD for
ATL08).
2.3.5 Refining the Photon Classifications
During the first surface finding iteration, the algorithm may mislabel some photons (most likely
classifying noise as canopy). After the first iteration, the algorithm then rejects photons as
mislabeled based on set of criteria designed to identify statistically unlikely and unphysical canopy
classifications. In addition, photons labeled as ground are evaluated and reassigned as needed based on the how
the ground surface was determined and whether canopy photons have been detected. If no canopy
photons are present for an L-km length segment, then the final ground surface is interpolated from
the identified ground photons and the segment receives a final round of median filtering and
smoothing. If canopy photons are present, then the final ground surface is interpolated based on
the amount of canopy at that location along the segment and constructed iteratively as a composite
of various intermediate surfaces. The ground and the canopy refinement criteria are detailed in
"Section 3.5 | Refining the Photon Labels" of the ATBD for ATL08. Page 17 of 19National Snow and Ice Data Center
nsidc.org
```

#### r5 — score 0.655

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 31
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 31
- **matched_tokens:** ['atl08', 'canopy', 'ground', 'noise', 'photons']

**Full text:**

```
520 1.6 Additional Potential Height Errors from ATLAS
521 Some additional potential height errors in the ATL08 terrain and vegetation
522 product can come from a variety of sources including:
523 a. Vertical sampling error. ATLAS height estimates are based on a
524 random sampling of the surface height distribution. Photons may
525 be reflected from anywhere within the PDF of the reflecting surface;
526 more specifically, anywhere from within the canopy. A detailed
527 look at the potential effect of vertical sampling error is provided in
528 Neuenschwander and Magruder (2016).
529 b. Background noise. Random noise photons are mixed with the
530 signal photons so classified photons will include random outliers.
531 c. Complex topography. The along-track product may not always
532 represent complex surfaces, particularly if the density of ground
533 photons does not support an accurate representation.
534 d. Vegetation. Dense vegetation may preclude reflected photon
535 events from reaching the underlying ground surface. An incorrect
536 estimation of the underlying ground surface will subsequently lead
537 to an incorrect canopy height determination.
538 e. Misidentified photons. The product from ATL03 combined with
539 additional noise filtering may not identify the correct photons as
540 signal photons.
541
542 1.7 Dense Canopy Cases
543 Although the height accuracy produced from ICESat-2 is anticipated to be
544 superior to other global height products (e.g.
```

---

