# Row 21 results: docsearch / version_history

> Auto-generated. Open this file alongside `21-recent-changes-to-atl06x-release-notes-review.md` —
> verdicts go there, this side is read-only.

**Query:** `recent changes to atl06x release notes`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-03-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** atl06x mentioned in v05-00-00 and v05-03-00

---

## 📚 docsearch results (top 5)

#### r1 — score 0.466

- **url:** https://docs.slideruleearth.io/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** 2025-12-08: Public Cluster Release v5
- **category:** `developer_guide`
- **matched_tokens:** ['changes', 'notes', 'release']

**Full text:**

```
Note Version 5.0 of SlideRule has been officially released. The changes include an overhaul of the private clusters, consistent ATL13 query formats, ATL24 release 002, improved earthdata error handling, and h5p slice support. See release notes for full details.
```

#### r2 — score 0.472

- **url:** https://docs.slideruleearth.io/developer_guide/articles/v5_server_release.html
- **title:** 2025-12-08: Public Cluster Release v5
- **section:** TL;DR
- **category:** `developer_guide`
- **matched_tokens:** ['changes', 'release']

**Full text:**

```
ps.slideruleearth.io has been retired and replaced by provisioner.slideruleearth.io There are breaking changes (which will hopefully be minimal because they involved features that have been deprecated for some time) ATL24 release 002 is now the default The internal Asset Metadata Service is used for ATL24, ATL13, and 3DEP (only when specified) Earthdata error reporting was made more intuitive h5p supports slices Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.474

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-11-00.html
- **title:** Release v4.11.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['changes', 'release']

**Full text:**

```
v4.11.0 - The official release of the SlideRule Web Client at https://client.slideruleearth.io v4.11.0 - The atl03x endpoint is being previewed. This implements a dataframe model for the data instead of a streaming model. v4.11.0 - The atl24x endpoint provides subsetting support for the ATL24 standard data product.
```

#### r4 — score 0.398

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **title:** Release v5.0.x
- **section:** New Functionality
- **category:** `release_notes`
- **matched_tokens:** ['atl06x', 'release']

**Full text:**

```
Rate limiting and endpoint metrics are now handled the SlideRule Intelligent Load Balancer . v5.0.3 - #552 - Ancillary field requests now support multidimensional data. v5.0.3 - #553 - Added x-series APIs for ATL06 ( atl06x ) and ATL08 ( atl08x ) v5.0.3 - #562 - Serial-mode raster sampling has been removed. v5.0.3 - #564 - Added x-series APIs for GEDI04A ( gedi04ax ), GEDI02A ( gedi02ax ), and GEDI01B ( gedi01bx ) v5.0.2 - ATL24 uses release 002 by default, which uses the internal Asset Metadata Service (AMS). v5.0.2 - #549 - h5p now supports slices. v5.0.2 - earthdata.py is no longer a standalone implementation of an interface to CMR and TNM, but instead makes a request to the SlideRule cluster to execute the server-side implementations in earth_data_query.lua . This consolidates the interface to these services in one place, and also provides a consistent interface between the web and Python clients. v5.0.2 - Added the 3dep1m asset which accesses the same USGS 3DEP data product but uses the internal AMS service for STAC queries. This is an attempt to alleviate issues with inconsistent availability and functionality in The National Map (TNM) service which made using 3DEP difficult.
```

#### r5 — score 0.465

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-02-00.html
- **title:** Release v5.2.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['changes', 'release']

**Full text:**

```
v5.2.0 - ATL09 and ATL13 supported release updated to 007 v5.2.1 - Various fixes/improvements for authenticator v5.2.1 - AMS update to support latest version of DuckDB (changes in spatial functionality)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.510

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.5 Goals of ICESat-2 Inland Water Body Height Data Products
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 27
- **matched_tokens:** ['recent', 'release']

**Full text:**

```
Also note that the ATL22 level L3B companion product containing the means of the ATL13
along-track products are co-developed developed and reported in a separate ATBD entitled
“Mean Inland Surface Water Data (ATL22)”, with its own release versions, currently Release 4
as of 20. The difference between the along track ATL13 products and the mean ATL22 products
is graphically illustrated in Figure 1-1 below. This ATL13 ATBD includes background (Chapter 2), details of the theoretical underpinnings of
the algorithms together with their testing on ATLAS or ATLAS prototype data (Chapters 3 and
4), a list of the specific ATL13 output product tables (Chapter 5), and several calibration and
validation background and opportunities (Chapter 6). Since this ATBD is refined over time due
to improvement to the algorithms, a summary of the principal updates to each version or release
is also provided in the Change Log and in Chapter 1. The complete documentation of the ATL13 product including the most recent version of this
ATL13 ATBD, Data Product Known Issues, and data acquisition, are available at link
https://nsidc.org/data/atl13.
1.5 Goals of ICESat-2 Inland Water Body Height Data Products
The Inland Water Body Height Data Product is computed as part of an integrated set of six
ICESat-2 geophysical products that also include ice sheets, sea ice, atmosphere, vegetation
structure and oceans.
```

#### r2 — score 0.421

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.7 Other ATLAS and Spacecraft Parameters
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 151
- **matched_tokens:** ['changes', 'release']

**Full text:**

```
Changes in detector side generate a break in ATL03 data, so we do not expect the detector side
to change during a granule.
7.7 Other ATLAS and Spacecraft Parameters
There are a number of other ATLAS and spacecraft parameters that are not associated with the
sections above. These are described here along with their location on the ATL03 data product.
135 Release Date: Fall 2022
```

#### r3 — score 0.469

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 4 Version History
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 22
- **matched_tokens:** ['changes']

**Full text:**

```
This update represents the best estimates of height uncertainty for
a reference photon in on-orbit data.
• Changed data type for ph_id_count to an unsigned 1-byte integer (bug fix). Prior releases
of ATL03 stored the value as a signed datatype, limiting the reported value to 127.
• Changed the geographic extent metadata from a predicted orbit path to a geodetic
polygon, providing better information on where ATL03 data exist for spatial queries.
• Updated the ANC42 TEP reference file to reflect changes in the ATL02 time-of-flight (TOF)
calculations stemming from calibration file updates. The updated reference TEPs allow the
appropriate TEPs passing QA to be written from ANC41 to ATL03 files.
• ATL03 V6 encompasses several updates affecting photon heights (h_ph), particularly
changes in the TOF calibrations, zero-range point, and range bias correction. The time and
temperature dependent range bias correction was first introduced in V5 but applied with an
incorrect sign. This was fixed in V6. The mean offset between the pre-launch (V5) and
post-launch (V6) zero range point is about -4 cm (V6 is ~4 cm lower than V5) and varies by
spot and strength. Table 6 below shows spot-specific mean offsets and standard
deviations. Page 21 of 22National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.403

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.2.1 ATLAS Start Pulse Detector
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 132
- **matched_tokens:** ['changes', 'release']

**Full text:**

```
While it is not possible to characterize the ATLAS impulse-
response function on-orbit for every transmitted laser pulse, this section presents an estimate of
this function derived from on-orbit data. These data are grouped into two categories (and
associated subgroups): pulse energy and impulse-response. The transmitted pulse energy will primarily vary due to the variable laser transmitter output, at
least over short (less than six month) timescales. We do not expect significant impact from
changes in the transmit optical path, though efficiency changes are possible over the life of the
mission (e.g. due to cumulative contamination). The ATLAS instrument has several methods of monitoring the output laser energy which are
described in Section 5.2.1 and Section 5.2.2 of ATL02. ATL03 makes use of the transmit energy
116 Release Date: Fall 2022
```

#### r5 — score 0.295

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 176
- **matched_tokens:** ['recent', 'release']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
tep_hist_time DOUBLE TEP histogram seconds The times associated with the
time TEP histogram bin centers,
measured from the laser
transmit time.
reference_tep_ INTEGER_ Reference TEP n/a A flag that indicates the
flag 1 Flag reference TEP has been used in
place of a more recent TEP
realization. Value = 1 when
reference TEP has been
applied.
/ancillary_data Contains information ancillary to the data product. This may
include product characteristics, instrument characteristics,
and/or processing constraints.
atl03_pad DOUBLE padding for seconds Seconds of padding data Control
ATL03 needed for ATL03 processing
processing
atlas_sdp_gps_ DOUBLE ATLAS epoch seconds Number of GPS seconds
epoch offset between the GPS epoch (1980-
01-06T00:00:000000Z UTC) and
the ATLAS standard data
product (SDP) epoch (2018-01-
01:T00.00.00.000000 UTC). Add this value to delta_time
parameters to compute full
gps_seconds (relative to GPS
epoch) for each data point.
control STRING control file n/a PGE-specific control file used to
generate a specific granule of
ATL03 data.
```

---

