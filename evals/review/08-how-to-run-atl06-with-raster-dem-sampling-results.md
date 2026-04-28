# Row 8 results: docsearch / conceptual

> Auto-generated. Open this file alongside `08-how-to-run-atl06-with-raster-dem-sampling-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to run atl06 with raster DEM sampling`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** pairing ATL06 with raster sampling (how_tos/arcticdem_request dropped after testsliderule.org rebaseline)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.461

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2. ATL06 - atl06x
- **category:** `user_guide`
- **matched_tokens:** ['atl06', 'raster', 'sampling']

**Full text:**

```
The SlideRule atl06x endpoint provides a service for ATL06 subsetting and custom processing. This endpoint queries ATL06 input granules for segment heights and locations based on geographic and temporal ranges. The resulting extents are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r2 — score 0.414

- **url:** https://docs.testsliderule.org/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['atl06', 'raster', 'run', 'sampling']

**Full text:**

```
SlideRule supports sampling raster data at points of interest and including those sampled values alongside its customized data products. For instance, when performing an ATL06-SR processing run ( atl06p ), the returned GeoDataFrame has a row for each calculated elevation; that row can also include values from different raster datasets that have been sampled at the geolocation of the calculated elevation. Note Raster data consists of 2-dimensional datasets that form a grid of square pixels, often called an image. A common format for storing raster data is TIFF. GeoTIFF is an extension to the TIFF format that embeds geospatial information into the TIFF file that ties the raster data to a geospatial reference. COGs are cloud-optimized GeoTIFFs that are internally optimized for access in the cloud. For more information see https://www.cogeo.org. In order to sample a raster dataset, SlideRule must first ascertain which individual raster files in the dataset intersect the point of interest, then obtain credentials to access the identified files, and then lastly, open up those files and read the necessary pixels to calculate the returned sample value. Unfortunately, most raster datasets are organized slightly differently and require a small amount of specialized code to perform the first step of determining which raster files need to be sampled.
```

#### r3 — score 0.422

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v03-03-00.html
- **title:** Release v3.3.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['dem', 'raster', 'sampling']

**Full text:**

```
Sampling support added for the Merit DEM Added raster module to Python client - returns GeoDataFrame of sampled raster points of interest
```

#### r4 — score 0.441

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl06', 'raster', 'run']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib.
```

#### r5 — score 0.449

- **url:** https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.1: Raster Sampling
- **category:** `developer_guide`
- **matched_tokens:** ['raster', 'sampling']

**Full text:**

```
The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land cover mapping Harmonized LandSat Sentinal-2 PGC Arctic Digital Elevation Model Mosaic PGC Arctic Digital Elevation Model Strips PGC Reference Elevation Model of Antarctica Mosaic PGC Reference Elevation Model of Antarctica Strips
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.413

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 72
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 72
- **matched_tokens:** ['atl06', 'sampling']

**Full text:**

```
The
1233 background rate is provided in ATL03 on a 50-shot sampling interval; we convert this to the per-
1234 PE rate by interpolating as a function of delta_time.
1235
1236 5.3 Processing Procedure for Parameters
1237 In this section, we give pseudocode for the calculation of ATL06 parameters. The flow chart for
1238 this process is summarized in Figure 5-1. The code is made up of several functions that call one
1239 another, following the process described in Section 5.1.
1240
60
```

#### r2 — score 0.448

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['atl06', 'dem']

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

#### r3 — score 0.316

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 117
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 117
- **matched_tokens:** ['dem', 'run']

**Full text:**

```
2354
2355 1. The input data are the signal photons identified by DRAGANN and the ATL03
2356 classification (signal_conf_ph) values of 3-4 further focused by YAPC weight
2357 analysis.
2358 2. Generate a rough surface by connecting all photons to each other. Let’s call this
2359 surface interp_A.
2360 3. Run a median filter through Asmooth_yapc_weights using the window size set by
2361 the software. Output = Asmooth.
2362 4. Define a reference DEM limit (ref_dem_limit) as 120 m (TBD).
2363 5. Remove any Asmooth values further than the ref_dem_limit threshold from the
2364 reference DEM, and interpolate the Asmooth surface based on the remaining
2365 Asmooth values. The interpolation method to use is the shape preserving
2366 piecewise cubic Hermite interpolating polynomial – hereafter labeled as “pchip”
2367 (Fritsch & Carlson, 1980).
2368 6. Compute the approximate relief of the L-km segment using the 95th - 5th
2369 percentile heights of the signal photons. We are going to filter Asmooth again
2370 and the smoothing is a function of the relief.
2371 7. Define the SmoothSize using the conditional statements below. The SmoothSize
2372 will be used to detrend the data as well as to create an interpolated ground
2373 surface later.
2374 SmoothSize = 2 * Window
2375 • If relief>=900, SmoothSize= round(SmoothSize/4)
2376 • If relief>=400 && <=900, SmoothSize=round(SmoothSize/3)
2377 • If relief>=200 && <=400, SmoothSize=round(SmoothSize/2)
2378 8.
```

#### r4 — score 0.416

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 57
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 57
- **matched_tokens:** ['dem']

**Full text:**

```
1047 2.3.5 DRAGANN_flag
1048 (parameter = d_flag). Flag indicating the labeling of DRAGANN noise filtering for
1049 a given photon. 0 = noise, 1=signal.
1050
1051 2.4 Subgroup: Reference data
1052 The reference data subgroup contains parameters and information that are
1053 useful for determining the terrain and canopy heights that are reported on the
1054 product. In addition to position and timing information, these parameters include the
1055 reference DEM height, reference landcover type, and flags indicating water or snow.
1056 Table 2.4. Summary table for reference parameters for the ATL08 product. Group Data Type Description Source
segment_id_beg Integer First along-track segment_id ATL03
number in 100-m segment
segment_id_end Integer Last along-track segment_id ATL03
number in 100-m segment
latitude Float Center latitude of signal ATL03
photons within each segment
longitude Float Center longitude of signal ATL03
photons within each segment
delta_time Float Mid-segment GPS time in ATL03
seconds past an epoch.
```

#### r5 — score 0.398

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 4 Version History
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 19
- **matched_tokens:** ['sampling']

**Full text:**

```
Uncertainty in computed terrain height estimates depends on the uncertainties in the ATL03 data
passed to the algorithm combined with any local uncertainties within each 100 m segment,
beginning with the number of photons classified as terrain photons. Potential error
sources in ATL08 height retrievals are detailed in Sections 1.5–1.8 of the ATL08 ATBD. Topics
include vertical sampling error, background noise, misidentified photons, complex topography,
dense vegetation, and dense and sparse canopies.
3 SOFTWARE AND TOOLS
PhoREAL is a free library of geospatial analysis tools and source code written specifically for
working with ATL03 and ATL08 data.
4 VERSION HISTORY
A summary of the version history is provided in Table 5. Page 18 of 19National Snow and Ice Data Center
nsidc.org
```

---

