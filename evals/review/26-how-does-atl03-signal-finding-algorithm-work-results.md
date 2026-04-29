# Row 26 results: nsidc / algorithm

> Auto-generated. Open this file alongside `26-how-does-atl03-signal-finding-algorithm-work-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does ATL03 signal finding algorithm work`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `signal finding`
  - `signal-finding`
- **expected_pages:** (none)
- **notes:** ATL03 ATBD Signal Finding chapter

---

## 📚 docsearch results (top 5)

#### r1 — score 0.463

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'signal']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r2 — score 0.546

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5.2 ATL06-SR Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03']

**Full text:**

```
Ancillary data returned from the fit algorithm (as well as atl06 and atl06p APIs) come from the ancillary fields specified for ATL03, but instead of being returned as-is, they are processed using the ATL06 least-squares-fit algorithm, and only the result is returned. In other words, ancillary data points from ATL03 to be included in an ATL06-SR result are treated just like the h_mean, latitude, and longitude variables, and returned as a fitted double-precision floating point value.
```

#### r3 — score 0.413

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'signal']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r4 — score 0.429

- **url:** https://docs.testsliderule.org/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl08
- **category:** `api_reference`
- **matched_tokens:** ['algorithm', 'atl03']

**Full text:**

```
sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame
```

#### r5 — score 0.460

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.462

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** List of Tables
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 16
- **matched_tokens:** ['algorithm', 'atl03', 'finding', 'signal']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
List of Tables
Table Page
Table 5-1. Input Variables for Photon Classification Algorithm. ................................................. 55
Table 5-2. Parameters Needed to Drive the Algorithm; Input Parameters. .................................. 61
Table 5-3. Parameters Calculated Interally Within the Algorithm. .............................................. 66
Table 5-4. Parameters Output from Signal Finding Algorithm. ................................................... 66
Table 6-1. Table of Geophysical Corrections and Reference Model Sources for ICESat-2. ..... 101
Table 6-2. Ocean Tidal Models Currently Available.................................................................. 104
Table 6-3. Performance Order of Tide Models Based on RSS over Main Constituents ............ 104
Table 7-1. Transmitted Pulse Energy Parameters. ...................................................................... 118
Table 7-2. Transmit Pulse Parameters. ....................................................................................... 119
Table 7-4. Altimetric Histogram Parameters. ............................................................................. 128
Table 7-5. Table to relate ph_id_channel to a photon’s path through ATLAS. ......................... 130
Table 7-6. Beam mapping when sc_orient == 1 (forward). ....................................................... 131
Table 7-7.
```

#### r2 — score 0.581

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['atl03', 'finding', 'signal']

**Full text:**

```
Once the signal photons have been identified by DRAGANN,
they are combined with the coarse signal finding output from ATL03. This process is described in
detail in "Section 3.1.1 | DRAGANN" in the ATDB for ATL08. Page 14 of 19National Snow and Ice Data Center
nsidc.org
```

#### r3 — score 0.503

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 30
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 30
- **matched_tokens:** ['algorithm', 'atl03', 'finding', 'signal']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
393
Table 3-1 signal_selection_source values
Value Meaning
0 Signal selection succeeded using ATL03 confident-or-
better flagged PE
1 Signal selection failed using ATL03 confident-or-
better flagged PE but succeeded using all flagged
ATL03 PE
2 Signal selection failed using all flagged ATL03 PE,
but succeeded using the backup algorithm
3 All signal-finding strategies failed.
394
395 The signal_selection_source parameter describes the success or failure of each step in this
396 process, and Table 3-1 describes the meaning of each value. For each signal-selection algorithm
397 that was attempted, the signal_selection_status_confident, signal_selection_status_all, and
398 signal_selection_status_backup parameters in the segment_quality group give details of the
399 success or failure of each part of the algorithm. The signal_selection_source parameter is
400 provided for all segments (successful or not) in the segment_quality group, and is provided for
401 segments for which at least one pair has an elevation in the fit_statistics subgroup.
```

#### r4 — score 0.505

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 95
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 95
- **matched_tokens:** ['algorithm', 'atl03', 'finding', 'signal']

**Full text:**

```
1768 4 ALGORITHM IMPLEMENTATION
1769 Prior to running the surface finding algorithms used for ATL08 data products, the
1770 superset of output from the GSFC medium-high confidence classed photons (ATL03
1771 signal_conf_ph: flags 3-4) and the output from DRAGANN will be considered as the input
1772 data set. ATL03 input data requirements include the along-track time, latitude, longitude,
1773 height, and classification for each photon. The motivation behind combining the results
1774 from two different noise filtering methods is to ensure that all of the potential signal
1775 photons for land surfaces will be provided as input to the surface finding software. Prior to
1776 running DRAGANN, reject telemetry bins that occur 150m above or below the reference
1777 DEM. Rejection of these noise blocks will ensure a better parameterization of DRAGANN.
1778 Some additional quality checks are also described here prior to implementing the
1779 ATL08 software. The first check utilizes the POD_PPD flag on ATL03. In instances where
1780 the satellite is maneuvering or the pointing/ranging solutions are suspect, ATL08 will not
1781 use those data. Thus, data will only flow to the ATL08 algorithm when the POD_PPD flag
1782 is set to 0 which indicates ‘nominal’ conditions.
1783 A second quality check pertains to the flags set on the ATL03 photon quality flag
1784 (quality_ph).
```

#### r5 — score 0.477

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 188
- **matched_tokens:** ['algorithm', 'atl03', 'finding', 'signal']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
/ancillary_data/gtx/signal_find Group contains the setup parameters for the signal finding ATL03, Section
_input algorithm. All parameters have dimension of 5,1 5, Table 5-2
corresponding with the 5 different surface types.
alpha_max FLOAT maximum slope radians Maximum slope allowed for ATL03, Section
slant histogram; if larger than 5, αmax
this then don’t attempt to fill
gap.
alpha_inc FLOAT slope increment radians Increment by which the slope is ATL03, Section
varied for slant histogramming 5,
over large gaps. αinc
sig_find_t_inc FLOAT histogram time seconds Time increment the algorithm ATL03, Section
increment uses to step through the 5, Δtime
photon cloud in a granule. Histograms are formed at each
Δtime to identify signal photon
events.
delta_t_gap_min FLOAT minimum delta seconds Minimum size of a time gap in ATL03, Section
time gap the height profile over which to 5, Δtime_gapmin
use variable slope slant
histogramming.
delta_t_lin_fit FLOAT linear fit time seconds Time span over which to ATL03, Section
increment perform a running linear fit to 5, Δt_linfit_edit
identified signal photon events
when editing outliers.
```

---

