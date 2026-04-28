# Row 9 results: docsearch / conceptual

> Auto-generated. Open this file alongside `09-how-to-use-sliderule-python-client-install-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to use SlideRule Python client install`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/getting_started/Install.html
  - https://docs.slideruleearth.io/user_guide/basic_usage.html
  - https://docs.slideruleearth.io/getting_started/Getting-Started.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** Python client install + basic usage

---

## 📚 docsearch results (top 5)

#### r1 — score 0.897

- **url:** https://docs.slideruleearth.io/getting_started/Install.html
- **title:** Installation
- **section:** PyPI
- **category:** `getting_started`
- **matched_tokens:** ['client', 'install', 'python', 'sliderule', 'use']

**Full text:**

```
Alternatively, you can use the PyPI package manager to install the SlideRule Python client. This is not the recommended way of installing, but is made available as an option for users who prefer to work with pip . pip install sliderule
```

#### r2 — score 0.804

- **url:** https://docs.slideruleearth.io/getting_started/Install.html
- **title:** Installation
- **section:** Installation
- **category:** `getting_started`
- **matched_tokens:** ['client', 'install', 'python', 'sliderule', 'use']

**Full text:**

```
The recommended way of installing the SlideRule Python client is to use the Conda Python package manager. conda install -c conda-forge sliderule In order to run the example notebooks , we provide an environment.yml that can be used to create an initial conda environment that has the SlideRule Python client installed along with all the dependencies necessary to run the examples. To install the client and its dependencies via the environment file: conda env create -f environment.yml
```

#### r3 — score 0.766

- **url:** https://docs.slideruleearth.io/getting_started/Install.html
- **title:** Installation
- **section:** Developer Install
- **category:** `getting_started`
- **matched_tokens:** ['client', 'install', 'python', 'sliderule']

**Full text:**

```
For developers and contributors, to get the latest unreleased version of the Python client, the contents of the sliderule repository can be cloned or download as a zipped file . If cloning, please consider forking into your own account before cloning onto your system. Warning The main branch is used for the public cluster running at slideruleearth.io . Private clusters may be running versions of the server code provided in other branches or even forks of the repository. To clone the repository: git clone https://github.com/SlideRuleEarth/sliderule.git You can then install the sliderule python client using setuptools : cd sliderule/clients/python pip install . Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.630

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-04-00.html
- **title:** Release v1.4.x
- **section:** Required Updates
- **category:** `release_notes`
- **matched_tokens:** ['client', 'install', 'python', 'sliderule', 'use']

**Full text:**

```
v1.4.0 - In order to use the latest SlideRule server deployments, the Python client must be updated. For conda users: $ conda update sliderule For developer installs: $ cd sliderule-python $ git checkout main $ git pull $ python3 setup.py install v1.4.0 - User scripts that use the Python client need to make the following updates: The track keyword argument of atl03sp , atl03s , atl06p , and atl06 has moved to the parm dictionary The block keyword argument of atl06p and atl03sp has been removed v1.4.0 - User scripts that use the Python client should make the following updates due to deprecated functionality: The object returned from the icesat2.toregion function is now a dictionary instead of a list; the polygon should be accessed via ["poly"] instead of with a numerical index. If the region of interest contains multiple polygons, the convex hull of those polygons is returned. For compatibility, for this version only, the returned polygon is also accessible at the [0] index.
```

#### r5 — score 0.707

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['client', 'python', 'sliderule', 'use']

**Full text:**

```
sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.431

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['client', 'python', 'sliderule']

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

#### r2 — score 0.376

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['client', 'python', 'sliderule']

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

#### r3 — score 0.405

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['python', 'sliderule', 'use']

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

#### r4 — score 0.354

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Deployment Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 50
- **matched_tokens:** ['client', 'sliderule', 'use']

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

#### r5 — score 0.191

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 ATBD Sections
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 14
- **matched_tokens:** ['client', 'sliderule']

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

---

