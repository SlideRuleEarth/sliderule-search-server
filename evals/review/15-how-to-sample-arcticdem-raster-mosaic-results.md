# Row 15 results: docsearch / example

> Auto-generated. Open this file alongside `15-how-to-sample-arcticdem-raster-mosaic-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to sample ArcticDEM raster mosaic`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: assets/arcticdem_mosaic.html and how_tos/arcticdem_request.html both removed; raster_sampling page is closest substitute

---

## 📚 docsearch results (top 5)

#### r1 — score 0.522

- **url:** https://docs.testsliderule.org/developer_guide/articles/gdal_vrt_benchmark.html
- **title:** 2022-11-10: VRT Performance Benchmarking
- **section:** Overview
- **category:** `developer_guide`
- **matched_tokens:** ['arcticdem', 'mosaic', 'raster']

**Full text:**

```
Test reads elevation value from ArcticDem. POI is lon: -74.60 lat: 82.86 Method used vrt file created from mosaic rasters, version 3.0, 2m, hosted on AWS. The mosaic.vrt file is stored locally on aws dev server at /data/ArcticDem/mosaic.vrt The actual raster containing the elevation for POI is: /vsis3/pgc-opendata-dems/arcticdem/mosaics/v3.0/2m/34_37/34_37_1_1_2m_v3.0_reg_dem.tif The elevation can be read from the aws file directly: gdallocationinfo -wgs84 /vsis3/pgc-opendata-dems/arcticdem/mosaics/v3.0/2m/34_37/34_37_1_1_2m_v3.0_reg_dem.tif -valonly -74.6 82.86 The elevation can be read from the mosaic.vrt on our dev server: gdallocationinfo -wgs84 /data/ArcticDem/mosaic.vrt -valonly -74.6 82.86 The test reads the same POI one million times. Gdal library should access the proper raster tile from S3 bucket and use it locally for all remaining elevation reads. In the first implementation the mosaic.vrt is opened, the vrtdataset and vrtband are used to do a direct read via: vrtband->RasterIO(GF_Read, col, row, 1, 1, &elevation, 1, 1, GDT_Float32, 0, 0, 0); col and row are calculated for the mosaic.vrt This approach works correctly but performance is very poor. It took almost 170 seconds to do one million reads. Each 100k reads takes almost 17 seconds.
```

#### r2 — score 0.533

- **url:** https://docs.testsliderule.org/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['arcticdem', 'mosaic', 'raster']

**Full text:**

```
ds that should be treated as elevation bands which allows a 3D transform to be applied key_space : 64-bit integer defining the upper 32-bits of the file_id ; this in general should never be set as the server will typically do the right thing assigning a key space; but for users that are parallelizing requests on the client-side, this parameter can be usedful when constructing the resulting file dictionaries that come back with the raster samples parms { "samples" : { "mosaic" : { "asset" : "arcticdem-mosaic" , "radius" : 10.0 , "zonal_stats" : True }, "strips" : { "asset" : "arcticdem-strips" , "algorithm" : "CubicSpline" } } } See the asset directory for details on which rasters can be sampled.
```

#### r3 — score 0.568

- **url:** https://docs.testsliderule.org/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.1: Raster Sampling
- **category:** `developer_guide`
- **matched_tokens:** ['mosaic', 'raster']

**Full text:**

```
The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land cover mapping Harmonized LandSat Sentinal-2 PGC Arctic Digital Elevation Model Mosaic PGC Arctic Digital Elevation Model Strips PGC Reference Elevation Model of Antarctica Mosaic PGC Reference Elevation Model of Antarctica Strips
```

#### r4 — score 0.435

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['arcticdem', 'mosaic', 'raster', 'sample']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib.
```

#### r5 — score 0.517

- **url:** https://docs.testsliderule.org/developer_guide/articles/gdal_vrt_benchmark.html
- **title:** 2022-11-10: VRT Performance Benchmarking
- **section:** 2022-11-10: VRT Performance Benchmarking
- **category:** `developer_guide`
- **matched_tokens:** ['arcticdem', 'mosaic']

**Full text:**

```
Note GDAL VRT performance was benchmarked using the ArcticDEM mosaic dataset.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.457

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

#### r2 — score 0.461

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

#### r3 — score 0.433

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

#### r4 — score 0.416

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

#### r5 — score 0.446

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

