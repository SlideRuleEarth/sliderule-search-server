# Row 38 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `38-atl24-file-contents-and-spatial-coverage-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL24 file contents and spatial coverage`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **expected_sections:**
  - `file contents`
  - `coverage`
- **expected_pages:** (none)
- **notes:** ATL24 user guide

---

## 📚 docsearch results (top 5)

#### r1 — score 0.384

- **url:** https://docs.slideruleearth.io/assets/atl24_access.html
- **title:** Subsetting and filtering ATL24 data
- **section:** (3) Detailed Access of a Single Track
- **category:** `tutorial`
- **matched_tokens:** ['atl24', 'file']

**Full text:**

```
[14]: parms = { "atl24" : { "compact" : False , "confidence_threshold" : 0.0 , "class_ph" : [ "unclassified" , "sea_surface" , "bathymetry" ] }, "beams" : "gt3r" , "rgt" : 202 , "cycle" : 12 } gdf3 = sliderule . run ( "atl24x" , parms , aoi = aoi ) request <AppServer.65190> retrieved 1 resources Starting proxy for atl24x to process 1 resource(s) with 1 thread(s) request <AppServer.65191> on ATL24_20210706203010_02021201_006_01_001_01.h5 generated dataframe [gt3r] with 35527 rows and 17 columns Successfully completed processing resource [1 out of 1]: ATL24_20210706203010_02021201_006_01_001_01.h5 Writing arrow file: /tmp/tmpeqf2fes_ Closing arrow file: /tmp/tmpeqf2fes_ [15]: gdf3 [15]: sensor_depth_exceeded night_flag region class_ph gt sigma_tvu surface_h invalid_wind_speed sigma_thu rgt ... invalid_kd low_confidence_flag confidence spot x_atc y_atc srcid cycle ellipse_h geometry time_ns 2021-07-06 20:35:11.531963136 0 0 1 0 60 0.133018 0.367559 0 7.071068 202 ... 1 0 1.005813e-07 1 2.146475e+06 -3246.021484 0 12 1.637071 POINT (-69.53822 19.31126) 2021-07-06 20:35:11.531963136 0 0 1 0 60 0.133018 0.367559 0 7.071068 202 ... 1 0 1.759629e-07 1 2.146475e+06 -3246.173584 0 12 -24.135511 POINT (-69.53821 19.31126) 2021-07-06 20:35:11.532163072 0 0 1 0 60 0.133018 0.367595 0 7.071068 202 ... 1 0 4.991626e-07 1 2.146476e+06 -3246.186035 0 12 -25.274578 POINT (-69.53822 19.31127) 2021-07-06 20:35:11.532163072 0 0 1 0 60 0.133018 0.367595 0 7.071068 202 ... 1 0 1.759629e-07 1 2.1464
```

#### r2 — score 0.478

- **url:** https://docs.slideruleearth.io/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Lessons Learned
- **category:** `developer_guide`
- **matched_tokens:** ['atl24']

**Full text:**

```
There were two validation checks in the processing code that caused no issues in our small test runs, but were overly restrictive when running globally. (1) We required all ATL03 granules to have all 6 beams present; this caused valid ATL03 granules with only the strong beams present to be discarded. (2) We had an internal check that the data within an HDF5 chunk in the ATL03 granule, when compressed, was smaller than or equal to in size to the uncompressed data. In both cases, these checks were removed and the granules that had failed these checks were reprocessed. In order to accerlate the generation of ATL24, the VIIRS data used for turbidity calculations was staged in a private S3 bucket. But at the time the data was staged, the later months of ATL03 had not been released; yet when we executed the processing run, those later ATL03 granules had been released. The result was that the last couple cycles of ATL03 all failed because the VIIRS data was not found. Once discovered, the necessary VIIRS data was staged and the ATL24 granules for the last couple of cycles was reprocessed. Throughout the processing run there were intermittent CMR failures. As a result, the processing code had to be very conservative in retrying the CMR requests. This often produced very long processing runs for granules that would otherwise have completed quickly.
```

#### r3 — score 0.525

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl24']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r4 — score 0.440

- **url:** https://docs.slideruleearth.io/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['atl24']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r5 — score 0.513

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl24']

**Full text:**

```
ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.482

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.3.2 Resolution
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 11
- **matched_tokens:** ['coverage', 'file', 'spatial']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
1.2.6 Browse Files
Browse files are provided as JPGs that contain images designed to quickly assess the location and
quality of each granule's data. Images include track location, canopy heights, and terrain and
canopy photon count for each ground track. Browse files utilize the same naming convention as
their corresponding data file but with "_BRW" and descriptive keywords appended.
Spatial Information
1.3.1 Coverage
Spatial coverage is global. However, data are not produced for orbital segments that cross open
ocean only (i.e., do not cross a land surface).
ATL08 data can be referenced by numbered geographical regions, unique to the ATL08
product, which roughly correspond to continents (Greenland is assigned to its own region and
Antarctica is divided into four), for a total of 11 regions (see Figure 5). The ATL08
regions encompassed by the ATL03 input granule are stored
in \ancillary_data\land\atl08_region.
Figure 3. ATL08 Geographic Regions
Static surface masks (land ice, sea ice, land, and ocean) are applied to ATL03 to reduce the
volume of data that a surface-specific along-track data product is required to process. The land
surface mask directs the ATL08 algorithm to consider data from only those areas of interest.
1.3.2 Resolution
Page 10 of 19National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.512

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 4
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 4
- **matched_tokens:** ['atl24', 'contents']

**Full text:**

```
Contents
1 Introduction 1
2 Context/Background 4
2.1 Historical Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3 ATL24 Overview 5
3.1 ATL24 Data Workflow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2 Data Dissemination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.3 ATL24 ATBD Sections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4 Technical Considerations 8
4.1 Scientific Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.2 ATL24 Input Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.3 ATL24 Output Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.3.1 ATL24 Data Structure and Naming Conventions . . . . . . . . . . . 15
4.4 Classification Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.4.1 CoastNet Classification . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.4.2 BathyPathFinder Classification . . . . . . . . . . . . . . . . . . . . . 19
4.4.3 OpenOceans++ Classification . . . . . . . . . . . . . . . . . . . . . . 20
4.4.4 Median Filter Classification . . . . . . . . . . . . . . . . . . . . . . . 23
4.4.5 C-SHELPh Classification . . . . . . . . . . . . . . . . . . . . . . . . 24
4.4.6 Quantile Trees Classification . . . . . . . . . . . . . . . . . . . . . . . 26
4.4.7 Ensemble Classification . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.8 Blunder Detection . . . . . . . . 
```

#### r3 — score 0.382

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.2 File Contents
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 3
- **matched_tokens:** ['atl24', 'contents', 'file']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
1 DATA DESCRIPTION
This user guide refers to the ICESat-2 Project Algorithm Theoretical Basis Document (ATBD) for Coastal
and Nearshore Along-Track Bathymetry Product (ATL24) (ATBD for ATL24, V1 |
https://doi.org/10.5067/PXJMCZD0MYLN).
1.1 Summary
ATL24 provides global along-track coastal and nearshore bathymetry, consisting of refraction-
corrected seafloor and sea surface heights (orthometric and ellipsoidal heights and instantaneous
depths), as well as associated uncertainties. The data are derived from ATLAS/ICESat-2 L2A
Global Geolocated Photon Data (ATL03).
1.2 File Information
1.2.1 Format
The data are provided as HDF5-formatted files.
1.2.2 File Contents
A complete list of ATL24 parameters is available in the ATL24 Data Dictionary.
Within data files, similar variables such as science data, instrument parameters, and ancillary data
are grouped together. Figure 1 shows data groups stored at the top level in ATL24 data files.
Figure 1. ATL24 top-level data groups and variables.
The following sections describe the data groups and their contents stored at the top level in ATL24
data files.
Page 2 of 15National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.375

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Performance Assessment and Validation
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 41
- **matched_tokens:** ['atl24', 'coverage', 'spatial']

**Full text:**

```
Figure 8: NOAA BlueTopo data set, which will be used as the reference data set in testing the
accuracy of ATL24.
5 Performance Assessment and Validation
The accuracy of ATL24 will be tested using the NOAA BlueTopo data set, which is a
compilation of best-available bathymetric data for U.S. waters, maintained and distributed
by NOAA’s Office of Coast Survey (OCS) through the National Bathymetric Source program
(Rice et al. 2023). The reasons for using BlueTopo as the reference for the accuracy test are: 1)
it is referenced consistently to a known vertical datum; 2) it has better spatial resolution than
many other publicly-available data sets; 3) being produced and maintained by NOAA OCS
for supporting NOAA’s nautical charting mission, it was created with a focus on accuracy,
datum consistency, and reliability; and 4) it is available via an AWS S3 bucket with code
for access provided on a public GitHub repository, facilitating use in SlideRule ATL24. A
disadvantage is that, while ATL24 has global coverage, BlueTopo currently only covers the
U.S. East Coast and Gulf Coast. However, despite the limited geographic extent, BlueTopo
was determined to be the best publicly-avaiable bathymetric data set for use as a reference
data set in testing the accuracy of ATL24.
```

#### r5 — score 0.466

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.3 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 5
- **matched_tokens:** ['atl24', 'file']

**Full text:**

```
VVV_RR Version and revision number of the input ATL03 files*.
vvv_rr Version and revision number of the ATL24 product*.
*Occasionally, NSIDC receives reprocessed granules from our data provider. These granules have the
same file name as the original (i.e., date, time, ground track, cycle, and region number), but the revision
Page 4 of 15National Snow and Ice Data Center
nsidc.org
```

---

