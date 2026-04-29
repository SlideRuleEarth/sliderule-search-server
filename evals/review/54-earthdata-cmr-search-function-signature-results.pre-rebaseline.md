# Row 54 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `54-earthdata-cmr-search-function-signature-review.md` —
> verdicts go there, this side is read-only.

**Query:** `earthdata CMR search function signature`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/earthdata.html
- **expected_sections:**
  - `cmr`
  - `search`
  - `earthdata`
- **expected_pages:** (none)
- **notes:** earthdata CMR search

---

## 📚 docsearch results (top 5)

#### r1 — score 0.511

- **url:** https://docs.slideruleearth.io/api_reference/earthdata.html
- **title:** earthdata
- **section:** cmr
- **category:** `api_reference`
- **matched_tokens:** ['cmr', 'earthdata']

**Full text:**

```
sliderule.earthdata. cmr ( short_name = None , version = None , polygon = None , time_start = '2018-01-01T00:00:00Z' , time_end = '2026-04-16T13:45:14Z' , return_metadata = False , name_filter = None ) [source] Query the NASA Common Metadata Repository (CMR) for a list of data within temporal and spatial parameters Parameters : short_name ( str ) â dataset short name as defined in the NASA CMR Directory version ( str ) â dataset version string, leave as None to get latest support version polygon ( list ) â either a single list of longitude,latitude in counter-clockwise order with first and last point matching, defining region of interest (see polygons ), or a list of such lists when the region includes more than one polygon time_start ( str ) â starting time for query in format <year>-<month>-<day>T<hour>:<minute>:<second>Z time_end ( str ) â ending time for query in format <year>-<month>-<day>T<hour>:<minute>:<second>Z return_metadata ( bool ) â flag indicating whether metadata associated with the query is returned back to the user name_filter ( str ) â filter to apply to resources returned by query Returns : files (granules) for the dataset fitting the spatial and temporal parameters Return type : list Examples >>> from sliderule import earthdata >>> region = [ { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 }, ... { "lon" : - 107.7677425431139 , "lat" : 38.90611184543033 }, ... { "lon" : - 107.7818591266989 , "lat" : 39.26613714985466 }, ... { "lon"
```

#### r2 — score 0.401

- **url:** https://docs.slideruleearth.io/api_reference/earthdata.html
- **title:** earthdata
- **section:** search
- **category:** `api_reference`
- **matched_tokens:** ['earthdata', 'search']

**Full text:**

```
sliderule.earthdata. search ( parm , resources = None ) [source] This is the highest-level API call and attempts to automatically determine which service needs to be queried to return the resources being requested. Parameters : parm ( dict ) â request parameters Returns : list of resources to process Return type : list Notes The asset parameter must be supplied Examples >>> from sliderule import earthdata >>> region = [ { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 }, ... { "lon" : - 107.7677425431139 , "lat" : 38.90611184543033 }, ... { "lon" : - 107.7818591266989 , "lat" : 39.26613714985466 }, ... { "lon" : - 108.3605610678553 , "lat" : 39.25086131372244 }, ... { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 } ] >>> parms = { "asset" : "icesat2" , "poly" : region , "cycle" : 20 , "rgt" : 232 } >>> resources = earthdata . search ( parms ) Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.457

- **url:** https://docs.slideruleearth.io/api_reference/earthdata.html
- **title:** earthdata
- **section:** stac
- **category:** `api_reference`
- **matched_tokens:** ['cmr', 'earthdata']

**Full text:**

```
sliderule.earthdata. stac ( short_name = None , collections = None , polygon = None , time_start = '2018-01-01T00:00:00Z' , time_end = '2026-04-16T13:45:14Z' , as_str = True ) [source] Perform a STAC query of the NASA Common Metadata Repository (CMR) catalog for a list of data within temporal and spatial parameters Parameters : short_name ( str ) â dataset short name as defined in the NASA CMR Directory collections ( list ) â list of dataset collections as specified by CMR, leave as None to use defaults polygon ( list ) â either a single list of longitude,latitude in counter-clockwise order with first and last point matching, defining region of interest (see polygons ), or a list of such lists when the region includes more than one polygon time_start ( str ) â starting time for query in format <year>-<month>-<day>T<hour>:<minute>:<second>Z time_end ( str ) â ending time for query in format <year>-<month>-<day>T<hour>:<minute>:<second>Z as_str ( bool ) â whether to return geojson as a dictionary or string Returns : geojson of the feature set returned by the query { âtypeâ: âFeatureCollectionâ, âfeaturesâ: [ { âtypeâ: âFeatureâ, âidâ: â<id>â, âgeometryâ: { âtypeâ: âPolygonâ, âcoordinatesâ: [..] }, âpropertiesâ: { âdatetimeâ: âYYYY-MM-DDTHH:MM:SS.SSSZâ, âstart_datetimeâ: âYYYY-MM-DDTHH:MM:SS.SSSZâ, âend_datetimeâ: âYYYY-MM-DDTHH:MM:SS.SSSZâ, â<tag>â: â<url>â, .. } ], âstac_versionâ: â
```

#### r4 — score 0.419

- **url:** https://docs.slideruleearth.io/api_reference/earthdata.html
- **title:** earthdata
- **section:** cmr
- **category:** `api_reference`
- **matched_tokens:** ['cmr', 'earthdata']

**Full text:**

```
: - 108.3605610678553 , "lat" : 39.25086131372244 }, ... { "lon" : - 108.3435200747503 , "lat" : 38.89102961045247 } ] >>> granules = earthdata . cmr ( short_name = 'ATL06' , polygon = region ) >>> granules ['ATL03_20181017222812_02950102_003_01.h5', 'ATL03_20181110092841_06530106_003_01.h5', ... 'ATL03_20201111102237_07370902_003_01.h5']
```

#### r5 — score 0.467

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-20-00.html
- **title:** Release v4.20.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['cmr', 'earthdata']

**Full text:**

```
7d8c96c - Updated playwright version to address vulnerability Added ATL24 support to the Python client earthdata module faf1de0 - Fixed errant CMR failure status message 8856215 - fix for with_flags and bands in dataframe sampling
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.414

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Appendix A: Acronyms
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 57
- **matched_tokens:** ['cmr']

**Full text:**

```
7 Appendices
7.1 Appendix A: Acronyms
Abbreviation Full Form
ATLAS Advanced Topographic Laser Altimetry System
AWS Amazon Web Services
CMR Common Metadata Repository
CSV Comma Separated Vector
CUDEM NOAA NCEI Continuously Updated Digital Eleva-
tion Model
DAAC Distributed Active Archive Center
ECEF Earth Centered Earth Fixed
ETOPO Earth Topography Global relief model (NOAA)
GEBCO General Bathymetric Chart of the Oceans
GSFC Goddard Space Flight Center
ICESat-2 Ice, Cloud, and land Elevation Satellite
LUT Lookup table
JSON JavaScript Object Notation
MBES Multibeam Echosounder
NCEI National Centers of Earth Information
NDWI Normalized Difference Water Index
NOAA National Oceanic and Atmospheric Administration
NSIDC National Snow and Ice Data Center
OSU Oregon State University
S3 Amazon Simple Storage Solution
SMCE Science Managed Cloud Environment
TEP Transmitter Echo Path
TPU Total propagated uncertainty
UTexas University of Texas at Austin
UTM Universal Transverse Mercator
VIIRS Visible Infrared Imaging Radiometry Suite
ZETOPO
50
```

#### r2 — score 0.387

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** CM Foreword
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 3
- **matched_tokens:** ['signature']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
CM Foreword
This document is an Ice, Cloud, and Land Elevation Satellite- 2 (ICESat-2) Project Science
Office controlled document. Changes to this document require prior approval of the Science
Development Team ATBD Lead or designee. Proposed changes shall be submitted in the
ICESat-2 Management Information System (MIS) via a Signature Controlled Request (SCoRe),
along with supportive material justifying the proposed change. Proposed changes will be vetted
through the ATLAS Science Algorithm Software (ASAS) Change Control Board (CCB) and be
submitted to the Technical Data Management System (TDMS).
In this document, a requirement is identified by “shall,” a good practice by “should,” permission
by “may” or “can,” expectation by “will,” and descriptive material by “is.”
Questions or comments concerning this document should be addressed to:
ICESat-2 Project Science Office
Mail Stop 615
Goddard Space Flight Center
Greenbelt, Maryland 20771
iii Release Date: Fall 2022
```

#### r3 — score 0.380

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 9.0 METADATA
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 159
- **matched_tokens:** ['earthdata']

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

#### r4 — score 0.361

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Historical Perspective
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 11
- **matched_tokens:** ['earthdata', 'search']

**Full text:**

```
The primary distribution architecture
is the Earth Observing system Data and Information system (EOSDIS) with major facilities
at the Distributed Active Archive Centers (DAAC) located across the United States. The
DAACs act as stewards of the Earth observing satellites and field measurement programs and
are responsible for processing, archiving, documenting and distributing data. For the original
ICESat mission and for the ICESat-2 mission the designated DAAC is the National Snow
and Ice Data Center (NSIDC) in Boulder Colorado. NSIDC is the primary DAAC for snow
and ice processes with a particular focus in snow, ice, atmosphere and ocean interactions and
has been operational since 1976. The partnership between the NSIDC team and the ICESat-2 mission has been extremely
successful in data product development and distribution via Earthdata Search. The mecha-
nisms of searching and selecting data repositories in NSIDC are well established and provide
useful tools for data filtering and visualization.
4
```

#### r5 — score 0.385

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Glossary/Acronyms
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 210
- **matched_tokens:** ['signature']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
OMCT Ocean Model for Circulation and Tides
RFA Request for Action
RGI Randolph Glacier Inventory
RGT Reference Ground Track
POD Precision Orbit Determination
PPD Precision Pointing Determination
PSO ICESat-2 Project Science Office
QA Quality Assessment
RGI Randolph Glacier Inventory
RGT Reference Ground Track
SCoRe Signature Controlled Request
SDMS Scheduling and Data Management System
SIPS ICESat-2 Science Investigator-led Processing System
SLA Sea Level Anomaly
SLP Sea level pressure
SLR Satellite Laser Ranging
SNR Signal to Noise Ratio
SPD Start Pulse Detector
SSH Sea Surface Height
SSMI/SMMR Special Sensor Microwave / Imager; Scanning Multichannel Microwave
Radiometer
TBD To Be Determined
194 Release Date: Fall 2022
```

---

