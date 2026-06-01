# Row 72 results: docsearch / identifier

> Auto-generated. Open this file alongside `72-phoreal-algorithm-parameters-atl08-review.md` —
> verdicts go there, this side is read-only.

**Query:** `phoreal algorithm parameters atl08`
**Panel signature:** `1aaf3f65b455`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `1.6 phoreal`
  - `phoreal algorithm`
- **expected_pages:** (none)
- **notes:** PhoREAL algorithm block

---

## 📚 docsearch results (top 5)

#### r1 — score 0.505

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl08
- **category:** `api_reference`
- **matched_tokens:** ['algorithm', 'atl08', 'parameters', 'phoreal']

**Full text:**

```
sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame
```

#### r2 — score 0.567

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl08', 'phoreal']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

#### r3 — score 0.412

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'parameters', 'phoreal']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r4 — score 0.400

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.1 PhoREAL Parameters
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'parameters', 'phoreal']

**Full text:**

```
The PhoREAL parameters are supplied in user requests under the phoreal key and include: phoreal : binsize : size of the vertical photon bin in meters geoloc : algorithm to use to calculate the geolocation (latitude, longitude, along-track distance, and time) of each custom length PhoREAL segment; âmeanâ - takes the average value across all photons in the segment; âmedianâ - takes the median value across all photons in the segment; âcenterâ - takes the halfway value calculated by the average of the first and last photon in the segment use_abs_h : boolean whether the absolute photon heights are used instead of the normalized heights send_waveform : boolean whether to send to the client the photon height histograms in addition to the vegetation statistics above_classifier : boolean whether to use the ABoVE photon classifier when determining top of canopy photons
```

#### r5 — score 0.408

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v04-01-00.html
- **title:** Release v4.1.x
- **section:** Release v4.1.x
- **category:** `release_notes`
- **matched_tokens:** ['algorithm', 'phoreal']

**Full text:**

```
2023-12-07 Version description of the v4.1.0 release of ICESat-2 SlideRule. * Important : This version requires an update of the Python client to use. The underlying mechanism used in support of including ancillary fields in processing requests was updated to support both the PhoREAL algorithm and the ATL06 subsetter. As a result, in order to include ancillary field requests in your code, you must have the latest client installed. No changes are needed to the code in your scripts.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.394

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 99
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 99
- **matched_tokens:** ['algorithm', 'atl08', 'parameters']

**Full text:**

```
1814 algorithm, ideally all clouds would be identified prior to processing through the
1815 ATL08 algorithm. There will be instances, however, where low lying clouds (e.g.
1816 <800 m above the ground surface) may be difficult to identify. Currently, ATL08
1817 provides an ATL09 derived cloud flag (layer_flag) on its 100 m product and
1818 encourages the user to make note of the presence of clouds when using ATL08
1819 output. Unfortunately at present, a review of on-orbit data from ATL03 and ATL09
1820 indicate that the cloud layer flag is not being set correctly in the ATL09 algorithm.
1821 Ultimately, the final cloud based filtering process used in the ATL08 algorithm will
1822 most likely be derived from parameters/flag on the ATL09 data product. Until the
1823 ATL09 cloud flags are proven reliable, however, a preliminary cloud screening
1824 method is presented below. This methodology utilizes the calibrated attenuated
1825 backscatter on the ATL09 data product to identify (and subsequently remove for
1826 processing) clouds or other problematic issues (i.e. incorrectly telemetered
1827 windows). Using this new method, telemetered windows identified as having either
1828 low or no surface signal due to the presence of clouds (likely situated above the
1829 telemetered band), as well as photon returns suspected to be clouds instead of
1830 surface returns, will be omitted from the ATL08 processing.
```

#### r2 — score 0.469

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 15
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['algorithm', 'atl08']

**Full text:**

```
169 4.2 Preparing ATL03 data for input to ATL08 algorithm ......................................... 101
170 4.3 Noise filtering via DRAGANN ........................................................................................ 102
171 4.3.1 DRAGANN Quality Assurance .............................................................................. 105
172 4.3.2 Preprocessing to dynamically determine a DRAGANN parameter ..... 106
173 4.3.3 Iterative DRAGANN processing ........................................................................... 109
174 4.4 Compute Filtering Window ............................................................................................ 110
175 4.5 Identification of single surface ..................................................................................... 110
176 4.6 Look for potential ground photons ............................................................................ 112
177 4.7 De-trend Data ....................................................................................................................... 115
178 4.8 Detect fog conditions and bypass photon classification .................................... 116
179 4.9 Filter outlier noise from signal ..................................................................................... 118
180 4.10 Finding the initial ground estimate ............................................................................ 118
181 4.11 Find the top of the canopy .......................
```

#### r3 — score 0.436

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 102
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 102
- **matched_tokens:** ['algorithm', 'atl08']

**Full text:**

```
1903 c. All other segments that are not extended will report a last_seg_extend
1904 value of 0.
1905 4. Add a buffer of 200 m (or 10 segment_id's) to both ends of each L-km
1906 segment. The total processing segment length is (L-km + 2*buffer), but will
1907 be referred to as L-km segments for simplicity.
1908 a. The first L-km segment from an ATL03 granule would only have a
1909 buffer at the end, and the last L-km segment from an ATL03 granule
1910 would only have a buffer at the beginning.
1911 5. The input data for ATL08 algorithm is X, Y, Z, T (where T is time).
1912
1913 4.3 Noise filtering via DRAGANN
1914 DRAGANN will use ATL03 photons with all signal classification flags (0-4). These
1915 will include both signal and noise photons. This section give a broad overview of the
1916 DRAGANN function. See Appendix A for more details.
1917 1. Determine the relative along-track time, ATT, of each geolocated photon
1918 from the beginning of each L-km segment.
1919 2. Rescale the ATT with equal-time spacing between each data photon, keeping
1920 the relative beginning and end time values the same.
1921 3. Normalize the height and rescaled ATT data from 0 – 1 for each L-km
1922 segment based on the min/max of each field. So, normtime = (time -
1923 mintime)/(maxtime - mintime).
1924 4. Build a kd-tree based on normalized Z and normalized and rescaled ATT.
1925 5. Determine the search radius starting with Equation 3.1.
```

#### r4 — score 0.411

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 101
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 101
- **matched_tokens:** ['algorithm', 'atl08']

**Full text:**

```
1874
1875 4.2 Preparing ATL03 data for input to ATL08 algorithm
1876 1. Alignment of weak and strong beam against to the ATL09 data product to aid
1877 in noise photon rejection based on segment distance (along-track distance
1878 from equator) within ATL08.
1879 2. At times, cloud attenuation will lead to a reduced L-km with a length that is
1880 not a multiple of 100 meters. If the last 100m land segment of the L-km
1881 segment contains fewer than 5 ATL03 20m geosegments and the current L-
1882 km segment is not the last one of the granule, do not report output for this
1883 last 100m land segment. Retain the starting geosegment of this land segment
1884 and begin the next L-km segment here.
1885 3. Break up data into L-km segments. Segments equivalent of 10 km in along-
1886 track distance of an orbit would be appropriate.
1887 a. If the last portion of an ATL03 granule being processed would result
1888 in an L-km segment with less than 3.4 km (170 geosegments) worth of
1889 data, that last portion is added to the previous L-km processing
1890 window to be processed together as one extended L-km processing
1891 segment.
1892 i. The resulting last_seg_extend value would be reported as a
1893 positive value of distance beyond 10 km that the ATL08
1894 processing segment was extended by.
1895 b.
```

#### r5 — score 0.385

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 57
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 57
- **matched_tokens:** ['atl08', 'parameters']

**Full text:**

```
1047 2.3.5 DRAGANN_flag
1048 (parameter = d_flag). Flag indicating the labeling of DRAGANN noise filtering for
1049 a given photon. 0 = noise, 1=signal.
1050
1051 2.4 Subgroup: Reference data
1052 The reference data subgroup contains parameters and information that are
1053 useful for determining the terrain and canopy heights that are reported on the
1054 product. In addition to position and timing information, these parameters include the
1055 reference DEM height, reference landcover type, and flags indicating water or snow.
1056 Table 2.4. Summary table for reference parameters for the ATL08 product. Group Data Type Description Source
segment_id_beg Integer First along-track segment_id ATL03
number in 100-m segment
segment_id_end Integer Last along-track segment_id ATL03
number in 100-m segment
latitude Float Center latitude of signal ATL03
photons within each segment
longitude Float Center longitude of signal ATL03
photons within each segment
delta_time Float Mid-segment GPS time in ATL03
seconds past an epoch.
```

---

