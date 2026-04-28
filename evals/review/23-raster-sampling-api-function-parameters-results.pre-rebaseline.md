# Row 23 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `23-raster-sampling-api-function-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `raster sampling API function parameters`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/raster.html
  - https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** raster module api reference

---

## 📚 docsearch results (top 5)

#### r1 — score 0.497

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['api', 'parameters', 'raster', 'sampling']

**Full text:**

```
losest_time : time used to filter rasters to be sampled; only the raster that is closest in time to the provided time will be sampled - can be multiple rasters if they all share the same time (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z) use_poi_time : overrides the âclosest_timeâ setting (or provides one if not set) with the time associated with the point of interest being sampled doy_range : day of year range to seasonally filter data target_crs : override the CRS of the raster dataset being sampled proj_pipeline : override the PROJ pipeline used to transform the source dataset into the CRS of the target dataset CRS to sample that dataset url : user provided URL of a raster dataset to sample aoi_bbox : area of interest bounding box to help PROJ select the best transform force_single_sample : forces the sampling code to select (or generate) a single value for the returned sample values; this has the result of changing the column type of the returned dataframe from being a list to being a single double-precision element; the available options are: first, last, min, max, mean, median; note that when mean or median are selected, the only valid sampled data returned is value , all other sample columns should be ignored catalog : geojson formatted stac query response (obtained through the sliderule.earthdata.stac Python API) bands : list of bands to read out of the raster, or a predefined algorithm that combines bands for a given dataset elevation_bands : list of ban
```

#### r2 — score 0.701

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['parameters', 'raster', 'sampling']

**Full text:**

```
To request raster sampling, the samples parameter must be populated as a dictionary in the request.
```

#### r3 — score 0.442

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-3.3: Advanced Mode
- **category:** `developer_guide`
- **matched_tokens:** ['api', 'raster', 'sampling']

**Full text:**

```
In advanced mode, the control panel shall display the following controls All control elements present in basic mode Resource query parameter controls specific to the API that has been selected that allow a user to make a processing request without an area of interest A list of parameter controls specific to the API that has been selected; the parameter controls are grouped into exandable category sets (e.g. there might be a âPhoton Classificationâ category with a expansion carrot next to it that once expanded displays a list of selection boxes for each of the photon classifiers supported by SlideRule) A list of selection controls for the different raster datasets that can be sampled as a part of the current processing request. A list of sampling parameter controls used to sample the selected rasters; only displayed once at least one raster is selected for sampling S3 output parameter controls to support the user requesting that the output be written to an S3 bucketâ to include their AWS S3 write credentials, S3 bucket, and output format information
```

#### r4 — score 0.442

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-3.3: Advanced Mode
- **category:** `developer_guide`
- **matched_tokens:** ['api', 'raster', 'sampling']

**Full text:**

```
In advanced mode, the control panel shall display the following controls All control elements present in basic mode Resource query parameter controls specific to the API that has been selected that allow a user to make a processing request without an area of interest A list of parameter controls specific to the API that has been selected; the parameter controls are grouped into exandable category sets (e.g. there might be a âPhoton Classificationâ category with a expansion carrot next to it that once expanded displays a list of selection boxes for each of the photon classifiers supported by SlideRule) A list of selection controls for the different raster datasets that can be sampled as a part of the current processing request. A list of sampling parameter controls used to sample the selected rasters; only displayed once at least one raster is selected for sampling S3 output parameter controls to support the user requesting that the output be written to an S3 bucketâ to include their AWS S3 write credentials, S3 bucket, and output format information
```

#### r5 — score 0.494

- **url:** https://docs.slideruleearth.io/user_guide/raster_sampling.html
- **title:** Raster Sampling
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['parameters', 'raster', 'sampling']

**Full text:**

```
Each key in the dictionary is used to label the data returned for that raster in the returned DataFrame. samples : dictionary of rasters to sample <key> : user supplied name used to identify results returned from sampling this raster asset : name of the raster (as supplied in the Asset Directory) to be sampled algorithm : algorithm to use to sample the raster; the available algorithms for sampling rasters are: NearestNeighbour, Bilinear, Cubic, CubicSpline, Lanczos, Average, Mode, Gauss radius : the size of the kernel in meters when sampling a raster; the size of the region in meters for zonal statistics zonal_stats : boolean whether to calculate and return zonal statistics for the region around the location being sampled slope_aspect : boolean whether to calculate slope and aspect for the region around the location being sampled slope_scale_length : the size of the region in meters to use when calculating the slope and aspect with_flags : boolean whether to include auxiliary information about the sampled pixel in the form of a 32-bit flag t0 : start time for filtering rasters to be sampled (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z) t1 : stop time for filtering rasters to be sampled (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z) substr : substring filter for rasters to be sampled; the raster will only be sampled if the name of the raster includes the provided substring (useful for datasets that have multiple rasters for a given geolocation to be sampled) c
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.352

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 72
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 72
- **matched_tokens:** ['function', 'parameters', 'sampling']

**Full text:**

```
The
1233 background rate is provided in ATL03 on a 50-shot sampling interval; we convert this to the per-
1234 PE rate by interpolating as a function of delta_time.
1235
1236 5.3 Processing Procedure for Parameters
1237 In this section, we give pseudocode for the calculation of ATL06 parameters. The flow chart for
1238 this process is summarized in Figure 5-1. The code is made up of several functions that call one
1239 another, following the process described in Section 5.1.
1240
60
```

#### r2 — score 0.304

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.4.2.1 /atlas_impulse_response/pce1_spot1 or /pce2_spot3
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 28
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
These parameters are described in section 7.3,
and are all posted at the 200-Hz rate.
2.4.1.5 Group: /gtx/signal_find_output
This subgroup contains the outputs of the signal finding algorithm that are not provided at the
photon rate, such as information related to the time interval boundaries along-track that were
used to identify signal photons, or the mean and standard deviation of the background count rate
used to determine thresholds for signal identification. These parameters are detailed in section
5.1.3, and are also described in Table 5-4.
2.4.2 Group: /atlas_impulse_response
Several of the higher-level data products use a deconvolution approach to further refine selection
of signal photons and reject background photons. These algorithms require knowledge of the
ATLAS instrument response over their algorithms’ along-track aggregation distance. While the
pulse spreading effects of the ATLAS instrument are expected to change slowly over time,
changes in the outgoing laser pulse shape are likely to vary over shorter timescales. In the two
subgroups, we provide parameters from two different sources to evaluate change in the ATLAS
impulse response function.
2.4.2.1 /atlas_impulse_response/pce1_spot1 or /pce2_spot3
The second group of parameters are derived from photon events detected via the transmitter echo
path (TEP). These photons are picked off from the transmitted laser pulse, and routed into the
ATLAS receiver, for two of the ATLAS strong beams.
```

#### r3 — score 0.316

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.5.2 Solution Approach
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 63
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
height distribution, and the subsurface distribution, are resolved together within the
deconvolution scheme.
A key element in the implementation is that each bin (5 cm width) of the IRF is convolved with
the model. This is shown in Figure 4-6 for the particular MABEL response function during a
2012 flight over the Chesapeake Bay.
Figure 4-6 Constrained Deconvolution Method- Unit water surface response for one 5cm MABEL bin, arbitrarily
selected as 6450 mm.
In the example, a Gaussian water surface height distribution is assumed with an exponential
subsurface decay. Figure 4-6 shows MABEL bin 6450, with a normalized frequency of 0.0600,
convolved with the model and an initial set of assumed parameters, resulting in a unit water
response associated with that bin. Figure 4-7 shows the full convolution of all MABEL bins
which are then summed and compared to the original MABEL observation. The optimal solution
occurs when the convolved model best fits the observed data. The best fit analysis that partitions
40
Release 007, January 31, 2025
```

#### r4 — score 0.281

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 2.3.3 The Multiple Altimeter Beam Experimental Lidar (MABEL)
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 44
- **matched_tokens:** ['sampling']

**Full text:**

```
The figures indicate raw MABEL
geolocated photon clouds. Given that the MABEL instrument sampling design scales well with
ATLAS, it has proven to be an important instrument for testing the ATL13 algorithm, described
in Chapter 6 (Jasinski et al., 2016).
21
Release 007, January 31, 2025
```

#### r5 — score 0.288

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.5.2 Solution Approach
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 62
- **matched_tokens:** ['function', 'parameters']

**Full text:**

```
Assigning the probability density function (pdf) of the instrument response function as x(t), and
the actual or true unit vertical distribution of the water signal photons per unit pulse as h(t), then
the integrated pdf of all signal photons returned to the receiver from the entire instrument
response function, y(t), can be written as the convolution of x(t) and h(t). In continuous form,
𝑡𝑡
𝑦𝑦(𝑡𝑡) = ∫ℎ(𝜏𝜏)𝑥𝑥(𝑡𝑡−𝜏𝜏)𝑑𝑑𝑑𝑑 0 (4.9)
In discrete form, (4.9) can be expressed
= Σ (4.10) yj hi-j xi
i = the number of instrument pulse bins and j is the number of output height bins. The yj
represents the histogram of the observed water photons for a given segment length, x i is the lidar
pulse histogram (IRF) measured over i bins. Finally, hi-j represents the actual or true unit water
surface response of the water, before bias correction.
4.5.2 Solution Approach
The solution to (4.10) is obtained by first assuming a functional form for the actual or unit water
column h(t) with unknown parameters. The h(t) and x(t) are then convolved over a range of
model parameters until a best fit of the model with the histogram of the observed signal photons
is achieved. Thus, the model parameters of the water column including the true water surface
39
Release 007, January 31, 2025
```

---

