# Row 100 results: nsidc / instrument

> Auto-generated. Open this file alongside `100-atlas-532nm-green-laser-photon-counting-detector-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATLAS 532nm green laser photon counting detector`
**Panel signature:** `00c1bad780db`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** ATLAS laser/detector specs in ATL03 ATBD

---

## 📚 docsearch results (top 5)

#### r1 — score 0.418

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5. ATL24 - atl24x
- **category:** `user_guide`
- **matched_tokens:** ['atlas', 'detector', 'photon']

**Full text:**

```
to false night_flag Photon collected at night, solar elevation < 5 degrees 0:day, 1:night Optional: compact set to false sensor_depth_exceeded Turbidity of water and depth of photon indicate unlikely return 0:valid, 1:exceeded Optional: compact set to false sigma_thu Total horizontal uncertainty meters (float) Optional: compact set to false sigma_tvu Total vertical uncertainty meters (float) Optional: compact set to false spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r2 — score 0.392

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['atlas', 'counting', 'laser', 'photon']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r3 — score 0.471

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atlas', 'photon']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r4 — score 0.365

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1. ATL03 - atl03x
- **category:** `user_guide`
- **matched_tokens:** ['atlas', 'detector', 'photon']

**Full text:**

```
, 2:canopy, 3:top of canopy, 4:unclassified Optional: must enable phoreal or specify atl08_class yapc_score YAPC photon weight 0-255, higher is denser Optional: must enable yapc atl24_class ATL24 photon classification 0:unclassified, 40:bathymetry, 41:sea surface Optional: must enable atl24 atl24_confidence ATL24 photon classification bathymetry confidence score 0 to 1.0, higher is more confident (float) Optional: must enable atl24 spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number region ATLAS granule region 1-14 rgt Reference Ground Track gt Beam 10: gt1l, 20: gt1r, 30: gt2l, 40: gt2r, 50: gt3l, 60: gt3r Dependent on spacecraft orientation
```

#### r5 — score 0.350

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atlas', 'counting', 'detector', 'photon']

**Full text:**

```
Potential errors in the average surface heights: Sampling error : average height estimates are based upon a random sampling of the surface heights, which might be skewed based on the horizontal distribution of PEs Background noise : signal PEs are intermixed with the background PEs, and so there are random outliers which may affect the surface determination, particularly in conditions with high background rates and low surface reflectivity Complex topography : the along-track linear fit will not always resolve complex surface topography Misidentified PEs : the ATL03 processing will not always correctly identify the signal PEs First-photon bias : this bias is inherent to photon-counting detectors and depends on the signal return strength Atmospheric forward scattering : photons traveling through a cloudy atmosphere or a wind-blown snow event may be repeatedly scattered through small angles but still be reflected by the surface and be within the ATLAS field of view Subsurface scattering : photons may be scattered many times within ice or snow before returning to the detector Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.600

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 23
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 23
- **matched_tokens:** ['counting', 'detector', 'laser', 'photon']

**Full text:**

```
346 planned to fly onboard the International Space Station (ISS) or imaging sensors, such
347 as Landsat 8, or NASA/ISRO –NISAR radar mission.
348
349 1.2 Photon Counting Lidar
350 Rather than using an analog, full waveform system similar to what was utilized
351 on the ICESat/GLAS mission, ICESat-2 will employ a photon counting lidar. Photon
352 counting lidar has been used successfully for ranging for several decades in both the
353 science and defense communities. Photon counting lidar systems operate on the
354 concept that a low power laser pulse is transmitted and the detectors used are
355 sensitive at the single photon level. Due to this type of detector, any returned photon
356 whether from the reflected signal or solar background can trigger an event within the
357 detector. A discussion regarding discriminating between signal and background noise
358 photons is discussed later in this document. A question of interest to the ecosystem
359 community is to understand where within the canopy is the photon likely to be
360 reflected. Figure 1.1 is an example of three different laser detector modalities: full
361 waveform, discrete return, and photon counting. Full waveform sensors record the
362 entire temporal profile of the reflected laser energy through the canopy. In contrast,
363 discrete return systems have timing hardware that record the time when the
364 amplitude of the reflected signal energy exceeds a certain threshold amount.
```

#### r2 — score 0.566

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.1 Background
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 17
- **matched_tokens:** ['atlas', 'counting', 'green', 'laser', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
1.0 INTRODUCTION
This section introduces the ICESat-2 mission, the measurement concept of its sole instrument
(ATLAS, the Advanced Topographic Laser Altimeter System), and the family of ICESat-2 data
products.
1.1 Background
The ICESat-2 observatory and ATLAS instrument use a photon-counting lidar and ancillary
systems (i.e. GPS and star cameras) to make three primary measurements: the time of flight of a
photon from ATLAS, to the Earth, and back to ATLAS; the pointing vector at the time a photon
is transmitted by ATLAS; and the position of ICESat-2 in space at the time a photon is recorded
by ATLAS. This measurement approach is fundamentally different from a full-waveform lidar
system (such as the 1064-nm GLAS instrument on ICESat). The ATLAS instrument transmits
green (532-nm) laser pulses at 10 kHz; the spacecraft velocity from the ICESat-2 nominal ~500-
km frozen orbit altitude yields one transmitted laser pulse every ~0.7 meter along ground tracks. Each transmitted laser pulse is split by a diffractive optical element in ATLAS to generate six
individual beams, arranged in three pairs (Figure 1-1). The beams within each pair have different
transmit energies (‘weak’ and ‘strong,’ with an energy ratio between them of approximately 1:4)
and are separated by 90 meters in the across-track direction.
```

#### r3 — score 0.594

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 24
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 24
- **matched_tokens:** ['atlas', 'counting', 'laser', 'photon']

**Full text:**

```
375 to canopy structure and vegetation physiology. For example, the PDF of a conifer tree
376 will look different than broadleaf trees.
377
378 Figure 1.1. Various modalities of lidar detection. Adapted from Harding, 2009.
379 A cautionary note, the photon counting PDF that is illustrated in Figure 1.1 is
380 merely an illustration if enough photons (i.e. hundreds of photons or more) were to
381 be reflected from a target. In reality, due to the spacecraft speed, ATLAS will record 0
382 – 4 photons per transmit laser pulse over vegetation.
383
384 1.3 The ICESat-2 concept
385 The Advanced Topographic Laser Altimeter System (ATLAS) instrument
386 designed for ICESat-2 will utilize a different technology than the GLAS instrument
387 used for ICESat. Instead of using a high-energy, single-beam laser and digitizing the
388 entire temporal profile of returned laser energy, ATLAS will use a multi-beam,
389 micropulse laser (sometimes referred to as photon-counting). The travel time of each
390 detected photon is used to determine a range to the surface which, when combined
391 with satellite attitude and pointing information, can be geolocated into a unique XYZ
392 location on or near the Earth’s surface. For more information on how the photons
393 from ICESat-2 are geolocated, refer to ATL03 ATBD. The XYZ positions from ATLAS
24
```

#### r4 — score 0.532

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 35
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 35
- **matched_tokens:** ['atlas', 'counting', 'detector', 'green', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Land Ice Height (ATL06)
Release 006
508
509 3.4 First-Photon Bias
Figure 3-7. First-photon bias correction
11 1.1
10 1
9 0.9
8 0.8
GHz 7 0.7
rate, 6 0.6 gain
photon 54 0.50.4
3 0.3
all
2 detected 0.2
corrected
1 true gain 0.1
est gain
0 0
0 −2 0 2 4 6 8
time, ns
Simulated rates of photon arrivals at the detector (gray) and of detected photons (red) for
a strong beam over a flat surface (at 0 ns). The first-photon bias correction gives a
corrected histogram (blue outline) and an estimate of the effective detector gain (green). The actual effective gain of the detector (black) is shown for comparison.
510
511 The first-photon bias (FPB) results from an inherent problem with the photon-counting detectors
512 selected for ATLAS. For a short time, tdead, after an individual pixel of each detector detects a
513 photon, it cannot detect another. This means that photons early in a ground return are more
514 likely to be detected than those later on, and, for a symmetric return-photon distribution, the
515 mean surface height estimate is biased upwards, an effect that is largest for more intense pulses
516 and for pulses from flat surfaces where the return energy is concentrated in a short period of
517 time.
```

#### r5 — score 0.583

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.1 Background
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 18
- **matched_tokens:** ['atlas', 'detector', 'laser', 'photon']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
observatory moves in the along-track direction, the aggregation of overlapping footprints form a
ground track on the Earth’s surface. Approximately 1014 photons begin the journey from ATLAS, travelling through the atmosphere
to reflect off the Earth’s surface, return through the atmosphere and back into the ATLAS
telescope. For highly reflective surfaces and clear skies, on the order of ten signal photons from a single
strong beam are expected to be recorded by ATLAS for a given transmit laser pulse. At the same
time, background photons from sunlight at the same 532-nm wavelength may be arriving at the
detector, and some of them will also be recorded by ATLAS. Any photon that ATLAS records
an arrival time for is called a photon event, regardless of the source of the photon. The number of
photon events recorded by ATLAS depends on the geometry and reflectance of the Earth’s
surface, solar conditions, and on scattering and attenuation in the atmosphere. The number of
returned photon events varies from near zero photon events per shot over very dark non-
reflective surfaces, up to twelve photon events per shot over very reflective surfaces.
```

---

