# Row 79 results: docsearch / example

> Auto-generated. Open this file alongside `79-sample-a-raster-dem-alongside-icesat-2-elevations-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sample a raster DEM alongside ICESat-2 elevations`
**Panel signature:** `670842a899fa`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** raster sampling workflow

---

## 📚 docsearch results (top 5)

#### r1 — score 0.540

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.3 L3 Raster
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'raster', 'sample']

**Full text:**

```
The following raster datasets are available to sample: "gedil3-elevation" : GEDI03_elev_lowestmode_mean_2019108_2022019_002_03.tif "gedil3-canopy" : GEDI03_rh100_mean_2019108_2022019_002_03.tif "gedil3-elevation-stddev" : GEDI03_elev_lowestmode_stddev_2019108_2022019_002_03.tif "gedil3-canopy-stddev" : GEDI03_rh100_stddev_2019108_2022019_002_03.tif "gedil3-counts" : GEDI03_counts_2019108_2022019_002_03.tif For example, if you wanted to sample the GEDI L3 Canopy raster and calculate zonal statistics for every ICESat-2 PhoREAL data point, then you could add the following entry to your parameters for your PhoREAL request: parms [ "samples" ]: { "canopy" : { "asset" : "gedil3-canopy" , "radius" : 10.0 , "zonal_stats" : True }}
```

#### r2 — score 0.492

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.3 L4B Raster
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'raster', 'sample']

**Full text:**

```
The following raster datasets are available to sample: "gedil4b" : GEDI04_B_MW019MW138_02_002_05_R01000M_V2.tif For example, if you wanted to sample the GEDI L4B biodensity raster and calculate zonal statistics for every ICESat-2 PhoREAL data point, then you could add the following entry to your parameters for your PhoREAL request: parms [ "samples" ]: { "agdb" : { "asset" : "gedil4b" , "radius" : 10.0 , "zonal_stats" : True }}
```

#### r3 — score 0.491

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-03-00.html
- **title:** Release v3.3.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['dem', 'raster']

**Full text:**

```
Sampling support added for the Merit DEM Added raster module to Python client - returns GeoDataFrame of sampled raster points of interest
```

#### r4 — score 0.433

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['elevations', 'raster', 'sample']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib.
```

#### r5 — score 0.415

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['alongside', 'raster', 'sample']

**Full text:**

```
SlideRule supports sampling raster data at points of interest and including those sampled values alongside its customized data products. For instance, when performing an ATL06-SR processing run ( atl06p ), the returned GeoDataFrame has a row for each calculated elevation; that row can also include values from different raster datasets that have been sampled at the geolocation of the calculated elevation. Note Raster data consists of 2-dimensional datasets that form a grid of square pixels, often called an image. A common format for storing raster data is TIFF. GeoTIFF is an extension to the TIFF format that embeds geospatial information into the TIFF file that ties the raster data to a geospatial reference. COGs are cloud-optimized GeoTIFFs that are internally optimized for access in the cloud. For more information see https://www.cogeo.org. In order to sample a raster dataset, SlideRule must first ascertain which individual raster files in the dataset intersect the point of interest, then obtain credentials to access the identified files, and then lastly, open up those files and read the necessary pixels to calculate the returned sample value. Unfortunately, most raster datasets are organized slightly differently and require a small amount of specialized code to perform the first step of determining which raster files need to be sampled.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.660

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['dem', 'elevations', 'icesat']

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

#### r2 — score 0.535

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 32
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 32
- **matched_tokens:** ['elevations', 'icesat']

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

#### r3 — score 0.620

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['dem', 'icesat']

**Full text:**

```
The DEM should be filtered to 40-m
1150 resolution before interpolation to the ICESat-2 reference points.
1151 • For areas outside the poles, a multi-sensor global DEM, posted at 7.5 arcsec
1152 (http://topotools.cr.usgs.gov/gmted_viewer).
1153 This group is sparse, meaning that parameters are provided only for pairs of segments for which
1154 at least one beam has a valid surface-height measurement. Table 4-8 DEM subgroup
Parameter Description
dem_h Height of the DEM, interpolated by cubic-
spline interpolation in the DEM coordinate
system to the PE location
dem_flag source for the DEM.1=Antarctic DEM,
2=Arctic DEM, 3=global DEM.
geoid_h Geoid height, meters
1155
54
```

#### r4 — score 0.545

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.8 Quality and classification flags throughout flow of analysis
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 80
- **matched_tokens:** ['dem', 'icesat']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Segment_fpb_correction = 0.00015 * ffb_corr [m] 4.24e
Note: The user should subtract the_fpb_correction from the mean height products such as
ht_ortho (EGM2008) and ht_water_surf (WGS84). The above correction is not applied when all
detectors are saturated. A future ATL03 correction for such severely biased returns is will be
applied to future ATL13 Releases.
4.7.3.7 Inclusion of best publicly available DEM. As indicated in the ATL13 output table, also included is the best publicly available Digital
Elevation Model) DEM (based on resolution and quality) at the ATL13 short segment rate
together with the source of the DEM. DEM location is assigned to the short segment index
photon. DEM selection sources include all available from ATL03. The currently available
selection source and hierarchy among those are:
1) ArcticDEM
2) DTU13 Mean Sea Surface (MSS).
3) Reference Elevation Model of Antarctica (REMA)
4) Multi-Error-Removed Improved-Terrain (MERIT) DEM. Inclusion of additional future ATL03 DEM products may alter the above hierarchy.
4.7.4 Dynamic Atmospheric Correction and Ocean Tides
Three fields associated with dynamic atmospheric correction and ocean tides were added to the
output table.
```

#### r5 — score 0.521

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 9
- **matched_tokens:** ['dem', 'icesat']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 007
ATL13 Release 003 (Cont’d)
- Added downscaled ATL09 input wind vector
components at 10m height (met_u10m, met_v10m).
-Included bottom in determining the minimum height to
calculate subsurface deconvolution.
-Updated threshold counts of photons within short
segment histogram multimode.
4.0 ATL13 Release 004 April 1,
2021
-Fixed adjustment in mean height after deconvolution due
to an earlier coding error Eqn 4.23a1.
- Added first photon bias (FBC) correction to the estimate
of true height as described in Eqns 4.23a-c, Section
4.7.3.6.
- Added best publicly available DEM to ATL13 output.
- Added quality flags for Clouds, Snow and Ice and
Temperature.
- Added H adj flag associated with impact of
deconvolution surface height
-Corrected the algorithm to keep the designated number
of photons per short segment, and then start the next short
segment with the next photon which could be from the
same shot as last short segment’s photon.
- Input parameters needed to drive algorithms added to
Chapter 5 (Table 15).
- Output parameters table for ATL13 products updated
(Tables 5.2 and 5.3).
ix
Release 007, January 31, 2025
```

---

