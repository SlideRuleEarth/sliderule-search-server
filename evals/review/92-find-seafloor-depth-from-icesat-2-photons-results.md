# Row 92 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `92-find-seafloor-depth-from-icesat-2-photons-review.md` —
> verdicts go there, this side is read-only.

**Query:** `find seafloor depth from ICESat-2 photons`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `5. atl24`
  - `atl24x`
- **expected_pages:** (none)
- **notes:** atl24x bathymetry without ATL24 terminology

---

## 📚 docsearch results (top 5)

#### r1 — score 0.573

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['from', 'icesat', 'photons']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

#### r2 — score 0.560

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['from', 'icesat', 'photons']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r3 — score 0.480

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['from', 'icesat', 'photons']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r4 — score 0.516

- **url:** https://docs.slideruleearth.io/user_guide/articles/250328_atl24_golden_run.html
- **title:** 2025-03-28: ATL24 Processing Run
- **section:** Background
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'photons']

**Full text:**

```
The University of Texas at Austin and Oregon State University partnered with the SlideRule team (University of Washington, Goddard Space Flight Center, and Wallops Flight Facility) to develop and generate a Near-Shore Coastal Bathymetry Product for ICESat-2 called ATL24. The initial development and generation of the data product was kicked off in January of 2024, started in earnest in May of 2024, and completed April 1st, 2025. ATL24 is a photon classification for ICESat-2 photons in ATL03. Algorithms designed and implemented by UT and OSU were integrated into SlideRule and run as the atl24g service. Each processing request to atl24g provided an ATL03 granule and produced a corresponding ATL24 granule. All ATL03 version 006 photons within a global bathymetry search mask that were within 50m above and 100m below the geoid were processed and labelled as either: unclassified, sea surface, or bathymetry.
```

#### r5 — score 0.509

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.6 PhoREAL Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'photons']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Along track distance meters (double) dist_ph_along + segment_distance y_atc Across track distance meters (float) dist_ph_across photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags ground_photon_count Number of photons classified as ground in the segment vegetation_photon_count Number of photons classified as canopy or top of canopy in the segment landcover ATL08 land cover flags snowcover ATL08 snow cover flags solar_elevation Sun elevation as provided in ATL03 degrees (float) h_te_median Median ellipsoidal height of the ground photons meters (float) vertical datum controlled by parameters, default is ITRF2014 h_max_canopy Maximum relief height for canopy photons meters (float) h_min_canopy Minimum relief height for canopy photons meters (float) h_mean_canopy Mean relief height for canopy photons meters (float) h_canopy 98th percentile relief height for canopy photons meters (float) canopy_openness Standard deviation of relief height for canopy photons canopy_h_metrics relief height at given percentile for canopy p
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.661

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** C-SHELPh Classification
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 31
- **matched_tokens:** ['from', 'icesat', 'photons', 'seafloor']

**Full text:**

```
4.4.5 C-SHELPh Classification
The C-SHELPh (Classification of Sub-aquatic Height Extracted Photons) algorithm was
developed by Thomas et al. in the effort to provide an open source tool for producing
bathymetric maps (N. Thomas et al. 2022). The work, published in 2022, was one of the first
techniques for automating the extraction of ICESat-2 shallow-water, regional bathymetry. The initial success of the approach was demonstrated at the Great Bahamas Bank around
the island of Andros, Bahamas and included 224 ICESat-2 tracks. At its core, C-SHELPh detects the dense clustering of photons as typically these clusters
are indicative of surface returns. The density values are determined across a user specified
grid with the default values being 0.5 m in the vertical direction and 10 m in the horizontal
direction. This gridding convention provide surface heights and along-track latitudes. The
photon clusters around a height of 0 m are labeled to be the ocean surface photons and
surface height is estimated to be the median value of cluster. Photon clusters that occur
below the ocean surface value are identified via evaluation per-grid-cell basis relative to user
defined thresholds of the signal to noise. C-SHELPh proved very successful in the Caribbean
environment as the water has fairly low turbidity, the depths range from 0-10 m and the
seafloor is highly reflective; all of which provide an ideal scenario for density driven signal
finding.
```

#### r2 — score 0.644

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Scientific Theory
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 15
- **matched_tokens:** ['depth', 'icesat', 'seafloor']

**Full text:**

```
Beyond a certain depth that is typically referred to as the extinction depth, which is a
function of Kd, as well as system-dependent parameters contained in Eq. 1, the received
optical power drops below the detection threshold, and bathymetric measurement is infeasible. For ICESat-2 bathymetry, the extinction depth can often be approximated visually as the
point at which the seafloor returns peter out in a profile plot, such as Figure 2. In this
particular example, the seafloor points begin to approach extinction at approximately 30 m
(non-refraction-corrected).
8
```

#### r3 — score 0.626

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** ATL24 Input Variables
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 18
- **matched_tokens:** ['depth', 'from', 'icesat', 'photons', 'seafloor']

**Full text:**

```
ICESat-2 Inputs
Trained ML models
Ensemble Classi- Ensemble Photon Classifications - fication predicted sea surface (40), and
seafloor (41) photon labels
available from the classification
algorithms
Blunder Detection - heuristi- ICESat-2 input
Error Correction cally evaluates each photon classi-
fication against list of checks Photon Classifications
Refraction Correction - calcu-
Refraction Cor- lates final depths of bathymetry Refractive index of water
rection photons using refraction index and data layer
surface heights
ICESat-2 Inputs
Uncertainty Calculation - cal- VIIRS Kd490
Uncertainty Cal- culates the vertical and horizontal
culation uncertainty of each photon’s loca- Subaqueous Uncertainty
tion Look Up Tables
Photon Classifications
ATL24 Granule Writer -
writes h5 file
Final Outputs All previous outputs Quality Checker - heuris-
tically evaluates each h5 file and
determines quality assessment
Further description of the input components for the ATL24 processing workflow are listed
in Table 3. These include the other ICESat-2 data used in production of the product and the
independent data needed for processing implementation. An example is the refractive index of
water data layer which is a global mask produced for the refractive correction to the subaqueous
photon heights using temperature and salinity values from the E.U. Copernicus Marine Service
Multi Observation Global Ocean 3D Temperature, Salinity, Height, Geostrophic Current, and
Mixed Layer Depth (MLD) dataset.
```

#### r4 — score 0.639

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** Parameters Output from Signal Finding Algorithm
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 82
- **matched_tokens:** ['find', 'from', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Name Units Description Section
Zslbeg meters The heights, calculated from an estimated surface, Egap, or 5.1.4.2.5.2
H(t) in a slant reference frame corresponding to time_hb, the
beginning of the integration time used for one slant histogram
Zslend meters The heights, calculated from a estimated surface, Egap, or H(t) 5.1.4.2.5.2
in a slant reference frame corresponding to time_he the end of
the integration time used for one slant histogram
Table 5-3. Parameters Calculated Internally Within the Algorithm. Parameters Output from Signal Finding Algorithm
Name
Description Units ATBD Section
(dimension)
All values from table 5-2 used to drive the algorithm. Parameters output for each photon event selected:
Conf (number of Confidence level for each photon event (0: noise, 1: N/A 5.1.4.1.3,
photon events in added to pad likely signal photon events, 2: low 5.1.4.2.3.5
the cloud, n3) confidence signal, 3: medium confidence signal, 4: high
confidence signal)
Histogram parameters output for each time interval, Δtime, when signal photon events were selected. The parameters are from the histogram used to find the majority of the signal photons in Δtime. Some parameters are
surface-type specific.
```

#### r5 — score 0.651

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.4 Algorithm Implementation
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 85
- **matched_tokens:** ['find', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
After an initial height profile is formed, a histogram relative to a slope is performed to identify
any missed signal photons that were spread out over the slopes (section 5.1.4.2.5). The process is
slightly different for strong and weak beams. All additional signal photon events found are then
merged with the previously identified signal photon events. The lslant parameter determines subsequent steps for the strong beam segments. If lslant(isurf) is
set to one (e.g. land or land ice), two signal-finding steps are performed. First, additional signal
is sought by histogramming the photon heights relative to the surface defined by a set of running
linear fits to the signal photons identified by ellipsoidal histogramming (section 5.1.4.2.5.1). This
is referred to as slant histogramming. Second, if gaps in the profile greater than Δtime_gapmin
are still present, the algorithm identifies the time intervals over which these gaps occur (section
5.1.4.2.5.3) and then performs slant histogramming over the time interval of each identified gap,
systematically varying the slope along which the histogram is formed to find additional signal
(section 5.1.4.2.5). This step is referred to as variable slope slant histogramming. If lslant(isurf)
is set to zero, we assume the Earth’s surface is essentially flat (e.g. sea ice, ocean) and slant
histograming is not performed.
```

---

