# Row 67 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `67-atl06-land-ice-along-track-segment-elevation-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL06 land ice along-track segment elevation`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL06-specific segment elevation

---

## 📚 docsearch results (top 5)

#### r1 — score 0.561

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['along', 'elevation', 'ice', 'land', 'segment', 'track']

**Full text:**

```
Using the Python client, this service is called via: sliderule . run ( 'atl08x' , parms ) The default resulting DataFrame from this endpoint contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) land_ice_segments/ground_track/x_atc y_atc Across track distance meters (float) land_ice_segments/ground_track/y_atc segment_id_beg First ATL03 segment used in ATL08 100m segment count land_segments/segment_id_beg segment_landcover UN-FAO Land Cover Surface type classification as reference from Copernicus Land Cover(ANC18) at the 100m resolution land_segments/segment_landcover segment_snowcover Daily snow/ice cover from ATL09 at the 25 Hz rate(275m) indicating likely presence of snow and ice within each segment 0: ice free water; 1: snow free land; 2: snow; 3: ice land_segments/segment_snowcover n_seg_ph Number of photons within each land segment count land_segments/n_seg_ph solar_elevation Solar elevation at time of measurement degrees (float) land_segments/solar_elevation terrain_slope Along-track slope of the terrain meters (float) land_segments/terrain/terrain_slope n_te_photons Number of terrain (ground) photons count land_segments/terrain/n_te_photons h_te_uncertainty Uncertainty of height of terrian meters (flo
```

#### r2 — score 0.629

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['along', 'atl06', 'elevation', 'segment', 'track']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r3 — score 0.512

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl06', 'elevation', 'ice', 'land', 'segment']

**Full text:**

```
The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of segments for each beam. In SlideRule the average segment elevations will not be corrected for transmit pulse shape biases or first photon biases as compared to the higher level data products.
```

#### r4 — score 0.494

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['along', 'atl06', 'elevation', 'segment', 'track']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r5 — score 0.522

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['along', 'atl06', 'segment', 'track']

**Full text:**

```
Using the Python client, this service is called via: sliderule . run ( 'atl06x' , parms ) The default resulting DataFrame from this endpoint contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) land_ice_segments/ground_track/x_atc y_atc Across track distance meters (float) land_ice_segments/ground_track/y_atc h_li Median-based height of segment meters (float) land_ice_segments/h_li h_li_sigma Propagated error due to sampling error and FPB correction meters (float) land_ice_segments/h_li_sigma sigma_geo_h Total vertical geolocation error due to PPD and POD meters (float) land_ice_segments/sigma_geo_h atl06_quality_summary Best-quality subset of all ATL06 data 0: no data-quality tests have found a problem with the segment, 1: some potential problem has been found land_ice_segments/atl06_quality_summary segment_id Segment ID for the second of the two 20m ATL03 segments included in the 40m ATL06 segment count land_ice_segments/segment_id seg_azimuth Azimuth of the pair-track, east of local north degrees (float) land_ice_segments/ground_track/seg_azimuth dh_fit_dx Along-track slope from along-track segment fit meters (float) land_ice_segments/fit_statistics/dh_fit_dx h_robust_sprd RDE of misfit between PE heights
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.751

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 19
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 19
- **matched_tokens:** ['along', 'atl06', 'ice', 'land', 'segment', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
179 and 2 of the mission, ICESat-2 did not point at the RPTS, and ICESat2’s pairs are offset by up to
180 2 km from the RPT locations. The first cycle that was collected over the RPTS was the third.
181 We define ATL06 heights based on fits of a linear model to ATL03 height data from short
182 (40 m) segments of the ground track, centered on reference points spaced at 20-m intervals
183 along-track. We refer to height estimates for these short segments as “segment heights”, and
184 segment’s horizontal location is that of the reference point, displaced in a direction perpendicular
185 to the RGT to match the GT offset. The choice of 40 m for the segment length provides data
186 from slightly more than two independent (non-overlapping) ATL03 heights (based on 17-m
187 footprints) for the along-track slope estimate, so that this component of the slope can be
188 eliminated as a cause of vertical scatter in the PE height distribution. The spacing between
189 reference points is 20 m, so that each segment overlaps its neighbors by 50%.
```

#### r2 — score 0.743

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 27
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 27
- **matched_tokens:** ['along', 'atl06', 'ice', 'land', 'segment', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
338
Figure 3-5. RGT coordinates
N
azimuth
Seg
PRGT
y
x
P
RGT
RPT
Along-track coordinates for point P relative to its RGT. The track drawn is ascending, in
the northern hemisphere, so x is increasing from south to north. Y at P is negative.
339
340 The AL06 along-track coordinate for each segment is given by the parameter x_atc. The across-
341 track coordinate is given by y_atc, and the angle between the along-track vector and local north
342 is given in the parameter seg_azimuth. To allow easy referencing between ATL06 and ATL03,
343 we provide the number for the second ATL03 segment in each ATL06 segment in the variable
344 segment_id.
345 3.3.3 Parameters describing selected PEs
346 ATL06 heights and slopes are estimated by piecewise-linear fits to PEs within each overlapping
347 40-m segment. Since ATL06 segments are 40-meters long and overlap by 50%, we can collect
15
```

#### r3 — score 0.712

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 25
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 25
- **matched_tokens:** ['along', 'atl06', 'ice', 'land', 'segment', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
312 same. Each cycle, i, contributes measurements from two beams, with different l values, to the
313 repeat; these different measurements allow the across-track slope to be constrained
314 independently from the height change, and the along-track segment fitting procedure allows us to
315 correct for the along-track slope. Both ATL03 and ATL06 use this segment numbering scheme;
316 however, ATL06 segments are 40 m long and overlap their neighbors by 50%, while ATL03
317 segments are 20 m long and are disjoint. ATL06 segments are defined as including PE from pairs
318 of adjacent ATL03 segments, and are numbered to match the second of the two, so that ATL06
Figure 3-4. Example PE selection
Selecting PEs for a reference point. Top: GT locations for eight simulated repeat
measurement of track 188 (colored lines). Black lines are plotted every 2 km in the
along-track coordinate x. Bottom: selected footprint locations for a reference point on PT
3 (circles, every 10th shown). Lines and circles are color coded by repeat. Solid points
show reference-point locations, dashed lines show the 40-m along-track extent of the
segments, filled circles show segment centers. Background image from (Scambos and
others, 2007)
319 segment m includes ATL03 segments m and m-1.
13
```

#### r4 — score 0.662

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 1
- **matched_tokens:** ['along', 'atl06', 'elevation', 'ice', 'land', 'track']

**Full text:**

```
Ice, Cloud, and land Elevation Satellite-2
(ICESat-2) Project
Algorithm Theoretical Basis Document (ATBD)
for
Land Ice Along-Track Height Product (ATL06)
Prepared by: Benjamin Smith, University of Washington Applied Physics Lab
with
David Hancock, Kaitlin Harbeck, LeeAnne Roberts, Thomas Neumann, Kelly
Brunt, Helen Fricker, Alex Gardner, Matthew Siegfried, Susheel Adusumilli,
Beata Csathó, Nicholas Holschuh, Johan Nilsson, and Fernando Paolo
Maintained by: Denis Felikson, NASA Goddard Space Flight Center
This document may be cited as:
Smith, B., D. Hancock, K. Harbeck, L. Roberts, T. Neumann, K. Brunt, H. Fricker, A. Gardner,
M. Siegfried, S. Adusumilli, B. Csatho, N. Holschuh, J. Nilsson, F. Paolo, and D. Felikson
(2022). Ice, Cloud, and Land Elevation Satellite (ICESat-2) Project Algorithm Theoretical Basis
Document (ATBD) for Land Ice Along-Track Height Product (ATL06), Version 6. ICESat-2
Project, DOI: 10.5067/VWOKQDYJ7ODB.
Goddard Space Flight Center
Greenbelt, Maryland
National Aeronautics and
Space Administration
```

#### r5 — score 0.690

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 23
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 23
- **matched_tokens:** ['along', 'atl06', 'ice', 'land', 'segment', 'track']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
274 3.2 Outline of processing
275 The outline of the process is as follows for each cycle for each along-track point. First, heights
276 and along-track slopes are calculated for each beam in each pair:
277 1. PEs from the current cycle falling into the along-track bin for the along-track point are
278 collected (3.3)
279 2. The heights and surface windows are iteratively refined (3.3.5.2)
280 3. Corrections and error estimates are calculated based on the edited PEs. ( 3.4, 3.5, 3.6 )
281 Once these steps are complete, based on the height values for the two beams,
282 4. The across-track slope is calculated (3.7)
283 Each of these steps is described in turn below.
284 3.3 PE selection
285 ATL03 provides PE locations and timings for each beam. The first step in ATL06 processing is
286 to select groups of PEs that determine the segment height at each along-track point. Processing
287 is only carried out if the ATL03 podppd_flag indicates that the PE geolocation was of high
288 quality for all pulses in the segment, otherwise the segment is skipped.
289 3.3.1 Along-track segments
290 Our height- and height-change schemes rely on dividing the data into repeatable along-track
291 segments.
```

---

