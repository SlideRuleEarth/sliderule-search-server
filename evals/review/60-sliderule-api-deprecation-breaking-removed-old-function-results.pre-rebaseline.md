# Row 60 results: docsearch / version_history

> Auto-generated. Open this file alongside `60-sliderule-api-deprecation-breaking-removed-old-function-review.md` —
> verdicts go there, this side is read-only.

**Query:** `sliderule api deprecation breaking removed old function`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-00-00.html
  - https://docs.slideruleearth.io/developer_guide/release_notes/release-v05-00-00.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** v04-00-00 and v05-00-00 are the major breaking-change releases

---

## 📚 docsearch results (top 5)

#### r1 — score 0.480

- **url:** https://docs.slideruleearth.io/user_guide/versioning.html
- **title:** Versioning
- **section:** Note on Reproducibility
- **category:** `user_guide`
- **matched_tokens:** ['old', 'removed', 'sliderule']

**Full text:**

```
It is the goal of the SlideRule development team to create a system where results are able to be reproduced; but this is often times either extremely difficult or impossible for reasons outside of the teams control. SlideRule relies on publicly hosted datasets. When those datasets are updated, older versions of the datasets are often removed. For instance, ICESat-2 Standard Data Products have a 6-month to 1-year release cycle and EarthData Cloud only stores the last two releases. Production systems must stay up-to-date with all security patches. This means libraries used by older versions of SlideRule may not be able to be deployed if newer versions of those libraries contain security patches. While we make every effort to keep backward compatibility for as long as possible, our development time is a limited resource and we are unable to maintain very old architectures of SlideRule. Once we increment a major version number, we often remove deprecated functionality and internal configurations needed to deploy those older system designs. That does not mean it would not be impossible to recreate the environment needed to run the older design - it does mean it becomes more and more impractical to do so. Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r2 — score 0.455

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v01-04-00.html
- **title:** Release v1.4.x
- **section:** Required Updates
- **category:** `release_notes`
- **matched_tokens:** ['function', 'removed', 'sliderule']

**Full text:**

```
v1.4.0 - In order to use the latest SlideRule server deployments, the Python client must be updated. For conda users: $ conda update sliderule For developer installs: $ cd sliderule-python $ git checkout main $ git pull $ python3 setup.py install v1.4.0 - User scripts that use the Python client need to make the following updates: The track keyword argument of atl03sp , atl03s , atl06p , and atl06 has moved to the parm dictionary The block keyword argument of atl06p and atl03sp has been removed v1.4.0 - User scripts that use the Python client should make the following updates due to deprecated functionality: The object returned from the icesat2.toregion function is now a dictionary instead of a list; the polygon should be accessed via ["poly"] instead of with a numerical index. If the region of interest contains multiple polygons, the convex hull of those polygons is returned. For compatibility, for this version only, the returned polygon is also accessible at the [0] index.
```

#### r3 — score 0.487

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['api', 'function', 'sliderule']

**Full text:**

```
sliderule.gedi. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 50 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 ) [source] Initializes the Python client for use with SlideRule and should be called before other GEDI API calls. This function is a wrapper for the sliderule.init(â¦) function . Examples >>> from sliderule import gedi >>> gedi . init ()
```

#### r4 — score 0.491

- **url:** https://docs.slideruleearth.io/api_reference/sliderule.html
- **title:** sliderule
- **section:** init
- **category:** `api_reference`
- **matched_tokens:** ['api', 'function', 'sliderule']

**Full text:**

```
sliderule. init ( url = 'slideruleearth.io' , verbose = False , loglevel = 20 , organization = 'sliderule' , desired_nodes = None , time_to_live = 60 , plugins = None , log_handler = None , github_token = None , rethrow = False , user_service = False ) [source] Initializes the Python client for use with SlideRule, and should be called before other ICESat-2 API calls. This function is a wrapper for a handful of sliderule functions that would otherwise all have to be called in order to initialize the client.
```

#### r5 — score 0.495

- **url:** https://docs.slideruleearth.io/user_guide/how_tos/plugins.html
- **title:** Building a Plugin for SlideRule
- **section:** Shared Object
- **category:** `user_guide`
- **matched_tokens:** ['api', 'function', 'sliderule']

**Full text:**

```
The pluginâs shared object must be named <plugin_name>.so and export two âCâ style functions: void init<plugin_name>(void) and void deinit<plugin_name>(void) . At startup, the SlideRule executable loads all plugins and calls their initialization function ( init ). When the SlideRule executable exits, the deinitialization ( deinit ) function for each loaded plugin is called. The init function should perform at least one of the following: Extend the Lua runtime environment with functions namespaced under the <pluging_name> . This is the primary method of extending the functionality of SlideRule. SlideRuleâs functionality is executing through Lua scripts; therefore, by providing additional functions available to the Lua runtime, any API or extension in SlideRule has the ability to access that function. For example, the atl24 plugin extends the Lua runtime with a function called hdf5file . This function is accessed via atl24.hdf5file within any Lua script, and it takes an ATL24 GeoDataFrame and writes an ATL24 HDF5 file. Register Raster ( RasterObject::registerRaster ) which allows the raster to be sampled. Register Asset Drivers ( Asset:RegisterDriver ) which read different datasets and formats. Perform various other SlideRule library exposed configurations and registrations that extend the functionality at the C++ level in the code. The deinit function should free all memory allocated by the init function.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.247

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Data Dissemination
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 13
- **matched_tokens:** ['sliderule']

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

#### r2 — score 0.160

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Development Environment
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 51
- **matched_tokens:** ['api', 'sliderule']

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

#### r3 — score 0.324

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

#### r4 — score 0.295

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** SlideRule Overview
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 49
- **matched_tokens:** ['sliderule']

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

#### r5 — score 0.156

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 155
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 155
- **matched_tokens:** ['function', 'removed']

**Full text:**

```
3238 histogram segments (in this case, errorWave and zeros with the same number of
3239 elements as errorWave). Hence, the result, oldError, is the sum of the squares of the
3240 values of errorWave. This function is applied in optimization loops, to refine the
3241 values of b and c, described below.
3242 Optimization of the b-parameter. The do-loop operates at a maximum of 1000 times.
3243 It’s purpose is to refine the value of b, in 0.02 increments. It increments the value of
3244 b by DeltaB, to the right, and computes a new Gaussian curve based on b+∆b, which
3245 is then removed from the histogram with the result going into the variable
3246 newWave. As before, checkFit_dragann is called by passing the range-limited part of
3247 newWave (errorWave) and returning a new estimate of the error (newError) which
3248 is then checked against oldError to determine which is smaller. If newError is ≥
3249 oldError, then the value of b that produced oldError is retained, and the testing loop
3250 is exited.
3251 Optimization of the c-parameter. Now the value of c is optimized, first to the left,
3252 then to the right. It is performed independently of, but similarly, to the b-parameter,
3253 using do-loops with a maximum of 1000 passes. These loops increment (to right) or
3254 decrement (to left) by a value of 0.05 (DeltaC) and use checkFit_dragann to, again,
3255 check the quality of the fit.
```

---

