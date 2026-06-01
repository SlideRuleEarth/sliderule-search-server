# Row 93 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `93-read-cloud-hdf5-files-without-downloading-them-review.md` —
> verdicts go there, this side is read-only.

**Query:** `read cloud HDF5 files without downloading them`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** h5coro without naming it

---

## 📚 docsearch results (top 5)

#### r1 — score 0.616

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'files', 'hdf5', 'read']

**Full text:**

```
The HDF5 Cloud-Optimized Read-Only Library NASAâs migration of science data products and services to AWS has sparked a debate on the best way to access science data stored in the cloud. Given that a large portion of NASAâs science data is in the HDF5 format or one of its derivatives, a growing number of efforts are looking at ways to efficiently access H5 files residing in S3. This article describes one of those efforts and argues for the creation of a standardized subset of the HDF5 specification targeting cloud environments. The challenge of optimizing H5 file access in different environments is not new. The HDF5 specification is large and flexible and supports many different data models for H5 files. Applications can use H5 files like they were self-contained file systems. Or they can use H5 files in place of databases. Or, as is the case with much of NASAâs science data, H5 files can be used as name-spaced annotated data stores. Yet, instead of having a small and efficient implementation of the HDF5 specification targeted for each of these different use-cases, they all use the same monolithic HDF5 library.
```

#### r2 — score 0.503

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Limitations of Initial Design
- **category:** `user_guide`
- **matched_tokens:** ['downloading', 'files', 'hdf5', 'read']

**Full text:**

```
Our initial architecture for processing ICESat-2 data in S3 used the native HDF5 library with the REST-VOL connector to read datasets via HDF5âs Highly Scalable Data Service (HSDS). HSDS was run as a cluster of Docker containers on each EC2 instance we deployed to, and fanned out requests to S3 across multiple reader nodes. This provided a significant performance improvement over other approaches at the time, which included downloading the entire file or mounting the remote file for local access. But the HSDS architecture still suffered from significant performance drawbacks, specifically: All read calls into the HDF5 library are serialized inside the library due to a global API lock. As a result, even though SlideRule issues many dataset read requests concurrently, and HSDS is capable of tremendous parallelism, the number of actual concurrent reads to S3 was limited to those associated with one dataset at a time. HSDS issues multiple HTTP requests per H5 dataset chunk being read. This means that the chunk size of the dataset is the single greatest factor in how performant the read is. Datasets that consist of many small chunks explode the number of TCP/IP socket connections that are needed and the per-read latencies dominate overall performance. A metadata repository is needed to hold pointers into the original H5 files which HSDS uses to know how to read the various datasets in the file.
```

#### r3 — score 0.527

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'files', 'hdf5', 'read']

**Full text:**

```
For example, at the start of this year, all of the following software systems on ICESat-2 used the same HDF5 library: (1) science product services running in AWS that access H5 data in S3, (2) Python scripts written by researchers that read H5 files stored locally, (3) the Fortran programs that generate the official ICESat-2 H5 data products that run on supercomputer clusters. For each of these applications, the historical approach has been to tune the use of the library for optimal performance in its environment. But with the recent migration to cloud environments and their pay-for-only-what-you-use cost model, tuning efforts have fallen short of cost effectively taking advantage of the cloud. By lifting current software systems and shifting them to the cloud, and then relying on application tuning to optimize them for their new environment, the move from on premise to cloud is costing more and providing less. As different projects have been confronted with this reality, various efforts have started to address the challenge of efficiently accessing H5 data in cloud-base storage systems. These efforts include approaches like restructuring the data inside the H5 file, overlaying cloud-optimized indexes overtop the original H5 files, and reformatting the data into cloud-optimized formats. All of these approaches revolve around either changing the data, or supplementing the data with additional tools and metadata.
```

#### r4 — score 0.529

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** The HDF5 Cloud-Optimized Read-Only Library (H5Coro)
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'files', 'hdf5', 'read']

**Full text:**

```
These key features come out of a design decision to focus on a narrow subset of HDF5âs capabilities specifically suited for reading data that is static (it never changes after it is written) and is stored in high-throughput, high-latency storage systems like S3. Given that the ICESat-2 data is static inside the H5 files and that it was written by a software process that had all of the data available to it prior to the writing of the file, the library can make certain assumptions about how the data is organized and what parts of the HDF5 specification donât need to be supported. As a result, the implementation focuses on the most efficient way to retrieve the values of a dataset and nothing else. Given that S3 has high-throughput and high-latency, the library strives to minimize the overall number of reads even when it comes at the cost of increasing the total amount of data read. In addition, the implementation uses a simple heuristic for predicting which sections of the file contain the requested data. It then attempts to read all of the requested data in as few read operations as possible.
```

#### r5 — score 0.650

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'hdf5', 'read']

**Full text:**

```
This article recommends a different approach: change the library . Given that there is currently only a single implementation of the HDF5 format in use â the HDF5 library, it becomes the de facto standard, and the limitations of the library become the limitations of the format. If the library performs poorly in a cloud environment, it is said that the format is not suited to the cloud environment. But when the focus shifts from the library to the format specification, then there is a path forward for efficiently using HDF5 data in future NASA cloud-based data systems: A small set of common data models for HDF5 cloud-based systems can be identified. Optimized implementations of the HDF5 specification can be developed and supported for each of those common data models. For each implementation, a subset of the HDF5 specification can be standardized, which the implementation is guaranteed to support. The existing HDF5 library can continue to be used and supported everywhere it is currently used. It becomes the reference implementation for the specification and the catchall utility for HDF5 tooling. The HDF5 Cloud-Optimized Read-Only Library (H5Coro) is a first attempt at this new approach, undertaken by ICESat-2âs SlideRule project. The H5Coro implementation is written in C++ and focuses on reading static time-series datasets from S3.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.386

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['cloud', 'downloading']

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

#### r2 — score 0.352

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.2.5 HDF5 Dataset Information
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 198
- **matched_tokens:** ['hdf5', 'read']

**Full text:**

```
Since HDF5 I/O is basically a memory copy to the HDF5 storage layer, the row/column order
difference between C-based languages and Fortran-based languages leads to a potential issue
with multi-dimension arrays. This cautionary note appears elsewhere with the Help pages, but is
repeated here because of its importance. Cautionary Note: The ICESat-2 Standard Data Products are written using the HDF5
Fortran-2003 interface. The HDF5 documentation provides this warning about multi-
dimension arrays written using Fortran:
When a C application reads data stored from a Fortran program, the data will appear to be
transposed due to the difference in the C and Fortran storage orders. For example, if Fortran
writes a 4x6 two-dimensional dataset to the file, a C program will read it as a 6x4 two-
dimensional dataset into memory. The HDF5 C utilities h5dump and h5ls will also display
transposed data, if data is written from a Fortran program. Dimension Scales are a particular type of Dataset that are used to identify axes of other arrays. For example, a time series of heights may identify a corresponding-length array of times as its
Dimension Scale. Another example is a 2-D grid that has a longitude dataset as the dimension
scale along the x-axis and a latitude dataset as the dimension scale along the Y-axis. Dimension
Scale datasets cannot contain FillValues. Fill Values
The unfortunate reality of data is that not all values will be valid.
```

#### r3 — score 0.331

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.2.5 HDF5 Dataset Information
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 198
- **matched_tokens:** ['hdf5', 'read']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
which an operating system writes a file using different sectors of physical storage media. In
addition, a filter pipeline is supported for chunked datasets. This pipeline includes filters such as
shuffle and compression that can significantly reduce the size of the data as stored on media. A
huge advantage of chunked storage is support for partial I/O. Partial datasets can be read/written
in parts by specifying the amount of data to read/write for each call. Since partial IO is made
possible by chunks, a chunk is the minimum amount of data that MUST be read/written. A
smaller amount of data can be requested (and processed), but data is internally read and
processed in multiples of the chunk size. Matching chunk size to the possible use cases is a bit of
black magic. However, in general, it is more efficient to read/write data as a multiple of the
chunk size and never attempt to read data smaller than a chunk. Nearly all ICESat-2 Datasets, except for those compact and contiguous cases mentions used
chunked storage. These datasets usually are internally compressed using the shuffle filter with
GZIP level 6 compression and have chunk sizes of at least 10,000. In testing, the combination of
the shuffle filter and level 6 compression reduce file sizes by as much as 50%. Unlimited is the term used when referring to extensible, chunked dimensions.
```

#### r4 — score 0.238

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 3
- **matched_tokens:** ['cloud', 'files', 'hdf5']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
1 DATA DESCRIPTION
Parameters
Height above the ellipsoid, time, and geodetic latitude and longitude for individual photons. Heights
are provided in the ITRF2014 reference frame; geographic coordinates are referenced to the
WGS84 ellipsoid. File Information
1.2.1 Format
Data are provided as HDF5 formatted files.
1.2.2 ATLAS/ICESat-2 Description
NOTE: The following brief description of the Ice, Cloud and land Elevation Satellite-2 (ICESat-2)
observatory and Advanced Topographic Laser Altimeter System (ATLAS) instrument is provided to help
users better understand the file naming conventions, internal structure of data files, and other details
referenced by this user guide. The ATL03 data product is described in detail in the Ice, Cloud, and land
Elevation Satellite-2 Project Algorithm Theoretical Basis Document for Global Geolocated Photon Data
(ATBD for ATL03 V6 | https://doi.org/10.5067/GA5KCLJT7LOT). The ICESat-2 observatory utilizes a photon-counting lidar (the ATLAS instrument) and ancillary
systems (GPS, star cameras, and ground processing) to measure the time a photon takes to travel
from ATLAS to Earth and back again and determine the reflected photon's geodetic latitude and
longitude. Laser pulses from ATLAS illuminate three left/right pairs of spots on the surface that
trace out six approximately 14 m wide ground tracks as ICESat-2 orbits Earth.
```

#### r5 — score 0.282

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 53
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 53
- **matched_tokens:** ['files', 'hdf5']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
929 4 ATL06 DATA PRODUCT DESCRIPTION
930 Here we describe how the parameters appear in the ATL06 product. The ATL06 parameters are
931 arranged by beam, and within each beam in a number of groups and subgroups. Where
932 parameter descriptions in the ATL06 data dictionary are considered adequate, they are not
933 repeated in this document.
934 4.1 Data Granules
935 ATL06 data are provided as HDF5 files. The HDF format allows several datasets of different
936 spatial and temporal resolutions to be included in a file. ATL06 files contain data primarily at the
937 single-segment resolution, divided into different groups to improve the conceptual organization
938 of the files. Each file contains data from a single cycle and a single RGT.
939 Within each file there are six top-level groups, each corresponding to data from GT: gt1l, gt1r,
940 gt2l, etc. The subgroups within these gtxx groups are segment_quality, land_ice_segments, and
941 residual_histogram.
942 In the segment_quality group, the data are nearly dense, providing signal-selection and location
943 information for every segment attempted (i.e. those that contain at least one ATL03 PE) in the
944 granule, at the 20-meter along-track segment spacing.
```

---

