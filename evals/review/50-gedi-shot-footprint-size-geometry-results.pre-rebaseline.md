# Row 50 results: nsidc / instrument

> Auto-generated. Open this file alongside `50-gedi-shot-footprint-size-geometry-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI shot footprint size geometry`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **expected_sections:** (none)
- **expected_pages:**
  - 1–20
- **notes:** GEDI L4A footprint geometry

---

## 📚 docsearch results (top 5)

#### r1 — score 0.662

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3. Returned data
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi', 'shot']

**Full text:**

```
The main kind of data returned by the GEDI APIs are elevation and vegetation measurements organized around the concept of a footprint . An footprint is a single laser shot reflection on the earth from one of GEDIâs laser beams and the resulting digitization and measurements made from it. Each footprint is uniquely identified by a shot number. The shot number is provided in the underlying source datasets and is consistent from request to request. This means subsequent runs of SlideRule with the same request parameters will return the same shot numbers.
```

#### r2 — score 0.557

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.2 L2A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation_lowestmode" : elevation in meters of reflection closest to the surface of the earth "elevation_highestreturn" : elevation in meters of reflection farthest from the surface of the earth "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

#### r3 — score 0.546

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.4 L4A Footprints
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi']

**Full text:**

```
The footprint data is stored along-track inside the GEDI granules. The data is read by SlideRule, organized into the individual footprints, subsetted to the area of interest specified by the user, and returned as a GeoDataFrame where each row is a footprint. "shot_number" : unique footprint identifier "time_ns" : UNIX timestamp, used as the index for the DataFrame "latitude" : latitude (-90.0 to 90.0) "longitude" : longitude (-180.0 to 180.0) "elevation" : elevation in meters of the surface of the earth "agbd" : above ground biodensity "solar_elevation" : solar elevation at time of measurement, in degrees "beam" : beam number "flags" : flags set for footprint (0x01: degrade, 0x02: l2 quality, 0x04: l4 quality, 0x80: surface)
```

#### r4 — score 0.488

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['footprint', 'gedi']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

#### r5 — score 0.288

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** Appendix A. Parameter Components
- **category:** `developer_guide`
- **matched_tokens:** ['gedi', 'size']

**Full text:**

```
Mission : dropdown or select button ICESat-2 GEDI ICESat-2 APIs : dropdown [ICESat-2] atl03s atl06 atl06s atl08 atl24s GEDI APIs : dropdown [GEDI] gedi01b gedi02a gedi04a General : accordion header Polygon : label Draw On Map : radio button Upload : radio button File Upload : file upload button Rasterize Polygon : checkbox Cell Size : input number (degrees) Ignore Polygon for CMR : checkbox Projection : label auto : radio button plate_carree : radio button north_polar : radio button south_polar : radio button Timeout : input number (seconds) rqst-timeout : input number (seconds) node-timeout : input number (seconds) read-timeout : input number (seconds) Granule Selection : accordion header [ICESat-2] Track : label 1 : checkbox 2 : checkbox 3 : checkbox all : checkbox / toggle others Beam : label gt1l : checkbox gt1r : checkbox gt2l : checkbox gt2r : checkbox gt3l : checkbox gt3r : checkbox all : checkbox / toggle others RGT : input number Cycle : input number Region : input number T0 : calendar T1 : calendar Photon Selection : accordion header [ICESat-2] ATL03 Confidence : input switch (enables inputs below) Surface Reference Type : label land : radio button ocean : radio button sea ice : radio button land_ice : radio button inland_water : radio button Signal Confidence : label tep : radio button not_considered : radio button background : radio button within_10m : radio button low : radio button medium : radio button high : radio button ATL08 Classification : input switch (en
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.498

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 6
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 6
- **matched_tokens:** ['footprint', 'gedi', 'size']

**Full text:**

```
Some of the allometric scaling models used to predict 𝑀𝑖 have a reported tree size
domain over which predictions are valid. These tree size domains are defined by the data used
to develop the equations (Chave et al., 2014; Forrester et al., 2017; Jenkins et al., 2003; Paul et
al., 2016; Roxburgh et al., 2019; Ung et al., 2008). If a footprint contained at least one tree with
a diameter, height, or wood specific gravity outside the range defined by the original data, the
footprint was excluded (640 footprints, or 5.27%).
3.2.5. Overlap between simulated footprints and field data
Some simulated GEDI footprints are not completely contained within the boundaries of
field-inventory plots. When this occurs, information about AGBD within the footprint is
incomplete. Previous work has demonstrated that inclusion of these observations in statistical
models causes relationships to be biased toward zero (Rejou-Mechain et al., 2014). If > 10% of
the area of a simulated footprint was outside the boundaries of a field inventory plot, it was
excluded (129 footprints, or 1.06%).
3.2.6. Large sample size
The data are organized into spatial units by project and then by plot. A project is single
contribution from a given research group. For example, La Selva, Costa Rica and Robson Creek,
Australia are individual projects. Some projects contain multiple plots.
```

#### r2 — score 0.492

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 11
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 11
- **matched_tokens:** ['footprint', 'gedi', 'size']

**Full text:**

```
When mapped individual stems are
available and the coordinates of a given stem are within the extent of the footprint, 𝑀𝑖, as
defined by a given allometric model, is assigned to the footprint. When stem positions are
unavailable, the mean AGBD in the square subplot is assigned to the footprint. Four
assumptions underpin this approach. First, across-beam laser intensity follows a Gaussian
distribution, but we ignore the impact of across-beam laser intensity on the relationship
between RH metrics and AGBD (Hofton & Blair, 2020; Hyde et al., 2005). Second, because the
across-beam laser intensity is Gaussian, intercepted surfaces > 12.5 m from the footprint center
contribute a small amount to the intensity of the returned laser waveform. For example,
assuming the across-beam σ is 5.5 m (Hancock et al., 2019) about 2.3% of the returned laser
energy on a uniform reflectance target orthogonal to the beam path is received from surfaces
beyond the 12.5 m threshold. The third and fourth assumptions address the size of GEDI
footprints relative to tree locations or subplots. A tree whose stem is outside the 12.5 m radius
used to assign 𝑀𝑖 to individual footprints could contribute to the simulated waveform if parts of
the tree crown are inside the footprint. Similarly, a tree whose stem coordinates are inside the
footprint has all of 𝑀𝑖 assigned to the footprint, even though some branch or crown material (a
portion of 𝑀𝑖) may be outside the extent of the simulated GEDI waveform.
```

#### r3 — score 0.458

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 19
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 19
- **matched_tokens:** ['footprint', 'gedi', 'size']

**Full text:**

```
For example, assuming the across-beam σ is 5.5 m (Hancock et al., 2019), about
2.3% of the returned laser energy on a uniform reflectance target with constant elevation is
received from surfaces beyond the 12.5 m threshold. The third and fourth assumptions address
the size of GEDI footprints relative to the trees within them. A tree whose stem is outside the
12.5 m radius used to assign 𝑀! to individual footprints could contribute to the simulated
waveform if parts of the tree crown are inside the footprint. Similarly, a tree whose stem
coordinates are inside the footprint has all of 𝑀! assigned to the footprint, even though some
branch or crown material (a portion of 𝑀!) may be outside the extent of the simulated GEDI
waveform.
18
```

#### r4 — score 0.438

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 14
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 14
- **matched_tokens:** ['footprint', 'gedi', 'size']

**Full text:**

```
specific gravity outside the range defined by the original authors, the footprint was excluded
(640 footprints, or 5.27%).
3.2.5. Overlap between simulated footprints and field data
Some simulated GEDI footprints are not completely contained within the boundaries of
field-inventory plots. When this occurs, information about AGBD within the footprint is
incomplete. Previous work has demonstrated that inclusion of these observations in statistical
models causes relationships to be biased toward zero (Rejou-Mechain et al., 2014). If > 10% of
the area of a simulated footprint was outside the boundaries of a field inventory plot, it was
excluded from the FSBD (129 footprints, or 1.06%).
3.2.6. Large sample size
Data in the FSBD were contributed by numerous researchers without whom the
development of comprehensive GEDI04_A models would not be possible. The data are
organized into spatial units by project and then by plot. A project is single contribution from a
given research group. For example, La Selva, Costa Rica and Robson Creek, Australia are
individual projects. Some projects contain multiple plots. Because the number and size of plots is
variable, a small number of large, stem-mapped plots contribute disproportionately to the total
number of observations in the FSBD.
```

#### r5 — score 0.476

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 42
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 42
- **matched_tokens:** ['gedi', 'shot']

**Full text:**

```
Figure S1. GEDI04_A algorithm flow. The GEDI04_A algorithm assimilates external data from
GEDI02_A and other sources. A prediction is generated for every GEDI shot where
algorithm_run_flag = 1. The algorithm looks up the GEDI04_A model using a world region grid
and error-corrected and infilled MODIS MCD12Q1 PFT (see Fig. 2, main text). xvar is the
transformed and scaled predictor data (GEDI02_A RH metrics). agbd and associated uncertainty
are outputs of the GEDI04_A algorithm for every GEDI02_A algorithm selection setting.
42
```

---

