# Row 74 results: docsearch / conceptual

> Auto-generated. Open this file alongside `74-how-does-sliderule-read-cloud-hdf5-with-h5coro-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how does SlideRule read cloud HDF5 with h5coro`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** h5coro cloud-optimized HDF5 reader article

---

## 📚 docsearch results (top 5)

#### r1 — score 0.636

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'h5coro', 'hdf5', 'read', 'sliderule']

**Full text:**

```
This article recommends a different approach: change the library . Given that there is currently only a single implementation of the HDF5 format in use â the HDF5 library, it becomes the de facto standard, and the limitations of the library become the limitations of the format. If the library performs poorly in a cloud environment, it is said that the format is not suited to the cloud environment. But when the focus shifts from the library to the format specification, then there is a path forward for efficiently using HDF5 data in future NASA cloud-based data systems: A small set of common data models for HDF5 cloud-based systems can be identified. Optimized implementations of the HDF5 specification can be developed and supported for each of those common data models. For each implementation, a subset of the HDF5 specification can be standardized, which the implementation is guaranteed to support. The existing HDF5 library can continue to be used and supported everywhere it is currently used. It becomes the reference implementation for the specification and the catchall utility for HDF5 tooling. The HDF5 Cloud-Optimized Read-Only Library (H5Coro) is a first attempt at this new approach, undertaken by ICESat-2âs SlideRule project. The H5Coro implementation is written in C++ and focuses on reading static time-series datasets from S3.
```

#### r2 — score 0.637

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Conclusion
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'h5coro', 'hdf5', 'read', 'sliderule']

**Full text:**

```
By implementing H5Coro on ICESat-2 SlideRuleâs project, we were able to meet our immediate goals of providing a cost-effect and responsive data system for our customers; but we also believe our approach is applicable to other projects and demonstrates a path forward to successfully using HDF5 data in the cloud. The dramatic improvement in performance of H5Coro over the existing HDF5 library shows that the original library was never designed to run in a cloud environment, and that changes to the data are not necessary in order to achieve performant data access. As more HDF5 data is migrated to the cloud, we should invest in taking the necessary steps to allow small, narrowly focused implementations of the HDF5 specification to thrive. These implementations will enable the massive investments already made to create these datasets to continue to provide value to the science community for years to come. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r3 — score 0.595

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** 2021-04-23: H5Coro
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'h5coro', 'hdf5', 'read', 'sliderule']

**Full text:**

```
Note The HDF5 Cloud-Optimized Read-Only Library is a new from-scratch implementation in C++ of the HDF5 specification that focuses on reading static time-series datasets from S3. Its use on SlideRule removed critical performance barriers in accessing ICESat-2 datasets hosted in S3 and has enabled the project to cost effectively offer science processing services to the ICESat-2 science community.
```

#### r4 — score 0.715

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** Executive Summary
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'h5coro', 'hdf5', 'sliderule']

**Full text:**

```
Its use on SlideRule removed critical performance barriers in accessing ICESat-2 datasets hosted in S3 and has enabled the project to cost effectively offer science processing services to the ICESat-2 science community. The demonstrated benefits of using the H5Coro library in SlideRule show that the approach of changing the library and not the data has merit, and that future efforts to utilize NASAâs HDF5 datasets could greatly benefit from a standardized subset of the HDF5 specification specifically suited for cloud environments.
```

#### r5 — score 0.570

- **url:** https://docs.slideruleearth.io/user_guide/articles/210423_h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** The HDF5 Cloud-Optimized Read-Only Library (H5Coro)
- **category:** `user_guide`
- **matched_tokens:** ['cloud', 'h5coro', 'hdf5', 'read', 'sliderule']

**Full text:**

```
H5Coro is a C++ module inside the SlideRule server that was written from scratch and implements an HDF5 reader for H5 files that reside on the local file system or in S3. Its purpose was to address the performance deficiencies in the existing HDF5 software identified above. To that end, it has these key features: All reads are concurrent. Multiple threads within the same application can issue read requests through H5Coro and those reads will get executed in parallel. Intelligent range gets are used to read as many dataset chunks as possible in each read operation. This drastically reduces the number of HTTP requests to S3 and means there is no longer a need to re-chunk the data (it actually works better on smaller chunk sizes due to the granularity of the request). The system is serverless. H5Coro is linked into the running application and scales naturally as the application scales. This reduces overall system complexity. No metadata repository is needed. Instead of caching the contents of the datasets which are large and may or may not be read again, the library focuses on caching the structure of the file so that successive reads to other datasets in the same file will not have to re-read and re-build the directory structure of the file.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.449

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

#### r2 — score 0.465

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['cloud', 'sliderule']

**Full text:**

```
SlideRule runs in Amazon’s
cloud under GSFC Code 606’s Science Managed Cloud Environment (SMCE) and has access
to NASA’s Cumulus data archives. SlideRule provides web-services for researchers and other
data systems to generate custom data products in real-time using processing parameters
supplied at the time of the request. Scientists access SlideRule directly from any Python environment using a provided client;
a Javascript client is also provided for integrating SlideRule into other web-based systems. SlideRule is currently being used by glacier, snow, and bathymetry researchers to process
tens of thousands of ICESat-2 granules each month. SlideRule also supports private instantiations of its infrastructure that require authen-
ticated access. These instantiations, called private clusters, are managed by the SlideRule
Provisioning System at https://ps.slideruleearth.io. Private clusters are used for execut-
ing large processing runs, providing dedicated compute resources, and running proprietary
algorithms.
42
```

#### r3 — score 0.355

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['cloud', 'sliderule']

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

#### r4 — score 0.332

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['cloud', 'sliderule']

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

#### r5 — score 0.320

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['cloud', 'sliderule']

**Full text:**

```
used alone or in combination with total propagated uncertainty (TPU) values to filter the
data. Figure 1: ATL24 flow diagram of computational architecture
3.2 Data Dissemination
The implementation architecture chosen for ATL24 r001 will follow the standard approach for
the dissemination of the ICESat-2 mission products through the National Snow and Ice Data
Center (NSIDC). However, in the last few years NSIDC has pushed the products to the cloud
for modernized access to the data, which will be an additional pathway to ATL24 data access
for the scientific community. Both means of access will provide capabilities for geographical
and temporal sub-setting to the user. Additionally, for ATL24 specifically, there is also a
planned, parallel capacity for allowing on-demand and customized, science-ready bathymetry
product from ATL03 granules via SlideRule, a public web application programming interface
(API) for processing of science data in the cloud (Shean et al. 2023). ATL24 will eventually
present a family of data products, which collectively will be referred to as ATL24.x. This
ATBD describes the version referred to as the ”gold standard” version, ATL24.g, hosted by
NSIDC and available in Earthdata cloud, with the metadata for the granules registered in
NASA’s Common Metadata Repository (CMR).
```

---

