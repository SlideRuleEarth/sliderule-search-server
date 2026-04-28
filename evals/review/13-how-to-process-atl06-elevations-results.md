# Row 13 results: docsearch / example

> Auto-generated. Open this file alongside `13-how-to-process-atl06-elevations-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to process atl06 elevations`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl06x`
  - `2. atl06`
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: assets/grandmesa.html removed; user_guide section on atl06 is closest substitute

---

## 📚 docsearch results (top 5)

#### r1 — score 0.569

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06
- **category:** `api_reference`
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
sliderule.icesat2. atl06 ( parm , resource ) [source] Performs ATL06-SR processing on ATL03 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated elevations (see Elevations ) Return type : GeoDataFrame
```

#### r2 — score 0.565

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl08
- **category:** `api_reference`
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame
```

#### r3 — score 0.475

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06sp
- **category:** `api_reference`
- **matched_tokens:** ['atl06', 'elevations', 'process']

**Full text:**

```
Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges as_numpy_array ( bool ) â whether to provide all sampled values as numpy arrays even if there is only a single value height_key ( str ) â identifies the name of the column provided for the 3D CRS transformation Returns : ATL06 elevations Return type : GeoDataFrame
```

#### r4 — score 0.517

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06s
- **category:** `api_reference`
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
sliderule.icesat2. atl06s ( parm , resource ) [source] Subsets ATL06 data given the polygon and time range provided and returns elevations Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) resource ( str ) â ATL06 HDF5 filename Returns : ATL06 elevations Return type : GeoDataFrame
```

#### r5 — score 0.521

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.486

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 23
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 23
- **matched_tokens:** ['atl06', 'process']

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

#### r2 — score 0.454

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.1 ATL03 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['atl06', 'process']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
2.0 ATL03 OVERVIEW AND DATA STRUCTURE
2.1 ATL03 Overview
The simplest way to describe the ATL03 data product is that it provides time, latitude, longitude,
and height for each photon that ICESat-2 downlinks. The ATL03 product is the bridge between
the lower level, instrumentation-specific products (ATL01/02) and the higher-level, surface-
specific, science-centric products (ATL06 and above). By design, ATL03 provides a single
source for all photon information needed by higher-level products (the corresponding
atmospheric science Level-2 product ATL09 also feeds all the higher-level products; Figure 1-2). Each of the surface-specific, higher-level data products, such as land ice height or sea ice
freeboard, will use the geolocated signal photon events and ancillary data provided in the ATL03
product. Consequently, ATL03 provides five surface masks (land ice, sea ice, ocean, land, and
inland water) to reduce the volume of data that each surface-specific along-track data product is
required to process. In addition, ATL03 classifies each photon event as either a likely signal photon event or a
background photon event and provides a confidence assessment on these classifications. This
classification is made by generating histograms of the number of photon events as a function of
height and calculating the signal-to-noise ratio of each histogram bin.
```

#### r3 — score 0.417

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 32
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 32
- **matched_tokens:** ['atl06', 'elevations', 'process']

**Full text:**

```
The
427 subset of segments with ATL06_quality_summary = 0 are unlikely to contain blunders due to
428 signal-finding errors. This choice of parameters may reject useful elevations collected over
429 rough, strongly sloping, or low-reflectivity surfaces and under clouds so obtain more height
430 estimates, users may need to examine additional parameters in ATL06, or regenerate a similar
431 flag for themselves based on a less-stringent set of parameters.
432 A variety of data flags are available to indicate why a particular segment does not have a
433 reported height parameter. In many cases, the strong-beam segment in a pair will have a
434 reported height, and the weak beam will not; in these cases, a full record is available for the
435 weak-beam segment, providing all parameters up to the step where the fitting process failed. In
436 cases where neither the strong nor the weak beam returned a surface height, the segment_quality
437 group provides the signal_selection_source parameter, which will show a value of 3 if all signal-
438 selection strategies failed.
```

#### r4 — score 0.424

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
snr unitless Signal-to-noise ratio in the final refined
window
snr_significance unitless Probability that signal-finding routine
would converge to at least the observed
SNR for a random-noise input. Small
values indicate a small likelihood of a
surface-detection blunder.
1138
1139 4.3.5 DEM subgroup
1140 This subgroup (Table 4-8) contains DEM elevations interpolated at the segment centers. It
1141 contains only three parameters: the DEM elevation (dem_h), the geoid height (geoid_h), and the
1142 DEM source (dem_flag). The best DEMs available in time for the ICESat-2 launch may be
1143 significantly better than those available at present (February 2015), but the best current choices
1144 are:
1145 • For Antarctica, the REMA DEM : https://www.pgc.umn.edu/data/rema/, filtered to 40-m
1146 resolution before interpolation to the ICESat-2 segment centers, with gaps filled with
1147 ATL06 data from cycles 1 and 2.
1148 • For the Arctic, the Arctic DEM, based on stereophotogrammetry
1149 https://www.pgc.umn.edu/data/arcticdem.
```

#### r5 — score 0.424

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 32
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 32
- **matched_tokens:** ['atl06', 'elevations']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
412 3.3.4 Handling of invalid segments
413 Segments must pass a series of tests before their elevations are reported in the ATL06
414 gtxx/land_ice_segments groups. The signal selection routines must return at least 10 PE, spread
415 over at least 20 m. Fitting does not proceed if these criteria are not met. For segments that
416 continue to the surface window refinement routine, after the surface window refinement is
417 complete, the final PE count and surface-window height are checked against the snr_significance
418 parameter, to ensure that the probability of the measured signal-to-noise ration resulting from a
419 random signal selection is small. Only segments with snr_significance <0.05 (indicating that,
420 given a random-noise input, the algorithm would converge to the calculated SNR less than 5% of
421 the time) proceed to the next stage.
422 These criteria allow a significant number of low-quality segment heights to be reported in
423 ATL06. This intended for the benefit of users who need to measure surface heights under
424 marginal conditions. To help other users remove these segments, the
425 land_ice_segments/ATL06_quality_summary parameter gives a synopsis of the parameters
426 relevant to segment quality (Table 4-3), any one of which could indicate unusable data.
```

---

