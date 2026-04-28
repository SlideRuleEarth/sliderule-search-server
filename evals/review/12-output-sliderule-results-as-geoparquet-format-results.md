# Row 12 results: docsearch / conceptual

> Auto-generated. Open this file alongside `12-output-sliderule-results-as-geoparquet-format-review.md` —
> verdicts go there, this side is read-only.

**Query:** `output SlideRule results as GeoParquet format`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/arrow_output.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** GeoParquet output format (how_tos/geoparquet_output dropped after testsliderule.org rebaseline)

---

## 📚 docsearch results (top 5)

#### r1 — score 0.711

- **url:** https://docs.testsliderule.org/developer_guide/articles/geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** Overview
- **category:** `developer_guide`
- **matched_tokens:** ['format', 'geoparquet', 'output', 'results', 'sliderule']

**Full text:**

```
SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters in Arrow Output for more details.
```

#### r2 — score 0.632

- **url:** https://docs.testsliderule.org/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['format', 'geoparquet', 'output', 'results', 'sliderule']

**Full text:**

```
To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported, specified as âparquetâ) open_on_complete : boolean; if true then the client is to open the file as a DataFrame once it is finished receiving it and writing it out; if false then the client returns the name of the file that was written as_geo : if the parquet format is specified, write the data compliant with the GeoParquet specification with_checksum : include a checksum of the returned file in the response with_validation : run the Apache Arrow validation routine on the resulting file before returning it to the user endpoint : AWS endpoint (i.e. region) when the output path is an S3 bucket (e.g. âs3.us-west-2.amazonaws.comâ) asset : the name of the SlideRule asset from which to get credentials for the optionally supplied S3 bucket specified in the output path credentials : the AWS credentials for the optionally supplied S3 bucket specified in the output path aws_access_key_id : AWS access key id aws_secret_access_key : AWS secret access key aws_session_token : AWS session token fields : the list of fields to include in the file output, trimming anything not found in this list
```

#### r3 — score 0.638

- **url:** https://docs.testsliderule.org/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['format', 'geoparquet', 'results', 'sliderule']

**Full text:**

```
By default, SlideRule returns all processing results in a native (i.e. custom to SlideRule) format as soon as they are generated. Those results are streamed back to the client and used by the client to construct a (Geo)DataFrame that is presented to the user. But sometimes it is desirable to have SlideRule build a (Geo)DataFrame on the server, and then stream that dataframe back to the client for easy reconstruction. This could be because the dataframe is quite large and the environment the client is running in does not have the resources to build the dataframe. Or it could be that the results need to be stored directly in an S3 bucket and having the dataframe already built expedites that process. To support this functionality, SlideRule uses the Apache Arrow library to build dataframes in either Parquet, CSV, or Feather formats. When using Parquet, the server also provides the option for using the GeoParquet convention to populate a geometry column and metadata compatible with GeoPandas .
```

#### r4 — score 0.605

- **url:** https://docs.testsliderule.org/developer_guide/articles/geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** Constraints
- **category:** `developer_guide`
- **matched_tokens:** ['format', 'geoparquet', 'results', 'sliderule']

**Full text:**

```
Currently, only support for the atl06 , atl08 , and flattened atl03 records is provided. This means that the ICESat-2 compact parameter being set is not supported when outputting to GeoParquet, and the atl03 results may look slightly different between native runs and runs that request the GeoParquet format. The results in the GeoParquet file are not sorted. The SlideRule server side version information only includes the server core version information and does not include version information for any of the plugins that the server has loaded and is running. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.0 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r5 — score 0.710

- **url:** https://docs.testsliderule.org/developer_guide/articles/geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** 2023-02-24: GeoParquet
- **category:** `developer_guide`
- **matched_tokens:** ['geoparquet', 'results', 'sliderule']

**Full text:**

```
Warning SlideRule now supports returning results back to data users as GeoParquet files. The functionality described in this article has been improved with broad support for returning data via Apache Arrow based formats.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.296

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['results', 'sliderule']

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

#### r2 — score 0.324

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

#### r3 — score 0.244

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

#### r4 — score 0.224

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['output', 'sliderule']

**Full text:**

```
ATL24.g The gold standard product will be generated by a private instantiation of SlideRule
running in the AWS US-West-2 data center. The granules will initially exist in SlideRule’s
private S3 bucket prior to transfer to NSIDC. Moving forward, the ATL24.g option will
exist in SlideRule as a client facing product with subsetting capabilities. ATL24.s and ATL24.p Web-services will be provided by the public instantiation of Slid-
eRule. Includes interfacing to the client, and reading the ATL24 granules from S3. Graphical web interface The interface will be hosted in AWS S3 and served by Amazon’s
CloudFront at https://client.slieruleearth.io
The gold standard ATL24 product will be generated on a per-granule basis using SlideRule
and following the prescribed nearshore/coastal bathymetry mask to coordinate and execute
the full suite of contributing classification algorithms. This gold standard data product will
be a global resource using the most current algorithmic workflow and will be available to
users via sub-setting. Ultimately, the ATL24.g product provides the most robust algorithm
parameterization for global applications but does not provide the option for users to adjust
the input parameters. Figure 1 shows the execution flow from an incoming ATL24.g request
all the way to the output of a gold standard h5 granule.
3.3 ATL24 ATBD Sections
ATL24 primary input is ATL03, using the geolocated photon point cloud to determine
classifications of sea surface and seafloor.
```

#### r5 — score 0.244

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 6
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 6
- **matched_tokens:** ['output', 'results']

**Full text:**

```
List of Tables
1 History of changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
2 ATL24 input variables and processing details within each stage of the product
production . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 ATL24 component input for processing pipeline . . . . . . . . . . . . . . . . 12
4 ATL24 output variables for each stage of the product production . . . . . . . 12
5 ATL24 naming convention . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 Sea Surface cross validation results from 180 labeled datasets. . . . . . . . . 39
7 Bathymetry cross validation results from 180 labeled datasets. . . . . . . . . 39
8 Cross validation results from 180 labeled datasets. . . . . . . . . . . . . . . . 39
9 Known issues, reasons and possible solutions to ATL24 classification accuracy 48
vi
```

---

