# Row 42 results: nsidc / product_disambiguation

> Auto-generated. Open this file alongside `42-atl08-dragann-noise-filtering-algorithm-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL08 DRAGANN noise filtering algorithm`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** DRAGANN is ATL08-specific

---

## 📚 docsearch results (top 5)

#### r1 — score 0.402

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'noise']

**Full text:**

```
The ATL06-SR algorithm fits a line segment to the photons in each extent, using an iterative selection refinement to eliminate noise photons not correctly identified by the photon classification. The results are then checked against three parameters : sigma_r_max , which eliminates segments for which the robust dispersion of the residuals is too large, and the ats and cnt parameters described above, which eliminate segments for which the iterative fitting has eliminated too many photons. The algorithm is run by supplying the fit parameter in the processing request, but can also be run via the legacy atl06 and atl06p endpoints.
```

#### r2 — score 0.331

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6.2 ATL08-PhoREAL Ancillary Data
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'noise']

**Full text:**

```
Ancillary data returned from the atl08 and atl08p APIs come from the land_segments group of the ATL08 granules. The data goes through a series of processing steps before being returned back to the user as per-extent (i.e. variable-length segment) result values. When a user requests an ATL08 ancillary field, the ATL08 classifications are automatically enabled with all unclassified photons filtered out (i.e. noise, ground, canopy, and top of canopy are included; unclassified photons are excluded). If the user is also requesting PhoREAL processing, then noise photons are automatically filtered out as well. Lastly, if the user manually specifies which ATL08 photon classifications to use, then that manual specification takes precedence and is used. If a user manually specifies that unclassified photons are to be included, the value used for an ancillary field for that photon has all 1âs in the binary encoding of that value. For example, if it is an 8-bit unsigned integer, the value would be 255. If it is a double-precision floating point, the value would be -nan. Since the ATL08 APIs return per-extent values and not per-photon values, the set of per-photon ancillary field values must be reduced in some way to a single per-extent value to be returned back to the user. There are currently two options available for how this reduction occurs. Nearest Neighbor (Mode): the value that appears most often in the extent is selected. This is the default method.
```

#### r3 — score 0.326

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.3 ATL08 Classification
- **category:** `user_guide`
- **matched_tokens:** ['atl08', 'filtering']

**Full text:**

```
If ATL08 classification parameters are specified, the ATL08 (vegetation height) files corresponding to the ATL03 files are queried for the more advanced classification scheme available in those files. Photons are then selected based on the classification values specified. Note that srt=0 (land) and cnf=0 (no native filtering) should be specified to allow all ATL08 photons to be used. atl08_class : list of ATL08 classifications used to select which photons are used in the processing (the available classifications are: âatl08_noiseâ, âatl08_groundâ, âatl08_canopyâ, âatl08_top_of_canopyâ, âatl08_unclassifiedâ)
```

#### r4 — score 0.283

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl08
- **category:** `api_reference`
- **matched_tokens:** ['algorithm', 'atl08']

**Full text:**

```
sliderule.icesat2. atl08 ( parm , resource ) [source] Performs ATL08-PhoREAL processing on ATL03 and ATL08 data and returns geolocated elevations Parameters : parms ( dict ) â parameters used to configure ATL06-SR algorithm processing (see Parameters ) resource ( str ) â ATL03 HDF5 filename Returns : geolocated vegatation statistics Return type : GeoDataFrame
```

#### r5 — score 0.308

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl08']

**Full text:**

```
The PhoREAL algorithm is a modified version of the ATL08 canopy metrics algorithm developed at the University of Texas at Austin that calculates canopy metrics on a segment of ATL03 photons. The algorithm is run by supplying the phoreal parameter in the atl03x request, but can also be accessed via the legacy endpoints atl08 and atl08p .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.624

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 15
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['algorithm', 'atl08', 'dragann', 'filtering', 'noise']

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

#### r2 — score 0.551

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 95
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 95
- **matched_tokens:** ['algorithm', 'atl08', 'dragann', 'filtering', 'noise']

**Full text:**

```
1768 4 ALGORITHM IMPLEMENTATION
1769 Prior to running the surface finding algorithms used for ATL08 data products, the
1770 superset of output from the GSFC medium-high confidence classed photons (ATL03
1771 signal_conf_ph: flags 3-4) and the output from DRAGANN will be considered as the input
1772 data set. ATL03 input data requirements include the along-track time, latitude, longitude,
1773 height, and classification for each photon. The motivation behind combining the results
1774 from two different noise filtering methods is to ensure that all of the potential signal
1775 photons for land surfaces will be provided as input to the surface finding software. Prior to
1776 running DRAGANN, reject telemetry bins that occur 150m above or below the reference
1777 DEM. Rejection of these noise blocks will ensure a better parameterization of DRAGANN.
1778 Some additional quality checks are also described here prior to implementing the
1779 ATL08 software. The first check utilizes the POD_PPD flag on ATL03. In instances where
1780 the satellite is maneuvering or the pointing/ranging solutions are suspect, ATL08 will not
1781 use those data. Thus, data will only flow to the ATL08 algorithm when the POD_PPD flag
1782 is set to 0 which indicates ‘nominal’ conditions.
1783 A second quality check pertains to the flags set on the ATL03 photon quality flag
1784 (quality_ph).
```

#### r3 — score 0.588

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 2
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 2
- **matched_tokens:** ['atl08', 'dragann', 'filtering']

**Full text:**

```
Reference source not
found.)
2017 July Revised alternative DRAGANN methodology (see bolded text
in Sec 4.3.1)
2017 July Added post-DRAGANN filtering methodology (Sec 4.9)
2017 July Updated SNR to be estimated from superset of ATL03 and
DRAGANN found signal used for processing ATL08 (Sec
2.5.18)
2017 September More details added to DRAGANN description (Sec 4.3), and
corrections to DRAGANN implementation (Sec 3.1.1, Sec 4.3
(9))
2017 September Added Appendix A – very detailed DRAGANN description
2017 September Revised alternative DRAGANN methodology (see bolded text
in Sec 4.3.1)
2017 September Clarified SNR calculation (Sec 2.5.18, Sec 4.3 (18))
2017 September Added cloud flag filtering option
2017 September Added top of canopy median surface filter (Sec 3.5 (a), Sec
4.12 (3), Sec 4.14 (1-3))
2
```

#### r4 — score 0.486

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 57
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 57
- **matched_tokens:** ['atl08', 'dragann', 'filtering', 'noise']

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

#### r5 — score 0.458

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 102
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 102
- **matched_tokens:** ['algorithm', 'atl08', 'dragann', 'filtering', 'noise']

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

---

