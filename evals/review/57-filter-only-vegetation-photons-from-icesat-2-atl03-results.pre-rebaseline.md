# Row 57 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `57-filter-only-vegetation-photons-from-icesat-2-atl03-review.md` —
> verdicts go there, this side is read-only.

**Query:** `filter only vegetation photons from ICESat-2 atl03`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
  - https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
  - https://docs.slideruleearth.io/assets/phoreal.html
- **expected_sections:**
  - `atl08 classification`
  - `atl08_class`
  - `1.2.3 atl08`
  - `phoreal`
- **expected_pages:** (none)
- **notes:** atl08_class with canopy label; user_guide/icesat2 has the class mapping

---

## 📚 docsearch results (top 5)

#### r1 — score 0.571

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'filter', 'from', 'icesat', 'photons', 'vegetation']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r2 — score 0.661

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'photons', 'vegetation']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r3 — score 0.605

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Retrieve ATL03 elevations with ATL08 classifications
- **category:** `tutorial`
- **matched_tokens:** ['atl03', 'icesat', 'only', 'photons']

**Full text:**

```
SRT_LAND , "len" : 20 , "res" : 20 , # classification and checks # still return photon segments that fail checks "pass_invalid" : True , # all photons "cnf" : - 2 , # all land classification flags "atl08_class" : [ "atl08_noise" , "atl08_ground" , "atl08_canopy" , "atl08_top_of_canopy" , "atl08_unclassified" ], # all photons "yapc" : dict ( knn = 0 , win_h = 6 , win_x = 11 , min_ph = 4 , score = 0 ), } # ICESat-2 data release release = '006' # region of interest poly = [ { 'lat' : 39.34603060272382 , 'lon' : - 108.40601489205419 }, { 'lat' : 39.32770853617356 , 'lon' : - 107.68485163209928 }, { 'lat' : 38.770676045922684 , 'lon' : - 107.71081820956682 }, { 'lat' : 38.788639821001155 , 'lon' : - 108.42635020791396 }, { 'lat' : 39.34603060272382 , 'lon' : - 108.40601489205419 } ] # time bounds for CMR query time_start = '2019-11-14' time_end = '2019-11-15' # find granule for each region of interest granules_list = earthdata . cmr ( short_name = 'ATL03' , polygon = poly , time_start = time_start , time_end = time_end , version = release ) # create geodataframe gdf = sliderule . run ( "atl03x" , parms , aoi = poly , resources = granules_list ) HTTP Request Error: HTTP Error 400: Bad Request Using simplified polygon (for CMR request only!), 5 points using tolerance of 0.0001 Starting proxy for atl03x to process 1 resource(s) with 1 thread(s) request <AppServer.78978> on ATL03_20191114034331_07370502_006_01.h5 generated dataframe [gt1l] with 66779 rows and 14 columns request <AppSe
```

#### r4 — score 0.684

- **url:** https://docs.slideruleearth.io/assets/grandmesa_atl03_classification.html
- **title:** Generating ATL03 photon classifications using ATL08 and YAPC
- **section:** Intro
- **category:** `tutorial`
- **matched_tokens:** ['atl03', 'icesat', 'vegetation']

**Full text:**

```
This notebook demonstrates how to use the SlideRule Icesat-2 API to retrieve ATL03 data with two different classifications, one based on the external ATL08-product classifications, designed to distinguish between vegetation and ground returns, and the other based on the experimental YAPC (Yet Another Photon Class) algorithm.
```

#### r5 — score 0.566

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'from', 'icesat', 'photons']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.644

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.5 Refining the Photon Classifications
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 18
- **matched_tokens:** ['filter', 'icesat', 'photons', 'vegetation']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
points that fall above the estimated surface as well as noise points that fall below the ground
(Section 3.2.5, ATBD for ATL08).
2.3.3 Top of Canopy Finding Filter
The same approach used to find the ground is applied to locate the top of canopy. The de-trended
data are effectively 'flipped' by multiplying the photon heights by -1 and adding the mean of all the
heights back in. The same procedure described in the preceding section is then applied to locate
points at the top of the canopy (Section 3.3, ATBD for ATL08).
2.3.4 Photon Classification
Once a composite ground surface is determined, photons are labeled as ground photons if they fall
within the point spread function of the surface—approximately 35 cm rms. Signal photons that are
not labeled as ground and are below the ground surface (buffered with the point spread function)
are labeled as noise but retain the signal label. The top of canopy photons are used to generate an
upper canopy surface by applying a shape-preserving surface fitting method. All signal photons
that are not labeled ground, lie above the ground surface (buffered with the point spread
function), and lie below the upper canopy surface are labeled as canopy photons. Signal photons
that lie above the top of canopy surface are labeled as noise but retain their signal label.
```

#### r2 — score 0.627

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.2.1 Signal Photon De-trending
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 16
- **matched_tokens:** ['filter', 'icesat', 'photons', 'vegetation']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
2.3.2 Surface Finding
The surface finding approach utilizes one algorithm to find the ground surface and canopy
surface (as noted previously, the science team anticipates that future releases will combine
multiple approaches to better distinguish individual photons as ground, canopy, top of canopy, or
noise).
Figure 7 shows a flowchart of the signal finding approach in ATL08. The sections that follow briefly
describe the steps in the surface finding algorithm. The process is detailed in "Section 3.2 | Surface
Finding" of the ATBD for ATL08.
Figure 5. Flowchart of ATL08 Surface Finding.
2.3.2.1 Signal Photon De-trending
The effect of topography on the input data is removed to improve the performance of the algorithm.
To achieve this, the input signal photons are de-trended by subtracting a heavily smoothed
representation of the surface. Essentially, this surface is a low pass filter of the original data; most
of the analyses to detect the canopy and ground are applied to a high pass filter of the data. The
amount of smoothing, i.e., the window size, depends on the underlying relief. For example, for
segments with high relief, the smoothing window is decreased to ensure topography is not filtered
out (Section 3.2.1, ATBD for ATL08).
Page 15 of 19National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.610

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 3
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 3
- **matched_tokens:** ['atl03', 'filter', 'from', 'only', 'photons']

**Full text:**

```
2017 September Modified 500 canopy photon segment filter (Sec 3.5 (c), Sec
4.14 (6))
2017 November Added solar_azimuth, solar_elevation, and n_seg_ph to
Reference Data group; parameters were already in product
(Sec 2.4)
2017 November Specified number of ground photons threshold for relative
canopy product calculations (Sec 4.18 (2)); no number of
ground photons threshold for absolute canopy heights (Sec
4.18.1 (1))
2017 November Changed the ATL03 signal used in superset from all ATL03
signal (signal_conf_ph flags 1-4) to the medium-high
confidence flags (signal_conf_ph flags 3-4) (Sec 3.1, Sec 4.3
(17))
2017 November Removed Date parameter from Table 2.4 since UTC date is in
file metadata
2018 March Clarified that cloud flag filtering option should be turned off
by default
2018 March Changed h_diff_ref QA threshold from 10 m to 25 m (Table
5.2)
2018 March Added absolute canopy height quartiles,
canopy_h_quartile_abs (Later removed)
2018 March Removed psf_flag from main product; psf_flag will only be a
QAQC alert (Sec 5.2)
2018 March Added an Asmooth filter based on the reference DEM value
(Sec 4.6 (4-5))
2018 March Changed relief calculation to 95th – 5th signal photon heights.
(Sec 4.6 (6))
2018 March Adjusted the Asmooth smoothing methodology (Sec 4.6 (8))
2018 March Recalculate the Asmooth surface after filtering outlying noise
from signal, then detrend signal height data (Sec 4.9 (3-4))
2018 March Added option to run alternative DRAGANN process again in
high noise cases (
```

#### r4 — score 0.723

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['atl03', 'from', 'icesat', 'photons', 'vegetation']

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

#### r5 — score 0.641

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 4.2 Date Last Updated
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['atl03', 'from', 'icesat', 'photons', 'vegetation']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Table 5. Version History Summary
Version Date Description
V1 May 2019 Initial release
V2 October 2019 Refer to V2 User Guide
V3 May 2020 Refer to V3 User Guide
V4 April 2021 Refer to V4 User Guide
V5 November 2021 Refer to V5 User Guide
• Added a quality check to reject segments for which the V6 May 2023
canopy photons fall more than 150 m below the reference
DEM.
• Calculated the background noise rate and number of noise
photons within a canopy segment and adjusted the canopy
radiometric rate accordingly.
• For segments with a solar elevation angle > 20°, if the
background noise rate is < 0.98 of the canopy rate, then
reassign the canopy photons as noise photons.
• Incorporated the YAPC photon weights from the ATL03
data product into the ground-finding approach.
• Reduced the number of labeled photons required to report
the canopy or terrain heights within each segment for the
strong and weak beams, resulting in more ATL08 reported
values.
V6.1 May 2024 Data from 13 November 2022 to 26 October 2023 were
reprocessed using ITRF2014 (replacing ITRF2020) for
consistency across the entire data set.
V6.1 March 2026 Data access was removed for v6.1. Data coverage was 14 Oct
2018 to 2 Mar 2025.
Publication Date
May 2023
Date Last Updated
March 2026
Page 19 of 19National Snow and Ice Data Center
nsidc.org
```

---

