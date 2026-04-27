# Row 39 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `39-gedi-l4a-footprint-geolocation-variables-agbd-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI L4A footprint geolocation variables AGBD`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **expected_sections:** (none)
- **expected_pages:**
  - 10–30
- **notes:** GEDI L4A user guide

---

## 📚 docsearch results (top 5)

#### r1 — score 0.596

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.4 L4A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['agbd', 'footprint', 'gedi', 'l4a']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation" : elevation in meters of the surface of the earth "agbd" : above ground biodensity "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

#### r2 — score 0.598

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi', 'l4a']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r3 — score 0.557

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi04a
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'l4a']

**Full text:**

```
sliderule.gedi. gedi04a ( parm , resource ) [source] Performs GEDI L4A subsetting of elevation footprints Parameters : parms ( dict ) â parameters used to configure subsetting process resource ( str ) â GEDI HDF5 filename asset ( str ) â data source asset Returns : gridded footrpints Return type : GeoDataFrame
```

#### r4 — score 0.654

- **url:** https://docs.slideruleearth.io/background/GEDI.html
- **title:** GEDI
- **section:** References
- **category:** `background`
- **matched_tokens:** ['gedi', 'geolocation']

**Full text:**

```
GEDI Project Homepage Earthdata GEDI Project Overview ATBD for GEDI Waveform Geolocation for L1 and L2 Products Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.565

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.2 L2A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation_lowestmode" : elevation in meters of reflection closest to the surface of the earth "elevation_highestreturn" : elevation in meters of reflection farthest from the surface of the earth "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.563

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 3
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 3
- **matched_tokens:** ['agbd', 'footprint', 'gedi']

**Full text:**

```
1. Introduction
The Global Ecosystem Dynamics Investigation (GEDI) is a multibeam waveform lidar on
the International Space Station (Dubayah et al., 2020). Two objectives of the mission are to
quantify the distribution of aboveground carbon in woody vegetation, and to use these
estimates to determine the impact of land use and land cover changes on aboveground carbon
stocks. Both of these objectives speak to fundamental uncertainties in the spatial distribution of
aboveground carbon density (Mitchard et al., 2013; Pan et al., 2011). This document describes the theoretical basis, scientific and mathematical assumptions
that underpin the algorithms developed by the GEDI Science Team to produce estimates of
footprint AGBD from GEDI lidar in release 1 and release 2 of the GEDI04_A data product. It also
describes quality assessment and filtering criteria used to minimize differences in measurement
characteristics between power and coverage ground tracks that may impact estimates of AGBD. Footprint AGBD is generated for 32 combinations of PFT and geographic world region using 13
linear models developed from a comprehensive set of simulated GEDI waveforms associated
with field estimates of AGBD from allometric scaling equations in 21 countries. The GEDI04_A
data product is publicly available through the Oak Ridge National Laboratory Distributed Active
Archive Center (ORNL DAAC).
```

#### r2 — score 0.605

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 10
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 10
- **matched_tokens:** ['agbd', 'footprint', 'gedi']

**Full text:**

```
with the best performance in comparison to other technologies (Saatchi et al., 2011; Zolkos et al.,
2013). Most previous efforts have developed site-specific or regional relationships between
AGBD and remote sensing measurements (Zolkos et al., 2013). GEDI faces a different
challenge: it needs to develop models and algorithms that perform well throughout the entire
observation domain of the ISS. Locally developed or regional relationships between AGBD and
height are unlikely to perform well at locations outside the limited geographic extent of training
data unless procedures are developed specifically to ensure transferability beyond the extent of
calibration measurements (Friedl et al., 2002; Ploton et al., 2020).
3. STATISTICAL MODEL DEVELOPMENT
Models to produce GEDI04_A were developed using field estimates of AGBD colocated
with simulated GEDI waveforms derived from discrete-return airborne lidar (Blair and Hofton,
1999; Hancock et al., 2019). The justification for using simulated GEDI waveforms is that few
locations on the land surface are associated with field estimates of AGBD that could be used to
train GEDI models. Because GEDI is a sampling mission and most field plots are small, GEDI
data will not intersect most of these locations during the mission life. The GEDI approach to
developing footprint AGBD models considers multiple candidates stratified by world region and
plant functional type (PFT; Fig. 1) with different functional forms.
```

#### r3 — score 0.597

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 9
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 9
- **matched_tokens:** ['agbd', 'footprint', 'gedi']

**Full text:**

```
This uncertainty propagates
through GEDI level-2A (GEDI02_A) RH metrics that are used to predict AGBD (Dubayah et al.,
2020b). The first release of the GEDI level-4A (GEDI04_A) data product is based on Version 1
of GEDI02_A (Dubayah et al., 2020b), and uses one of six algorithm setting groups to interpret
the received waveform and identify the elevation of the lowest mode (Hofton and Blair, 2020). The Version 1 of GEDI04_A uses linear statistical models selected from an ensemble of
candidates that predict AGBD as a function of one or more RH metrics. GEDI04_A models are a
required input to the 1 km GEDI level-4B (GEDI04_B) AGBD data product (Patterson et al.,
2019).
2. HISTORICAL PERSPECTIVE
Estimating AGBD using remote sensing requires aboveground biomass, 𝑀!, for a sample
of trees that has been computed using an allometric model in a fixed area, such as a field-
inventory plot or lidar footprint. Summing the 𝑀! over all individuals in the plot or footprint and
expressing it per unit ground area produces an estimate of AGBD. Coincident remote sensing
data are used to develop an empirical relationship between AGBD and a remotely sensed
measurement. This relationship can then be used to predict AGBD using remotely sensed data
(Drake et al., 2002; Lefsky et al., 2002).
```

#### r4 — score 0.532

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 2
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 2
- **matched_tokens:** ['agbd', 'footprint', 'gedi']

**Full text:**

```
biomass density (AGBD) data product. The GEDI04_A data product contains estimates of AGBD
for individual GEDI footprints and associated prediction intervals. The algorithm uses GEDI02_A
relative height (RH) metrics and 13 linear models to predict AGBD in 32 combinations of plant
functional type (PFT) and world region within the observation limits of the ISS. GEDI04_A
models for the release 1 and release 2 data products were developed using 8,587 quality-
filtered simulated GEDI waveforms associated with field estimates of AGBD in 21 countries. Although this is the most geographically comprehensive data available for the development of
AGBD models using lidar remote sensing, important regions are underrepresented, including
the forests of continental Asia, deciduous broadleaf forests and savannas of the dry tropics, and
evergreen broadleaf forests north of Australia. We describe the scientific and mathematical
assumptions required to develop globally representative estimates of AGBD using GEDI lidar,
including generalization beyond training data, and exclusion of GEDI02_A observations that do
not meet requirements of the GEDI04_A algorithm. The footprint-level predictions generated
by this process provide globally comprehensive estimates of AGBD. These footprint-level
predictions are a prerequisite for the GEDI GEDI04_B gridded AGBD data product. Plain language summary / significance:
The amount of carbon stored in aboveground vegetation is uncertain.
```

#### r5 — score 0.504

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 1
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 1
- **matched_tokens:** ['footprint', 'gedi', 'l4a']

**Full text:**

```
Algorithm Theoretical Basis Document (ATBD)
for
GEDI Level-4A (L4A) Footprint Level Aboveground
Biomass Density
James R. Kellner1,2, John Armston3, Laura Duncanson3
1 Institute at Brown for Environment and Society, Brown University, Providence RI
2 Department of Ecology, Evolution and Organismal Biology, Brown University,
Providence RI
3 Department of Geographical Sciences, University of Maryland, College Park MD
Version 1.0
Release date: August 11th, 2021
University of Maryland, College Park MD
Authors: Principal Investigator:
________________________________ ________________________________
________________________________
________________________________
```

---

