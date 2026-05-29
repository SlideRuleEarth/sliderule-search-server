# Row 97 results: nsidc / cross_product

> Auto-generated. Open this file alongside `97-atl24-uses-atl03-photons-for-bathymetry-classification-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL24 uses ATL03 photons for bathymetry classification`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL24 ingests ATL03 photons

---

## 📚 docsearch results (top 5)

#### r1 — score 0.851

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'classification', 'photons']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r2 — score 0.733

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'classification', 'photons']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r3 — score 0.769

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'photons']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r4 — score 0.722

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Statistics
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'photons']

**Full text:**

```
452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea surface 0.73% of classified photons were bathymetry
```

#### r5 — score 0.580

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'photons']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.628

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'classification']

**Full text:**

```
3 ATL24 Overview
3.1 ATL24 Data Workflow
Similar to other ICESat-2 Level 3a products, the input to the ATL24 pipeline is Level 2a,
Global geolocated point cloud data; ATL03 (T. A. Neumann et al. 2019b). ATL03 provides
every detected photon (signal and noise), with the calculated geolocation (geodetic latitude
and longitude) and associated parameters (operational) for each of ATLAS’s six beams. The
ATL03 product also provides signal confidence flags and estimated uncertainties at the photon
level. Gridded surface masks for land ice, sea ice, land, ocean and inland water products are
used within the L3b processing workflows to reduce the volume of data processed and guide
the production of these surface-specific, higher-level ICESat-2 data products. The ATL24
workflow requires a similar search approach to limit data processing to coastal and nearshore
environments that present a reasonable opportunity for capturing bathymetry. As such, a
gridded bathymetry mask based on possible retrievability was created to guide the processing
extents and is discussed in detail in section subsection 6.4. Figure 1 provides the overarching processing pipeline for ATL24, including the search
mask step to identify relevant ATL03 granules. The ATL24 algorithm’s main goal is to
provide a solution for robust, global bathymetric and sea surface signal extraction and
classification.
```

#### r2 — score 0.657

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3 Processing
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 7
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'classification']

**Full text:**

```
On-demand and customizable, science-ready bathymetry is also available via SlideRule, a public
web application programming interface for processing of science data in the cloud.
2.2 Acquisition
ATL03 provides heights above the WGS84 ellipsoid, the latitude and longitude, and time for every
ATLAS photon detection. These values and data quality flags are the primary input to ATL24.
2.3 Processing
The ATL24 workflow utilizes an ensemble of classification models to handle the full extent of
seafloor types, morphologies, depth ranges, water types, and cover types that exist throughout
coastal and nearshore areas, as described in the following sections. See "Section 4.4 Classification
Algorithms" of the ATL24 ATBD for full details. Use of a bathymetric search mask drastically
reduces computation time by removing data that are on land or too deep/turbid for measurement. Page 6 of 15National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.598

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Known Issues
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 56
- **matched_tokens:** ['atl03', 'atl24', 'classification', 'photons', 'uses']

**Full text:**

```
4. Refraction correction: The refractive index of water layer usid in the ATL24
refraction correction is based on global, 0.25 degree resolution temperature and
salinity datasets processed using the Quan-Fry equation Quan and Fry 1995. The
current version of the refractive index layer uses only annual averages of salinity
and temperature at each geographical location and does not currently account for
temporal variability.
• User Utility
1. Uncertainty value: For the subaqueous photons the uncertainty value on each
photon is a combination of the uncertainty in ATL03 and the TPU model uncer-
tainty. If the user would like to separate these values the original ATL03 sigma_h,
sigma_lat, the index_ph value can provide the link back to the original ATL03
photon’s uncertainties.
2. Refraction correction: For the subaqueous photons the correction value applied
from the index of refraction data layer can be removed by using the index_ph to
link back to the original ATL03 photon’s position.
• Product Parameterization
1. Waves: Currently there are no parameters on ATL24 related to wave characteristics
derived from the sea surface photons
2. Classification confidence: When the value of the confidence is less than 0.6
the low_confidence = 1. This threshold value will change with future iterations of
ATL24.
49
```

#### r4 — score 0.611

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 2.3.1.8 Ensemble Classification
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 9
- **matched_tokens:** ['atl03', 'atl24', 'bathymetry', 'classification', 'photons']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
the PointNet++ algorithm is not being used in the ensemble, but it may be activated at a future
date.
2.3.1.5 Median Filter Classification
Median Filter is a simple empirical method for extracting bathymetry profiles from ICESat-2 data. For ATL24, all ATL03 photon ellipsoid heights are converted to orthometric heights (EGM08), and
all photons more than 1.5 m below the sea surface median are retained. The method calculates
median elevations for 50-photon windows and a moving standard deviation of elevations for 30-
photon windows. Photons remaining after filtering are separated into 0.001º latitude segments. Segments with more than 14 photons are considered bathymetry.
2.3.1.6 C-SHELPh Classification
The Classification of Sub-aquatic Height Extracted Photons (C-SHELPh) algorithm is an open-
source tool for producing bathymetric maps. The algorithm detects the dense clustering of photons
indicative of surface returns. A gridding convention provides surface heights and along-track
latitudes, where 0 m is the ocean surface. The ATL24 implementation of C-SHELPh bins photons
into 0.001º along-track blocks and 0.5 m vertical blocks. The number of photons in each block is
counted, and a threshold is calculated based on the number of photons in all blocks.
```

#### r5 — score 0.656

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** C-SHELPh Classification
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 31
- **matched_tokens:** ['atl24', 'bathymetry', 'classification', 'photons']

**Full text:**

```
The ATL24 implementation of C-SHELPh bins photons into 0.001 degree along track
blocks and 0.5 meter vertical blocks. The number of photons in each block is counted and
then using these bin counts, a threshold is calculated based on the number of photons in all
the blocks. The threshold is defined as the nth percentile of photon counts per block where
n=0.5. Although CSHELPh has been used in the past to determine the sea surface, the
ATL24 usage takes the surface input from the Quantile Trees output (section 4.4.6). The threshold is calculated for the 85% and 65% and if these are equal, or the 65%
threshold number of photons in a bin is less than five, the algorithm sets the required number
of photons in a bin for bathymetry prediction to occur equal to five.
24
```

---

