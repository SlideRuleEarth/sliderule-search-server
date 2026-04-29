# Row 16 results: docsearch / example

> Auto-generated. Open this file alongside `16-how-to-subset-atl24-bathymetry-data-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to subset atl24 bathymetry data`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `atl24x`
  - `5. atl24`
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: assets/atl24_access.html removed; user_guide section on atl24x is closest substitute

---

## 📚 docsearch results (top 5)

#### r1 — score 0.689

- **url:** https://docs.testsliderule.org/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r2 — score 0.580

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `developer_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r3 — score 0.675

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
The SlideRule atl24x endpoint provides a service for ATL24 subsetting and custom processing. This endpoint queries ATL24 input granules for bathymetry data for ATL03 photons based on geographic and temporal ranges. ATL24 provides bathymetry labels and metrics which are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling.
```

#### r4 — score 0.602

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.4 ATL24 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
If ATL24 classification parameters are specified, the ATL24 (bathymetry) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=-1 (dynamic) and cnf=-1 (no native filtering) should be specified to allow all ATL24 photons to be used. atl24 class_ph : list of ATL24 classifications used to select which photons are used in the processing (the available classifications are: âbathymetryâ, âsea_surfaceâ, âunclassifiedâ) Note ATL24 is typically a release behind the ATL03 standard data product which it is based on. In order to correlate ATL24 classifications to ATL03, a release of ATL03 must be selected that has a corresponding ATL24 release.
```

#### r5 — score 0.536

- **url:** https://docs.testsliderule.org/developer_guide/articles/atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Statistics
- **category:** `developer_guide`
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
452,173 ATL03 granules were processed (constituting cycles 1 through 25). 277,255 ATL24 granules were produced 145,283 processing runs resulted in empty output (no bathymetry was identified) and therefore no ATL24 granule was produced 29,635 processing runs failed to produce a valid result 27.649 TB of ATL24 data was produced 989.46 B photons were classified 59.19% of classified photons were sea surface 0.73% of classified photons were bathymetry
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.654

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Introduction
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 10
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
This new product, ATL24, will provide
automated bathymetry extraction, sea surface/wave parameters, and water column statistics
in all regions that provide adequate conditions for probable measurements. In contrast to
other ATLAS data products that were designed pre-launch, a great benefit to the ATL24
development effort is the opportunity to learn from and leverage the great wealth of ICESat-2
bathymetry studies that have been published over the past six years.
3
```

#### r2 — score 0.597

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 17
- **matched_tokens:** ['atl24', 'bathymetry', 'data', 'subset']

**Full text:**

```
Table 2: ATL24 input variables and processing details within each stage of the product production
Stage Processing Input Products
ATL24.g - accept an incoming Client Request ATL03 granule name HTTP request
Global Bathymetry Mask - a
shapefile capturing all areas where ATL03/09 Granule Reader there is bathymetry detectable by - subset granules to bathymetry ICESat-2 Input Data and mask
Data Configura- ATL03 Granule - ICESat- tion Photon Filtering - option- 2 standard data product h5 file ally filter photons based on
certain fields (e.g. quality_ph) ATL09 Granule - ICESat-
2 standard data product h5 file
CoastNet
ICESat-2 inputs Photon Classi- Quantile Trees fiers: Sea surface Trained ML models
OpenOceans++
CoastNet
Quantile Trees ICESat-2 inputs
C-SHELPH Trained ML models Photon Classi-
fiers: Seafloor OpenOceans++ Sea Surface - some classifi-
cation algorithms require an
BathyPathFinder initial estimate of sea surface
Median Filter
10
```

#### r3 — score 0.575

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Output Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 19
- **matched_tokens:** ['atl24', 'bathymetry', 'data', 'subset']

**Full text:**

```
Table 3: ATL24 component input for processing pipeline
Item Description
ATL03 Granule ATLAS/ICESat-2 Level 2a global geolocated photon data
ATLAS/ICESat-2 Level 3a calibrated backscatter profiles and at- ATL09 mopsheric layer characteristics
Global Used to spatially subset the ATL03/ATL09 granules prior to initi-
Bathymetry ating the ATL24 workflow.(Note: this is also referred to internally
Mask as the “search mask”)
NOAA product from the Visible Infrared Imaging Spectrometer to
VIIRS Kd490 provide a diffuse attenuation coefficient at 490 nm to the uncertainty
calculation.
Generated by an offline Monte Carlo simulation; used with turbidity, Uncertainty windspeed (ATL09), and photon depth to generate vertical and Look up Table horizontal subaqueous geolocation uncertainty.
Global data product using a seasonal value using temperature and
salinity data from the E.U. Copernicus 2022 Multi Observation Refractive Index Global Ocean 3D Temperature Salinity Height Geostrophic Current
and MLD dataset datasets
4.3 ATL24 Output Variables
Table 4: ATL24 output variables for each stage of the product production
Stage of Origin Output Variables
12
```

#### r4 — score 0.578

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Data Workflow
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 12
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

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

#### r5 — score 0.558

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['atl24', 'bathymetry', 'data']

**Full text:**

```
used alone or in combination with total propagated uncertainty (TPU) values to filter the
data. Figure 1: ATL24 flow diagram of computational architecture
3.2 Data Dissemination
The implementation architecture chosen for ATL24 r001 will follow the standard approach for
the dissemination of the ICESat-2 mission products through the National Snow and Ice Data
Center (NSIDC). However, in the last few years NSIDC has pushed the products to the cloud
for modernized access to the data, which will be an additional pathway to ATL24 data access
for the scientific community. Both means of access will provide capabilities for geographical
and temporal sub-setting to the user. Additionally, for ATL24 specifically, there is also a
planned, parallel capacity for allowing on-demand and customized, science-ready bathymetry
product from ATL03 granules via SlideRule, a public web application programming interface
(API) for processing of science data in the cloud (Shean et al. 2023). ATL24 will eventually
present a family of data products, which collectively will be referred to as ATL24.x. This
ATBD describes the version referred to as the ”gold standard” version, ATL24.g, hosted by
NSIDC and available in Earthdata cloud, with the metadata for the granules registered in
NASA’s Common Metadata Repository (CMR).
```

---

