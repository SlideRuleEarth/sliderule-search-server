# Row 64 results: nsidc / instrument

> Auto-generated. Open this file alongside `64-icesat-2-orbit-altitude-inclination-mission-specifications-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ICESat-2 orbit altitude inclination mission specifications`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `orbit`
  - `mission`
  - `atlas`
- **expected_pages:** (none)
- **notes:** mission-level specs in ATL03 docs

---

## 📚 docsearch results (top 5)

#### r1 — score 0.603

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['icesat', 'mission']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r2 — score 0.421

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'orbit']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r3 — score 0.392

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.5 ATL06-SR Algorithm
- **category:** `user_guide`
- **matched_tokens:** ['icesat', 'orbit']

**Full text:**

```
This algorithm replaces the columns of the source DataFrame with the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude Fitted latitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame longitude Fitted longitude of the segment, EPSG:7912 degrees (double) replaced by geometry column when GeoDataFrame x_atc Fitted along track distance meters (double) y_atc Fitted across track distance meters (float) photon_start ATL03 index (per beam) of the first photon in the segment photon_count Number of ATL03 photons in the segment pflags Processing flags see ICESat-2 Processing Flags h_mean Fitted elevation of the segment meters (float) vertical datum controlled by parameters, default is ITRF2014 dh_fit_dx Fitted slope of the segment window_height Height of window used in final fit meters rms_misfit h_sigma spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation Using the Python client, this service is called via: parms = { "fit" : {} } sliderule . run ( 'atl03x' , parms )
```

#### r4 — score 0.529

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-00-00.html
- **title:** Release v2.0.x
- **section:** Release v2.0.x
- **category:** `release_notes`
- **matched_tokens:** ['icesat']

**Full text:**

```
2023-01-11 Version description of the v2.0.0 release of ICESat-2 SlideRule.
```

#### r5 — score 0.515

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **title:** Release v2.1.x
- **section:** Release v2.1.x
- **category:** `release_notes`
- **matched_tokens:** ['icesat']

**Full text:**

```
2023-03-03 Version description of the v2.1.0 release of ICESat-2 SlideRule.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.612

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.3 ICESat-2 ATLAS Instrument
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 26
- **matched_tokens:** ['altitude', 'icesat', 'inclination', 'orbit']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Parameter ATLAS MABEL
Operational altitude 500 km 20 km
Wavelength 532 nm 532 and 1064 nm
Telescope diameter 0.8 m 0.127 m
Laser pulse repetition
10 kHz Variable 5-25 kHz
frequency
Strong beam: 121 µJ Variable, nominal
Laser pulse energy
Week beam: 30 µJ 5-7 µJ per beam
Mean Pulse Width
< 1.5 ns < 2.0 ns
(FWHM)
Laser footprint diameter 17 m 100 µrad (2 m)
Telescope field of view 210 µrad (4.2 m)
Swath width 3.3 km Variable up to 1.05 km
Inclination 94 deg N/A
Table 1-1 Summary comparison of the principal ATLAS and MABEL instrument parameters.
An additional unique feature of ICESat-2 is its two orbit modes. Above approximately +/-65 deg
latitude, ATLAS operates in a repeat track mode over designated reference tracks similar to
ICESat in order to obtain continuous time series of ice sheet change along those tracks. Below
+/- 65 deg, however, ICESat-2 will systematically point left or right off the reference tracks in
subsequent orbits, in order to conduct a two-year global mapping of vegetation. Additional
scheduled off-pointing also is planned to observe targets of opportunity and
calibration/validation sites.
3
Release 007, January 31, 2025
```

#### r2 — score 0.616

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 26
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 26
- **matched_tokens:** ['icesat', 'mission', 'orbit']

**Full text:**

```
409
Weak (1) Weak (1) Weak (1)
2.5 km*
3.305 km*
Strong (4) Strong (4) Strong (4)
410
411 Figure 1.2. Schematic of 6-beam configuration for ICESat-2 mission. The laser energy will
412 be split into 3 laser beam pairs – each pair having a weak spot (1X) and a strong spot (4X).
413 The motivation behind this multi-beam design is its capability to compute
414 cross-track slopes on a per-orbit basis, which contributes to an improved
415 understanding of ice dynamics. Previously, slope measurements of the terrain were
416 determined via repeat-track and crossover analysis. The laser beam configuration as
417 proposed for ICESat-2 is also beneficial for terrestrial ecosystems compared to GLAS
418 as it enables a denser spatial sampling in the non-polar regions. To achieve a spatial
419 sampling goal of no more than 2 km between equatorial ground tracks, ICESat-2 will
420 be off-nadir pointed a maximum of 1.8 degrees from the reference ground track
421 during the entire mission.
26
```

#### r3 — score 0.575

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.3.1 Range bias determination
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 43
- **matched_tokens:** ['icesat', 'mission', 'orbit']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
2. If exactly two photons are equidistant from the center, and their distance is the closest to
the center, the reference photon is the equidistant photon with the higher ellipsoidal
height.
3. If more than two photons are equidistant from the center, and their distance is the closest
to the center, the reference photon is the equidistant photon with the median ellipsoidal
height.
3.3 ATLAS Range Bias Correction and Uncertainty
The primary measurement of the ICESat-2 mission is the height of the earth’s surface. Therefore, careful consideration is needed to evaluate and quantify potential sources of
measurement bias (time of flight bias, or range bias), and account for the bias in the ATL03
photon heights. In addition, we evaluate the uncertainty in that bias, and determine both the bias
and the bias uncertainty. In this section, we present the logic and data flows used to determine
the likely sources of bias and bias uncertainty, as well as the concept to evaluate the range bias
using on-orbit data after launch.
```

#### r4 — score 0.589

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 71
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 71
- **matched_tokens:** ['icesat', 'mission', 'orbit']

**Full text:**

```
1293 2.5.5 ATLAS_Pointing_Angle
1294 (parameter = atlas_pa). Off nadir pointing angle (in radians) of the satellite to
1295 increase spatial sampling in the non-polar regions.
1296 2.5.6 Reference_ground_track
1297 (parameter = rgt). The reference ground track (RGT) is the track on the earth
1298 at which the vector bisecting laser beams 3 and 4 (or GT2L and GT2R) is pointed
1299 during repeat operations. Each RGT spans the part of an orbit between two ascending
1300 equator crossings and are numbered sequentially. The ICESat-2 mission has 1387
1301 RGTs, numbered from 0001xx to 1387xx. The last two digits refer to the cycle number.
1302 2.5.7 Sigma_h
1303 (parameter = sigma_h). Total vertical uncertainty due to PPD (Precise Pointing
1304 Determination), POD (Precise Orbit Determination), and geolocation errors.
1305 Specifically, this parameter includes radial orbit error, 𝜎!"#$%, tropospheric errors,
1306 𝜎9"&' , forward scattering errors, 𝜎+&",-".(/-%%*"$01, instrument timing errors, 𝜎%$2$01,
1307 and off-nadir pointing geolocation errors. The component parameters are pulled
1308 from ATL03 and ATL09. Sigma_h is the root sum of squares of these terms as detailed
1309 in Equation 1.1. The sigma_h reported here is the mean of the sigma_h values reported
1310 within the five ATL03 geosegments that are used to create the 100 m ATL08 segment.
1311 2.5.8 Sigma_along
1312 (parameter = sigma_along). Total along-track uncertainty due to PPD and POD
1313 knowledge.
```

#### r5 — score 0.622

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 2
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 2
- **matched_tokens:** ['icesat', 'mission']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
Abstract
This document describes the theoretical basis of the land ice height processing algorithms and
the products that are produced by the ICESat-2 mission. It includes descriptions of the
parameters that are provided with each product as well as ancillary geophysical parameters used
in the derivation of the products.
ii
```

---

