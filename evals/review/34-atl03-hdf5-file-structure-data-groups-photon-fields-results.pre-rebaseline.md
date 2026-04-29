# Row 34 results: nsidc / variable_lookup

> Auto-generated. Open this file alongside `34-atl03-hdf5-file-structure-data-groups-photon-fields-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 HDF5 file structure data groups photon fields`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **expected_sections:**
  - `data groups`
  - `file contents`
  - `file structure`
- **expected_pages:** (none)
- **notes:** ATL03 user guide HDF5 structure

---

## 📚 docsearch results (top 5)

#### r1 — score 0.684

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/ancillary_fields.html
- **title:** Including Ancillary Fields
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'data', 'fields', 'file', 'hdf5', 'photon']

**Full text:**

```
The ATL03 granules include data associated with the photons in different subgroups inside the HDF5 file. SlideRule currently supports including ancillary fields from three subgroups inside those granules: gtxx/geolocation gtxx/geophys_corr gtxx/heights When an atl03sp or at06p processing request specifies ancillary fields, SlideRule reads those fields from the ATL03 granules, subsets them to the region of interest, and correlates them to the dynamically generated photon segment (called and âextentâ in the code) they belong to. The result is a GeoDataFrame with a column for each ancillary field populated by the value associated with each photon for atl03sp requests, and elevation for atl06p requests. Note, including ancillary fields in a processing request will increase the amount of time it takes for the request to be processed, and also the amount of data returned, so it should only be used when the fields are needed by the end user.
```

#### r2 — score 0.556

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'data', 'file', 'groups', 'photon', 'structure']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r3 — score 0.585

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.4 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'data', 'fields', 'photon']

**Full text:**

```
The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable (atl03_ph_fields), a per-segment variable (atl03_geo_fields, atl03_corr_fields), or a rate variable (atl03_bckgrd_fields). Ancillary fields are used to specify additional fields in the ATL03, ATL08, and ATL09 granules to be returned with the photon extent and dowstream customized products. Each field provided by the user will result in a corresponding column added to the returned GeoDataFrame. Note: if a field is requested that is already present in the default GeoDataFrame, then the name of both fields will be changed to include a _x suffix for the default incusion of the field, and a _y for the ancillary inclusion of the field.
```

#### r4 — score 0.562

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl03s
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'data', 'hdf5', 'photon']

**Full text:**

```
sliderule.icesat2. atl03s ( parm , resource ) [source] Subsets ATL03 data given the polygon and time range provided and returns segments of photons Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : ATL03 extents (see Photon Segments ) Return type : GeoDataFrame
```

#### r5 — score 0.555

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl03v
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'data', 'hdf5', 'photon']

**Full text:**

```
sliderule.icesat2. atl03v ( parm , resource ) [source] Subsets ATL03 data given the polygon and time range provided and returns counts of photons in segments Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : ATL03 extents (see Photon Segments ) Return type : GeoDataFrame
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.516

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.2.5 HDF5 Dataset Information
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 197
- **matched_tokens:** ['atl03', 'data', 'fields', 'file', 'hdf5']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
possible that the resulting TEP histogram will have non-zero bin counts between the primary and
secondary TEP return regions. We therefore suggest the following checks before a higher-level
algorithm uses the TEP:
(a) If the TEP histogram is to be used as a proxy for the system impulse response
function, we recommend using the region between 15 and 30 nanoseconds to avoid the
secondary TEP return.
(b) if the primary TEP return has a full-width at half max value greater than 3
nanoseconds, we recommend not using this particular realization of the TEP as a proxy for the
system impulse response. With sufficient on-orbit TEP data, we intend to refine these guidelines to automate rejection of
spurious TEP realizations.
10.2.5 HDF5 Dataset Information
Dataset are the primary data storage containers within a HDF5 file. A dataset contains either a
scalar or (more likely) homogeneous arrays of data. Datasets, like Attributes, are assigned a
datatype. In addition, there are several different storage methodologies used for efficiently
storing the data. Designer creates 'empty' datasets. This allows Designer to focus generically on
the organization of the data product and leave the heavy data processing to external science
software. ICESat-2 datasets, by default, include a set of standard attributes corresponding to selected CF
convention parameter-level metadata fields.
```

#### r2 — score 0.552

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.4 ATL03 Data Structure for Each Ground Track
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 26
- **matched_tokens:** ['atl03', 'data', 'groups', 'photon', 'structure']

**Full text:**

```
The smaller
downlinked photon bandwidth (telemetry bandwidth) is generally not sufficient to generate a
robust estimate of the background count rate, but can be used if the atmospheric histograms are
not available. Section 8.0 describes data quality and browse products. Section 9.0 summarizes the metadata groups in the ATL03 data product. The appendices contain the table of inputs and outputs for ATL03, and the ICESat-2 ATBD
lexicon, which aims to define the most commonly used terms within the ATBDs.
2.4 ATL03 Data Structure for Each Ground Track
In accordance with the HDF-driven structure of the ICESat-2 products, the top level ‘Group’
provides the syntax and structure for all the elements of the ATL03 product. Subsequent
subsections of the ATL03 data product will characterize each of the six ground tracks associated
with each reference ground track for each cycle and orbit number (see Appendix C – ATBD
Lexicon). Each ground track has a different beam number and distance from the reference track,
but all beams will be processed using the same sequence of steps within ATL03, except where
noted otherwise. The subsections below summarize the parameters contained within each group
and subgroup of the ATL03 product. The ATL03 output data product table is provided in
Appendix A. Along-track time in each group is provided by a parameter called delta_time.
```

#### r3 — score 0.522

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 9.0 METADATA
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 159
- **matched_tokens:** ['atl03', 'data', 'hdf5', 'photon', 'structure']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
9.0 METADATA
The following metadata structure is planned for the ATLAS data within this product:
1) HDF structure overview
2) Each of the six ATLAS ground tracks (GT) have common data
• reference ground track and cycle number
• instrument performance / status parameters
• background photon counts
• signal finding algorithm (section 5.1.4) and associated quality assessment
statistics
• geolocation assessment (those parameters common to all beams, such as orbit)
• geophysical corrections (section 6.0)
3) Associated metadata for all ground tracks
4) Associated ancillary data for all ground tracks
This version of ATL03 incorporates lessons learned from the GLAS_HDF development process. The development team has incorporated code written for the GLAS_HDF effort into the ATLAS
codebase to 1) ensure CF-compliance, 2) to make the ATLAS products NetCDF-compatible, and
3) provide necessary metadata in accordance with current standards
(https://earthdata.nasa.gov/about-eosdis/requirements). The ATL03 product design continues to
evolve and we welcome comments on the design of the HDF5 files. In ATL03, attributes (rather than datasets) are used for non-science data parameters because of
HDFGroup recommendations. Attributes are significantly more efficient for containing small
amounts of data. The primary information affected by this change is metadata and ancillary data.
```

#### r4 — score 0.525

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.4.1 METADATA
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 8
- **matched_tokens:** ['atl03', 'data', 'groups', 'photon', 'structure']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
Table 2. ATLAS/ICESat-2 Granule Boundaries and Region Numbers
Region Latitude Bounds Region Latitude Bounds
# #
01 Equator → 27° N (ascending) 08 Equator → 27° S (descending)
02 27° N → 59.5° N (ascending) 09 27° S → 50° S (descending)
03 59.5° N → 80° N (ascending) 10 50° S → 79° S (descending)
04 80° N (ascending) → 80° N 11 79° S (descending) → 79° S
(descending) (ascending)
05 80° N → 59.5° N (descending) 12 79° S → 50° S (ascending)
06 59.5° N → 27° N (descending) 13 50° S → 27° S (ascending)
07 27° N (descending) → Equator 14 27° S → Equator (ascending)
1.2.4 Data Groups
Within data files, similar variables such as science data, instrument parameters, altimetry data, and
metadata are grouped together according to the HDF model. ATL03 data files contain the top-level
groups shown in Figure . Heights, times, latitudes, and longitudes for individual photons are stored
in the /heights group within each ground track group. Figure 4. Top-level data groups for an ATL03 granule as
displayed in HDFView. Individual photon heights, times, latitudes,
and longitudes for each ground track (1L–3R) are stored in the
corresponding gt1l–gt3r/heights data group, along with other
ground-track related parameters. The following sections summarize the structure and primary variables of interest in ATL03 data
files. Additional details are available in Section 2 and Appendix A of the ATL03 ATBD.
```

#### r5 — score 0.510

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.4.5 gt1l–gt3r
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 9
- **matched_tokens:** ['atl03', 'data', 'groups', 'hdf5', 'photon']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
ISO19115 structured metadata with sufficient content to generate the required geospatial metadata
(ATL03 ATBD | Section 2.4.9).
1.2.4.2 ancillary_data
Parameters related to ATLAS that provide insight about the instrument transmit pulse, optics,
receiver sensitivity, etc. These parameters are needed by higher level products and are generally
passed to ATL03 from the ICESat-2 Science Unit Converted Telemetry product, ATL02 (ATL02
and ATL03 ATBDs Sections 2.4.3–2.4.6).
1.2.4.3 atlas_impulse_response
Parameters needed by higher level data products that require knowledge of the ATLAS system
impulse-response function to account for how the ATLAS system impacts ground return statistics
(ATL03 ATBD | Section 2.4.2).
1.2.4.4 Dimension Scales
Two HDF5 dimension scales are stored at the top level alongside the data groups:
• ds_surf_type: dimension scale indexing the surface type array
(gt[x]/geolocation/surf_type)
• ds_xyz: dimension scale indexing the X-Y-Z components of the spacecraft velocity (east
component, north component, up component) an observer on the ground would measure
(gt[x]/geolocation/velocity_sc)
1.2.4.5 gt1l–gt3r
Six gt[x] groups, each of which contains the parameters for one of the six ATLAS ground tracks
including height above the WGS 84 ellipsoid, time, latitude, and longitude for individual photons
(ATL03 ATBD | Section 2.4.1).
```

---

