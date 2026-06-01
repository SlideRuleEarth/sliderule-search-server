# Row 86 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `86-atl08p-phoreal-vegetation-api-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl08p phoreal vegetation api parameters`
**Panel signature:** `ec5548a2ca6b`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
- **expected_sections:**
  - `atl08p`
  - `atl08`
- **expected_pages:** (none)
- **notes:** atl08p api block

---

## 📚 docsearch results (top 5)

#### r1 — score 0.502

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.3 Vegetation Metrics (PhoREAL) - atl08p
- **category:** `user_guide`
- **matched_tokens:** ['atl08p', 'phoreal', 'vegetation']

**Full text:**

```
The vegetation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) ph_count : total number of photons used by PhoREAL algorithm for this extent gnd_count : number of ground photons used by PhoREAL algorithm for this extent veg_count : number of vegetation (canopy and top of canopy) photons used by PhoREAL algorithm for this extent landcover : flag indicating if segment includes land surfaces snowcover : flag indicating if snow is present in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) x_atc : along track distance from the equator in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees h_te_median : median terrain elevation in meters (absolute heights) h_max_canopy : maximum relief height for canopy photons h_min_canopy : minimum relief height for canopy photons h_mean_canopy : average relief height for canopy photons h_canopy : 98th percentile relief height for canopy photons canopy_openness : standard deviation of relief height for canopy photons canopy_h_metrics : relief height at given percentile for canopy phot
```

#### r2 — score 0.480

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.3 Vegetation Metrics (PhoREAL) - atl08p
- **category:** `user_guide`
- **matched_tokens:** ['atl08p', 'phoreal', 'vegetation']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 PhoREAL processing requests is a set of geolocated vegetation metrics corresponding to a geolocated ATL03 along-track segment. The metrics are contained in a GeoDataFrame where each row represents a segment.
```

#### r3 — score 0.564

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.1 PhoREAL Parameters
- **category:** `user_guide`
- **matched_tokens:** ['parameters', 'phoreal', 'vegetation']

**Full text:**

```
The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the median value across all photons in the segment; âcenterâ - takes the halfway value calculated by the average of the first and last photon in the segment use_abs_h : boolean whether the absolute photon heights are used instead of the normalized heights send_waveform : boolean whether to send to the client the photon height histograms in addition to the vegetation statistics above_classifier : boolean whether to use the ABoVE photon classifier when determining top of canopy photons
```

#### r4 — score 0.567

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['atl08p', 'phoreal']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

#### r5 — score 0.568

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['parameters', 'vegetation']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.473

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 4 Version History
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 19
- **matched_tokens:** ['phoreal', 'vegetation']

**Full text:**

```
Uncertainty in computed terrain height estimates depends on the uncertainties in the ATL03 data
passed to the algorithm combined with any local uncertainties within each 100 m segment,
beginning with the number of photons classified as terrain photons. Potential error
sources in ATL08 height retrievals are detailed in Sections 1.5–1.8 of the ATL08 ATBD. Topics
include vertical sampling error, background noise, misidentified photons, complex topography,
dense vegetation, and dense and sparse canopies.
3 SOFTWARE AND TOOLS
PhoREAL is a free library of geospatial analysis tools and source code written specifically for
working with ATL03 and ATL08 data.
4 VERSION HISTORY
A summary of the version history is provided in Table 5. Page 18 of 19National Snow and Ice Data Center
nsidc.org
```

#### r2 — score 0.523

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 3
- **matched_tokens:** ['parameters', 'vegetation']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
1 DATA DESCRIPTION
Parameters
Along-track terrain and canopy height above the WGS 84 ellipsoid (ITRF2014 reference frame). File Information
1.2.1 Format
Data are provided as HDF5 formatted files.
1.2.2 ATLAS/ICESat-2 Description
The following brief description of the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory and
Advanced Topographic Laser Altimeter System (ATLAS) instrument is provided to help users better
understand the file naming conventions, internal structure of data files, and other details referenced by
this user guide. The ATL08 data product is described in detail in the Ice, Cloud, and land Elevation
Satellite-2 Project Algorithm Theoretical Basis Document for the Land - Vegetation Along-Track Product
(ATBD for ATL08 | V6, https://doi.org/10.5067/8ANPSL1NN7YS). The ICESat-2 observatory utilizes a photon-counting lidar (the ATLAS instrument) and ancillary
systems (GPS, star cameras, and ground processing) to measure the time a photon takes to travel
from ATLAS to Earth and back again and determine the reflected photon's geodetic latitude and
longitude. Laser pulses from ATLAS illuminate three left/right pairs of spots on the surface that
trace out six approximately 14 m wide ground tracks as ICESat-2 orbits Earth.
```

#### r3 — score 0.552

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.4.6 Dimension Scales
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 9
- **matched_tokens:** ['parameters', 'vegetation']

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

#### r4 — score 0.485

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 2
- **matched_tokens:** ['parameters', 'vegetation']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
TABLE OF CONTENTS
1 DATA DESCRIPTION ................................................................................................................. 2
Parameters ............................................................................................................................................ 2
File Information ...................................................................................................................................... 2
1.2.1 Format.......................................................................................................................................... 2
1.2.2 ATLAS/ICESat-2 Description ....................................................................................................... 2
1.2.3 File Contents ................................................................................................................................ 6
1.2.4 Data Groups................................................................................................................................. 7
1.2.5 Naming Convention ..................................................................................................................... 9
1.2.6 Browse Files .............................................................................................................................. 10
Spatial Information..................................................................
```

#### r5 — score 0.461

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 20
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 20
- **matched_tokens:** ['parameters', 'vegetation']

**Full text:**

```
From an
276 analysis perspective, it is difficult and cumbersome to attempt to relate canopy cover
277 over variable lengths. Furthermore, a segment size of 100 m will facilitate a simpler
278 combination of along-track data to create the gridded products.
279 We anticipate that the signal returned from the weak beam will be sufficiently
280 weak and may prohibit the determination of both a terrain and canopy segment
281 height, particularly over areas of dense vegetation. However, in more arid regions we
282 anticipate producing a terrain height for both the weak and strong beams.
283 In this document, section 1 provides a background of lidar in the ecosystem
284 community as well as describing photon counting systems and how they differ from
285 discrete return lidar systems. Section 2 provides an overview of the Land and
286 Vegetation parameters and how they are defined on the data product. Section 3
287 describes the basic methodology that will be used to derive the parameters for ATL08.
20
```

---

