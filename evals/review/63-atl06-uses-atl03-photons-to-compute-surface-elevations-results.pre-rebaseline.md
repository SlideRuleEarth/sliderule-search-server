# Row 63 results: nsidc / cross_product

> Auto-generated. Open this file alongside `63-atl06-uses-atl03-photons-to-compute-surface-elevations-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL06 uses ATL03 photons to compute surface elevations algorithm`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl06-v006-userguide.pdf
- **expected_sections:**
  - `surface`
  - `elevations`
  - `data groups`
- **expected_pages:**
  - 20–50
- **notes:** cross-product: ATL06 ingests ATL03

---

## 📚 docsearch results (top 5)

#### r1 — score 0.613

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['atl03', 'atl06', 'elevations', 'photons', 'surface']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r2 — score 0.701

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03', 'atl06', 'photons']

**Full text:**

```
The SlideRule atl03x endpoint provides a service for ATL03 custom processing. This endpoint queries ATL03 input granules for photon heights and locations based on a set of photon-input parameters that select geographic and temporal ranges. It then selects a subset of these photons based on a set of photon classification parameters, and divides these selected photons into short along-track extents, each of which is suitable for generating a single height estimate. These extents may be returned to the client, or may be passed to downstream algorithms like the ATL06-SR height-estimation module, or the PhoREAL algorithm.
```

#### r3 — score 0.674

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'photons', 'surface']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.3.2 . Built with Sphinx using a theme provided by Read the Docs .
```

#### r4 — score 0.560

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'atl06', 'elevations', 'surface']

**Full text:**

```
The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of segments for each beam. In SlideRule the average segment elevations will not be corrected for transmit pulse shape biases or first photon biases as compared to the higher level data products.
```

#### r5 — score 0.557

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.1 Segmented Photon Data - atl03sp
- **category:** `user_guide`
- **matched_tokens:** ['algorithm', 'atl03', 'atl06', 'uses']

**Full text:**

```
The photon data is stored as along-track segments inside the ATL03 granules, which is then broken apart by SlideRule and re-segmented according to processing parameters supplied at the time of the request. The new segments are called extents . When the length of an extent is 40 meters, and the step size is 20 meters, the extent matches the ATL06 segments. Most of the time, the photon extents are kept internal to SlideRule and not returned to the user. But there are some APIs that do return raw photon extents for the user to process on their own. Even though this offloads processing on the server, the API calls can take longer since more data needs to be returned to the user, which can bottleneck over the network. Photon extents are returned as GeoDataFrames where each row is a photon. Each extent represents the data that the ATL06 algorithm uses to generate a single ATL06 elevation. When the step size is shorter than the length of the extent, the extents returned overlap each other which means that each photon is being returned multiple times and will be duplicated in the resulting GeoDataFrame.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.689

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** OpenOceans++ Classification
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 28
- **matched_tokens:** ['algorithm', 'atl03', 'compute', 'elevations', 'photons', 'surface']

**Full text:**

```
Algorithm 3 OO++ General Algorithm
Input: ATL03 track consisting of a list of photons. Each photon contains an along-track distance,
x, and an elevation, z. Output: ATL24 track, where each photon has an associated classification (unclassified, sea surface,
or bathymetry), an estimate of the sea surface elevation at that photon’s along-track distance,
and an estimate of the bathymetry elevation at that photon’s along-track distance.
1. Compute a surface elevation estimate for the entire collection of photons. This estimate is
used as an input to the surface and bathymetry detection algorithms in steps 3b and 3d.
(a) Filter photons that are beyond a threshold distance (e.g. ±20 meters) from zero mean
sea level elevation
(b) Calculate the median elevation of the filtered photons
(c) Filter the photons again that are beyond a threshold distance (e.g. ±1 meter) from the
median elevation
(d) Compute the median elevation of the second set of filtered photons. This is the initial
surface estimate for the entire set of photons.
2. Partition the photons into along-track bins whose boundaries are spaced at, for example, 10
meter intervals.
3. For each along-track bin
(a) Identify sea surface photons in the bin. See Algorithm 4 below for a description of the
sea surface identification algorithm.
(b) Compute the surface estimate for this bin by taking the average of all photon elevations
identified as sea surface.
```

#### r2 — score 0.668

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.1 Introduction
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 64
- **matched_tokens:** ['algorithm', 'atl03', 'photons', 'surface', 'uses']

**Full text:**

```
The ground tracks of
a strong and weak beam pair are essentially parallel to each other, and separated by ~90 meters
in the across-track direction, so the slopes of the resultant surface profiles should be very similar. Therefore for the weak beam of each pair, the algorithm uses the surface profile found in the
strong beam to guide slant histogramming in the weak beam. Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03
data product have provided guidance regarding the fidelity to which the ATL03 algorithm needs
to discriminate signal and background photon events. In general, each higher-level data product
requires ATL03 to identify likely signal photon events within +/- 10 meters of the surface. Since
this algorithm uses histograms, the vertical resolution at which signal photons are selected is
directly proportional to the histogram bin size. All photons in any one bin are either classified as
48 Release Date: Fall 2022
```

#### r3 — score 0.661

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 3 SOFTWARE AND TOOLS
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 21
- **matched_tokens:** ['algorithm', 'atl03', 'photons', 'surface', 'uses']

**Full text:**

```
Authors of each of the higher-level surface-specific ICESat-2 ATBDs that draw on the ATL03 data
product have provided guidance regarding the fidelity to which the ATL03 algorithm needs to
discriminate signal and background photon events. In general, each higher-level data product
requires ATL03 to identify likely signal photon events within ±10 meters of the surface. Because the
signal-finding algorithm uses histograms, the vertical resolution at which signal photons are
selected is directly proportional to the histogram bin size. All photons in any one bin are either
classified as signal or background events. One of the goals of the algorithm is to use the smallest
bin size for which signal can be found to classify photons at the finest resolution possible. Test
cases indicate that this resolution meets or exceeds the needs of the higher-level data products in
all but very weak signal conditions. This smallest bin size varies as a function of surface slope and
background count rate (see ATL03 ATBD | Section 5.1).
3 SOFTWARE AND TOOLS
PhoREAL is a free library of geospatial analysis tools and source code written specifically for
working with ATL03 (and ATL08) data. Page 20 of 22National Snow and Ice Data Center
nsidc.org
```

#### r4 — score 0.634

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl08-v006-userguide.pdf
- **title:** ATL08 v006 user guide
- **section:** 2.3.1 Noise Filtering
- **category:** `user_guide`
- **source_product:** `ATL08` · **page:** 15
- **matched_tokens:** ['algorithm', 'atl03', 'photons', 'surface', 'uses']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L3A Land and Vegetation Height, Version 6
Processing
To detect both the canopy surface and the underlying topography, the ATL08 software has been
designed to accept multiple approaches to capture both the upper and lower surface signal
photons. The algorithm utilizes iterative photon filtering in the along-track direction, which best
preserves signal photons returned from the canopy and topography while rejecting noise photons. The following sections outline the approach implemented by the algorithm. More detailed
descriptions are available in "Section 3 | Algorithm Methodology" and "Section 4 | Algorithm
Implementation" of the ATBD for ATL08.
2.3.1 Noise Filtering
Removing solar background photons represents one of the biggest challenges with photon
counting lidar data. The ATL03 signal finding approach uses a histogramming strategy that places
photons into vertical bins along a consistent horizontal span and then assumes the signal lies
within the bins that contain the highest number of photons. This method works well over simple
surfaces such as ice sheets; however, photons that are reflected from the top of the canopy in
vegetated areas are not always flagged as signal.
```

#### r5 — score 0.623

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 188
- **matched_tokens:** ['algorithm', 'atl03', 'photons', 'surface', 'uses']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
/ancillary_data/gtx/signal_find Group contains the setup parameters for the signal finding ATL03, Section
_input algorithm. All parameters have dimension of 5,1 5, Table 5-2
corresponding with the 5 different surface types.
alpha_max FLOAT maximum slope radians Maximum slope allowed for ATL03, Section
slant histogram; if larger than 5, αmax
this then don’t attempt to fill
gap.
alpha_inc FLOAT slope increment radians Increment by which the slope is ATL03, Section
varied for slant histogramming 5,
over large gaps. αinc
sig_find_t_inc FLOAT histogram time seconds Time increment the algorithm ATL03, Section
increment uses to step through the 5, Δtime
photon cloud in a granule. Histograms are formed at each
Δtime to identify signal photon
events.
delta_t_gap_min FLOAT minimum delta seconds Minimum size of a time gap in ATL03, Section
time gap the height profile over which to 5, Δtime_gapmin
use variable slope slant
histogramming.
delta_t_lin_fit FLOAT linear fit time seconds Time span over which to ATL03, Section
increment perform a running linear fit to 5, Δt_linfit_edit
identified signal photon events
when editing outliers.
```

---

