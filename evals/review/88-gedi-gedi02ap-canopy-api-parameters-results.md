# Row 88 results: docsearch / api_lookup

> Auto-generated. Open this file alongside `88-gedi-gedi02ap-canopy-api-parameters-review.md` —
> verdicts go there, this side is read-only.

**Query:** `gedi gedi02ap canopy api parameters`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/api_reference/gedi.html
- **expected_sections:**
  - `gedi02ap`
  - `gedi02a`
  - `gedi`
- **expected_pages:** (none)
- **notes:** gedi module api

---

## 📚 docsearch results (top 5)

#### r1 — score 0.536

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 3.3 L3 Raster
- **category:** `user_guide`
- **matched_tokens:** ['canopy', 'gedi', 'parameters']

**Full text:**

```
The following raster datasets are available to sample: "gedil3-elevation" : GEDI03_elev_lowestmode_mean_2019108_2022019_002_03.tif "gedil3-canopy" : GEDI03_rh100_mean_2019108_2022019_002_03.tif "gedil3-elevation-stddev" : GEDI03_elev_lowestmode_stddev_2019108_2022019_002_03.tif "gedil3-canopy-stddev" : GEDI03_rh100_stddev_2019108_2022019_002_03.tif "gedil3-counts" : GEDI03_counts_2019108_2022019_002_03.tif For example, if you wanted to sample the GEDI L3 Canopy raster and calculate zonal statistics for every ICESat-2 PhoREAL data point, then you could add the following entry to your parameters for your PhoREAL request: parms [ "samples" ]: { "canopy" : { "asset" : "gedil3-canopy" , "radius" : 10.0 , "zonal_stats" : True }}
```

#### r2 — score 0.471

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-01-00.html
- **title:** Release v3.1.x
- **section:** Major Changes
- **category:** `release_notes`
- **matched_tokens:** ['api', 'gedi', 'parameters']

**Full text:**

```
GEDI functionality officially supported Subsetting for L1B, L2A, L4A datasets (L1 and L2 products limited to Grand Mesa, Colorado area of interest until LP DAAC migrates them to the cloud) Raster Sampling for L3, L4B datasets User Guide: https://slideruleearth.io/user_guide/GEDI.html API Reference: https://slideruleearth.io/api_reference/gedi.html Example Notebooks: https://github.com/SlideRuleEarth/sliderule-python/tree/main/examples PhoREAL functionality officially supported User Guilde: https://slideruleearth.io/user_guide/ICESat-2.html#photon-extent-parameters API Reference: https://slideruleearth.io/api_reference/icesat2.html#atl08p Example Notebooks: https://slideruleearth.io/getting_started/Examples.html (look for PhoREAL Example )
```

#### r3 — score 0.439

- **url:** https://docs.slideruleearth.io/api_reference/gedi.html
- **title:** gedi
- **section:** gedi02ap
- **category:** `api_reference`
- **matched_tokens:** ['gedi', 'gedi02ap']

**Full text:**

```
sliderule.gedi. gedi02ap ( parm , callbacks = {} , resources = None , keep_id = False , as_numpy_array = False , height_key = None ) [source] Performs subsetting in parallel on GEDI data and returns geolocated footprints. This function expects that the parm argument includes a polygon which is used to fetch all available resources from the CMR system automatically. If resources is specified then any polygon or resource filtering options supplied in parm are ignored.
```

#### r4 — score 0.547

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.0: APIs
- **category:** `developer_guide`
- **matched_tokens:** ['gedi02ap']

**Full text:**

```
The following APIs shall be supported: atl03sp atl06sp atl06p atl08sp - future atl08p atl024sp - future atl024p - future gedi04ap gedi02ap gedi01bp samples subsets
```

#### r5 — score 0.487

- **url:** https://docs.slideruleearth.io/user_guide/gedi.html
- **title:** GEDI Module
- **section:** 1. Overview
- **category:** `user_guide`
- **matched_tokens:** ['api', 'gedi']

**Full text:**

```
The GEDI API currently provides subsetting and raster sampling capabilities to SlideRule for the L1B, L2A, L3, L4A, and L4B datasets. * The L1B dataset can be subsetted with waveforms returned for each footprint inside a user-supplied area of interest * The L2A dataset can be subsetted with elevations returned for each footprint inside a user-supplied area of interest * The L3 dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated * The L4A dataset can be subsetted with elevation and above-ground vegetation density returned for each footprint inside a user-supplied area of interest * The L4B dataset can be sampled at specific coordinates and associated with any other SlideRule generated data product that is geolocated
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.531

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 12
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 12
- **matched_tokens:** ['canopy', 'gedi']

**Full text:**

```
Some EBT forests and woodlands
experience periods of partial deciduousness during which some percentage of crowns are
leafless while the canopy as a whole is not. For example, a study across a rainfall gradient in
Panama classified as EBT using MODIS data product MCD12Q1 found that 3.6 – 19.1% of crown
area was leafless at peak deciduousness (Condit et al., 2000). This indicates that some GEDI
waveforms may represent partial leaf-off conditions in practice. An important assumption is
that GEDI04_A training data are representative of the variability introduced by partial leaf-off
conditions, and that the impact of this variability is subsumed into the GEDI04_A model
parameter uncertainty estimates. A final assumption is that GEDI04_A models are representative of the geographic
conditions to which they will be applied. Although the GEDI FSBD is comprehensive, important
regions are under-represented or missing entirely (Table 1). Training data are lacking in
continental Asia and throughout the GSW and DNT stratifications worldwide. In strata where
training data are lacking, the need to select a model for on-orbit prediction necessitates the
assumption that a model developed for a different location can be applied to that stratum to
produce unbiased predictions of AGBD.
4.3.
```

#### r2 — score 0.534

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 16
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 16
- **matched_tokens:** ['canopy', 'gedi']

**Full text:**

```
This is determined by
the following six tests: rx_algrunflag = 1, rx_assess/quality_flag = 1, zcross > 0, toploc > 0,
sensitivity > 0 and sensitivity < 1. Beam sensitivity is a measure of signal-to-noise that is related
to the maximum canopy cover that can be penetrated by a waveform (Hofton and Blair, 2020). For more information about waveform processing, see the ATBD for GEDI transmit and receive
waveform processing (Hofton and Blair, 2020). When these conditions are met, the GEDI04_A
algorithm_run_flag = 1. The algorithm looks up the PFT, world region, and algorithm selection
setting, then applies the selected model to scaled and transformed GEDI02_A RH metrics. Additional checks are performed to determine whether the GEDI04_A prediction is valid, and
ancillary data are computed (Table 3). After a prediction is generated, the algorithm determines the value of two quality
flags: l2_quality flag and l4_quality flag. The l2_quality_flag indicates whether GEDI02_A input
metrics met minimum quality standards for AGBD estimation. The l2_quality_flag = 1 when the
footprint passes five tests: algorithm_run_flag = 1, surface_flag = 1, stale_return_flag = 0,
sensitivity > 0.9, and rx_maxamp > 8 × sd_corrected. The surface_flag = 1 when
elev_lowestmode is within 300 m of the TanDEM-X 90 DEM or mean sea surface. The
stale_return_flag = 0 when the pulse detection algorithm detects a return signal > the detection
threshold within the search window.
```

#### r3 — score 0.517

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 16
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 16
- **matched_tokens:** ['canopy', 'gedi']

**Full text:**

```
The model selection favors candidates that contain larger valued RH metrics over models with
similar mean residual error and RMSE than models that contain smaller valued RH metrics. This is because RH metrics closer to the ground are more sensitive to differences between
simulated and real GEDI waveforms than RH metrics higher in the canopy. Reducing simulator
error for smaller valued RH metrics using the on-orbit transmit pulse shape and characteristics of
recorded GEDI noise will be addressed in a subsequent version of GEDI04_A. Models with
fewer coefficients and fewer RH metrics are preferred based on parsimony. The number of
coefficients is not directly proportional to the number of RH metrics because candidate models
contain interactions. For example, a model that contains the interaction between RH98 and RH50
as a single predictor contains two coefficients and two RH metrics. A model that contains only
RH98 and RH50 as main effects contains three coefficients and two RH metrics.
4. ALGORITHM DESCRIPTION
The GEDI04_A data product is AGBD (Mg · ha-1) for individual GEDI footprints and the
associated prediction uncertainty. The GEDI04_A algorithm ingests GEDI02_A data and
external input variables (Fig. 2, Table 2). A prediction is generated for every GEDI02_A
measurement for which it is possible to initiate the GEDI04_A algorithm.
```

#### r4 — score 0.506

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 47
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 47
- **matched_tokens:** ['canopy', 'gedi']

**Full text:**

```
799 2.2.3 Canopy_height_metrics_abs
800 (parameter = canopy_h_metrics_abs). The absolute height metrics (H##) of
801 classified canopy photons (labels 2 and 3) above the ellipsoid. The height metrics are
802 sorted based on a cumulative distribution and calculated at the following percentiles:
803 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95. These height metrics
804 are often used in the literature to characterize vertical structure of vegetation. One
805 important distinction of these canopy height metrics compared to those derived from
806 other lidar systems (e.g., LVIS or GEDI) is that the ICESat-2 canopy height metrics are
807 heights above the ground surface. These metrics do not include the ground photons.
808 Required input data are the relative canopy heights of all canopy photons above the
809 estimated terrain surface and the mid-segment elevation. The absolute canopy
810 heights metrics are determined by adding the relative canopy height metric to the
811 best-fit terrain (h_te_bestfit). For cases where the h_te_bestfit is invalid, the
812 cumulative distribution will be calculated for the absolute canopy heights (not the
813 relative canopy heights) and those cumulative heights will be reported.
814
815 2.2.4 Canopy_height_metrics
816 (parameter = canopy_h_metrics). Relative height metrics above the estimated
817 terrain surface (RH##) of classified canopy photons (labels 2 and 3).
```

#### r5 — score 0.502

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 20
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 20
- **matched_tokens:** ['canopy', 'gedi']

**Full text:**

```
Optimal settings for
every combination of the GEDI04_A modified MCD12Q1 PFT and world region have been
identified by the GEDI Science Team using a comprehensive dataset of GEDI-ALS crossovers. GEDI-ALS crossovers are locations where recorded GEDI data intersects discrete-return
airborne lidar. At these locations we can remove systematic geolocation error in recorded GEDI
data and compare GEDI waveforms to simulated waveforms developed using discrete-return
lidar data. These comparisons enable selection of optimal algorithm settings by comparison to
true ground. GEDI04_A models were developed using training data collected under leaf-on
conditions. We use leaf_off_flag to identify GEDI waveforms that are likely to be under leaf-on
conditions. However the use of this flag in drought deciduous tropical forests may be
problematic. This is because some EBT forests experience periods of partial deciduousness
during which some percentage of crowns are leafless while the canopy as a whole is green. For
example, a study across a rainfall gradient in Panama found that 3.6 – 19.1% of crown area was
leafless at peak deciduousness (Condit et al., 2000). All of the areas in this study are classified as
EBT using MCD12Q1. This indicates that some GEDI footprints with leaf_off_flag = 0 may
represent partial leaf-off conditions in practice.
```

---

