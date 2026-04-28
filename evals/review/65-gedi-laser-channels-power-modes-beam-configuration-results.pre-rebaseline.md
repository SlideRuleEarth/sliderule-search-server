# Row 65 results: nsidc / instrument

> Auto-generated. Open this file alongside `65-gedi-laser-channels-power-modes-beam-configuration-review.md` —
> verdicts go there, this side is read-only.

**Query:** `GEDI laser channels power modes beam configuration`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
  - https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **expected_sections:** (none)
- **expected_pages:**
  - 1–20
- **notes:** GEDI instrument basics

---

## 📚 docsearch results (top 5)

#### r1 — score 0.351

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3. Returned data
- **category:** `user_guide`
- **matched_tokens:** ['gedi', 'laser']

**Full text:**

```
The main kind of data returned by the GEDI APIs are elevation and vegetation measurements organized around the concept of a footprint . An footprint is a single laser shot reflection on the earth from one of GEDIâs laser beams and the resulting digitization and measurements made from it. Each footprint is uniquely identified by a shot number. The shot number is provided in the underlying source datasets and is consistent from request to request. This means subsequent runs of SlideRule with the same request parameters will return the same shot numbers.
```

#### r2 — score 0.283

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['beam', 'laser']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r3 — score 0.331

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-02-00.html
- **title:** Release v3.2.x
- **section:** Development Updates
- **category:** `release_notes`
- **matched_tokens:** ['beam', 'gedi']

**Full text:**

```
The use_poi_time parameter was added to the raster sampling requests; when set to true, the only raster sampled is the one closest in time to the icesat2 or gedi data point. This is different than the closest_time parameter which is a single fixed time that is provided in the request. For the use_poi_time, the time for each row in the DataFrame is used to select the raster closest in time to that row. There were significant optimizations in retrieving rasters that intersect a point of interest GEDI beam selection can be provided as a list GEDU beam sensitivity returned as part of the GeoDataFrame (for gedi04a and gedi02a ) Raster sampling documentation updated with more details
```

#### r4 — score 0.345

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 2. Parameters
- **category:** `user_guide`
- **matched_tokens:** ['beam', 'gedi']

**Full text:**

```
The GEDI module provides additional parameters specific to making GEDI processing requests. "beam" : specifies which beam to process (0, 1, 2, 3, 5, 6, 8, 11; -1 for all) "degrade_filter" : if set to true, will filter out footprints that DO have the degrade flag set (default = false) "l2_quality_filter" : if set to true, will filter out footprints that do NOT have the L2 quality flag set (default = false) "l4_quality_filter" : if set to true, will filter footprints that do NOT have the L4 quality flag set (default = false) "surface_filter" : if set to true, will filter out footprints that do NOT have the surface flag set (default = false)
```

#### r5 — score 0.370

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.1 Photon-input Parameters
- **category:** `user_guide`
- **matched_tokens:** ['beam']

**Full text:**

```
The photon-input parameters allow the user to select an area, a time range, or a specific ATL03 granule to use for input to the photon-selection algorithm. If multiple parameters are specified, the result will be those photons that match all of the parameters. poly : polygon defining region of interest (see polygons ) region_mask : geojson describing region of interest which enables rasterized subsetting on servers (see geojson ) track : reference pair track number (1, 2, 3, or 0 to include for all three; defaults to 0); note that this is combined with the beam selection as a union of the two beams : list of beam identifiers (gt1l, gt1r, gt2l, gt2r, gt3l, gt3r; defaults to all) spots : list of spots (1, 2, 3, 4, 5, 6); this is only supporting by the atl03x endpoint rgt : reference ground track (defaults to all if not specified) cycle : counter of 91-day repeat cycles completed by the mission (defaults to all if not specified) region : geographic region for corresponding standard product (defaults to all if not specified) t0 : start time for filtering granules (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z) t1 : stop time for filtering granuels (format %Y-%m-%dT%H:%M:%SZ, e.g. 2018-10-13T00:00:00Z)
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.444

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 19
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 19
- **matched_tokens:** ['beam', 'gedi', 'laser']

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

#### r2 — score 0.417

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 11
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 11
- **matched_tokens:** ['beam', 'gedi', 'laser']

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

#### r3 — score 0.389

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 16
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 16
- **matched_tokens:** ['gedi', 'power']

**Full text:**

```
Algorithm sensitivity to GEDI data waveform properties
Training data must also be representative of GEDI waveform properties. The release 1
and release 2 GEDI04_A models were developed using simulated noiseless waveforms, where
ground elevation was known from discrete-return ALS. In practice, identifying the ground-
return in recorded GEDI data can be challenging under conditions of dense canopy cover and
complex terrain. The GEDI02_A data product includes results for six algorithm setting groups to
interpret the received waveform and identify the signal start, end, and elevation of the lowest
mode (Hofton & Blair, 2020), which is treated as ground elevation. Ground-finding errors will
propagate through RH metrics and impact AGBD predictions. A priority for subsequent releases
of the GEDI04_A data product is examining the frequency of ground-finding errors and the
impact of these errors on estimates of AGBD. Subsequent releases of the GEDI04_A data
product will be updated using models trained on simulated waveform data that has been
parameterized with on-orbit measurements of the transmitted pulse and sensor noise. Additional analyses will examine whether there are systematic differences among GEDI lasers
or between power and coverage ground tracks that result in different estimates of AGBD.
8.3 Strengthening allometric models
All remote sensing of AGBD depends on field measurements of individual trees and
allometric models to estimate individual tree mass.
```

#### r4 — score 0.325

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.3 ICESat-2 ATLAS Instrument
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 25
- **matched_tokens:** ['beam', 'configuration', 'laser']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
1.3 ICESat-2 ATLAS Instrument
NASA’s Ice, Cloud, and land Elevation Satellite-2 (ICESat-2) mission is the second of the
ICESat laser altimetry missions launch in September 2018. ICESat-2 carries an improved
Advanced Topographic Laser Altimeter System (ATLAS) consisting of a low energy,
micropulse, multibeam, high-resolution photon-counting laser altimeter possessing three pairs of
beams. Each pair, separated by about 90 m, consists of a high energy (~100 mJ) beam and a low
energy (25 mJ) beam each with an approximately 11 m footprint. Th pairs of beams are
separated by about 3 km. An instrument pulse rate of 10kHz and a nominal ground speed of
~7000m/s allow observations about every 70 cm. A schematic of the shot configuration is
shown in Figure 1-1. Figure 1-1 ICESat-2 ATLAS six-beam configuration. ICESat-2/ATLAS is thus significantly different than its predecessor, ICESat/GLAS that fired at a
much lower rate (40 Hz) but employed ~80 mJ lasers for full waveform detection (Abshire et al.
2005; Schutz et al., 2005). Each returned ATLAS photon is time-tagged with a vertical precision
of approximately 30 cm and a geolocation error ranging from 3.6 to 43 cm depending on off-
pointing angle (0 to 5 deg respectively, See Luthcke et al., 2019 ATL03g Received Photon
Geolocation), and surface and atmospheric characteristics.
```

#### r5 — score 0.373

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 15
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 15
- **matched_tokens:** ['gedi', 'power']

**Full text:**

```
The GEDI04_A algorithms were developed for prediction of AGBD using GEDI data. Although the approach developed here could be replicated for other sensors, the GEDI04_A
models should not be directly applied to alternative sensor data. For example, Duncanson et al.
(2020) applied the GEDI04_A model framework to simulated ICEsat-2 data. This required the
development of alternative statistical models. These models were developed specifically to
accommodate the instrument response and spatial resolution of ICESat-2.
7. Performance assessment
The performance of the GEDI04_A algorithm was evaluated by quantifying the
frequency of observations that were excluded by quality filters in every prediction stratum for
coverage and power lasers, and by disaggregating the impact of variables that can trigger
l4_quality_flag = 0. This performance assessment determines the percentages of GEDI shots
that are flagged as low-quality observations in every prediction stratum relative to the number
of observations where algorithm_run_flag = 1, and it identifies the causes of the low-quality
trigger. The analysis is based on mission weeks 16 – 153 of release 2, generation 2 of the
GEDI04_A data product. Quality filtering results in data losses when it is possible to implement the GEDI04_A
algorithm. These data losses are expected, because most conditions under which it is possible
to run the GEDI04_A algorithm do not meet minimum quality standards.
```

---

