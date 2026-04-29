# Row 55 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `55-generate-a-dem-from-icesat-2-data-over-my-area-of-interest-review.md` —
> verdicts go there, this side is read-only.

**Query:** `generate a DEM from ICESat-2 data over my area of interest`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/assets/grandmesa.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl06`
  - `atl06-sr`
  - `2. atl06`
- **expected_pages:** (none)
- **notes:** asking for ATL06 elevations without using ATL06 terminology

---

## 📚 docsearch results (top 5)

#### r1 — score 0.540

- **url:** https://docs.slideruleearth.io/developer_guide/why_sliderule.html
- **title:** Why SlideRule
- **section:** Why Develop SlideRule?
- **category:** `developer_guide`
- **matched_tokens:** ['data', 'from', 'icesat', 'over']

**Full text:**

```
The tremendous growth in the size of Earth science datasets being produced by institutions over the past ten to fifteen years has broken the historical data archive model. When datasets changed from being a few hundred Gigabytes to hundreds of Terabytes (and now Petabytes), comprehensive analysis of those datasets using existing technology became impossible. For example, ICESat (the original mission), launched in 2003 and in its lifetime produced 148GB of global elevation data. That data could be downloaded at 6MBps in just under 1 day, and stored on a single hard drive on a single workstation. ICESat-2 (the follow-on mission), launched in 2018 and has produced 320TB of data as of 2021, with 100TB of data being added each year. In order to download the existing dataset at 100MBps, it would take 296 days, and require 40 workstations with 8TBs of storage each to hold. Performing comprehensive analysis on current Earth science datasets requires sophisticated compute and storage infrastructure, and high bandwidth connectivity to the data sources; both of which are insurmountable barriers of entry to all but the most funded institutions. The interim solution to this problem currently offered by most missions is the pre-generation and distribution of higher level data products which target specific science applications. By targeting a narrow application these data products are smaller and therefore easier to download and work with.
```

#### r2 — score 0.555

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/first_request.html
- **title:** Making Your First Request
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['data', 'icesat', 'over']

**Full text:**

```
This tutorial walks you through the steps necessary to make your first request to SlideRule. By the end of this tutorial you will have used SlideRule to calculate and plot elevations over Grand Mesa, Colorado, using ICESat-2 photon cloud data. Prerequisites : This walk-through assumes you are comfortable using git and the conda Python packaging system. See the installation instructions in the reference documentation for details on other methods of installation.
```

#### r3 — score 0.489

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/arcticdem_request.html
- **title:** Including ArcticDEM Samples
- **section:** Sampling the ArcticDEM mosaic in an atl06p request
- **category:** `user_guide`
- **matched_tokens:** ['data', 'from', 'icesat', 'interest']

**Full text:**

```
The âsamplesâ parameter is used to request ArcticDEM samples be included in atl06p responses. For the ArcticDEM, there are two possible values that can be provided: âarcticdem-mosaicâ and âarcticdem-stripsâ . Step 1 : Import and initialize the SlideRule Python package for ICESat-2. >>> from sliderule import sliderule , icesat2 >>> icesat2 . init ( "slideruleearth.io" ) Step 2 : Create parameters for a typical atl06p processing request. >>> grand_mesa = sliderule . toregion ( 'dicksonfjord.geojson' ) >>> parms = { "poly": grand_mesa["poly"], "srt": icesat2.SRT_LAND, "cnf": icesat2.CNF_SURFACE_HIGH, "len": 40.0, "res": 20.0 } The dicksonfjord.geojson file used in this example can be downloaded by navigating to our downloads page; alternatively, you can create your own GeoJSON file at geojson.io . Be sure that your region of interest is in the arctic, otherwise there will be no data in the ArcticDEM for it.
```

#### r4 — score 0.402

- **url:** https://docs.slideruleearth.io/assets/phoreal.html
- **title:** Running the PhoREAL algorithm over Grand Mesa, CO
- **section:** Processing parameters
- **category:** `tutorial`
- **matched_tokens:** ['area', 'generate', 'interest', 'over']

**Full text:**

```
[3]: parms = { "poly" : sliderule . toregion ( 'grandmesa.geojson' )[ 'poly' ], # subset to Grand Mesa area of interest "t0" : '2019-11-14T00:00:00Z' , # time range is one day - November 14, 2019 "t1" : '2019-11-15T00:00:00Z' , "srt" : icesat2 . SRT_LAND , # use the land surface type for ATL03 photon confidence levels "len" : 100 , # generate statistics over a 100m segment "res" : 100 , # generate statistics every 100m "pass_invalid" : True , # do not perform any segment-level filtering "atl08_class" : [ "atl08_ground" , "atl08_canopy" , "atl08_top_of_canopy" ], # exclude noise and unclassified photons "atl08_fields" : [ "h_dif_ref" ], # include these fields as extra columns in the dataframe "phoreal" : { "binsize" : 1.0 , "geoloc" : "center" } # run the PhoREAL algorithm }
```

#### r5 — score 0.453

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['data', 'from', 'interest', 'over']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib. ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.560

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.2 Land Ice
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 50
- **matched_tokens:** ['data', 'from', 'generate', 'icesat', 'interest']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
4.0 SURFACE MASKS
4.1 Introduction
The goal of providing a set of gridded surface masks (for land ice, sea ice, land, ocean, and
inland water) is to reduce the volume of data processed to generate surface-specific higher-level
ICESat-2 data products. For example, the land ice surface mask directs the ATL06 land ice
algorithm to consider data from only those areas of interest to the land ice community. In order to protect against errors of omission in these masks, a buffer has been added to the best
estimate of the geographic bounds of the regions of interest. Consequently, the grids do not
perfectly tessellate the surface of the Earth but have overlap on the order of tens of kilometers in
most regions. This means that a given latitude and longitude point could appear in two or more
surface masks, and two or more higher-level data products. Differences among the algorithms
used by higher-level data products for a multiply-classified granule of ATL03 are expected. For
example, many permafrost areas are included in the land, land ice, and inland water masks and
will be included in the associated ATL08, ATL06, and ATL13 data products, although they will
all take as input the same ATL03 granule. The masks are provided to the SIPS as text files of latitude, longitude, and a flag (=1 if the grid
node contains the surface of interest), and are stored and accessed by SIPS as ANC12-01.
```

#### r2 — score 0.562

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.4.1.2 MOD44W
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 54
- **matched_tokens:** ['area', 'data', 'dem', 'from', 'icesat']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Figure 4-2. Final Buffered Sea Ice Mask.
4.4 Land and Ocean
The ATL03 land and ocean masks are 0.05°x0.05° logical masks that will be used to isolate
records to be processed using the land and ocean algorithms, respectively. The source material
for both of the masks is the same. These masks are fully described in the Land and Ocean
Surface Masks for ATL03 supporting document.
4.4.1 Data Sources
4.4.1.1 IBCAO
The International Bathymetry Chart of the Arctic Ocean
(http://www.ngdc.noaa.gov/mgg/bathymetry/arctic/) is a 500-m resolution DEM covering the
Arctic area north of latitude 60°N. Version 3.0 of this DEM was released 2012 Jun 8 (Jakobsson
et al., 2012). Jamie Morison converted this to a 0.05°x0.05° DEM (pers. comm.) for use in this
global mask.
4.4.1.2 MOD44W
The MODIS 250-m resolution water mask (Carroll et al., 2009) was downloaded from the land
process data center (https://lpdaac.usgs.gov/products/mod44wv006/) on 2013 Dec 24. This
38 Release Date: Fall 2022
```

#### r3 — score 0.679

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 66
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 66
- **matched_tokens:** ['data', 'dem', 'from', 'icesat']

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

#### r4 — score 0.543

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 4.2.1.5 Permafrost
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 51
- **matched_tokens:** ['data', 'dem', 'from', 'generate', 'icesat']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
4.2.1 Data Sources
4.2.1.1 Antarctica
Helen Fricker and Geir Moholdt supplied a set of polygons defining the Antarctic continent and
surrounding islands, including ice shelves. A 40-km buffer was added to the Antarctic dataset to
account for future movement of the ice front.
4.2.1.2 Greenland
The Greenland Ice Mapping Project used Landsat 7 and RADARSAT-1 data to generate a DEM,
an ice-cover map, and an ocean mask (Howat et al., 2015). The GIMP ocean mask is available at
resolutions of 15 m, 30 m, and 90 m. The 15-m mask was too large to work with, so the 30-m
resolution GIMP ocean mask was used. The non-ocean portion of this mask defined the
Greenland land mass. This procedure was used rather than working from the GIMP Greenland
ice mask so that the entire land surface would be included in the land ice mask. The land mask
for Greenland was further augmented as needed with the non-water tiles of the MOD44W global
water mask.
4.2.1.3 GLIMS
The Global Land Ice Measurements from Space (GLIMS) database consists of a single shapefile
with roughly 119,000 polygons. It was downloaded from http://glims.org on 2016 Oct 4. The
data release date is 2015 Jul 28.
4.2.1.4 RGI
Version 5.0 of the RGI (Pfeffer et al., 2014) consists of a set of shapefiles with multiple polygons
in each. They were downloaded from https://www.glims.org/RGI/rgi50_dl.html
on 2016 Sep 30.
```

#### r5 — score 0.549

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 8
- **matched_tokens:** ['data', 'dem', 'from', 'icesat', 'over']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Revision Date
Description of Change
Level Approved
4.0 Added roll, pitch, and yaw from ANC04 POD file and 12/1/2020
interpolated to the geolocation segment rate. Replaced GMTED2010 with the 3-arc-second MERIT DEM 12/1/2020
as the global DEM. The 3 arcsecond spatial resolution of
the MERIT DEM is a marked improvement over the 7.5
arcsecond resolution of GMTED2010 and provides better
terrain heights that compare more favorably to on-orbit data,
particularly over forested regions and river basins. The
MERIT DEM has improved absolute bias, striping and
speckling noise compared to GMTED, and also an
improved tree height bias. Changed geoid from the EGM2008 mean-tide system to the 12/1/2020
EGM2008 tide-free system. The prior EGM2008 geoid was
provided in the mean-tide system that includes geoid
deformation induced by the permanent tide. However, the
ATL03 time-variant solid earth tides are computed in a tide-
free system where the permanent tide is excluded. Changing the geoid on ATL03 from the EGM2008 mean-
tide system to the tide-free system allows users to more
easily re-reference photons heights above the geoid without
additional corrections, bringing consistency to the tidal
systems on ATL03. Added conversion factors for geoid and solid earth tide that 12/1/2020
allow easy conversion to/from tide-free/mean-tide systems.
```

---

