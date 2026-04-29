# Row 41 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `41-atl06-data-groups-structure-for-land-ice-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL06 data groups structure for land ice`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATL06-specific; must not return ATL03 chunks

---

## 📚 docsearch results (top 5)

#### r1 — score 0.478

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['data', 'groups', 'land', 'structure']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r2 — score 0.592

- **url:** https://docs.slideruleearth.io/assets/grandmesa.html
- **title:** Generating a Custom ATL06 over Grand Mesa, CO
- **section:** Generating a Custom ATL06 over Grand Mesa, CO
- **category:** `tutorial`
- **matched_tokens:** ['atl06', 'data']

**Full text:**

```
Process ATL03 data from the Grand Mesa, CO region and produce a customized ATL06 dataset.
```

#### r3 — score 0.496

- **url:** https://docs.slideruleearth.io/background/NASA-Earthdata.html
- **title:** NASA Earthdata
- **section:** NSIDC
- **category:** `background`
- **matched_tokens:** ['data', 'ice']

**Full text:**

```
The National Snow and Ice Data Center (NSIDC) DAAC provides data and information for snow and ice processes, particularly interactions among snow, ice, atmosphere, and ocean, in support of research in global change detection and model validation. If any problems contact NSIDC support at nsidc @ nsidc . org or the NASA EOSDIS support team support @ earthdata . nasa . gov .
```

#### r4 — score 0.482

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['ice', 'land']

**Full text:**

```
Using the Python client, this service is called via: sliderule . run ( 'atl08x' , parms ) The default resulting DataFrame from this endpoint contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) land_ice_segments/ground_track/x_atc y_atc Across track distance meters (float) land_ice_segments/ground_track/y_atc segment_id_beg First ATL03 segment used in ATL08 100m segment count land_segments/segment_id_beg segment_landcover UN-FAO Land Cover Surface type classification as reference from Copernicus Land Cover(ANC18) at the 100m resolution land_segments/segment_landcover segment_snowcover Daily snow/ice cover from ATL09 at the 25 Hz rate(275m) indicating likely presence of snow and ice within each segment 0: ice free water; 1: snow free land; 2: snow; 3: ice land_segments/segment_snowcover n_seg_ph Number of photons within each land segment count land_segments/n_seg_ph solar_elevation Solar elevation at time of measurement degrees (float) land_segments/solar_elevation terrain_slope Along-track slope of the terrain meters (float) land_segments/terrain/terrain_slope n_te_photons Number of terrain (ground) photons count land_segments/terrain/n_te_photons h_te_uncertainty Uncertainty of height of terrian meters (flo
```

#### r5 — score 0.448

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl06', 'data', 'ice', 'land']

**Full text:**

```
The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of segments for each beam. In SlideRule the average segment elevations will not be corrected for transmit pulse shape biases or first photon biases as compared to the higher level data products.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.727

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 53
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 53
- **matched_tokens:** ['atl06', 'data', 'groups', 'ice', 'land']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
929 4 ATL06 DATA PRODUCT DESCRIPTION
930 Here we describe how the parameters appear in the ATL06 product. The ATL06 parameters are
931 arranged by beam, and within each beam in a number of groups and subgroups. Where
932 parameter descriptions in the ATL06 data dictionary are considered adequate, they are not
933 repeated in this document.
934 4.1 Data Granules
935 ATL06 data are provided as HDF5 files. The HDF format allows several datasets of different
936 spatial and temporal resolutions to be included in a file. ATL06 files contain data primarily at the
937 single-segment resolution, divided into different groups to improve the conceptual organization
938 of the files. Each file contains data from a single cycle and a single RGT.
939 Within each file there are six top-level groups, each corresponding to data from GT: gt1l, gt1r,
940 gt2l, etc. The subgroups within these gtxx groups are segment_quality, land_ice_segments, and
941 residual_histogram.
942 In the segment_quality group, the data are nearly dense, providing signal-selection and location
943 information for every segment attempted (i.e. those that contain at least one ATL03 PE) in the
944 granule, at the 20-meter along-track segment spacing.
```

#### r2 — score 0.704

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **title:** ATLAS/ICESat-2 L3A Land Ice Height
- **section:** 1.2.4.5 quality_assessment
- **category:** `user_guide`
- **source_product:** `ATL06` · **page:** 9
- **matched_tokens:** ['atl06', 'data', 'groups', 'ice', 'land']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land Ice Height, Version 6
The following sections summarize the contents of the data groups and certain parameters of
interest. Data groups are described in detail in "Section 4 | ATL06 Data Product Description" in the
ATBD for ATL06. A complete list of parameters is available in the ATL06 Data Dictionary.
1.2.4.1 METADATA
ISO19115 structured metadata with sufficient content to generate the required geospatial
metadata.
1.2.4.2 ancillary_data
Ancillary information such as product and instrument characteristics and/or processing constants. Data in this group pertain to the granule in its entirety.
1.2.4.3 gt1l–gt3r
Each ground track group (six in all) contains three subgroups:
• land_ice_segments: contains primary ATL06 derived parameters, e.g., land-ice height
(h_li), latitude, longitude, standard error, and quality measures. Heights represent the
mean surface height, averaged along 40 m segments of ground track spaced 20 m apart,
for each of ATLAS’s six beams. Data are only provided for segment pairs for which at least
one beam has a valid land-ice height measurement. Each reported height has a
corresponding segment ID (stored in segment_ID), which indicates the second of the two
20 m ATL03 segments used to generate the 40 m ATL06 height segment.
• residual_histogram: contains histograms of the residuals between photon event heights
and the least-squares fit segment heights.
```

#### r3 — score 0.713

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.4.6 Dimension Scales
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 9
- **matched_tokens:** ['data', 'groups', 'land', 'structure']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
The following sections summarize the structure and primary variables of interest in ATL08 data
files. Additional details are available in "Section 2 | ATL08 Data Product" of the ATBD for ATL08. A
complete list of parameters is available in the ATL08 Data Dictionary.
1.2.4.1 METADATA
ISO19115 structured metadata with sufficient content to generate the required geospatial
metadata.
1.2.4.2 ancillary_data
Information that is ancillary to the data product. This may include product characteristics,
instrument characteristics and/or processing constants. This group also contains the /land/
subgroup, which houses constants specific to the land/vegetation product.
1.2.4.3 gt1l–gt3r
Six gt[x] groups, each of which contains the parameters for one of the six ATLAS ground tracks. Each gt[x] top-level group contains the following subgroups:
• /land_segments/ contains parameters related to 100 m land segments. Key parameters
include time, latitude, and longitude of the centermost signal photon; the number of signal
photons in the segment (n_seg_ph); a night flag; land, snow, and water masks; and
descriptive statistics.
```

#### r4 — score 0.706

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 55
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 55
- **matched_tokens:** ['atl06', 'ice', 'land', 'structure']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
A value of 3 indicates that all
algorithms failed.
984
985 4.2.1 Signal_selection_status subgroup
986 This subgroup includes the Signal_selection_status_confident, Signal_selection_status_all, and
987 Signal_selection_status_backup parameters. Their values are described in Table 3-2. Its density
988 structure matches that of the segment_quality group.
989
990 4.3 Land_ice_segments group
991 The primary set of derived ATL06 parameters are given in the land_ice_segments group (Table
992 4-2). This group contains geolocation, height, and standard error and quality measures for each
993 segment. This group is sparse, meaning that parameters are provided only for pairs of segments
994 for which at least one beam has a valid surface-height measurement.
```

#### r5 — score 0.634

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 53
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 53
- **matched_tokens:** ['atl06', 'data', 'groups', 'structure']

**Full text:**

```
Datasets in this group can be used to check
945 the geographic distribution of data gaps in the ATL06 record.
946 In the land_ice_segments group, data are sparse, meaning that values are reported only for those
947 pairs for which adequate signal levels (i.e. more than 10 PE, snr_significance > 0.05) were found
948 for at least one segment: This means that within each pair, every dataset has the same number of
949 values, and that datasets are pre-aligned between pairs, with invalid values (NaNs) posted where
950 the algorithm provided a value for only one beam in a pair. Conversely, if neither beam in a pair
951 successfully obtained a value for h_li, that segment is skipped for both beams in the pair. The
952 segment_id, timing, and geolocation fields for the valid segments should allow the along-track
953 structure of the data to be reconstructed within these sparse groups.
```

---

