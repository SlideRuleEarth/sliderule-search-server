# Row 68 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `68-atl08-100-meter-segment-terrain-canopy-height-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL08 100-meter segment terrain canopy height`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL08 100m segment is its signature; must not return ATL06 (which also uses segments)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.458

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'height', 'terrain']

**Full text:**

```
at) land_segments/terrain/h_te_uncertainty h_te_median Median height of the terrain meters (float) land_segments/terrain/h_te_median h_canopy 98 percentile height of canopy photons meters (float) land_segments/canopy/h_canopy (or land_segments/canopy/h_canopy_abs if use_abs_h is true) h_canopy_uncertainty Vertical uncertainty of canopy height meters (float) land_segments/canopy/h_canopy_uncertainty segment_cover Average percentage value of the valid Copernicus fractional cover product scalar land_segments/canopy/segment_cover n_ca_photons Number of canopy photons land_segments/canopy/n_ca_photons h_max_canopy Maximum canopy height meters (float) land_segments/canopy/h_max_canopy (or land_segments/canopy/h_max_canopy_abs if use_abs_h is true) h_min_canopy Minimum canopy height meters (float) land_segments/canopy/h_min_canopy (or land_segments/canopy/h_min_canopy_abs if use_abs_h is true) h_mean_canopy Mean canopy height meters (float) land_segments/canopy/h_mean_canopy (or land_segments/canopy/h_mean_canopy_abs if use_abs_h is true) canopy_openness Standard Deviation of all canopy photons meters (float) land_segments/canopy/canopy_openness canopy_h_metrics Cumulative distribution of relative canopy heights calculated at the following percentiles: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 meters (float) land_segments/canopy/canopy_h_metrics (or land_segments/canopy/canopy_h_metrics_abs if use_abs_h is true) spot ATLAS detector field of view 1-6 Inde
```

#### r2 — score 0.478

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'canopy', 'segment']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

#### r3 — score 0.448

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** Appendix A. Parameter Components
- **category:** `developer_guide`
- **matched_tokens:** ['atl08', 'canopy', 'height', 'segment']

**Full text:**

```
ables inputs below) Land Type : label noise : checkbox ground : checkbox canopy : checkbox top_of_canopy : checkbox unclassified : checkbox ATL03 YAPC : input switch (enables inputs below) Score : input number SR YAPC : input switch (enables inputs below) Score : input number Knn : input number Window Height : input number Window Width : input number Version : label version 1 : radio button version 2 : radio button version 3 : radio button Extents (Variable-Length Segmentation) : accordion header [ICESat-2] Length : input number (meters) Step Size : input number (meters) Distance in Segments : checkbox (changes above inputs to segments instead of meters) Pass Invalid : checkbox Along Track Spread : input number [greyed out when pass invalid selected] Minimum Photon Count : input number [greyed out when pass invalid selected] Surface Elevation Algorithm : accordion header [atl06] Maximum Iterations : input number Minimum Window Height : input number (meters) Maximum Robust Dispersion : input number (meters) Vegetation Density Algorithm : accordion header [atl08] Bin Size : input number (meters) Geolocation : label mean : radio button median : radio button center : radio button Use Absolute Heights : checkbox Send Waveforms : checkbox Use ABoVE Classifier : checkbox Ancillary Fields : accordion header [ICESat-2] ATL03 Geospatial Fields : multiselect [atl03, atl06] ATL03 Photon Fields : multiselect [atl03, atl06] ATL06 Ice Segment Fields : multiselect [atl06s] ATL08 Land Segment
```

#### r4 — score 0.416

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.3 Vegetation Metrics (PhoREAL) - atl08p
- **category:** `user_guide`
- **matched_tokens:** ['canopy', 'height', 'segment', 'terrain']

**Full text:**

```
The vegetation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) ph_count : total number of photons used by PhoREAL algorithm for this extent gnd_count : number of ground photons used by PhoREAL algorithm for this extent veg_count : number of vegetation (canopy and top of canopy) photons used by PhoREAL algorithm for this extent landcover : flag indicating if segment includes land surfaces snowcover : flag indicating if snow is present in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) x_atc : along track distance from the equator in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees h_te_median : median terrain elevation in meters (absolute heights) h_max_canopy : maximum relief height for canopy photons h_min_canopy : minimum relief height for canopy photons h_mean_canopy : average relief height for canopy photons h_canopy : 98th percentile relief height for canopy photons canopy_openness : standard deviation of relief height for canopy photons canopy_h_metrics : relief height at given percentile for canopy phot
```

#### r5 — score 0.448

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** Appendix A. Parameter Components
- **category:** `developer_guide`
- **matched_tokens:** ['atl08', 'canopy', 'height', 'segment']

**Full text:**

```
ables inputs below) Land Type : label noise : checkbox ground : checkbox canopy : checkbox top_of_canopy : checkbox unclassified : checkbox ATL03 YAPC : input switch (enables inputs below) Score : input number SR YAPC : input switch (enables inputs below) Score : input number Knn : input number Window Height : input number Window Width : input number Version : label version 1 : radio button version 2 : radio button version 3 : radio button Extents (Variable-Length Segmentation) : accordion header [ICESat-2] Length : input number (meters) Step Size : input number (meters) Distance in Segments : checkbox (changes above inputs to segments instead of meters) Pass Invalid : checkbox Along Track Spread : input number [greyed out when pass invalid selected] Minimum Photon Count : input number [greyed out when pass invalid selected] Surface Elevation Algorithm : accordion header [atl06] Maximum Iterations : input number Minimum Window Height : input number (meters) Maximum Robust Dispersion : input number (meters) Vegetation Density Algorithm : accordion header [atl08] Bin Size : input number (meters) Geolocation : label mean : radio button median : radio button center : radio button Use Absolute Heights : checkbox Send Waveforms : checkbox Use ABoVE Classifier : checkbox Ancillary Fields : accordion header [ICESat-2] ATL03 Geospatial Fields : multiselect [atl03, atl06] ATL03 Photon Fields : multiselect [atl03, atl06] ATL06 Ice Segment Fields : multiselect [atl06s] ATL08 Land Segment
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.648

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 44
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 44
- **matched_tokens:** ['100', 'atl08', 'canopy', 'height', 'segment', 'terrain']

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

#### r2 — score 0.631

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 94
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 94
- **matched_tokens:** ['100', 'atl08', 'canopy', 'height', 'segment', 'terrain']

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

#### r3 — score 0.573

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 20
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['100', 'atl08', 'canopy', 'height', 'segment', 'terrain']

**Full text:**

```
259 1 INTRODUCTION
260 This document describes the theoretical basis and implementation of the
261 processing algorithms and data parameters for Level 3 land and vegetation heights
262 for the non-polar regions of the Earth. The ATL08 product contains heights for both
263 terrain and canopy in the along-track direction as well as other descriptive
264 parameters derived from the measurements. At the most basic level, a derived surface
265 height from the ATLAS instrument at a given time is provided relative to the WGS-84
266 ellipsoid. Height estimates from ATL08 can be compared with other geodetic data and
267 used as input to higher-level ICESat-2 products, namely ATL13 and ATL18. ATL13
268 will provide estimates of inland water-related heights and associated descriptive
269 parameters. ATL18 will consist of gridded maps for terrain and canopy features.
270 The ATL08 product will provide estimates of terrain heights, canopy heights,
271 and canopy cover at fine spatial scales in the along-track direction. Along-track is
272 defined as the direction of travel of the ICESat-2 satellite in the velocity vector.
273 Parameters for the terrain and canopy will be provided at a fixed step-size of 100 m
274 along the ground track referred to as a segment. A fixed segment size of 100 m was
275 chosen to provide continuity of data parameters on the ATL08 data product.
```

#### r4 — score 0.704

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 49
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 49
- **matched_tokens:** ['atl08', 'canopy', 'height', 'segment', 'terrain']

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

#### r5 — score 0.654

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 48
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 48
- **matched_tokens:** ['atl08', 'canopy', 'height', 'segment', 'terrain']

**Full text:**

```
826 2.2.5 Absolute_segment_canopy_height
827 (parameter = h_canopy_abs). The absolute 98% height of classified canopy
828 photon heights (labels 2 and 3) above the ellipsoid. The relative height from classified
829 canopy photons are sorted into a cumulative distribution, and the height associated
830 with the 98% height above the h_te_bestfit for that segment is reported. For cases
831 where the h_te_bestfit is invalid, the cumulative distribution will be calculated for the
832 absolute canopy heights and the 98% absolute height will be reported.
833 2.2.6 Segment_canopy_height
834 (parameter = h_canopy). The relative 98% height of classified canopy photon
835 heights (labels 2 and 3) above the estimated terrain surface. Relative canopy heights
836 have been computed by differencing the canopy photon height from the estimated
837 terrain surface in the ATL08 processing. The relative canopy heights are sorted into
838 a cumulative distribution, and the height associated with the 98% height is reported.
839 2.2.7 canopy_height GeoSegment {1:5}
840 (parameter = h_canopy_20m). The relative 98% height of classified canopy
841 photon heights (labels 2 and 3) above the estimated terrain surface in each 20 m
842 geosegment. Relative canopy heights have been computed by differencing the canopy
843 photon height from the estimated terrain surface in the ATL08 processing.
```

---

