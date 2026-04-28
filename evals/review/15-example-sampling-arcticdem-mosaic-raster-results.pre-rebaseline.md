# Row 15 results: docsearch / example

> Auto-generated. Open this file alongside `15-example-sampling-arcticdem-mosaic-raster-review.md` —
> verdicts go there, this side is read-only.

**Query:** `example sampling ArcticDEM mosaic raster`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/arcticdem_mosaic.html
  - https://docs.slideruleearth.io/user_guide/how_tos/arcticdem_request.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** arcticdem mosaic tutorial

---

## 📚 docsearch results (top 5)

#### r1 — score 0.568

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/arcticdem_request.html
- **title:** Including ArcticDEM Samples
- **section:** Sampling the ArcticDEM mosaic in an atl06p request
- **category:** `user_guide`
- **matched_tokens:** ['arcticdem', 'mosaic', 'sampling']

**Full text:**

```
Step 3 : Specify sampling the ArcticDEM mosaic. >>> parms [ "samples" ] = { "mosaic" : { "asset" : "arcticdem-mosaic" , "radius" : 10.0 , "zonal_stats" : True }} Step 4 : Issue the processing request to SlideRule, for only a single granule (to keep the data volume down). >>> resource = "ATL03_20190314093716_11600203_007_01.h5" >>> gdf = icesat2 . atl06p ( parms , resources = [ resource ]) When this completes (~10 seconds), the gdf variable should now contain all of the results of the elevations calculated by SlideRule with a corresponding column for the âarcticdem-mosaicâ. Note that the granule provided must be in the region of interest. Step 5 : Display a summary of the results. >>> print ( gdf ) segment_id rgt n_fit_photons spot h_sigma gt delta_time cycle rms_misfit dh_fit_dy ... geometry mosaic.time mosaic.max mosaic.mad mosaic.mean mosaic.median mosaic.value mosaic.count mosaic.stdev mosaic.min time 2019-03-14 09:40:46.282934432 405226 1160 12 1 0.551360 10 3.779165e+07 2 0.874532 0.0 ... POINT (-26.27920 72.77984) 1.176077e+09 558.497131 2.760759 550.909552 550.701904 550.909729 81 3.328835 544.854675 2019-03-14 09:40:46.284351344 405227 1160 32 1 0.246645 10 3.779165e+07 2 1.308783 0.0 ... POINT (-26.27924 72.77993) 1.176077e+09 568.031189 4.222864 559.327384 559.479126 559.673889 81 4.824281 551.360779 2019-03-14 09:40:46.285767320 405227 1160 20 1 1.144088 10 3.779165e+07 2 1.318949 0.0 ...
```

#### r2 — score 0.604

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.1: Raster Sampling
- **category:** `developer_guide`
- **matched_tokens:** ['mosaic', 'raster', 'sampling']

**Full text:**

```
The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land cover mapping Harmonized LandSat Sentinal-2 PGC Arctic Digital Elevation Model Mosaic PGC Arctic Digital Elevation Model Strips PGC Reference Elevation Model of Antarctica Mosaic PGC Reference Elevation Model of Antarctica Strips
```

#### r3 — score 0.604

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.1: Raster Sampling
- **category:** `developer_guide`
- **matched_tokens:** ['mosaic', 'raster', 'sampling']

**Full text:**

```
The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land cover mapping Harmonized LandSat Sentinal-2 PGC Arctic Digital Elevation Model Mosaic PGC Arctic Digital Elevation Model Strips PGC Reference Elevation Model of Antarctica Mosaic PGC Reference Elevation Model of Antarctica Strips
```

#### r4 — score 0.453

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **title:** Release v2.1.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['arcticdem', 'mosaic', 'raster', 'sampling']

**Full text:**

```
GeoParquet output option fully supported, including user specified S3 bucket as a destination; #72 #171 Full raster sampling support for ArcticDEM Mosaic and Strips, and REMA; this includes Python client side updates needed to efficiently represent the returned sample data in the GeoDataFrames; #165 Raster sampling now supports time range filters t0 and t1 , clostest time filters closest_time , and substring filters substr Raster sampling now supports including additional flags with each sample via the with_flags option Streamlined private cluster setup in the Python client; added sliderule.scaleout and updated behavior of sliderule.init function to transparently handle starting and scaling a cluster if desired; #126 Python client supports TIME8 fields from SlideRule PhoREAL/atl08 endpoint added as a feature-preview GEDI L4A subsetting endpoint added as a feature-preview
```

#### r5 — score 0.525

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['arcticdem', 'mosaic', 'raster']

**Full text:**

```
ds that should be treated as elevation bands which allows a 3D transform to be applied key_space : 64-bit integer defining the upper 32-bits of the file_id ; this in general should never be set as the server will typically do the right thing assigning a key space; but for users that are parallelizing requests on the client-side, this parameter can be usedful when constructing the resulting file dictionaries that come back with the raster samples parms { "samples" : { "mosaic" : { "asset" : "arcticdem-mosaic" , "radius" : 10.0 , "zonal_stats" : True }, "strips" : { "asset" : "arcticdem-strips" , "algorithm" : "CubicSpline" } } } See the asset directory for details on which rasters can be sampled.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.467

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.3.2 Mask Generation
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 53
- **matched_tokens:** ['mosaic']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
4.3.1 Data Sources
4.3.1.1 SSMI/SMMR Monthly Sea Ice Maps
The ATL03 sea ice mask was generated primarily from the 25-km resolution SSMI/SMMR
monthly sea ice concentration maps available from NSIDC. These maps cover the period 1978
Oct through 2012 Dec, with change dates of 2013 Feb 6 and 2013 Jun 14. The mask includes
some areas of inland water known to freeze seasonally such as Lake Superior and Lake Baikal.
4.3.1.2 Antarctica
The Antarctic sea ice mask uses the 2004 MODIS Mosaic of Antarctica (MOA)
(https://nsidc.org/data/nsidc-0280) coastline to determine the southern extent of Antarctic sea ice.
4.3.1.3 Greenland
The Greenland sea ice mask uses the MODIS Mosaic of Greenland (MOG)
(http://nsidc.org/data/nsidc-0547) to define the landward edge of sea ice around Greenland.
4.3.2 Mask Generation
Step 1: The monthly maps were first combined into one maximum sea ice concentration map for
the Arctic and one for the Antarctic. Step 2: Each 25-km resolution cell in the composite grids with a sea ice concentration ≥10% was
subdivided into a grid of 51x51 evenly spaced (in projected space) test points, with the outer
columns and rows lying along the edges of the cells. The polar-stereographic coordinates were
converted to latitude and longitude, and these lat/lon were then converted to indices into a global
0.05°x0.05° grid, and the associated tiles were flagged.
```

#### r2 — score 0.442

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['arcticdem']

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

#### r3 — score 0.471

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 104
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 104
- **matched_tokens:** ['mosaic']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
2080 References
2081 Bamber, J.L., J.L. Gomez-Dans and J.A. Griggs 2009. A new 1 km digital elevation model of the
2082 Antarctic derived from combined satellite radar and laser data - Part 1: Data and methods.
2083 Cryosphere, 3(1): 101-111.
2084 Menke, W. 1989. Geophysical data analysis: discrete inverse theory. San Diego, CA, Academic
2085 Press.
2086 Scambos, T.A., T.M. Haran, M.A. Fahnestock, T.H. Painter and J. Bohlander 2007. MODIS-
2087 based Mosaic of Antarctica (MOA) data sets: Continent-wide surface morphology and snow
2088 grain size. Remote Sensing of Environment, 111(2-3): 242-257.
2089 Warren, S.G., R.E. Brandt and T.C. Grenfell 2006. Visible and near-ultraviolet absorption
2090 spectrum of ice from transmission of solar radiation into snow. Applied Optics, 45(21): 5320-
2091 5334.
2092 Yang, Y., A. Marshak, S.P. Palm, T. Varnai and W.J. Wiscombe 2011. Cloud Impact on Surface
2093 Altimetry From a Spaceborne 532-nm Micropulse Photon-Counting Lidar: System Modeling for
2094 Cloudy and Clear Atmospheres. Ieee Transactions on Geoscience and Remote Sensing, 49(12):
2095 4910-4919.
2096 Yang, Y., A. Marshak, S.P. Palm, Z. Wang and C. Schaaf 2013. Assessment of Cloud Screening
2097 With Apparent Surface Reflectance in Support of the ICESat-2 Mission. Ieee Transactions on
2098 Geoscience and Remote Sensing, 51(2): 1037-1045.
2099 Yi, D.H. and C.R. Bentley 1999.
```

#### r4 — score 0.428

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.3.2 Mask Generation
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 53
- **matched_tokens:** ['mosaic']

**Full text:**

```
Step 3: A 10-km buffer was added to this mask by marking any tile as sea ice that lies within 10
kilometers of a sea ice tile. Step 4: The buffered map, and the area along the 2004 MODIS Mosaic of Antarctica (MOA)
coastline show a number of anomalies. These were adjusted in a two-step process.
• Step 1: Areas that were incorrectly flagged as sea ice were unflagged. Each tile
containing an Antarctic coastline point was flagged as sea ice, as were all tiles within 10
kilometers of each point.
• Step 2: Some areas that should have been flagged were further than 10 kilometers from
the coastline. The region along the Antarctic coastline was examined in detail and the
coordinates of these areas were noted. Then all of them were flagged. The final sea ice mask is shown in Figure 4-2.
37 Release Date: Fall 2022
```

#### r5 — score 0.435

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **title:** ATLAS/ICESat-2 L3A Land Ice Height
- **section:** 5.2 Date Last Updated
- **category:** `user_guide`
- **source_product:** `ATL06` · **page:** 17
- **matched_tokens:** ['mosaic']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land Ice Height, Version 6
Scambos, T. A., Haran, T. M., Fahnestock, M. A., Painter, T. H., & Bohlander, J. (2007). MODIS-
based Mosaic of Antarctica (MOA) data sets: Continent-wide surface morphology and snow grain
size. Remote Sensing of Environment, 111(2–3), 242–257.
https://doi.org/10.1016/j.rse.2006.12.020
Warren, S. G., Brandt, R. E., & Grenfell, T. C. (2006). Visible and near-ultraviolet absorption
spectrum of ice from transmission of solar radiation into snow. Applied Optics, 45(21), 5320–5334.
https://doi.org/10.1364/AO.45.005320
Yang, Y., Marshak, A., Palm, S. P., Varnai, T., & Wiscombe, W. J. (2011). Cloud Impact on Surface
Altimetry From a Spaceborne 532-nm Micropulse Photon-Counting Lidar: System Modeling for
Cloudy and Clear Atmospheres. IEEE Transactions on Geoscience and Remote Sensing, 49(12),
4910–4919. https://doi.org/10.1109/TGRS.2011.2153860
Yang, Y., Marshak, A., Palm, S. P., Wang, Z., & Schaaf, C. (2013). Assessment of Cloud
Screening With Apparent Surface Reflectance in Support of the ICESat-2 Mission. IEEE
Transactions on Geoscience and Remote Sensing, 51(2), 1037–1045.
https://doi.org/10.1109/TGRS.2012.2204066
Yi, D. H., & Bentley, C. R. (1999). Geoscience Laser Altimeter System waveform simulation and its
applications.
```

---

