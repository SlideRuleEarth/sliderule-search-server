# Row 87 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `87-atl03sp-segmented-photon-api-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `atl03sp segmented photon api parameters`
**Panel signature:** `c5626f92e0c9`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
- **expected_sections:**
  - `atl03sp`
  - `atl03s`
- **expected_pages:** (none)
- **notes:** atl03sp api block

---

## 📚 docsearch results (top 5)

#### r1 — score 0.698

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['api', 'atl03sp', 'parameters', 'photon', 'segmented']

**Full text:**

```
The photon data is stored as along-track segments inside the ATL03 granules, which is then broken apart by SlideRule and re-segmented according to processing parameters supplied at the time of the request. The new segments are called extents . When the length of an extent is 40 meters, and the step size is 20 meters, the extent matches the ATL06 segments. Most of the time, the photon extents are kept internal to SlideRule and not returned to the user. But there are some APIs that do return raw photon extents for the user to process on their own. Even though this offloads processing on the server, the API calls can take longer since more data needs to be returned to the user, which can bottleneck over the network. Photon extents are returned as GeoDataFrames where each row is a photon. Each extent represents the data that the ATL06 algorithm uses to generate a single ATL06 elevation. When the step size is shorter than the length of the extent, the extents returned overlap each other which means that each photon is being returned multiple times and will be duplicated in the resulting GeoDataFrame.
```

#### r2 — score 0.668

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-02-00.html
- **title:** Release v1.2.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['api', 'parameters', 'photon']

**Full text:**

```
The along track distance from the equator of each elevation and each photon has been added to their respective record definitions. For the atl03 APIâs the field name is segment_dist ; for the atl06 APIâs the field name is distance . The atl03 and atl06 APIâs now support specifying the len (extent length) and res (extent resolution) parameters in terms of whole ATL03 segments. This is achieved by setting the dist_in_seg field in the request parameters to true. Added post function to the netsvc package Lua function calls.
```

#### r3 — score 0.688

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.3 Photon-extent Parameters
- **category:** `user_guide`
- **matched_tokens:** ['api', 'parameters', 'photon']

**Full text:**

```
Selected photons are divided and aggregated using along-track samples (âextentsâ) with user-specified length. These extends may or may not align with the original 20-m segments of ATL03 photons. The len parameter specifies the length of each extent, and the _res_parameter specifies the distance between subsequent extent centers. If res is less than len , subsequent segments will contain duplicate photons. The API may also select photons based on their along-track distance, or based on the segment-id parameters in the ATL03 product (see the dist_in_seg parameter). len : length of each extent in meters res : step distance for successive extents in meters dist_in_seg : true|false flag indicating that the units of the len and res are in ATL03 segments (e.g. if true then a len=2 is exactly 2 ATL03 segments which is approximately 40 meters) Extents are optionally filtered based on the number of photons in each extent and the distribution of those photons. If the pass_invalid parameter is set to False , only those extents fulfilling these criteria will be returned. pass_invalid : true|false flag indicating whether or not extents that fail validation checks are still used and returned in the results ats : minimum along track spread, which is the distance in meters between the outermost valid photons in the variable length segment cnt : minimum photon count in segment
```

#### r4 — score 0.611

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.4 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl03sp', 'parameters', 'photon']

**Full text:**

```
The ancillary field parameters allow the user to request additional fields from the source datasets being subsetted. Ancillary data returned from the atl03x (as well as the atl03s and atl03sp ) APIs are per-photon values that are read from the ATL03 granules. No processing is performed on the data read out of the ATL03 granule. The fields must come from either a per-photon variable (atl03_ph_fields), a per-segment variable (atl03_geo_fields, atl03_corr_fields), or a rate variable (atl03_bckgrd_fields). Ancillary fields are used to specify additional fields in the ATL03, ATL08, and ATL09 granules to be returned with the photon extent and dowstream customized products. Each field provided by the user will result in a corresponding column added to the returned GeoDataFrame. Note: if a field is requested that is already present in the default GeoDataFrame, then the name of both fields will be changed to include a _x suffix for the default incusion of the field, and a _y for the ancillary inclusion of the field.
```

#### r5 — score 0.523

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['atl03sp', 'photon', 'segmented']

**Full text:**

```
The GeoDataFrame for each photon extent has the following columns: track : reference pair track number (1, 2, 3) sc_orient : spacecraft orientation (0: backwards, 1: forwards) rgt : reference ground track cycle : cycle segment_id : segment ID of first ATL03 segment in result segment_dist : along track distance from the equator to the center of the extent (in meters) count : the number of photons in the segment time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds latitude : latitude (-90.0 to 90.0) longitude : longitude (-180.0 to 180.0) x_atc : along track distance of the photon in meters (with respect to the center of the segment) y_atc : across track distance of the photon in meters across : across track distance of the photon in meters height : height of the photon in meters solar_elevation : solar elevation from ATL03 at time of measurement, in degrees background_rate : background photon counts per second atl08_class : the photonâs ATL08 classification (0: noise, 1: ground, 2: canopy, 3: top of canopy, 4: unclassified) atl03_cnf : the photonâs ATL03 confidence level (-2: TEP, -1: not considered, 0: background, 1: within 10m, 2: low, 3: medium, 4: high) quality_ph : the photonâs quality classification (0: nominal, 1: possible after pulse, 2: possible impulse responpse effect, 3: possible tep) yapc_score : the photonâs YAPC classification (0 - 255, the larger the number the higher the confidence in surface reflection) Note: when PhoREAL is enabl
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.616

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.1 ATL03 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['parameters', 'photon']

**Full text:**

```
Those photon events in
bins with a signal-to-noise ratio greater than a threshold are classified as signal, while other
photon events are classified as background. ATL03 applies multiple geophysical corrections to provide corrected heights for all the
downlinked photon events. Additionally, ATL03 also supplies certain geophysical corrections as
reference values to be applied at the end users’ discretion (i.e., geoid, ocean tides, dynamic
atmospheric correction). These corrections include the effects of the atmosphere, as well as tides
and solid earth deformation. By design, each of the corrections applied to the photon cloud can
easily be removed by the end user from the ATL03 data products if desired. By default, they are
applied to generate a best estimate of the photon height. Lastly, ATL03 provides all other spacecraft or instrument information needed by the higher-level
data products. For example, the algorithms for sea ice height and ocean height require some
knowledge of the ATLAS transmitted pulse shape or the ATLAS impulse-response function. While not explicitly needed to generate the ATL03 data product, the parameters are included in
the ATL03 product files to provide a single source for all subsequent data products. ATL03 uses the product from ATL02 and the POD and PPD processes to create its output. The
surface masks and geophysical corrections require a number of models and data products that
have been assembled with the participation of the science community.
```

#### r2 — score 0.572

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.4.5 Group: /ancillary_data/tep
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 29
- **matched_tokens:** ['parameters', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
data product (typically occurs about every five granules or twice an orbit); otherwise data from a
reference TEP is included on the ATL03 granule. In addition to single-valued parameters, a
histogram of the TEP photons are provided and the TEP photon event arrival times are also
provided in tep_hist_time, so that a user can conduct their own analysis of the TEP arrival times. These parameters are described in section 7.2.
2.4.3 Group: /ancillary_data/atlas_engineering
This group contains parameters primarily from ATL02 that provide insight into the ATLAS
transmit pulse, receiver and other ATLAS parameters needed for higher-level data products.
2.4.3.1 Group: /ancillary_data/atlas_engineering/transmit
This group contains parameters related to the ATLAS transmitter, including the laser, transmit
optics and the like. These parameters are generally passed from ATL02 to ATL03 and so are
defined in detail in the ATL02 ATBD.
2.4.3.2 Group: /ancillary_data/atlas_engineering/receiver
Similarly, this group contains parameters related to the ATLAS receiver, such as metrics for the
receiver sensitivity. These parameters are generally passed from ATL02 to ATL03 and so are
defined in detail in the ATL02 ATBD.
2.4.4 Group: /ancillary_data/calibrations
This group contains information about the ATLAS calibrations data products that are necessary
for the generation of upper-level data products.
```

#### r3 — score 0.550

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** List of Tables
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 16
- **matched_tokens:** ['parameters', 'photon']

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

#### r4 — score 0.549

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.2 Data Flow Within ATL03
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 24
- **matched_tokens:** ['parameters', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Along with the telemetered photon events, there are a number of other parameters that also
require geolocation (section 3.3). The most important is the location of the top of the telemetry
bands. The telemetry band tops and widths can change every two hundred shots (often called the
major frame rate) and is useful to several subsequent steps in ATL03 and higher-level products. Consequently, the range to the top of the telemetry band is treated just like a received photon
event and is geolocated along with the rest of the photon events. The preliminary ellipsoidal heights from ATL03g are then used to determine the surface type
(section 4.0) of a given ground track. The surface type masks are provided at 0.05 x 0.05 degree
resolution (or ~5-km resolution). Furthermore, the masks include buffer and overlap between
surface types. Consequently, it is not necessary to determine the surface type of every photon
individually. The resulting surface types and preliminary ellipsoidal heights are then passed to the signal-
finding algorithm described in section 5.0. The main outputs of this algorithm are a classification
for all photon events between likely background photon events and likely signal photon events
(with low, medium, and high confidence). The resulting photon event classifications are then
stored.
```

#### r5 — score 0.584

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 164
- **matched_tokens:** ['parameters', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
/gtx/geolocation Contains parameters related to geolocation. The rate of all of ATL03g
these parameters is at the rate corresponding to the ICESat-2
geolocation along-track segment interval (nominally 20
meters along-track). In the case of no photons within the
segment (segment_ph_cnt=0), most parameters are filled
with invalid or best-estimate values. Maintaining geolocation
segments with no photons allows for the geolocation segment
arrays to be directly aligned across the /gtx groups.
index for the n/a Index of the reference photon ATL03, Section
reference within the set of photons 3.2.
photon grouped within a segment. To
recover the position of the
reference photon within the
photon-rate arrays, add
reference_photon_index to the
reference_photo INTEGER_ corresponding ph_index_beg
n_index 4 and subtract 1. If no reference
photon was selected, this value
will indicate that the reference
photon defaulted to the first
photon. In the case of no
photons within the segment
(segment_ph_cnt=0), the value
should be 0.
reference_photo DOUBLE reference degrees Latitude of each reference ATL03g, Section
n_lat photon latitude photon. Computed from the 3.4, N
ECEF Cartesian coordinates of
the bounce point.
```

---

