# Row 46 results: nsidc / cross_product

> Auto-generated. Open this file alongside `46-how-atl08-uses-atl03-photons-for-classification-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how ATL08 uses ATL03 photons for classification`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **expected_sections:**
  - `classification`
  - `noise filtering`
  - `input`
- **expected_pages:**
  - 6–30
- **notes:** cross-product: ATL08 ingests ATL03

---

## 📚 docsearch results (top 5)

#### r1 — score 0.819

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2 Photon-selection Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'classification', 'photons']

**Full text:**

```
Once the ATL03 input data are are selected, a set of photon-selection photon parameters are used to select from among the available photons. At this stage, additional photon-classification algorithms (ATL08, YAPC) may be selected beyond what is available in the ATL03 files. The criterial described by these parameters are applied together, so that only photons that fulfill all of the requirements are returned.
```

#### r2 — score 0.760

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl08', 'classification', 'photons']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r3 — score 0.660

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v01-01-00.html
- **title:** Release v1.1.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['atl08', 'classification', 'photons', 'uses']

**Full text:**

```
Time is also used as the index. (APIs affected: atl06 , atl06p , atl03s , atl03sp ). v1.1.0 - ATL08 classifications are now supported in the atl06 , atl06p , atl03s , atl03sp APIs: sliderule#71 when the request parameters supply a list of ATL08 classifications to use, the server code will read the corresponding ATL08 data and only use the supplied classifications in the calculation the following classifications are supported: noise, ground, canopy, top of canopy, unclassified for the atl03s , atl03sp , the presence of the ATL08 classification list also enables the returned photon data to include each photons classification v1.1.0 - The following APIs now return GeoDataFrames instead of dictionaries: atl06 , atl06p , atl03s , atl03sp . this standardizes the return structure at no cost to performance each GeoDataFrame has a âtimeâ column which is a Python datetime value each GeoDataFrame uses the geometry.x and geometry.y to represent the âlongitudeâ and âlatitudeâ fields respectively. the âdelta_timeâ column now represents the time from the ATLAS Standard Data Product (SDP) epoch (January 1, 2018) The GeoDataFrames returned by atl03s and atl03sp contain a row for each photon that is returned v1.1.0 - All APIs default to using version 004 of the data products. v1.1.0 - Added the ground track field ( âgtâ ) to the atl06 and atl06p elevation returns. added the following constants to the icesat2.py module: GT1L, GT1R, GT2L, GT2R, GT3L, GT3R you can now do thing
```

#### r4 — score 0.764

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'classification', 'photons']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r5 — score 0.690

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-07-00.html
- **title:** Release v4.7.x
- **section:** Development Updates
- **category:** `release_notes`
- **matched_tokens:** ['atl03', 'photons', 'uses']

**Full text:**

```
v4.7.1 - The ATL03 photons are stored in a table in memory and operated on in place instead of streamed v4.7.1 - The Python classifiers are all executed from a single Python script that uses multiprocessing instead of having the data transferred to and from disk
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.598

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['atl03', 'atl08', 'photons', 'uses']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Processing
To detect both the canopy surface and the underlying topography, the ATL08 software has been
designed to accept multiple approaches to capture both the upper and lower surface signal
photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best
preserves signal photons returned from the canopy and topography while rejecting noise photons. The following sections outline the approach implemented by the algorithm. More detailed
descriptions are available in "Section 3 | Algorithm Methodology" and "Section 4 | Algorithm
Implementation" of the ATBD for ATL08.
2.3.1 Noise Filtering
Removing solar background photons represents one of the biggest challenges with photon
counting lidar data. The ATL03 signal finding approach uses a histogramming strategy that places
photons into vertical bins along a consistent horizontal span and then assumes the signal lies
within the bins that contain the highest number of photons. This method works well over simple
surfaces such as ice sheets; however, photons that are reflected from the top of the canopy in
vegetated areas are not always flagged as signal.
```

#### r2 — score 0.590

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 3 SOFTWARE AND TOOLS
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['atl03', 'atl08', 'photons', 'uses']

**Full text:**

```
Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03 data
product have provided guidance regarding the fidelity to which the ATL03 algorithm needs to
discriminate signal and background photon events. In general, each higher-level data product
requires ATL03 to identify likely signal photon events within ±10 meters of the surface. Because the
signal-finding algorithm uses histograms, the vertical resolution at which signal photons are
selected is directly proportional to the histogram bin size. All photons in any one bin are either
classified as signal or background events. One of the goals of the algorithm is to use the smallest
bin size for which signal can be found to classify photons at the finest resolution possible. Test
cases indicate that this resolution meets or exceeds the needs of the higher-level data products in
all but very weak signal conditions. This smallest bin size varies as a function of surface slope and
background count rate (see ATL03 ATBD | Section 5.1).
3 SOFTWARE AND TOOLS
PhoREAL is a free library of geospatial analysis tools and source code written specifically for
working with ATL03 (and ATL08) data. Page 20 of 22National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.603

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 28
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 28
- **matched_tokens:** ['atl03', 'atl08', 'classification', 'photons']

**Full text:**

```
In addition to
459 recording photons from the reflected signal, the ATLAS instrument will detect
460 background photons from sunlight which are continually entering the telescope. A
461 primary objective of the ICESat-2 data processing software is to correctly
462 discriminate between signal photons and background photons. Some of this
463 processing occurs at the ATL03 level and some of it also occurs within the software
464 for ATL08. At ATL03, this discrimination is done through a series of three steps of
465 progressively finer resolution with some processing occurring onboard the satellite
466 prior to downlink of the raw data. The ATL03 data product produces a classification
467 between signal and background (i.e. noise) photons, and further discussion on that
468 classification process can be read in the ATL03 ATBD. In addition, not all geophysical
469 corrections (e.g. ocean tide) are applied to the position of the individual geolocated
470 photons at the ATL03 level, but they are provided on the ATL03 data product if there
28
```

#### r4 — score 0.581

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 96
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 96
- **matched_tokens:** ['atl03', 'atl08', 'classification', 'photons']

**Full text:**

```
1793 For this release of the software, we want to mention that there are cases of after-pulsing
1794 that occur 0.5 – 2.3 m below the surface that have been flagged with a value of 10 or 20.
1795 For this release of the software, we have determined that we will include saturated photons.
1796 Thus, the output from the DRAGANN algorithm (i.e. the DRAGANN flag) will be set to
1797 a value of 0 when ATL03 quality_ph flags photons with values other than 0, 10, or 20 such
1798 that they are ignored in the ATL08 algorithm.
1799 A third quality check pertains to the signal photons (DRAGANN + ATL03 signal
1800 confidence photons) and whether those heights are near the surface heights. To pass this
1801 check, signal photons that lie 120 m above the reference DEM will be disregarded. Signal
1802 photons lying below the reference DEM will be allowed to continue for additional ATL08
1803 processing. The motivation for this quality check is to eliminate ICESat-2 photons that are
1804 reflecting from clouds rather than the true surface.
1805 Table 4.1. Input parameters to ATL08 classification algorithm. Name Data Type Long Units Description Source
Name
delta_time DOUBLE GPS seconds Elapsed GPS seconds since start of ATL03
elapsed the granule for a given photon. Use
time the metadata attribute
granule_start_seconds to compute
full gps time.
lat_ph FLOAT latitude of degrees Latitude of each received photon.
```

#### r5 — score 0.614

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.1 Introduction
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 64
- **matched_tokens:** ['atl03', 'photons', 'uses']

**Full text:**

```
The ground tracks of
a strong and weak beam pair are essentially parallel to each other, and separated by ~90 meters
in the across-track direction, so the slopes of the resultant surface profiles should be very similar. Therefore for the weak beam of each pair, the algorithm uses the surface profile found in the
strong beam to guide slant histogramming in the weak beam. Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03
data product have provided guidance regarding the fidelity to which the ATL03 algorithm needs
to discriminate signal and background photon events. In general, each higher-level data product
requires ATL03 to identify likely signal photon events within +/- 10 meters of the surface. Since
this algorithm uses histograms, the vertical resolution at which signal photons are selected is
directly proportional to the histogram bin size. All photons in any one bin are either classified as
48 Release Date: Fall 2022
```

---

