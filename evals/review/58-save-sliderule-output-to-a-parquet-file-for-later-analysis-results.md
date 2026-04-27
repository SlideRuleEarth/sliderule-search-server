# Row 58 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `58-save-sliderule-output-to-a-parquet-file-for-later-analysis-review.md` —
> verdicts go there, this side is read-only.

**Query:** `save sliderule output to a parquet file for later analysis`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/how_tos/geoparquet_output.html
  - https://docs.slideruleearth.io/user_guide/arrow_output.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** parquet/arrow output; phrased as save-for-later rather than 'return in format'

---

## 📚 docsearch results (top 5)

#### r1 — score 0.691

- **url:** https://docs.slideruleearth.io/developer_guide/articles/geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** Overview
- **category:** `developer_guide`
- **matched_tokens:** ['later', 'output', 'parquet', 'sliderule']

**Full text:**

```
SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters for more details.
```

#### r2 — score 0.642

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** S3 Staging
- **category:** `user_guide`
- **matched_tokens:** ['file', 'later', 'output', 'parquet', 'sliderule']

**Full text:**

```
SlideRule also supports writing the output to its own S3 bucket for times when temporary storage is needed and the user does not have access to a bucket they own. To use this feature, the following parameters can be used: "output" : { "asset" : "sliderule-stage" , "path" : "myfile.parquet" , "open_on_complete" : False , } The sliderule-stage asset tells sliderule to stage the output in SlideRuleâs own bucket. The full path of the file is then returned back to the user so that the user can later open the file directly. For instance, in the above example, a call to icesat2.atl06p could return âs3://sliderule-public/myfile.parquetâ. If no path is specified, the server code generates a random file name and uses it to store the results. The generated file name including the path is returned back to the user. There are a couple of constraints to using this feature: In order to access the file staged in the SlideRule owned bucket, the user has to have read-access to the bucket. Typically, this is only provided through partnered organizations like CryoCloud . When running on CryoCloud, a user can specify the âsliderule-stageâ asset, and know that they returned file path is immediately accessible from their environment. Files are only stored for a short period of time before they are automatically deleted. Typically, the retention time is 2 weeks. Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 .
```

#### r3 — score 0.646

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['file', 'output', 'parquet', 'sliderule']

**Full text:**

```
To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported, specified as âparquetâ) open_on_complete : boolean; if true then the client is to open the file as a DataFrame once it is finished receiving it and writing it out; if false then the client returns the name of the file that was written as_geo : if the parquet format is specified, write the data compliant with the GeoParquet specification with_checksum : include a checksum of the returned file in the response with_validation : run the Apache Arrow validation routine on the resulting file before returning it to the user endpoint : AWS endpoint (i.e. region) when the output path is an S3 bucket (e.g. âs3.us-west-2.amazonaws.comâ) asset : the name of the SlideRule asset from which to get credentials for the optionally supplied S3 bucket specified in the output path credentials : the AWS credentials for the optionally supplied S3 bucket specified in the output path aws_access_key_id : AWS access key id aws_secret_access_key : AWS secret access key aws_session_token : AWS session token fields : the list of fields to include in the file output, trimming anything not found in this list
```

#### r4 — score 0.625

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/geoparquet_output.html
- **title:** Returning Data from SlideRule in the GeoParquet Format
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['file', 'later', 'sliderule']

**Full text:**

```
But as responses get larger, the client is unable to keep up with the SlideRule servers, and can bottleneck the process or even crash if it runs out of memory. To address these shortcomings, SlideRule supports sending responses back as GeoParquet files. When a GeoParquet file is requested, the results of the request are built entirely on the servers as a GeoParquet file, and then the final file is streamed back to the client where it is directly written to disk. This allows large requests to consume server-side resources in parsing, rearranging, and building a DataFrame-like structure. Clients can then choose to open the resulting GeoParquet file immediately, or open it at some later time with different software.
```

#### r5 — score 0.511

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** S3 Output to User Bucket
- **category:** `user_guide`
- **matched_tokens:** ['file', 'output', 'parquet', 'sliderule']

**Full text:**

```
SlideRule supports writing the output to an S3 bucket instead of streaming the output back to the client. In order to enable this behavior, the output.path field must start with âs3://â followed by the bucket name and object key. For example, if you wanted the result to be written to a file named âgrandmesa.parquetâ in your S3 bucket âmybucketâ, in the subfolder âmapsâ, then the output.path would be âs3://mybucket/maps/grandmesa.parquetâ. When writing to S3, it is required by the user to supply the necessary credentials. Here is an example code snippet for writing to your own bucket. import os import argparse import configparser # Setup Config Parser for Credentials home_directory = os . path . expanduser ( '~' ) aws_credential_file = os . path . join ( home_directory , '.aws' , 'credentials' ) config = configparser . RawConfigParser () # Read AWS Credentials config . read ( aws_credential_file ) # Populate Output Parameters parms [ "output" ] = { "path" : "s3://mybucket/myfile.parquet" , "format" : "parquet" , "open_on_complete" : False , "region" : "us-west-2" , "credentials" : { "aws_access_key_id" : config . get ( 'default' , 'aws_access_key_id' ), "aws_secret_access_key" : config . get ( 'default' , 'aws_secret_access_key' ), "aws_session_token" : config . get ( 'default' , 'aws_session_token' ) } }
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.356

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

#### r2 — score 0.243

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['analysis', 'sliderule']

**Full text:**

```
6 ATL24 Implementation Architecture and Product Accessibility
6.1 SlideRule Overview
The current user experience with ICESat-2 data is associated with downloading large volumes
of standard data products from NSIDC and then developing independent routines if the goal
is to explore new parameterizations or data resolutions for their own research. This paradigm
is the case for ICESat-2 but it is also the scenario for many NASA satellite missions and the
supporting NASA DAACs. Often the only data tools made available to users are those for
geographical and/or temporal subsetting and although extremely useful in data downloads
the requests can take hours depending on the size of the area. State-of-the-art solutions
to length and voluminous data downloads seem to be leveraging on-demand, cloud-based
processing. One example of this is the Alaska Satellite Facility’s Hybrid Pluggable Processing
Pipeline (ASFHyP3) for customized processing of SAR images across multiple missions. The
OpenTopography Project provides another example through its support of web-based services
for scalable capabilities in processing and analysis of Earth science-oriented topography data
(Shean et al. 2023). These more modern approaches to data production and dissemination
inspired SlideRule, with specific applications for ICESat-2. SlideRule is an on-demand data processing system for rapid, scalable, open science, which
is open to the public and accessible at https://slideruleearth.io.
```

#### r3 — score 0.222

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

#### r4 — score 0.202

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl24-v001-userguide.pdf
- **title:** ATL24 v001 user guide
- **section:** 1.2.3 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL24` · **page:** 5
- **matched_tokens:** ['file', 'sliderule']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry, Version 1
• x_atc: along-track distance (m) in a segment projected to the ellipsoid of the received
photon
• y_atc: across-track distance (m) projected to the ellipsoid of the received photon from the
reference ground track (RGT)
1.2.2.3 metadata
Query metadata (geospatial and temporal extents), algorithm run times, SlideRule metadata, and
granule-level statistics.
1.2.2.4 orbit_info
Orbit parameters that are constant for a granule, such as the RGT number, cycle, and spacecraft
orientation.
1.2.3 Naming Convention
Data files utilize the following naming convention:
ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[VVV_RR]_[vvv_rr].h5
Example:
ATL24_20230704193540_02232008_006_02_001_01.h5
The following table describes the file naming convention variables:
Table 1. File Naming Convention Variables and Descriptions
Variable Description
ATL24 ATLAS/ICESat-2 L3A Along Track Coastal and Nearshore Bathymetry
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit RGT number. The ICESat-2 mission has 1,387 RGTs, numbered from
0001 to 1387.
cc Cycle number. The cycle number tracks the number of 91-day periods that have
elapsed since ICESat-2 entered the science orbit.
ss Region number. ATL03 data files are segmented into approximately 1/14th of an
orbit. Region numbers range from 01 to 14. Note that some regions may not be
available.
```

#### r5 — score 0.213

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['output', 'sliderule']

**Full text:**

```
includes long-running Python scripts. In addition to using the native runtime, the atl24g
endpoint will also use the SlideRule Container Runtime.
SlideRule Container Runtime
The container runtime environment for SlideRule services is a new runtime implemented
specifically to meet the needs of the atl24g endpoint. It uses the cluster management,
intelligent load balancing, and job orchestration components of SlideRule to kick-off and
communicate with Docker containers that are u
Figure 11: Top Container Schematic of SlideRule runtime environment
Applications written in Python will execute inside a Docker container running a Python
environment, and will use a provided Python API to retrieve a list of input files and return
a list of output files. Additional Docker container environments will be made available for
programs not written in Python.
6.3 Development Environment
The development of the atl24g, atl24s, and graphical web page will be done on local de-
velopment machines and coordinated through the GitHub ICESat-2 organization. This
includes training models, writing source code, compiling code, and deploying to both test
and production environments.
44
```

---

