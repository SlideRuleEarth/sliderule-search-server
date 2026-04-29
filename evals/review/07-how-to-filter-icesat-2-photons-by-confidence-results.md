# Row 7 results: docsearch / conceptual

> Auto-generated. Open this file alongside `07-how-to-filter-icesat-2-photons-by-confidence-review.md` —
> verdicts go there, this side is read-only.

**Query:** `how to filter ICESat-2 photons by confidence`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/icesat2.html
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `native atl03`
  - `photon-selection`
  - `atl06p`
  - `atl03sp`
- **expected_pages:** (none)
- **notes:** photon confidence filtering via cnf

---

## 📚 docsearch results (top 5)

#### r1 — score 0.515

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** ICESat-2 Module
- **category:** `user_guide`
- **matched_tokens:** ['filter', 'icesat', 'photons']

**Full text:**

```
The ICESat-2 module within SlideRule supports a number of both legacy p-series and s-series endpoints, as well as the newer DataFrame-based x-series endpoints. This document focuses on the x-series endpoints while still referencing the other legacy endpoints when helpful. Three main kinds of data are returned by the ICESat-2 endpoints: segmented photon data, elevation data (from the ATL06-SR algorithm), and vegetation data (from the PhoREAL algorithm). All data returned by the ICESat-2 endpoints are organized around the concept of an extent . An extent is a variable length, customized ATL03 segment. It takes the ATL03 photons and divides them up based on their along-track distance, filters them, and then packages them together a single new custom segment. Given that the ICESat-2 standard data products have a well defined meaning for segment, SlideRule uses the term extent to indicate this custom-length and custom-filtered segment of photons. The following processing flags are used for all ICESat-2 endpoints: 0x0001 : Along track spread too short 0x0002 : Too few photons 0x0004 : Maximum iterations reached 0x0008 : Out of bounds 0x0010 : Underflow 0x0020 : Overflow In addition, most endpoints support the generation of a name filter using the granule parameter: rgt : Reference ground track cycle : Orbit cycle region : ATL03 region {1 to 14} version : ATL03 release version (e.g. 007)
```

#### r2 — score 0.542

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 1.2.1 Native ATL03 Photon Classification
- **category:** `user_guide`
- **matched_tokens:** ['confidence', 'photons']

**Full text:**

```
ATL03 contains a set of photon classification values, that are designed to identify signal photons for different surface types with specified confidence: srt : surface type: 0-land, 1-ocean, 2-sea ice, 3-land ice, 4-inland water cnf : confidence level for photon selection, can be supplied as a single value (which means the confidence must be at least that), or a list (which means the confidence must be in the list); note - the confidence can be supplied as strings {âatl03_tepâ, âatl03_not_consideredâ, âatl03_backgroundâ, âatl03_within_10mâ, âatl03_lowâ, âatl03_mediumâ, âatl03_highâ} or as numbers {-2, -1, 0, 1, 2, 3, 4}. quality_ph : quality classification based on an ATL03 algorithms that attempt to identify instrumental artifacts, can be supplied as a single value (which means the classification must be exactly that), or a list (which means the classification must be in the list). podppd : pointing/geolocation degradation mask; each bit in the mask represents a pointing/geolocation solution quality assessment to be included; the bits are 0: nominal, 1: pod_degrade, 2: ppd_degrade, 3: podppd_degrade, 4: cal_nominal, 5: cal_pod_degrade, 6: cal_ppd_degrade, 7: cal_podppd_degrade.
```

#### r3 — score 0.432

- **url:** https://docs.testsliderule.org/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 5.1 Query Parameters
- **category:** `user_guide`
- **matched_tokens:** ['confidence', 'filter', 'photons']

**Full text:**

```
The following parameters are supported under the atl24 key for customizing the request to ATL24 and filtering which data is returned. atl24 : compact : reduces number of fields to minimal viable set (boolean) class_ph : ATL24 classification filter (list; 0:unclassified, 40:bathymetry, 41:sea surface) confidence_threshold|minimal bathymetry confidence score|double; 0 to 1.0|0| invalid_kd : invalid kd flag values to allow (âonâ: includes only photons with invalid kd; âoffâ: includes only photons without invalid kd; defaults to both when not specified) invalid_wind_speed : invalid wind speed flag values to allow (âonâ: includes only photons with invalid wind speed; âoffâ: includes only photons without invalid wind speed; defaults to both when not specified) low_confidence : low confidence flag values to allow (âonâ: includes only low confidence photons; âoffâ: includes only high confidence photons; defaults to both when not specified) night : night flag values to allow (âonâ: includes only photons collected at night; âoffâ: includes only photons collected during the day; defaults to both when not specified) sensor_depth_exceeded : sensor depth exceeded flag values to allow (âonâ: includes only photons at a depth greater than the sensor depth; âoffâ: includes only photons at a depth less then the sensor depth; defaults to both when not specified)
```

#### r4 — score 0.438

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['confidence', 'photons']

**Full text:**

```
Some photons will be returns from the Transmit Echo Path (TEP) Some photons are from the ATLAS instrument that have reflected off the surface or vegetation (these are our signal photons). The ATLAS instrument receives a vast amount of data and decides on-board whether or not to telemeter packets of received photons back to Earth. ATLAS uses a digital elevation model (DEM) and a few simple rules when making this decision. The photon events (PEs) that are returned are classified as being either signal or background for different surface types (land ice, sea ice, land, and ocean). These PEs have a confidence level flag associated with it for each surface type: -2 : possible Transmit Echo Path (TEP) photons -1 : events not associated with a specific surface type 0 : noise 1 : buffer but algorithm classifies as background 2 : low 3 : medium 4 : high There will be photons transmitted by the ATLAS instrument will never be recorded back. The vast majority of these photons never reached the ATLAS instrument again (only about 10 out of the 10 14 photons transmitted are received), but some are not detected due to the âdead timeâ of the instrument. This can create a bias towards the first photons that were received by the instrument, particularly for smooth and highly reflective surfaces. The transmitted pulse is also not symmetric in time, which can introduce a bias when calculating average surfaces.
```

#### r5 — score 0.471

- **url:** https://docs.testsliderule.org/background/ICESat-2.html
- **title:** ICESat-2
- **section:** ATL03 - Global Geolocated Photon Data
- **category:** `background`
- **matched_tokens:** ['icesat', 'photons']

**Full text:**

```
The data from ATLAS and the secondary instrumentation onboard the ICESat-2 observatory (the global positioning system (GPS) and the star cameras) are combined to create three primary measurements: the time of flight of a photon transmitted and received from ATLAS, the position of the satellite in space, and the pointing vector of the satellite during the transmission of photons. These three measurements are used to create ATL03 , the geolocated photon product of ICESat-2. ATL03 contains precise latitude, longitude and elevation for every received photon, arranged by beam in the along-track direction. The structure of the ATL03 file has (at most) six beam groups, along with data describing the responses of the ATLAS instrument, ancillary data for correcting and transforming the ATL03 data, and a group of metadata. Photon events can come to the ATLAS receiver in a few different ways: Many photons come from the sun either by reflecting off clouds or the land surface. These photon events are spread in a random distribution along the telemetry band. In ATL03, a large majority of these âbackgroundâ photon events are classified, but some may be incorrectly classified as signal. Some photons are from the ATLAS instrument that have reflected off clouds. These photons can be clustered together or widely dispersed depending on the properties of the cloud and a few other variables.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.665

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.2 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 69
- **matched_tokens:** ['confidence', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Figure 5-4. Final Classified Likely Signal Photons. Confidence level - high (blue, 29153 photons), medium (green, 12587 photons),
low (red, 4292), padding (black, 3393 photons). The figures above illustrate the algorithm performance on a segment of MABEL data over land
ice. As the algorithm development progressed, it became clear that different surfaces, and
different beam energies required different parameter values in order to best identify likely signal
photon events and minimize the number of false positives. As described in detail in a companion
document, Optimization of Signal Finding Algorithm, we optimized the parameter settings
according to surface type (land, ocean, sea ice, land ice, inland water) and beam energy (strong
and weak). Consequently, many parameters in Table 5-2 are surface type or beam energy
dependent. The likelihood of identifying likely signal photons varies as a function of background rate. We
simulated a surface and varied the background photon rate to determine the sensitivity of the
photon classification algorithm to background photon rate. In Figure 5-5, the simulated surface
is shown on the left with two different background rates. On the right of Figure 5-5, we
summarize the results of seven simulations. In general, the surface is classified with high
confidence up to a few MHz of background photon events.
```

#### r2 — score 0.658

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.3 Definitions of Variables used in Algorithm
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 70
- **matched_tokens:** ['confidence', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
high-, medium-, and low-confidence photon events are summed, although the relative fraction of
each classification changes. Although the surface used in this example is relatively simple, we expect this example to be a
useful example for similarly simple surface topologies, such as the ocean, sea ice, or ice sheet
interior. For other more complex surfaces, the background rates where high- or medium-
confidence photon events dominate will likely be lower, and low-confidence photon events will
likely dominate. Figure 5-5: Figure on the left shows a simulated photon cloud with 1 MHz of background
photon events on the left half and 8 MHz on the right. Likely signal photons are color-coded as
in Figure 5-4. Figure on the right shows the distribution of low- medium- and high-confidence
photon events as a function of background rate. The photon confidence level decreases as the
background rate increases.
5.1.3 Definitions of Variables used in Algorithm
The variables used in this algorithm are divided into four sets. Table 5-1 reports input variables
from external data sources (e.g. ATL02). Table 5-2 lists parameters required to drive the
algorithm (written to the ATL03 data product once per granule). Many of these parameters are
constants (according to our pre-launch simulations), while others are either beam- or surface-
type dependent.
```

#### r3 — score 0.637

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.1 Introduction
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 64
- **matched_tokens:** ['confidence', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
5.1 Photon Signal Confidence
5.1.1 Introduction
ICESat-2 will telemeter time tags for all photon events that fall within the downlink bands,
which are surface type and terrain dependent. The downlink bands contain both signal and
background. The goal of this algorithm is to identify all the signal photon events while
classifying as few as possible of the background photon events erroneously as signal. If the rate
of background photon events is known, then the algorithm can identify likely signal photon
events by finding regions where the photon event rate is significantly larger than the background
photon event rate. The telemetry band is limited (30 meters to ~1500 meters), so the downlinked
photon data is not optimal for calculating a robust background count rate. However, for
atmospheric research, ICESat-2 telemeters histograms of the sums of all photons over four
hundred laser transmit pulses (0.04 seconds; ~280 meters along-track) in 30-m vertical bins for
~14 kilometers in height that includes the atmosphere, surface echoes, and extends below the
Earth’s surface. These histograms are referred to as atmospheric histograms. After removing the
relatively few bins that may contain signal photon events from these atmospheric histograms, the
algorithm uses the remaining bins to estimate the background photon event rate (section
5.1.4.1.1).
```

#### r4 — score 0.634

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 5.1.2 Overview
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 68
- **matched_tokens:** ['confidence', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Figure 5-3. Additional Signal Photon Events.
Identified via slant histogramming. Black indicates photons found from slant histogramming
using the slope from the profile defined by ellipsoidal histogramming.
Additional surrounding background photons are added if the identified signal photons for a
Δtime do not meet a minimal height span requirement, Htspanmin. Higher-level data products
currently require the region identified as signal spans at least 20 meters vertically. The final
results for this profile are shown in Figure 5-4, color coded by confidence (blue = high; green =
medium, red = low, black = padding) which when compared to Figure 5-1 appears to identify all
the returns reflected from the surface.
52 Release Date: Fall 2022
```

#### r5 — score 0.661

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl03_atbd_v006.pdf
- **title:** Table of Contents
- **section:** 10.1 Appendix A – ATL03 Output Parameter Table.
- **category:** `atbd`
- **source_product:** `ATL03` · **page:** 162
- **matched_tokens:** ['confidence', 'icesat', 'photons']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Global Geolocated Photons (ATL03)
Release 006
Parameter ATBD
Name Data Type Long Name Units Description
Source
ph_id_channel INTEGER_ photon channel counts Channel number assigned for ATL03, Section
2 id received photon event. This is 7.4
part of the photon ID. Values 1
to 240 to span all channels and
all detectors. For the A side
detectors, values 1 to 60 are
for rising edge PCE1 (1 to 20),
PCE 2 (21 to 40) and PCE3 (41
to 60). Values 61 to 120 are for
falling edge PCE1 (61 to 80),
PCE 2 (81 to 100) and PC3 (101
to 120). For the B side
detectors, values similarly span
from 121 to 240.
signal_conf_ph UINT_1_L photon signal counts Confidence level associated ATL03, Section
E confidence with each photon event 5, Conf
selected as signal, per surface
type (0-noise. 1- added to allow
for buffer but algorithm
classifies as background, 2-low,
3-med, 4-high). Events not
associated with a specific
surface type have a confidence
level of -1. Possible TEP events
have a confidence level of -2
This parameter is a 5xN array
where N is the number of
photons in the granule, and the
5 rows indicate signal finding
for each surface type (in order:
land, ocean, sea ice, land ice
and inland water).
dist_ph_across FLOAT distance off RGT meters Across-track distance projected ATL03, Section
to the ellipsoid of the received 3.1.2, Step 3
photon from the reference
ground track.
```

---

