# Row 52 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `52-h5-hdf5-read-function-parameters-h5p-h5x-review.md` —
> verdicts go there, this side is read-only.

**Query:** `h5 hdf5 read function parameters h5p h5x`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/h5.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** h5 api reference; h5p and h5x are canonical read helpers

---

## 📚 docsearch results (top 5)

#### r1 — score 0.575

- **url:** https://docs.slideruleearth.io/developer_guide/endpoints.html
- **title:** Endpoints
- **section:** h5p
- **category:** `developer_guide`
- **matched_tokens:** ['function', 'h5', 'h5p', 'hdf5', 'parameters']

**Full text:**

```
POST /source/h5p <request payload> Reads a list of datasets from an HDF5 file and returns the values of the datasets in a dictionary of lists. See h5.h5p function for a convenient method for accessing HDF5 datasets. Request Payload (application/json) parameter description default asset data source asset (see Assets) required resource HDF5 filename required datasets list of datasets (see h5 for a list of parameters for each dataset) required datasets[*].slice optional multi-dimensional slice for a dataset; list of ranges [[start0, end0], [start1, end1], ...] per dimension. Ranges are half-open [start, end) with -1 meaning âto the endâ. Up to H5Coro::MAX_NDIMS dimensions are honored; missing trailing dimensions default to [0, end] . If slice is omitted, the legacy col , startrow , and numrows parameters are used for 2D column/row selection.
```

#### r2 — score 0.599

- **url:** https://docs.slideruleearth.io/developer_guide/endpoints.html
- **title:** Endpoints
- **section:** h5
- **category:** `developer_guide`
- **matched_tokens:** ['function', 'h5', 'hdf5']

**Full text:**

```
POST /source/h5 <request payload> Reads a dataset from an HDF5 file and return the values of the dataset in a list. See h5.h5 function for a convenient method for accessing HDF5 datasets.
```

#### r3 — score 0.531

- **url:** https://docs.slideruleearth.io/api_reference/h5.html
- **title:** h5
- **section:** h5
- **category:** `api_reference`
- **matched_tokens:** ['function', 'h5', 'h5p', 'hdf5']

**Full text:**

```
sliderule.h5. h5 ( dataset , resource , asset , datatype = 3 , col = 0 , startrow = 0 , numrows = -1 ) [source] Reads a dataset from an HDF5 file and returns the values of the dataset in a list This function provides an easy way for locally run scripts to get direct access to HDF5 data stored in a cloud environment. But it should be noted that this method is not the most efficient way to access remote H5 data, as the data is accessed one dataset at a time. The h5p api is the preferred solution for reading multiple datasets. One of the difficulties in reading HDF5 data directly from a Python script is converting the format of the data as it is stored in HDF5 to a data format that is easy to use in Python. The compromise that this function takes is that it allows the user to supply the override the data type of the returned data via the datatype parameter, and the function will then return a numpy array of values with that data type. If the datatype parameter is not supplied, then the code does its best to match the HDF5 type to the corresponding Python type.
```

#### r4 — score 0.569

- **url:** https://docs.slideruleearth.io/developer_guide/articles/h5coro.html
- **title:** 2021-04-23: H5Coro
- **section:** H5Coro::read
- **category:** `developer_guide`
- **matched_tokens:** ['function', 'h5', 'parameters', 'read']

**Full text:**

```
H5Coro :: Future * H5Coro :: readp ( const char * asset , const char * resource , const char * datasetname , RecordObject :: valType_t valtype , long col , long startrow , long numrows , Context * context = NULL ) {parameters} see H5Coro::read for parameter descriptions H5Coro::Future* a pointer to a structure that will contain the info_t information read from the H5 file when the read operation completes The H5Coro::readp call is thread-safe, concurrent, and highly parallel. It is non-blocking and publishes the read request to a read queue that is serviced by a compile-time configurable number of reader threads. This is intended to provide the capability to read data in parallel for applications that are inherently limited in the number of threads they are able to run. Once a read request is picked up by one of the reader threads, the process of reading the dataset is identical to the H5Coro::read function.
```

#### r5 — score 0.506

- **url:** https://docs.slideruleearth.io/assets/grandmesa.html
- **title:** Generating a Custom ATL06 over Grand Mesa, CO
- **section:** Retrieve ATL06 Elevations Directly using icesat2.h5p API
- **category:** `tutorial`
- **matched_tokens:** ['h5', 'h5p', 'read']

**Full text:**

```
This method of reading H5 data directly is the recommended method and runs faster than icesat2.h5 as each dataset is read in parallel on the server and shares a common cache. The code below has a couple other optimizations including only sampling every 10th coordinate for point inclusion, and reading the lat,lon information first and then reading only the necessary heights.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.492

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

#### r2 — score 0.423

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.2.5 HDF5 Dataset Information
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 197
- **matched_tokens:** ['function', 'hdf5']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
possible that the resulting TEP histogram will have non-zero bin counts between the primary and
secondary TEP return regions. We therefore suggest the following checks before a higher-level
algorithm uses the TEP:
(a) If the TEP histogram is to be used as a proxy for the system impulse response
function, we recommend using the region between 15 and 30 nanoseconds to avoid the
secondary TEP return.
(b) if the primary TEP return has a full-width at half max value greater than 3
nanoseconds, we recommend not using this particular realization of the TEP as a proxy for the
system impulse response. With sufficient on-orbit TEP data, we intend to refine these guidelines to automate rejection of
spurious TEP realizations.
10.2.5 HDF5 Dataset Information
Dataset are the primary data storage containers within a HDF5 file. A dataset contains either a
scalar or (more likely) homogeneous arrays of data. Datasets, like Attributes, are assigned a
datatype. In addition, there are several different storage methodologies used for efficiently
storing the data. Designer creates 'empty' datasets. This allows Designer to focus generically on
the organization of the data product and leave the heavy data processing to external science
software. ICESat-2 datasets, by default, include a set of standard attributes corresponding to selected CF
convention parameter-level metadata fields.
```

#### r3 — score 0.399

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Classification Algorithms
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 22
- **matched_tokens:** ['h5', 'hdf5']

**Full text:**

```
4.3.1 ATL24 Data Structure and Naming Conventions
The naming and internal organization of the final HDF5 file for each ATL24 granule will
match the conventions used on the rest of the project. Each granule will also have the naming
convention similar to the other ICESat-2 data products. Each variable within the name
(place holders) are described in Table 5. Please note that there are two sets of version and
revision numbers that represent both ATL03 input version and revision and then the version
and revision of ATL24. ATL24_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr]_[vvv_rr].h5
Table 5: ATL24 naming convention
Variable Description
ATL24 ICESat-2 Level 3 Global nearshore and coastal bathymetry
ATLAS/ICESat-2 Level 3a calibrated backscatter profiles and at- ATL09 mopsheric layer characteristics
yyyymmdd Year, month and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC). Four digit Reference Ground Track number. The ICESat-2 mission tttt has 1,387 RGTs, numbered from 0001 to 1387. Cycle Number. Each of the 1387 RGTs is targeted in the polar
regions once every 91 days. The cycle number tracks the number of cc 91-day periods that have elapsed since ICESat-2 entered the science
orbit. Segment number. ATL03 data files are segmented into approxi-
ss mately 1/14th of an orbit. Segment numbers range from 01-14.
```

#### r4 — score 0.324

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.4.5 gt1l–gt3r
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 9
- **matched_tokens:** ['function', 'hdf5', 'parameters']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
ISO19115 structured metadata with sufficient content to generate the required geospatial metadata
(ATL03 ATBD | Section 2.4.9).
1.2.4.2 ancillary_data
Parameters related to ATLAS that provide insight about the instrument transmit pulse, optics,
receiver sensitivity, etc. These parameters are needed by higher level products and are generally
passed to ATL03 from the ICESat-2 Science Unit Converted Telemetry product, ATL02 (ATL02
and ATL03 ATBDs Sections 2.4.3–2.4.6).
1.2.4.3 atlas_impulse_response
Parameters needed by higher level data products that require knowledge of the ATLAS system
impulse-response function to account for how the ATLAS system impacts ground return statistics
(ATL03 ATBD | Section 2.4.2).
1.2.4.4 Dimension Scales
Two HDF5 dimension scales are stored at the top level alongside the data groups:
• ds_surf_type: dimension scale indexing the surface type array
(gt[x]/geolocation/surf_type)
• ds_xyz: dimension scale indexing the X-Y-Z components of the spacecraft velocity (east
component, north component, up component) an observer on the ground would measure
(gt[x]/geolocation/velocity_sc)
1.2.4.5 gt1l–gt3r
Six gt[x] groups, each of which contains the parameters for one of the six ATLAS ground tracks
including height above the WGS 84 ellipsoid, time, latitude, and longitude for individual photons
(ATL03 ATBD | Section 2.4.1).
```

#### r5 — score 0.309

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 1.2.5 Naming Convention
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 10
- **matched_tokens:** ['h5', 'hdf5', 'parameters']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Three HDF5 dimension scales are stored at the top level alongside the data groups—
ds_geosegments, ds_metrics, and ds_surf_type—which index the within-land geosegments,
surface type, and metrics arrays. For details about how the parameters are organized in the ATL08 product, see "Section 2 | ATL08:
Data Product" in the ATBD for ATL08.
1.2.5 Naming Convention
Data files utilize the following naming convention:
ATL08_[yyyymmdd][hhmmss]_[ttttccss]_[vvv_rr].h5
Example:
ATL08_20181014001049_02350102_006_01.h5
The following table describes the file naming convention variables:
Table 3. File Naming Convention Variables and Descriptions
Variable Description
ATL08 ATLAS/ICESat-2 L3A Land and Vegetation Height product
yyyymmdd Year, month, and day of data acquisition
hhmmss Data acquisition start time, hour, minute, and second (UTC)
tttt Four-digit Reference Ground Track number. The ICESat-2 mission has 1,387
RGTs, numbered from 0001 to 1387.
cc Cycle Number. Each of the 1,387 RGTs is targeted in the polar regions once every
91 days. The cycle number tracks the number of 91-day periods that have elapsed
since ICESat-2 entered the science orbit.
ss Orbital segment (region) number (see Figure 3). ATL08 data files cover
approximately 1/14th of an orbit. Orbital segment numbers range from 01–14.
vvv_rr Version and revision number.*
From time to time, NSIDC receives reprocessed granules from our data provider.
```

---

