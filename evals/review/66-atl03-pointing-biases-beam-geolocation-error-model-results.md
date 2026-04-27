# Row 66 results: nsidc / instrument

> Auto-generated. Open this file alongside `66-atl03-pointing-biases-beam-geolocation-error-model-review.md` —
> verdicts go there, this side is read-only.

**Query:** `ATL03 pointing biases beam geolocation error model`

## Auto-labeled (current ground truth)

- **corpus:** `nsidc`
- **expected_urls:**
  - https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **expected_sections:**
  - `pointing`
  - `bias`
  - `geolocation`
- **expected_pages:** (none)
- **notes:** pointing bias + error model is ATBD territory

---

## 📚 docsearch results (top 5)

#### r1 — score 0.508

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['atl03', 'beam', 'biases']

**Full text:**

```
The magnitude of this bias depends on the shape of the transmitted waveform, the width of the window used to calculate the average surface, and the slope and roughness of the surface that broadens the return pulse. ATL03 contains most of the data needed to create the higher level data products (such as the ATL06-SR land ice product). With SlideRule , we will calculate the average elevation of segments for each beam. In SlideRule the average segment elevations will not be corrected for transmit pulse shape biases or first photon biases as compared to the higher level data products.
```

#### r2 — score 0.460

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl06p
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'geolocation', 'pointing']

**Full text:**

```
sliderule.icesat2. atl06p ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs ATL06-SR processing in parallel on ATL03 data and returns geolocated elevations. This function expects that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. If resources is specified then any polygon or resource filtering options supplied in parm are ignored. Warning It is often the case that the list of resources (i.e. granules) returned by the CMR system includes granules that come close, but do not actually intersect the region of interest. This is due to geolocation margin added to all CMR ICESat-2 resources in order to account for the spacecraft off-pointing. The consequence is that SlideRule will return no data for some of the resources and issue a warning statement to that effect; this can be ignored and indicates no issue with the data processing.
```

#### r3 — score 0.445

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl03sp
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'geolocation', 'pointing']

**Full text:**

```
sliderule.icesat2. atl03sp ( parm , callbacks = {} , resources = None , keep_id = False , height_key = None ) [source] Performs ATL03 subsetting in parallel on ATL03 data and returns photon segment data. Unlike the atl03s function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. Warning Note, it is often the case that the list of resources (i.e. granules) returned by the CMR system includes granules that come close, but do not actually intersect the region of interest. This is due to geolocation margin added to all CMR ICESat-2 resources in order to account for the spacecraft off-pointing. The consequence is that SlideRule will return no data for some of the resources and issue a warning statement to that effect; this can be ignored and indicates no issue with the data processing.
```

#### r4 — score 0.558

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** References
- **category:** `background`
- **matched_tokens:** ['atl03', 'geolocation']

**Full text:**

```
ATBD for ATL03 Global Geolocated Photon Data ATBD for ATL03g Received Photon Geolocation ATBD for ATL03a Atmospheric Delay Corrections Userâs Guide for ATL03
```

#### r5 — score 0.423

- **url:** https://docs.slideruleearth.io/api_reference/icesat2.html
- **title:** icesat2
- **section:** atl03vp
- **category:** `api_reference`
- **matched_tokens:** ['atl03', 'geolocation', 'pointing']

**Full text:**

```
sliderule.icesat2. atl03vp ( parm , callbacks = {} , resources = None , keep_id = False ) [source] Performs ATL03 subsetting in parallel on ATL03 data and returns counts of photons in segments. Unlike the atl03v function, this function does not take a resource as a parameter; instead it is expected that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. Warning Note, it is often the case that the list of resources (i.e. granules) returned by the CMR system includes granules that come close, but do not actually intersect the region of interest. This is due to geolocation margin added to all CMR ICESat-2 resources in order to account for the spacecraft off-pointing. The consequence is that SlideRule will return no data for some of the resources and issue a warning statement to that effect; this can be ignored and indicates no issue with the data processing. Parameters : parms ( dict ) â parameters used to configure ATL03 subsetting (see Parameters ) callbacks ( dictionary ) â a callback function that is called for each result record resources ( list ) â a list of granules to process (e.g. [âATL03_20181019065445_03150111_007_01.h5â, â¦]) keep_id ( bool ) â whether to retain the âextent_idâ column in the GeoDataFrame for future merges Returns : ATL03 segments (see Photon Segments ) Return type : GeoDataFrame
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.673

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 2.2 Data Flow Within ATL03
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 23
- **matched_tokens:** ['atl03', 'beam', 'biases', 'pointing']

**Full text:**

```
ATL03g uses these
inputs and determines a preliminary latitude, longitude, and height above the ellipsoid for each
photon in steps 1 through 7 in section 3.1 of the ATL03g document. In addition, ATL03g estimates the range bias for each beam, which is stored for additional
analysis. The range bias estimates are used to potentially update the beam-specific time of flight
biases applied in ATL02. ATL03g also estimates the pointing angle biases for each beam. These
pointing angle biases are used in ATL03g and used to refine the PPD algorithm.
7 Release Date: Fall 2022
```

#### r2 — score 0.568

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.3.2 Range bias uncertainty
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 46
- **matched_tokens:** ['beam', 'error', 'geolocation', 'model']

**Full text:**

```
The atmospheric delay
(combining wet and dry tropospheric effects) is described in ATL03a. This range correction is
based on imperfect atmospheric models of temperature and humidity and has a residual error that
is determined in the ATL03a processing. From a data flow standpoint, the ISF produces TEP for each realization of the TEP along with
the TEP-based bias correction. The POD/PPD facility generates bias for each beam at the same
rate as the model-based range bias correction. This is passed along with ANC04 to the SIPS. The third term (atm) is generated during ATL03a processing and is combined in quadrature with
the other two terms during geolocation processing to produce a single height uncertainty
estimate. This estimate is provided at the along-track geolocation segment rate and contributes
to the overall sigma_h, the theoretical total height uncertainty of a given reference photon. The
sigma_h term is dominated by the overall ATLAS timing uncertainty
/ancillary_data/atlas_engineering/ph_uncorrelated_error (as described in Neumann et al.,
2019) but also includes the terms above and uncertainties in the geophysical corrections applied
to the photon heights (Section 6). The value for sigma_h is calculated as the sum of the
uncorrelated error and correlated error. The uncorrelated error is as described in Section 7.7.2.
```

#### r3 — score 0.537

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 3.3.1 Range bias determination
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 44
- **matched_tokens:** ['biases', 'error', 'geolocation']

**Full text:**

```
In post-launch operations, the surface return times of flight are passed from
ATL02 to the geolocation algorithm (ATL03g), converted to range, and then eventually to
photon height. In parallel, the TEP times of flight of the likely TEP photons are passed to the
Instrument Support Facility (ISF). The ISF uses the TEP photons, and changes in their time of
flight, to generate the TEP-based range bias offset in meters that are applied to h_ph starting in
rel005. We note that not every ATL02 granule will have likely TEP photons, as described in
Section 7.2.2. Whenever such TEP photons are likely present, these corrections for the two
beams with the TEP optical path are passed from the ISF to the POD/PPD facility via ANC13. These TEP-based corrections are based on a comparison of pre-launch sets of TEP data under the
relevant instrument configuration with those collected on-orbit. Because TEP data only exist for
ATLAS spots 1 and 3, pre-launch testing data is used to map the offsets computed for the TEP
spots to the non-TEP spots (2, 4, 5, and 6) spot-specific range biases. The full details are
provided in the Computation of the ICESat-2 Range Vector document, available upon request. We include the inherent uncertainty in this time-dependent range bias correction in the overall
photon height uncertainty (sigma_h). When one or more threshold crossing times from the Start Pulse Detector is missing, an
additional time of flight error must be accounted for.
```

#### r4 — score 0.556

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl06_atbd_v006.pdf
- **title:** Microsoft Word - ICESat2_Land_ICE_ATBD_ATL06_r006_16Nov2022.docx
- **section:** Page 62
- **category:** `atbd`
- **source_product:** `ATL06` · **page:** 62
- **matched_tokens:** ['atl03', 'beam', 'error', 'geolocation']

**Full text:**

```
Table 4-5 ground_track subgroup
Parameter Units Description Derived
ref_azimuth degrees The direction, eastwards from north, ATL03
of the laser beam vector as seen by
an observer at the laser ground spot
viewing toward the spacecraft (i.e.,
the vector from the ground to the
spacecraft).
ref_coelv degrees Coelevation (CE) is direction from ATL03
vertical of the laser beam as seen by
an observer located at the laser
ground spot.
seg_azimuth degrees The azimuth of the pair track, east 3.1.2.2
of local north
sigma_geo_at meters Geolocation error in the along-track 3.10
direction
sigma_geo_xt meters Geolocation error in the across-track 3.10
direction
sigma_geo_r meters Radial orbit error 3.10
50
```

#### r5 — score 0.574

- **url:** https://nsidc.org/sites/default/files/documents/user-guide/atl03-v006-userguide.pdf
- **title:** ATL03 v006 user guide
- **section:** 2.3.6 Surface Masks
- **category:** `user_guide`
- **source_product:** `ATL03` · **page:** 19
- **matched_tokens:** ['atl03', 'beam', 'geolocation', 'model']

**Full text:**

```
The ATLAS zero-range distance was measured before launch to account for optical and electrical
path lengths within the instrument for many permutations of ATLAS settings and configurations
(documented in the ATLAS pre-launch calibration product CAL-08). The TEP provides an option to
internally calibrate ATLAS in orbit. Range bias uncertainty is due to (1) uncertainty in the TEP-based bias estimate, (2) uncertainty in
the model of the TEP variation around the orbit, and (3) uncertainty in the atmospheric delay
correction. The overall height uncertainty estimate is provided at the along-track geolocation
segment rate and contributes to sigma_h. NOTE: For ATL03 Versions 1–4, the range bias was calculated from pre-launch analysis and instrument
calibration. This range bias correction was beam-specific and constant over time. Beginning with Version
5, the range bias correction is dynamically calculated to include time- and temperature-dependent
corrections from on-orbit calibration data. The mean offset between the pre-launch (Version 4 and lower)
and post-launch (Version 5 and higher) range bias correction is about 1.2 cm. An additional time-
dependent range bias on the order of ± 2 mm is indicated by the analysis of on-orbit calibrations over the
first two years of the mission.
```

---

