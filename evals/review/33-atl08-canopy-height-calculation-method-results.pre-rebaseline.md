# Row 33 results: nsidc / algorithm

> Auto-generated. Open this file alongside `33-atl08-canopy-height-calculation-method-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL08 canopy height calculation method`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 40–130
- **notes:** ATL08 ATBD canopy height

---

## 📚 docsearch results (top 5)

#### r1 — score 0.556

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **title:** Release v2.1.x
- **section:** Known Issues
- **category:** `release_notes`
- **matched_tokens:** ['calculation', 'canopy', 'height']

**Full text:**

```
PhoREAL processing includes some known bugs - the median ground height uses the relative heights instead of absolute heights, and the canopy openness calculation is incorrect
```

#### r2 — score 0.565

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-00-00.html
- **title:** Release v3.0.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['calculation', 'canopy', 'height']

**Full text:**

```
PhoREAL processing bug fixes: the median ground height now uses the absolute heights, and the canopy openness calculation is now correctly implements the standard deviation
```

#### r3 — score 0.545

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'height']

**Full text:**

```
at) land_segments/terrain/h_te_uncertainty h_te_median Median height of the terrain meters (float) land_segments/terrain/h_te_median h_canopy 98 percentile height of canopy photons meters (float) land_segments/canopy/h_canopy (or land_segments/canopy/h_canopy_abs if use_abs_h is true) h_canopy_uncertainty Vertical uncertainty of canopy height meters (float) land_segments/canopy/h_canopy_uncertainty segment_cover Average percentage value of the valid Copernicus fractional cover product scalar land_segments/canopy/segment_cover n_ca_photons Number of canopy photons land_segments/canopy/n_ca_photons h_max_canopy Maximum canopy height meters (float) land_segments/canopy/h_max_canopy (or land_segments/canopy/h_max_canopy_abs if use_abs_h is true) h_min_canopy Minimum canopy height meters (float) land_segments/canopy/h_min_canopy (or land_segments/canopy/h_min_canopy_abs if use_abs_h is true) h_mean_canopy Mean canopy height meters (float) land_segments/canopy/h_mean_canopy (or land_segments/canopy/h_mean_canopy_abs if use_abs_h is true) canopy_openness Standard Deviation of all canopy photons meters (float) land_segments/canopy/canopy_openness canopy_h_metrics Cumulative distribution of relative canopy heights calculated at the following percentiles: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 meters (float) land_segments/canopy/canopy_h_metrics (or land_segments/canopy/canopy_h_metrics_abs if use_abs_h is true) spot ATLAS detector field of view 1-6 Inde
```

#### r4 — score 0.440

- **url:** https://docs.slideruleearth.io/assets/phoreal.html
- **title:** Running the PhoREAL algorithm over Grand Mesa, CO
- **section:** Plot Canopy Height
- **category:** `tutorial`
- **matched_tokens:** ['atl08', 'canopy', 'height']

**Full text:**

```
[6]: canopy_gt1l = atl08 [ atl08 [ 'gt' ] == icesat2 . GT1L ] canopy_gt1l . plot . scatter ( x = 'x_atc' , y = 'h_canopy' ) [6]: <Axes: xlabel='x_atc', ylabel='h_canopy'>
```

#### r5 — score 0.588

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.688

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 7
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 7
- **matched_tokens:** ['atl08', 'calculation', 'canopy', 'height']

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

#### r2 — score 0.638

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.2.5 Ground-Finding Filter
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 17
- **matched_tokens:** ['atl08', 'canopy', 'height', 'method']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
2.3.2.2 Canopy Determination
The success of the surface finding algorithm relies heavily on correctly identifying the presence of
canopy along any given L-km length segment. Due to the large volume of data ATLAS generates,
this process is automated so that the correct methodology can be applied for surface extraction. In
the absence of canopy, the iterative filtering approach is useful; otherwise, canopy must be
accounted for when recovering the ground surface. For ATL08 product regions over Antarctica
(regions 7, 8, 9, 10) and Greenland (region 11), the algorithm assumes only ground photons
(Section 3.2.2, ATBD for ATL08).
2.3.2.3 Variable Window Determination
For both the canopy/no canopy cases, the surface finding algorithm uses a window of varying size
(i.e., span) to compute statistics and smooth and filter the data. The window size is determined
using Savitzky-Golay smoothing/median filtering, bound appropriately to prevent over-filtering. To
apply this method, the algorithm uses an empirically determined shape function that sets the
window size based on the number of photons in the L-km length segment.
```

#### r3 — score 0.619

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 121
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 121
- **matched_tokens:** ['atl08', 'canopy', 'height', 'method']

**Full text:**

```
2469 cutOff = median filter (ground, medianSpan)
2470 cutOff = smooth filter (cutOff, Window)
2471 ground = ground( (cutOff – ground) > -1 )
2472 end
2473 15. Run the ground output once more through a median filter using window side
2474 medianSpan and a smoothing filter using window size Window, but this time
2475 with the Savitzky-Golay method.
2476 16. Finally, linearly interpolate a surface from the ground points.
2477 17. The first estimate of canopy points are those indices of points that are between 2
2478 and 150 meters above the estimated ground surface. Save these indices for the
2479 next section on finding the top of canopy.
2480 18. The output from the final iteration of ground points is temp_interpA – an
2481 interpolated ground estimate.
2482 19. Find ground indices that lie within 10 m below and 0.5 m above of
2483 temp_interpA . Now, find ground indices that lie <=6 m above the refDEM
2484 20. Apply the ground indices to the original heights (i.e., not the de-trended data) to
2485 label ground photons.
2486 21. Interpolate a ground surface using the pchip method based on the ground
2487 photons. Output is interp_Aground.
2488 22. All initial ground results (interp_Aground) must lie within 6m or below the
2489 reference DEM height.
2490
2491 4.11 Find the top of the canopy
2492 The top of canopy filtering and all canopy finding shall only occur in ATL08
2493 regions 1 – 6.
```

#### r4 — score 0.732

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 49
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 49
- **matched_tokens:** ['atl08', 'canopy', 'height']

**Full text:**

```
851 2.2.8 Absolute_segment_mean_canopy
852 (parameter = h_mean_canopy_abs). The absolute mean canopy height for the
853 segment. relative canopy heights are the photons heights for canopy photons (labels
854 2 and 3) above the estimated terrain surface. These relative heights are averaged and
855 then added to h_te_bestfit.
856 2.2.9 Segment_mean_canopy
857 (parameter = h_mean_canopy). The mean canopy height for the segment.
858 Relative canopy heights have been computed by differencing the canopy photon
859 height (labels 2 and 3) from the estimated terrain surface in the ATL08 processing.
860 These heights are averaged.
861 2.2.10 Segment_dif_canopy
862 (parameter = h_dif_canopy). Difference between h_canopy and
863 canopy_h_metrics(50). This parameter is one metric used to describe the vertical
864 distribution of the canopy within the segment.
865 2.2.11 Absolute_segment_min_canopy
866 (parameter = h_min_canopy_abs). The minimum absolute canopy height for
867 the segment. Relative canopy heights are the photons heights for canopy photons
868 (labels 2 and 3) above the estimated terrain surface. Required input data is classified
869 point cloud (i.e. photons labeled as either canopy or ground in the ATL08 processing).
870 The minimum relative canopy height for each segment is added to h_te_bestfit and
871 reported as the absolute minimum canopy height.
872 2.2.12 Segment_min_canopy
873 (parameter = h_min_canopy). The minimum relative canopy height for the
874 segment.
```

#### r5 — score 0.710

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 44
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 44
- **matched_tokens:** ['atl08', 'canopy', 'height']

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

---

