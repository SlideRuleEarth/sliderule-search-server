# Row 36 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `36-atl08-terrain-classification-output-variables-hdf5-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL08 terrain classification output variables HDF5`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **expected_sections:**
  - `classification`
  - `data groups`
  - `ground`
- **expected_pages:** (none)
- **notes:** ATL08 user guide terrain variables

---

## 📚 docsearch results (top 5)

#### r1 — score 0.580

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3.1 Quality Filter Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'terrain']

**Full text:**

```
The ATL08 data can be filtered based on different quality filters. te_quality_score : terrain quality score threshold can_quality_score : canopy quality score threshold
```

#### r2 — score 0.499

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-09-00.html
- **title:** Release v4.9.x
- **section:** Changes
- **category:** `release_notes`
- **matched_tokens:** ['output', 'variables']

**Full text:**

```
v4.9.2 - Optimized raster sampling code v4.9.2 - Fixed Python client to support output format specified as geoparquet with open_on_complete v4.9.2 - Changed default atl03 confidence flags to low, medium, and high v4.9.2 - Added separate geophysical corrections ancillary fields list in support of future ATL03 dataframe class v4.9.0 - Added ancillary field support to GEDI ( gedi01bp , gedi02ap , gedi04ap ) Bathy Version #15 - Separated out processing flags into their own variables in the h5 file: sensor depth exceeded, invalid kd, invalid wind speed, night flight Bathy Version #15 - Added low confidence flag to h5 Bathy Version #15 - Added ensemble confidence to h5 Bathy Version #15 - ISO.XML polygon is now taken directly from ATL03 Bathy Version #14 - Updated ensemble
```

#### r3 — score 0.574

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl08
- **category:** `api_reference`
- **matched_tokens:** ['atl08', 'hdf5']

**Full text:**

```
sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame
```

#### r4 — score 0.469

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Generating ATL03 photon classifications using ATL08 and YAPC
- **category:** `tutorial`
- **matched_tokens:** ['atl08', 'classification']

**Full text:**

```
Plot ATL03 data with different classifications for a region over the Grand Mesa, CO region ATL08 Land and Vegetation Height product photon classification Experimental YAPC (Yet Another Photon Classification) photon-density-based classification
```

#### r5 — score 0.504

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'classification']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.603

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.5 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 10
- **matched_tokens:** ['atl08', 'hdf5', 'variables']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Three HDF5 dimension scales are stored at the top level alongside the data groups—
ds_geosegments, ds_metrics, and ds_surf_type—which index the within-land geosegments,
surface type, and metrics arrays. For details about how the parameters are organized in the ATL08 product, see "Section 2 | ATL08:
Data Product" in the ATBD for ATL08.
1.2.5 Naming Convention
Data files utilize the following naming convention:
ATL08_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr].h5
Example:
ATL08_20181014001049_02350102_006_01.h5
The following table describes the file naming convention variables:
Table 3. File Naming Convention Variables and Descriptions
Variable Description
ATL08 ATLAS/ICESat-2 L3A Land and Vegetation Height product
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit Reference Ground Track number. The ICESat-2 mission has 1,387
RGTs, numbered from 0001 to 1387.
cc Cycle Number. Each of the 1,387 RGTs is targeted in the polar regions once every
91 days. The cycle number tracks the number of 91-day periods that have elapsed
since ICESat-2 entered the science orbit.
ss Orbital segment (region) number (see Figure 3). ATL08 data files cover
approximately 1/14th of an orbit. Orbital segment numbers range from 01–14.
vvv_rr Version and revision number.*
From time to time, NSIDC receives reprocessed granules from our data provider.
```

#### r2 — score 0.540

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 3
- **matched_tokens:** ['atl08', 'hdf5', 'terrain']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
1 DATA DESCRIPTION
Parameters
Along-track terrain and canopy height above the WGS 84 ellipsoid (ITRF2014 reference frame). File Information
1.2.1 Format
Data are provided as HDF5 formatted files.
1.2.2 ATLAS/ICESat-2 Description
The following brief description of the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory and
Advanced Topographic Laser Altimeter System (ATLAS) instrument is provided to help users better
understand the file naming conventions, internal structure of data files, and other details referenced by
this user guide. The ATL08 data product is described in detail in the Ice, Cloud, and land Elevation
Satellite-2 Project Algorithm Theoretical Basis Document for the Land - Vegetation Along-Track Product
(ATBD for ATL08 | V6, https://doi.org/10.5067/8ANPSL1NN7YS). The ICESat-2 observatory utilizes a photon-counting lidar (the ATLAS instrument) and ancillary
systems (GPS, star cameras, and ground processing) to measure the time a photon takes to travel
from ATLAS to Earth and back again and determine the reflected photon's geodetic latitude and
longitude. Laser pulses from ATLAS illuminate three left/right pairs of spots on the surface that
trace out six approximately 14 m wide ground tracks as ICESat-2 orbits Earth.
```

#### r3 — score 0.525

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 34
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 34
- **matched_tokens:** ['atl08', 'hdf5', 'terrain']

**Full text:**

```
582
583 Figure 2.1. HDF5 data structure for ATL08 products
584
585 For each data parameter, terrain surface elevation and canopy heights will be
586 provided at a fixed segment size of 100 meters along the ground track. Based on the
587 satellite velocity and the expected number of reflected photons for land surfaces, each
588 segment should have more than 100 signal photons, but in some instances there may
589 be less than 100 signal photons per segment. If a segment has less than 50 classed
590 (i.e., labeled by ATL08 as ground, canopy, or top of canopy) photons we feel this
591 would not accurately represent the surface. Thus, an invalid value will be reported in
34
```

#### r4 — score 0.546

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 7
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 7
- **matched_tokens:** ['atl08', 'terrain']

**Full text:**

```
The
saturation flag indicates that the ATL08 segment
experienced some saturation which is often an indicator for
water
2020 May 15 Canopy height metrics (relative and absolute heights) were
expanded to every 5% ranging from 5 – 95%.
2020 May 15 The Landsat canopy cover check to determine whether the
algorithm should search for both ground and canopy or just
ground has been disabled. Now the ATL08 algorithm will
search for both ground and canopy points everywhere.
2020 June 15 Corrected the calculation of the absolute canopy heights
2020 June 15 Changed the search radius for initial top of canopy
determination (Section 4.9)
2020 September 1 Incorporate the quality_ph flag from ATL03 into the ATL08
workflow (beginning of Section 4)
2020 September 1 Added the calculation of Terrain photon rate
(photon_rate_te) for each ATL08 segment to the land
product (Section 2.1.16)
2020 September 1 Added the calculation of canopy photon rate
(photon_rate_can) for each ATL08 segment to the land
product (Section 2.2.26)
7
```

#### r5 — score 0.523

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Classification Algorithms
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 22
- **matched_tokens:** ['classification', 'hdf5']

**Full text:**

```
4.3.1 ATL24 Data Structure and Naming Conventions
The naming and internal organization of the final HDF5 file for each ATL24 granule will
match the conventions used on the rest of the project. Each granule will also have the naming
convention similar to the other ICESat-2 data products. Each variable within the name
(place holders) are described in Table 5. Please note that there are two sets of version and
revision numbers that represent both ATL03 input version and revision and then the version
and revision of ATL24. ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr]_[vvv_rr].h5
Table 5: ATL24 naming convention
Variable Description
ATL24 ICESat-2 Level 3 Global nearshore and coastal bathymetry
ATLAS/ICESat-2 Level 3a calibrated backscatter profiles and at- ATL09 mopsheric layer characteristics
yyyymmdd Year, month and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC). Four digit Reference Ground Track number. The ICESat-2 mission tttt has 1,387 RGTs, numbered from 0001 to 1387. Cycle Number. Each of the 1387 RGTs is targeted in the polar
regions once every 91 days. The cycle number tracks the number of cc 91-day periods that have elapsed since ICESat-2 entered the science
orbit. Segment number. ATL03 data files are segmented into approxi-
ss mately 1/14th of an orbit. Segment numbers range from 01-14.
```

---

