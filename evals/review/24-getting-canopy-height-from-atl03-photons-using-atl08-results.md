# Row 24 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `24-getting-canopy-height-from-atl03-photons-using-atl08-review.md` —
> verdicts go there, this side is read-only.

**Query:** `getting canopy height from atl03 photons using atl08`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/phoreal.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
  - https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **expected_sections:**
  - `atl08 classification`
  - `phoreal`
  - `1.2.3 atl08`
  - `1.6 phoreal`
  - `3. atl08`
- **expected_pages:** (none)
- **notes:** phoreal / atl08_class usage

---

## 📚 docsearch results (top 5)

#### r1 — score 0.688

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'height', 'photons']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r2 — score 0.651

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'photons']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

#### r3 — score 0.513

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height', 'photons']

**Full text:**

```
The GeoDataFrame for each photon extent has the following columns: track : reference pair track number (1, 2, 3) sc_orient : spacecraft orientation (0: backwards, 1: forwards) rgt : reference ground track cycle : cycle segment_id : segment ID of first ATL03 segment in result segment_dist : along track distance from the equator to the center of the extent (in meters) count : the number of photons in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds latitude : latitude (-90.0 to 90.0) longitude : longitude (-180.0 to 180.0) x_atc : along track distance of the photon in meters (with respect to the center of the segment) y_atc : across track distance of the photon in meters across : across track distance of the photon in meters height : height of the photon in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees background_rate : background photon counts per second atl08_class : the photonâs ATL08 classification (0: noise, 1: ground, 2: canopy, 3: top of canopy, 4: unclassified) atl03_cnf : the photonâs ATL03 confidence level (-2: TEP, -1: not considered, 0: background, 1: within 10m, 2: low, 3: medium, 4: high) quality_ph : the photonâs quality classification (0: nominal, 1: possible after pulse, 2: possible impulse responpse effect, 3: possible tep) yapc_score : the photonâs YAPC classification (0 - 255, the larger the number the higher the confidence in surface reflection) Note: when PhoREAL is enabl
```

#### r4 — score 0.449

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'height', 'photons']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) dist_ph_along + segment_distance y_atc Across track distance meters (float) dist_ph_across photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags ground_photon_count Number of photons classified as ground in the segment vegetation_photon_count Number of photons classified as canopy or top of canopy in the segment landcover ATL08 land cover flags snowcover ATL08 snow cover flags solar_elevation Sun elevation as provided in ATL03 degrees (float) h_te_median Median ellipsoidal height of the ground photons meters (float) vertical datum controlled by parameters, default is ITRF2014 h_max_canopy Maximum relief height for canopy photons meters (float) h_min_canopy Minimum relief height for canopy photons meters (float) h_mean_canopy Mean relief height for canopy photons meters (float) h_canopy 98th percentile relief height for canopy photons meters (float) canopy_openness Standard deviation of relief height for canopy photons canopy_h_metrics relief height at given percentile for canopy p
```

#### r5 — score 0.627

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'height', 'photons']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.635

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 4.2 Date Last Updated
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height', 'photons', 'using']

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

#### r2 — score 0.677

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 7
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 7
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height']

**Full text:**

```
The
saturation flag indicates that the ATL08 segment
experienced some saturation which is often an indicator for
water
2020 May 15 Canopy height metrics (relative and absolute heights) were
expanded to every 5% ranging from 5 – 95%.
2020 May 15 The Landsat canopy cover check to determine whether the
algorithm should search for both ground and canopy or just
ground has been disabled. Now the ATL08 algorithm will
search for both ground and canopy points everywhere.
2020 June 15 Corrected the calculation of the absolute canopy heights
2020 June 15 Changed the search radius for initial top of canopy
determination (Section 4.9)
2020 September 1 Incorporate the quality_ph flag from ATL03 into the ATL08
workflow (beginning of Section 4)
2020 September 1 Added the calculation of Terrain photon rate
(photon_rate_te) for each ATL08 segment to the land
product (Section 2.1.16)
2020 September 1 Added the calculation of canopy photon rate
(photon_rate_can) for each ATL08 segment to the land
product (Section 2.2.26)
7
```

#### r3 — score 0.627

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 44
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 44
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height', 'photons']

**Full text:**

```
775
776 Figure 2.4. Illustration of canopy photons (red dots) interaction in a vegetated area.
777 Relative canopy heights, Hi, are computed by differencing the canopy photon height from
778 an interpolated terrain surface.
779 Table 2.2. Summary table of canopy parameters on ATL08.
Group Data Type Description Source
segment_id_beg Integer First along-track segment_id number ATL03
in 100-m segment
segment_id_end Integer Last along-track segment_id number ATL03
in 100-m segment
canopy_h_metrics_abs Float Absolute (H##) canopy height computed
metrics calculated at the following
percentiles: 5, 10, 15, 20, 25, 30, 35,
40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
90, 95.
canopy_h_metrics Float Relative (RH##) canopy height computed
metrics calculated at the following
percentiles: 5, 10, 15, 20, 25, 30, 35,
40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
90, 95.
h_canopy_abs Float 98% height of all the individual computed
absolute canopy heights (height
above WGS84 ellipsoid) for segment.
h_canopy Float 98% height of all the individual computed
relative canopy heights (height
above terrain) for segment.
44
```

#### r4 — score 0.616

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height', 'photons']

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

#### r5 — score 0.584

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 54
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 54
- **matched_tokens:** ['atl03', 'atl08', 'canopy', 'from', 'height', 'photons', 'using']

**Full text:**

```
979 2.2.26 Segment Background Photons in Canopy
980 (parameter = can_noise). This value represents the number of background
981 photons that occur within the canopy height span of the 100 m ATL08 segment. Using
982 the parameters from the ATL03 bckgrd_atlas subgroup (bckgrd_counts_reduced) and
983 (bckgrd_in_height_reduced) we calculate the background noise rate (counts/m). The
984 background noise rate is averaged across the ATL08 and finally multiplied by the
985 ATL08 relative canopy height_(h_canopy).
986 Pseudocode for background noise photon removal
987 bcr = ATL03[gt + '/bckgrd_atlas/bckgrd_counts_reduced']
988 bihr = ATL03[gt + '/bckgrd_atlas/bckgrd_int_height_reduced']
989 # Calculate the Background Count Error Rate
990 rate = bcr / bihr
991
992 # Append the error rate from the 'Background Atlas' bins to the ATL03 Photon Level
993 ph_rate = rate[inds]
994
995 # Aggregate the error rate to the ATL08 rate by calculating the mean ph_rate
996 f08_rate = mean(ph_rate)
997
998 # Multiply the photon error rate at the ATL08 level to the h_max_canopy
999 canopy_noise_count = (f08_rate) * h_ canopy
1000
1001 2.2.27 Canopy Quality Score
1002 (Parameter = can_quality_score). The computed skill score of multiple
1003 parameters for each 100 m ATL08 segment. A score of 100 indicates a likely high
1004 quality estimate of canopy height. Deductions for the canopy skill score are as follows.
54
```

---

