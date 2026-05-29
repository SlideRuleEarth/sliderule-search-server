# Row 48 results: nsidc / instrument

> Auto-generated. Open this file alongside `48-atlas-laser-altimeter-instrument-specifications-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATLAS laser altimeter instrument specifications`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `atlas`
  - `instrument`
- **expected_pages:** (none)
- **notes:** ATLAS instrument canonically described in ATL03 docs

---

## 📚 docsearch results (top 5)

#### r1 — score 0.586

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['altimeter', 'atlas', 'instrument', 'laser']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r2 — score 0.424

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atlas', 'instrument']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

#### r3 — score 0.346

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atlas', 'instrument']

**Full text:**

```
Some photons will be returns from the Transmit Echo Path (TEP) Some photons are from the ATLAS instrument that have reflected off the surface or vegetation (these are our signal photons). The ATLAS instrument receives a vast amount of data and decides on-board whether or not to telemeter packets of received photons back to Earth. ATLAS uses a digital elevation model (DEM) and a few simple rules when making this decision. The photon events (PEs) that are returned are classified as being either signal or background for different surface types (land ice, sea ice, land, and ocean). These PEs have a confidence level flag associated with it for each surface type: -2 : possible Transmit Echo Path (TEP) photons -1 : events not associated with a specific surface type 0 : noise 1 : buffer but algorithm classifies as background 2 : low 3 : medium 4 : high There will be photons transmitted by the ATLAS instrument will never be recorded back. The vast majority of these photons never reached the ATLAS instrument again (only about 10 out of the 10 14 photons transmitted are received), but some are not detected due to the âdead timeâ of the instrument. This can create a bias towards the first photons that were received by the instrument, particularly for smooth and highly reflective surfaces. The transmitted pulse is also not symmetric in time, which can introduce a bias when calculating average surfaces.
```

#### r4 — score 0.417

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['atlas']

**Full text:**

```
This is reversed in the backward orientation, and the strong beams lead the weak beams with a strong beam on the left edge of the beam pattern. ATLAS beam mapping when in the forward orientation ATLAS Spot Number Ground track Designation Beam Strength 1 gt3r Strong 2 gt3l Weak 3 gt2r Strong 4 gt2l Weak 5 gt1r Strong 6 gt1l Weak
```

#### r5 — score 0.353

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** A.2 Elevations - atl06p
- **category:** `user_guide`
- **matched_tokens:** ['laser']

**Full text:**

```
The primary result returned by SlideRule for ICESat-2 ATL06-SR processing requests is a set of geolocated elevations corresponding to a geolocated ATL03 along-track segment. The elevations are contained in a GeoDataFrame where each row represents a calculated elevation. The elevation GeoDataFrame has the following columns: extent_id : unique ID associated with custom ATL03 segment (removed from final GeoDataFrame by default) segment_id : segment ID of first ATL03 segment in result n_fit_photons : number of photons used in final calculation pflags : processing flags (0x1 - spread too short; 0x2 - too few photons; 0x4 - max iterations reached) rgt : reference ground track cycle : cycle region : region of source granule spot : laser spot 1 to 6 gt : ground track (10: GT1L, 20: GT1R, 30: GT2L, 40: GT2R, 50: GT3L, 60: GT3R) x_atc : along track distance from the equator in meters time : nanoseconds from Unix epoch (January 1, 1970) without leap seconds lat : latitude (-90.0 to 90.0) lon : longitude (-180.0 to 180.0) h_mean : elevation in meters from ellipsoid dh_fit_dx : along-track slope y_atc : across-track distance w_surface_window_final : width of the window used to select the final set of photons used in the calculation rms_misfit : measured error in the linear fit of the surface h_sigma : error estimate for the least squares fit model
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.640

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 24
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 24
- **matched_tokens:** ['altimeter', 'atlas', 'instrument', 'laser']

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

#### r2 — score 0.567

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 1.1 Background
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 17
- **matched_tokens:** ['altimeter', 'atlas', 'instrument', 'laser']

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

#### r3 — score 0.586

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 1.3 ICESat-2 ATLAS Instrument
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 25
- **matched_tokens:** ['altimeter', 'atlas', 'instrument', 'laser']

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

#### r4 — score 0.605

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 104
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 104
- **matched_tokens:** ['altimeter', 'laser']

**Full text:**

```
Geoscience Laser Altimeter System waveform simulation and
2100 its applications. Annals of Glaciology, Vol 29, 1999, 29: 279-285.
2101
92
```

#### r5 — score 0.519

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 1.2.2 ATLAS/ICESat-2 Description
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 3
- **matched_tokens:** ['altimeter', 'atlas', 'instrument', 'laser']

**Full text:**

```
USER GUIDE: ATLAS/ICESat-2 L2A Global Geolocated Photon Data, Version 6
1 DATA DESCRIPTION
Parameters
Height above the ellipsoid, time, and geodetic latitude and longitude for individual photons. Heights
are provided in the ITRF2014 reference frame; geographic coordinates are referenced to the
WGS84 ellipsoid. File Information
1.2.1 Format
Data are provided as HDF5 formatted files.
1.2.2 ATLAS/ICESat-2 Description
NOTE: The following brief description of the Ice, Cloud and land Elevation Satellite-2 (ICESat-2)
observatory and Advanced Topographic Laser Altimeter System (ATLAS) instrument is provided to help
users better understand the file naming conventions, internal structure of data files, and other details
referenced by this user guide. The ATL03 data product is described in detail in the Ice, Cloud, and land
Elevation Satellite-2 Project Algorithm Theoretical Basis Document for Global Geolocated Photon Data
(ATBD for ATL03 V6 | https://doi.org/10.5067/GA5KCLJT7LOT). The ICESat-2 observatory utilizes a photon-counting lidar (the ATLAS instrument) and ancillary
systems (GPS, star cameras, and ground processing) to measure the time a photon takes to travel
from ATLAS to Earth and back again and determine the reflected photon's geodetic latitude and
longitude. Laser pulses from ATLAS illuminate three left/right pairs of spots on the surface that
trace out six approximately 14 m wide ground tracks as ICESat-2 orbits Earth.
```

---

