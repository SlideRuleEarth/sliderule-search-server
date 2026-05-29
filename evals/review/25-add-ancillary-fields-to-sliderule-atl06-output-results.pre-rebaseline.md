# Row 25 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `25-add-ancillary-fields-to-sliderule-atl06-output-review.md` —
> verdicts go there, this side is read-only.

**Query:** `add ancillary fields to sliderule atl06 output`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `anc_fields`
  - `ancillary`
  - `atl06p`
- **expected_pages:** (none)
- **notes:** rebaselined for testsliderule.org: how_tos/ancillary_fields removed; anc_fields parameter is documented in api_reference/icesat2.html atl06p signature

---

## 📚 docsearch results (top 5)

#### r1 — score 0.529

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 2.1 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['ancillary', 'atl06', 'fields', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl06x endpoint (as well as atl06 and atl06p endpoints) come from the land_ice_segments group of the ATL06 granules. The data is mostly returned as-is, with one exception. Double-precision and single-precision floating point variables are checked to see if they contain the maximum value of their respective encodings, and if so, a floating point NaN (not-a-number) is returned instead. This check is not performed for integer variables because the maximum value of an encoded integer can sometimes be a valid value (e.g. bit masks). atl06_fields : fields in the âland_ice_segmentsâ group of the ATL06 granule, provided as a list of strings For example, parms = { "atl06_fields" : [ "ground_track/ref_azimuth" ], } gdf = sliderule . run ( "atl06x" , parms )
```

#### r2 — score 0.472

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v04-01-00.html
- **title:** Release v4.1.x
- **section:** Release v4.1.x
- **category:** `release_notes`
- **matched_tokens:** ['ancillary', 'atl06', 'fields', 'sliderule']

**Full text:**

```
2023-12-07 Version description of the v4.1.0 release of ICESat-2 SlideRule. * Important : This version requires an update of the Python client to use. The underlying mechanism used in support of including ancillary fields in processing requests was updated to support both the PhoREAL algorithm and the ATL06 subsetter. As a result, in order to include ancillary field requests in your code, you must have the latest client installed. No changes are needed to the code in your scripts.
```

#### r3 — score 0.681

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['ancillary', 'fields', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl08x endpoint (as well as atl08 and atl08p endpoints) come from the {beam} group of the ATL08 granules. atl08_fields : fields in the beam group of the ATL08 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "asr" ], } gdf = sliderule . run ( "atl08x" , parms )
```

#### r4 — score 0.637

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['ancillary', 'fields', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl24x endpoint comes from the {beam} group of the ATL24 granules. anc_fields : fields in the beam group of the ATL24 granule, provided as a list of strings For example, parms = { "anc_fields" : [ "index_ph" ], } gdf = sliderule . run ( "atl24x" , parms )
```

#### r5 — score 0.629

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.2 Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['ancillary', 'fields', 'sliderule']

**Full text:**

```
Ancillary data returned from the atl13x endpoint comes from the {beam} group of the ATL13 granules. atl13_fields : fields in the beam group of the ATL13 granule, provided as a list of strings For example, parms = { "atl08_fields" : [ "ice_flag" ], } gdf = sliderule . run ( "atl13x" , parms )
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.467

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['output', 'sliderule']

**Full text:**

```
Subsequent versions, ATL24.s and ATL24.p
will leverage the full capabilities of SlideRule to provide a subsetting service and on-demand
product generation service using a Python client, Javascript client, or web map GUI. This
functionality will enable users to optimize the output data product for their particular science
need, resulting in truly ”science-ready” data. The descriptions of each planned ATL24.x
product goals and client service plans are listed below:
6
```

#### r2 — score 0.303

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 53
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 53
- **matched_tokens:** ['atl06', 'fields']

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

#### r3 — score 0.370

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['sliderule']

**Full text:**

```
6.2 Deployment Environment
ATL24 will use SlideRule to provide the compute infrastructure for all four project objectives:
• The atl24g gold standard product will be generated by a private instantiation of SlideRule
running in the AWS us-west-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to being transferred to the NSIDC.
• The atl24s and atl24p web services will be provided by the public instantiation of
SlideRule that runs in the AWS us-west-2 data center.
• The graphical web interface will be hosted in AWS S3 and served by Amazon’s CloudFront
at https://client.slideruleearth.io. Figure 10: Top Level SlideRule Architecture
SlideRule Native Runtime
The native runtime environment for SlideRule services is an extended Lua interpreter
where each request maps to a Lua script that instantiates custom classes written in C++ to
perform the processing needed to fulfill the request. The runtime is designed to quickly complete requests and return results back to users in
near real-time. To that end, all requests are expected to complete within 10 minutes, and
results are streamed back to the user as soon as they are available, over a TCP/IP connection
that remains open for the entire time of the request. (It is typical for the users that request
many granules to be processed at once to start receiving results for parts of their request
that have finished before other parts of their request have even begun to be processed).
```

#### r4 — score 0.333

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 6
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 6
- **matched_tokens:** ['add', 'output']

**Full text:**

```
2019 March 13 Replace canopy_closure with new landsat_perc parameter
2019 March 13 Change ATL08 product output regions to match ATL03
regions (Sec 2), but keep ATL08 regions internally and
report in new parameter atl08_regions (Table 2.4, Sec
2.4.24)
2019 March 13 Add methodology for handling short ATL08 processing
segments at the end of an ATL03 granule (Sec 4.2), and
output distance the processing segment length is extended
into new parameter last_seg_extend (Table 2.4, Sec 2.4.25)
2019 March 13 Add preprocessing step for removing atmospheric and ocean
tide corrections from ATL03 heights (Later removed)
2019 March 27 Remove preprocessing step for removing atmospheric and
ocean tide corrections from ATL03 heights, since those
values are now removed from the ATL03 photon heights.
2019 March 27 Replaced ATL03 region figure with corrected version (Figure
2.2)
2019 March 27 Specified that at least 50 classed photons are required to
create the 100 m land and canopy products (Secs 2, 4.17(1),
4.18(1))
2019 March 27 Clarified that any non-extended segments would report a
land_seg_extend value of 0 (Sec 4.2, Sec 2.4.25)
2019 April 30 Fixed the error in Eqn 1.4 for the sigma topo value
2019 May 13 Specified for cloud flag carry-over from ATL09 that ATL08
will report the highest cloud flag if an 08 segment straddles
two 09 segments. (Section 2.5)
2019 May 13 Changed parameter cloud_flag_asr to cloud_flag_atm since
the cloud_flag_asr is likely not to work over land due to
varying surfa
```

#### r5 — score 0.260

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 69
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 69
- **matched_tokens:** ['atl06', 'fields']

**Full text:**

```
Steps 5 and 6 require information
1208 about the background rate, which is provided with the atmospheric data
1209 Table 5-1 lists parameters needed from ATL03 and ATL09 for generation of ATL06.
1210 Individual PE heights, times, IDs, and geolocations are provided by ATL03. A variety of tidal
1211 and atmospheric-delay parameters are derived from subsamples of ATL03 fields or by
1212 interpolation into data tables used during ATL03 processing. Some ATL03 parameters are
1213 provided for every PE (e.g. height and horizontal position). These are averaged over the selected
1214 PEs for each segment. Others are provided for ‘reference’ photons spaced approximately every
1215 40 m along track. For these fields, ATL06 values are interpolated as a function of along-track x
1216 from the values for the ‘nominal’ photons to the segment centers.
1217 In addition, parameters from the atmospheric channel are used to define the blowing-snow height
1218 parameter, the blowing-snow confidence parameter, and the cloud-flag confidence parameter.
1219 The 200-Hz background-rate parameter is used to estimate background rates for each segment, as
1220 is the 50-Hz background-rate parameter based on the full atmospheric window.
```

---

