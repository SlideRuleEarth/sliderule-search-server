# Row 45 results: nsidc / cross_product

> Auto-generated. Open this file alongside `45-strong-versus-weak-beams-icesat-2-atlas-review.md` —
> verdicts go there, this side is read-only.

**Query:** `strong versus weak beams ICESat-2 ATLAS`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **expected_sections:**
  - `beam`
  - `atlas`
- **expected_pages:** (none)
- **notes:** beam geometry is ATL03-defined but referenced across products

---

## 📚 docsearch results (top 5)

#### r1 — score 0.651

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r2 — score 0.531

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['atlas', 'beams', 'strong', 'weak']

**Full text:**

```
This is reversed in the backward orientation, and the strong beams lead the weak beams with a strong beam on the left edge of the beam pattern. ATLAS beam mapping when in the forward orientation ATLAS Spot Number Ground track Designation Beam Strength 1 gt3r Strong 2 gt3l Weak 3 gt2r Strong 4 gt2l Weak 5 gt1r Strong 6 gt1l Weak
```

#### r3 — score 0.478

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atlas', 'icesat']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r4 — score 0.448

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v01-01-00.html
- **title:** Release v1.1.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['atlas', 'icesat']

**Full text:**

```
v1.1.5 - Default asset switched from projectâs s3 bucket (atlas-s3) to NSIDCâs Cumulus bucket (nsidc-s3). v1.1.5 - Non-blocking read API added to H5Coro to support greater parallelization of reads. When configured, H5Coro creates a thread-pool, assigns read requests to the next available thread, and returns a future to the calling application. The Atl03Reader in ICESat-2 plugin was updated to use the non-blocking API. Concurrent reads when from a maximum of 18 reads at a time to 128 reads at a time.
```

#### r5 — score 0.543

- **url:** https://docs.testsliderule.org/developer_guide/release_notes/release-v02-00-00.html
- **title:** Release v2.0.x
- **section:** Release v2.0.x
- **category:** `release_notes`
- **matched_tokens:** ['icesat']

**Full text:**

```
2023-01-11 Version description of the v2.0.0 release of ICESat-2 SlideRule.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.677

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.1 Background
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 17
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
The beam pairs are separated by
~3.3 kilometers in the across-track direction, and the strong and weak beams are separated by
~2.5 kilometers in the along-track direction. Figure 1-1 shows the idealized beam and footprint
pattern for ICESat-2. Figure 1-1. ATLAS Idealized Beam and Footprint Pattern. The left panel (Figure 1-1) shows the beam pattern for ICESat-2, while the right panel shows the
instantaneous footprint pattern generated by each transmitted laser pulse from ATLAS. Light
green circles indicate footprints from the relatively low energy (weak) beams, while the dark
green circles indicate footprints from the relatively high-energy (strong) beams. As the
1 Release Date: Fall 2022
```

#### r2 — score 0.666

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 7.5 The Spacecraft Orientation Parameter
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 147
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
the pce_mframe_cnt roll-over every 2.7 years, this framework establishes a unique identification
for every photon in the ICESat-2 data products.
7.5 The Spacecraft Orientation Parameter
The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of
travel. ATL03 includes the sc_orient parameter in the group /orbit_info/ to record the
observatory information. The orientation is tracked on-orbit by the Instrument Support Facility
(ISF) and is passed to ATL03 via the ANC13 ancillary file. As noted above, the mapping
between the strong and weak beams of ATLAS and their relative position on the ground depend
on the observatory orientation (Figure 10-1 and Figure 10-2). The forward orientation (sc_orient == 1) corresponds to ATLAS traveling along the +x
coordinate in the ATLAS instrument reference frame (see ATL02). In this orientation, the weak
beams lead the strong beams and a weak beam is on the left edge of the beam pattern (Figure
10-1). The table below indicates the mapping between ATLAS spots, beam strength, PCE card
number, and the ground track designation used on the ATL03 data product when ATLAS is
oriented in the forward orientation. PCE Beam strength ATLAS spot ATL03 ground track
number designation
1 strong 1 gt3R
1 weak 2 gt3L
2 strong 3 gt2R
2 weak 4 gt2L
3 strong 5 gt1R
3 weak 6 gt1L
Table 7-6. Beam mapping when sc_orient == 1 (forward).
```

#### r3 — score 0.626

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.4 Algorithm Implementation
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 86
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
beam strength, have been derived based on MABEL data. Of the parameters in Table 5-2, those
that are associated with time (i.e. Δtime and δtmax) have been scaled for use with ATLAS data. For example, most MABEL data have 1,000 laser pulses fired every 40 meters along-track
(MABEL’s laser pulse rate was typically 5 kHz at an average along-track velocity of 200 m/sec). For ATLAS, we expect ~57 laser pulses every 40 meters (at the ATLAS pulse repetition rate of
10 kHz and spacecraft velocity of 7 km/sec). Our initial estimates for time-based parameters are
based on these considerations, along with the radiometric differences between the instruments
(e.g. MABEL returned approximately 1 signal photon every ~50 laser pulses over the interior of
Greenland, while ATLAS is predicted to return ~10 signal photons per laser pulse over the
interior of Greenland for the strong beams, and ~2 signal photons per laser pulse over the interior
of Greenland for the weak beams). We expect that these values will need to be revisited shortly
after launch. The processing steps for each of the beam strengths are summarized below with a reference to
the appropriate section where the methodology is described in detail.
```

#### r4 — score 0.701

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 2.2 Acquisition
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 14
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
Figure 5. ICESat-2 data processing flow. ATL02 processing converts ATL01 data to science units and applies
instrument corrections. The Precision Pointing Determination (PPD) and Precision Orbit Determination (POD)
solutions compute the pointing vector and position of the ICESat-2 observatory.
Acquisition
The ATLAS instrument transmits green (532 nm) laser pulses at 10 kHz. At the nominal ICESat-2
orbit altitude of 500 km, this yields approximately one transmitted laser pulse every 0.7 meters
along ground tracks. Each transmitted laser pulse is split by a diffractive optical element in ATLAS
to generate six individual beams, arranged in three pairs. Within each pair, the beams have
different transmit energies—so-called weak and strong beams with an energy ratio of
Page 13 of 22National Snow and Ice Data Center
nsidc.org
```

#### r5 — score 0.677

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 3
- **matched_tokens:** ['atlas', 'beams', 'icesat', 'strong', 'weak']

**Full text:**

```
Each ground track is
numbered according to the laser spot number that generates it, with ground track 1L (GT1L) on the
far left and ground track 3R (GT3R) on the far right. Left/right spots within each pair are
approximately 90 m apart in the across-track direction and 2.5 km in the along-track
direction. Higher level ATLAS/ICESat-2 data products (ATL03 and above) are organized by ground
track, with ground tracks 1L and 1R forming pair one, ground tracks 2L and 2R forming pair two,
and ground tracks 3L and 3R forming pair three. Each pair also has a Pair Track—an imaginary
line halfway between the actual location of the left and right beams (see Figure 1). Pair tracks are
approximately 3 km apart in the across-track direction. The beams within each pair have different transmit energies—so-called weak and strong beams—
with an energy ratio between them of approximately 1:4. The mapping between the strong and
weak beams of ATLAS, and their relative position on the ground, depends on the orientation (yaw)
Page 2 of 22National Snow and Ice Data Center
nsidc.org
```

---

