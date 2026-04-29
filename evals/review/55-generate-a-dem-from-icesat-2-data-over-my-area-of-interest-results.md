# Row 55 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `55-generate-a-dem-from-icesat-2-data-over-my-area-of-interest-review.md` —
> verdicts go there, this side is read-only.

**Query:** `generate a DEM from ICESat-2 data over my area of interest`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl06`
  - `atl06-sr`
  - `2. atl06`
- **expected_pages:** (none)
- **notes:** asking for ATL06 elevations without using ATL06 terminology (assets/grandmesa.html dropped after testsliderule.org rebaseline)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.540

- **url:** https://docs.testsliderule.org/developer_guide/why_sliderule.html
- **title:** Why SlideRule
- **section:** Why Develop SlideRule?
- **category:** `developer_guide`
- **matched_tokens:** ['data', 'from', 'icesat', 'over']

**Full text:**

```
The tremendous growth in the size of Earth science datasets being produced by institutions over the past ten to fifteen years has broken the historical data archive model. When datasets changed from being a few hundred Gigabytes to hundreds of Terabytes (and now Petabytes), comprehensive analysis of those datasets using existing technology became impossible. For example, ICESat (the original mission), launched in 2003 and in its lifetime produced 148GB of global elevation data. That data could be downloaded at 6MBps in just under 1 day, and stored on a single hard drive on a single workstation. ICESat-2 (the follow-on mission), launched in 2018 and has produced 320TB of data as of 2021, with 100TB of data being added each year. In order to download the existing dataset at 100MBps, it would take 296 days, and require 40 workstations with 8TBs of storage each to hold. Performing comprehensive analysis on current Earth science datasets requires sophisticated compute and storage infrastructure, and high bandwidth connectivity to the data sources; both of which are insurmountable barriers of entry to all but the most funded institutions. The interim solution to this problem currently offered by most missions is the pre-generation and distribution of higher level data products which target specific science applications. By targeting a narrow application these data products are smaller and therefore easier to download and work with.
```

#### r2 — score 0.465

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['data', 'from', 'interest', 'over']

**Full text:**

```
The following Jupyter notebooks provide examples of how to use some of SlideRuleâs functionality. They are listed roughly in the order of complexity, with the simpler examples first and the more complex examples farther down. The source code for all of these notebooks as well as additional notebooks can be found in our repository . Additional files are necessary to run some of the notebooks locally. grandmesa.geojson dicksonfjord.geojson Notebooks Boulder Watershed ( download ) A simple notebook to demonstrate a basic atl03x processing request. Elevation data is generated for the Boulder watershed region and plotted using matplotlib. Grand Mesa ( download ) Demonstrates how to request custom ATL06 elevations from SlideRule for a region of interest, and then use SlideRule APIs to read and compare the results to the ATL06 standard data product. PhoREAL ( download ) Demonstrate use of the PhoREAL algorithm running inside SlideRule. Vegetation metrics are calculated over the Grand Mesa region and then later combined with calculated elevations. ArcticDEM Mosaic ( download ) Demonstrates how to sample the ArcticDEM Mosaic raster at generated ATL06-SR points and return all of the data as a unified GeoDataFrame. ATL03 Classification ( download ) An in-depth example of requesting ATL03 photon data classified using ATL08 and YAPC. The results are plotted using matplotlib.
```

#### r3 — score 0.512

- **url:** https://docs.testsliderule.org/developer_guide/articles/h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** SlideRule Project Background
- **category:** `developer_guide`
- **matched_tokens:** ['data', 'icesat', 'interest']

**Full text:**

```
The NASA/ICESat-2 program is investing in a collaboration between Goddard Space Flight Center and the University of Washington to develop a cloud-based on-demand science data processing system called SlideRule to lower the barrier of entry to using the ICESat-2 data for scientific discovery and integration into other data services. SlideRule is a server-side framework implemented in C++/Lua that provides REST APIs for processing science data and returning results. This enables researchers and other data systems to have low-latency access to generated data products using processing parameters supplied at the time of the request. SlideRule is able to communicate with back-end data services like HSDS as well as directly access H5 data stored in AWS S3 through its H5Coro library. This combination provides cloud-optimized access to the ICESat-2 source datasets while preserving the existing HDF5-based tooling the project has already heavily invested in. The initial target application for SlideRule is processing the ICESat-2 point-cloud and atmospheric datasets for seasonal snow depth mapping and glacier research. We chose this application because there is a growing interest in these areas of research across both universities and government, and because no high-level ICESat-2 data products targeting these communities currently exist.
```

#### r4 — score 0.449

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['data', 'generate', 'icesat']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r5 — score 0.444

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v03-03-00.html
- **title:** Release v3.3.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['dem', 'interest']

**Full text:**

```
Sampling support added for the Merit DEM Added raster module to Python client - returns GeoDataFrame of sampled raster points of interest
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

