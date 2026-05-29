# Row 84 results: docsearch / version_history

> Auto-generated. Open this file alongside `84-geoparquet-arrow-output-format-added-version-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GeoParquet arrow output format added version`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-00-00.html
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** arrow/geoparquet output introduced v02-00/01-00

---

## 📚 docsearch results (top 5)

#### r1 — score 0.633

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['arrow', 'format', 'geoparquet', 'output']

**Full text:**

```
To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported, specified as âparquetâ) open_on_complete : boolean; if true then the client is to open the file as a DataFrame once it is finished receiving it and writing it out; if false then the client returns the name of the file that was written as_geo : if the parquet format is specified, write the data compliant with the GeoParquet specification with_checksum : include a checksum of the returned file in the response with_validation : run the Apache Arrow validation routine on the resulting file before returning it to the user endpoint : AWS endpoint (i.e. region) when the output path is an S3 bucket (e.g. âs3.us-west-2.amazonaws.comâ) asset : the name of the SlideRule asset from which to get credentials for the optionally supplied S3 bucket specified in the output path credentials : the AWS credentials for the optionally supplied S3 bucket specified in the output path aws_access_key_id : AWS access key id aws_secret_access_key : AWS secret access key aws_session_token : AWS session token fields : the list of fields to include in the file output, trimming anything not found in this list
```

#### r2 — score 0.434

- **url:** https://docs.slideruleearth.io/user_guide/articles/230224_geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['arrow', 'format', 'geoparquet', 'output']

**Full text:**

```
SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters in Arrow Output for more details.
```

#### r3 — score 0.389

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-04-00.html
- **title:** Release v4.4.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['added', 'arrow', 'format', 'output']

**Full text:**

```
v4.4.0 - Resources are queried from servers instead of client. If a processing request does not include a list of resources to process, the server processing the request will query CMR and populate the resources parameter. In addition, any sampling requests that need a populated catalog parameter will also be queried on the server side and have that parameter populated. v4.4.0 - 389 and 383 - updates to demo plotting and added support for downloading results v4.4.0 - Raster sampling support when the output is an Arrow generated format (Geo/Parquet, CSV, Feather). v4.4.0 - Added Feather output support v4.4.0 - 43d536b - Request parameters and record information added to metadata of generated Parquet files. v4.4.0 - 763e553 - max confidence in the signal_conf variable can be selected when filtering ATL03 photons based on confidence level v4.4.0 - 392 - GEBCO raster sampling support added v4.4.0 - 9d71b6e - Meta global canopy height raster support added
```

#### r4 — score 0.398

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['arrow', 'format', 'geoparquet']

**Full text:**

```
By default, SlideRule returns all processing results in a native (i.e. custom to SlideRule) format as soon as they are generated. Those results are streamed back to the client and used by the client to construct a (Geo)DataFrame that is presented to the user. But sometimes it is desirable to have SlideRule build a (Geo)DataFrame on the server, and then stream that dataframe back to the client for easy reconstruction. This could be because the dataframe is quite large and the environment the client is running in does not have the resources to build the dataframe. Or it could be that the results need to be stored directly in an S3 bucket and having the dataframe already built expedites that process. To support this functionality, SlideRule uses the Apache Arrow library to build dataframes in either Parquet, CSV, or Feather formats. When using Parquet, the server also provides the option for using the GeoParquet convention to populate a geometry column and metadata compatible with GeoPandas .
```

#### r5 — score 0.586

- **url:** https://docs.slideruleearth.io/user_guide/articles/230224_geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** 2023-02-24: GeoParquet
- **category:** `user_guide`
- **matched_tokens:** ['arrow', 'geoparquet']

**Full text:**

```
Warning SlideRule now supports returning results back to data users as GeoParquet files. The functionality described in this article has been improved with broad support for returning data via Apache Arrow based formats.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.254

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 176
- **matched_tokens:** ['format', 'output']

**Full text:**

```
To re-use, replace
breaks (BR) with linefeeds.
data_end_utc STRING end UTC time of n/a UTC (in CCSDS-A format) of the
a granule last data point within the
granule.
data_start_utc STRING start UTC time n/a UTC (in CCSDS-A format) of the
of a granule first data point within the
granule.
end_cycle DOUBLE ending cycle n/a The ending cycle number
associated with the data
contained within this granule. The cycle number is the
counter of the number of 91-
day repeat cycles completed by
the mission.
160 Release Date: Fall 2022
```

#### r2 — score 0.266

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 181
- **matched_tokens:** ['output', 'version']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
start_region INTEGER_ starting region n/a The starting product-specific
4 region number associated with
the data contained within this
granule. ICESat-2 data products
are separated by geographic
regions. The data contained
within a specific region are the
same for ATL01 and ATL02. ATL03 regions differ slightly
because of different
geolocation segment locations
caused by the irregular shape
of the Earth. The region indices
for other products are
completely independent.
start_rgt INTEGER_ starting n/a The starting reference
4 reference groundtrack (RGT) number
groundtrack associated with the data
contained within this granule. There are 1387 reference
groundtrack in the ICESat-2
repeat orbit. The reference
groundtrack increments each
time the spacecraft completes
a full orbit of the Earth and
resets to 1 each time the
spacecraft completes a full
cycle.
version STRING version n/a Version number of this granule
within the release.
```

#### r3 — score 0.204

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.2 Data Flow Within ATL03
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 22
- **matched_tokens:** ['format', 'output']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
All ICESat-2 data products, including ATL03, are provided as HDF5 files
(https://earthdata.nasa.gov/standards/hdf5). This file format allows similar parameters (such as
instrument parameters, altimetry data, metadata, etc.) to be grouped together, and simplifies the
organization of the data. The ATL03 data product is segmented into granules that each span
about 1/14th of an orbit.
Figure 2-1. Flowchart for ATL03.
The overall ATL03 data product is described by three documents. ATL03g (elements enclosed
with the red dashes) describes the process of geolocation and is summarized in section 3.0. The
atmospheric delay correction is described in ATL03a (outlined in green). The elements enclosed
by the blue dashes are described in this document, with the section numbers indicated. See the
ATL03a (ICESat-2 Atmospheric Delay Correction to Laser Altimetry Ranges) and ATL03g
(ICESat-2 Receive Photon Geolocation) ATBDs posted at NSIDC for further details on the
atmospheric delay correction and geolocation, respectively.
2.2 Data Flow Within ATL03
As discussed above, the overall ATL03 process takes input from ATL02, POD, PPD and related
Ancillary Files, and ultimately provides the parameters listed in Appendix A (the ATL03 data
output table). Note that ATL03 and subsequent data products are only routinely generated when
6 Release Date: Fall 2022
```

#### r4 — score 0.169

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** Change History Log
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 13
- **matched_tokens:** ['added', 'output', 'version']

**Full text:**

```
June 22 Added updates from ATL13 rel006 final version ATBD.
2023
June 28 Added sseg_length and sseg_dist_from_eq to output.
2023
Reversed 0/1 on/off assignments used for apply_mirror September
and limit_hist_depth arrays to match convention used for 15 2023
previous parameters. Removed instrument effects from all analysis based on September
photon quality flag. Refined long segment bathymetry 29 2023
results for each member short segment based on its
individual photon distribution.
xiii
Release 007, January 31, 2025
```

#### r5 — score 0.168

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl13-v007-userguide.pdf
- **title:** ATL13 v007 user guide
- **section:** 3 Version History
- **category:** `user_guide`
- **source_product:** `ATL13` · **page:** 13
- **matched_tokens:** ['added', 'output', 'version']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data, Version 7
Version Date Description of Changes
• Added an improved methodology for identifying bathymetry that couples
density thresholds with examination of photon distribution in the water
column, controllable by water body type.
• Added apparent standard deviation to the non-anomalous short segment
output.
• Updated min mirror cnt for coastal water bodies.
6.1 1 May 2024 Data from 13 Nov 2022 to 26 Oct 2023 were reprocessed using ITRF2014
(replacing ITRF2020) for consistency across the entire data set.
5.0 12 Feb 2024 Removed data access for v5.0. Data coverage was 13 Oct 2018 to 13 Oct
(retire) 2022.
6.0 29 Jun 2023 • Modified the computations of the deconvolution of subsurface backscatter
profile and deconvolution of surface water profile.
• Expanded iteration range of subsurface parameters within deconvolution
scheme and added quality flags
• Added surface quality flags
• Defined end of partial short segments as the final signal photon
• To avoid inadvertently capturing subsurface photons associated with bottom
reflection and machine error, such photons are further screened and removed
from processing using a mirroring approach applied to the water surface
• Replaced “crossing-number” algorithm with “winding number” algorithm for
better determination of ICESat-2 transects within the inland water mask
shapes
4.0 13 Jun 2022 Removed data access for v4.0.
```

---

