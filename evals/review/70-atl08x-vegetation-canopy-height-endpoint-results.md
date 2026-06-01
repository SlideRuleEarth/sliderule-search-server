# Row 70 results: docsearch / identifier

> Auto-generated. Open this file alongside `70-atl08x-vegetation-canopy-height-endpoint-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl08x vegetation canopy height endpoint`
**Panel signature:** `30eaf1cfec17`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `3. atl08`
  - `atl08x`
- **expected_pages:** (none)
- **notes:** atl08x endpoint

---

## 📚 docsearch results (top 5)

#### r1 — score 0.512

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['atl08x', 'endpoint', 'vegetation']

**Full text:**

```
The SlideRule atl08x endpoint provides a service for ATL08 subsetting and custom processing. This endpoint queries ATL08 input granules for segment vegetation statistics and locations based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r2 — score 0.576

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['height', 'vegetation']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r3 — score 0.446

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['atl08x', 'canopy', 'height']

**Full text:**

```
at) land_segments/terrain/h_te_uncertainty h_te_median Median height of the terrain meters (float) land_segments/terrain/h_te_median h_canopy 98 percentile height of canopy photons meters (float) land_segments/canopy/h_canopy (or land_segments/canopy/h_canopy_abs if use_abs_h is true) h_canopy_uncertainty Vertical uncertainty of canopy height meters (float) land_segments/canopy/h_canopy_uncertainty segment_cover Average percentage value of the valid Copernicus fractional cover product scalar land_segments/canopy/segment_cover n_ca_photons Number of canopy photons land_segments/canopy/n_ca_photons h_max_canopy Maximum canopy height meters (float) land_segments/canopy/h_max_canopy (or land_segments/canopy/h_max_canopy_abs if use_abs_h is true) h_min_canopy Minimum canopy height meters (float) land_segments/canopy/h_min_canopy (or land_segments/canopy/h_min_canopy_abs if use_abs_h is true) h_mean_canopy Mean canopy height meters (float) land_segments/canopy/h_mean_canopy (or land_segments/canopy/h_mean_canopy_abs if use_abs_h is true) canopy_openness Standard Deviation of all canopy photons meters (float) land_segments/canopy/canopy_openness canopy_h_metrics Cumulative distribution of relative canopy heights calculated at the following percentiles: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 meters (float) land_segments/canopy/canopy_h_metrics (or land_segments/canopy/canopy_h_metrics_abs if use_abs_h is true) spot ATLAS detector field of view 1-6 Inde
```

#### r4 — score 0.493

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.3 Vegetation Metrics (PhoREAL) - atl08p
- **category:** `user_guide`
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
The vegetation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) ph_count : total number of photons used by PhoREAL algorithm for this extent gnd_count : number of ground photons used by PhoREAL algorithm for this extent veg_count : number of vegetation (canopy and top of canopy) photons used by PhoREAL algorithm for this extent landcover : flag indicating if segment includes land surfaces snowcover : flag indicating if snow is present in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) x_atc : along track distance from the equator in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees h_te_median : median terrain elevation in meters (absolute heights) h_max_canopy : maximum relief height for canopy photons h_min_canopy : minimum relief height for canopy photons h_mean_canopy : average relief height for canopy photons h_canopy : 98th percentile relief height for canopy photons canopy_openness : standard deviation of relief height for canopy photons canopy_h_metrics : relief height at given percentile for canopy phot
```

#### r5 — score 0.510

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **title:** Release v2.1.x
- **section:** Known Issues
- **category:** `release_notes`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
PhoREAL processing includes some known bugs - the median ground height uses the relative heights instead of absolute heights, and the canopy openness calculation is incorrect
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.624

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 20
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
From an
276 analysis perspective, it is difficult and cumbersome to attempt to relate canopy cover
277 over variable lengths. Furthermore, a segment size of 100 m will facilitate a simpler
278 combination of along-track data to create the gridded products.
279 We anticipate that the signal returned from the weak beam will be sufficiently
280 weak and may prohibit the determination of both a terrain and canopy segment
281 height, particularly over areas of dense vegetation. However, in more arid regions we
282 anticipate producing a terrain height for both the weak and strong beams.
283 In this document, section 1 provides a background of lidar in the ecosystem
284 community as well as describing photon counting systems and how they differ from
285 discrete return lidar systems. Section 2 provides an overview of the Land and
286 Vegetation parameters and how they are defined on the data product. Section 3
287 describes the basic methodology that will be used to derive the parameters for ATL08.
20
```

#### r2 — score 0.654

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 43
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 43
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
753 3. Optical Depth <0.2 – 0.3; deduct 5 points >0.3 deduct 10 points
754 4. Cloud Fold flag >0; deduct 10 points
755 5. DEM_removal_flag > 0; deduct 10 points
756 6. Terrain radiometry < 0.2; deduct 10 points; terrain radiometry between
757 0.2 and 0.5 deduct 5 points
758 7. Track telemetry band removal, if 40% of 10km removed, deduct 10 points
759 for entire 10 km.
760 8. MSW_flag > 0; deduct 10 points
761 9. SNR < 1; deduct 10 points
762 2.2 Subgroup: Vegetation Parameters
763 Canopy parameters will be reported on the ATL08 data product in terms of both
764 the absolute height above the reference ellipsoid as well as the relative height above
765 an estimated ground. The relative canopy height, Hi, is computed as the height from
766 an identified canopy photon minus the interpolated ground surface for the same
767 horizontal geolocation (see Figure 2.3). Thus, each identified signal photon above an
768 interpolated surface (including a buffer distance based on the instrument point
769 spread function) is by default considered a canopy photon. For strong beams, canopy
770 parameters will only be computed for segments where more than 10 of the at least
771 50 labeled signal photons are labeled as canopy photons. For weak beams, canopy
772 parameters will only be computed for segments having at least 30 signal photons with
773 6 of them being labeled as canopy photons.
774
43
```

#### r3 — score 0.669

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 94
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 94
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
1751 Canopy photons (shown as blue) are considered as photons lying between the terrain
1752 surface and top of canopy.
1753
1754 3.6 Canopy Height Determination
1755 Once a final ground surface is determined, canopy heights for individual
1756 photons are computed by removing the ground surface height for that photon’s
1757 latitude/longitude. These relative canopy height values will be used to compute the
1758 canopy statistics on the ATL08 data product.
1759
1760 3.7 Link Scale for Data products
1761 The link scale for each segment within which values for vegetation parameters
1762 will be derived will be defined over a fixed distance of 100 m. A fixed segment length
1763 ensures that canopy and terrain metrics are consistent between segments, in addition
1764 to increased ease of use of the final products. A size of 100 m was selected as it should
1765 provide approximately 140 photons (a statistically sufficient number) from which to
1766 make the calculations for terrain and canopy height.
1767
94
```

#### r4 — score 0.645

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 47
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 47
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
The height
818 metrics are sorted based on a cumulative distribution and calculated at the following
819 percentiles: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95. These
820 height metrics are often used in the literature to characterize vertical structure of
821 vegetation. One important distinction of these canopy height metrics compared to
822 those derived from other lidar systems (e.g., LVIS or GEDI) is that the ICESat-2 canopy
823 height metrics are heights above the ground surface. These metrics do not include the
824 ground photons. Required input data are relative canopy heights above the estimated
825 terrain surface for all canopy photons.
47
```

#### r5 — score 0.615

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 47
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 47
- **matched_tokens:** ['canopy', 'height', 'vegetation']

**Full text:**

```
799 2.2.3 Canopy_height_metrics_abs
800 (parameter = canopy_h_metrics_abs). The absolute height metrics (H##) of
801 classified canopy photons (labels 2 and 3) above the ellipsoid. The height metrics are
802 sorted based on a cumulative distribution and calculated at the following percentiles:
803 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95. These height metrics
804 are often used in the literature to characterize vertical structure of vegetation. One
805 important distinction of these canopy height metrics compared to those derived from
806 other lidar systems (e.g., LVIS or GEDI) is that the ICESat-2 canopy height metrics are
807 heights above the ground surface. These metrics do not include the ground photons.
808 Required input data are the relative canopy heights of all canopy photons above the
809 estimated terrain surface and the mid-segment elevation. The absolute canopy
810 heights metrics are determined by adding the relative canopy height metric to the
811 best-fit terrain (h_te_bestfit). For cases where the h_te_bestfit is invalid, the
812 cumulative distribution will be calculated for the absolute canopy heights (not the
813 relative canopy heights) and those cumulative heights will be reported.
814
815 2.2.4 Canopy_height_metrics
816 (parameter = canopy_h_metrics). Relative height metrics above the estimated
817 terrain surface (RH##) of classified canopy photons (labels 2 and 3).
```

---

