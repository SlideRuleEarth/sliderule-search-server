# Row 91 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `91-measure-forest-canopy-height-with-space-lidar-review.md` —
> verdicts go there, this side is read-only.

**Query:** `measure forest canopy height with space lidar`
**Panel signature:** `0c7ae3622e99`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `3. atl08`
  - `1.6 phoreal`
  - `atl08 classification`
- **expected_pages:** (none)
- **notes:** atl08x/phoreal without ATL08 terminology

---

## 📚 docsearch results (top 5)

#### r1 — score 0.375

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-5.1: Raster Sampling
- **category:** `developer_guide`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
The following raster datasets shall be supported for sampling: GEDI L3 gridded ground elevation GEDI L3 gridded canopy height GEDI L3 gridded ground elevation-standard deviation GEDI L3 gridded canopy heigh-standard deviation GEDI L3 gridded counts of valid laser footprints MERIT Digital Elevation Model Simulated SWOT Data Simulated SWOT Data USGS 3DEP 1m Digital Elevation Model Worldwide land cover mapping Harmonized LandSat Sentinal-2 PGC Arctic Digital Elevation Model Mosaic PGC Arctic Digital Elevation Model Strips PGC Reference Elevation Model of Antarctica Mosaic PGC Reference Elevation Model of Antarctica Strips
```

#### r2 — score 0.387

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** Appendix A. Parameter Components
- **category:** `developer_guide`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
ables inputs below) Land Type : label noise : checkbox ground : checkbox canopy : checkbox top_of_canopy : checkbox unclassified : checkbox ATL03 YAPC : input switch (enables inputs below) Score : input number SR YAPC : input switch (enables inputs below) Score : input number Knn : input number Window Height : input number Window Width : input number Version : label version 1 : radio button version 2 : radio button version 3 : radio button Extents (Variable-Length Segmentation) : accordion header [ICESat-2] Length : input number (meters) Step Size : input number (meters) Distance in Segments : checkbox (changes above inputs to segments instead of meters) Pass Invalid : checkbox Along Track Spread : input number [greyed out when pass invalid selected] Minimum Photon Count : input number [greyed out when pass invalid selected] Surface Elevation Algorithm : accordion header [atl06] Maximum Iterations : input number Minimum Window Height : input number (meters) Maximum Robust Dispersion : input number (meters) Vegetation Density Algorithm : accordion header [atl08] Bin Size : input number (meters) Geolocation : label mean : radio button median : radio button center : radio button Use Absolute Heights : checkbox Send Waveforms : checkbox Use ABoVE Classifier : checkbox Ancillary Fields : accordion header [ICESat-2] ATL03 Geospatial Fields : multiselect [atl03, atl06] ATL03 Photon Fields : multiselect [atl03, atl06] ATL06 Ice Segment Fields : multiselect [atl06s] ATL08 Land Segment
```

#### r3 — score 0.405

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-01-00.html
- **title:** Release v2.1.x
- **section:** Known Issues
- **category:** `release_notes`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
PhoREAL processing includes some known bugs - the median ground height uses the relative heights instead of absolute heights, and the canopy openness calculation is incorrect
```

#### r4 — score 0.434

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v03-00-00.html
- **title:** Release v3.0.x
- **section:** Issues Resolved
- **category:** `release_notes`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
PhoREAL processing bug fixes: the median ground height now uses the absolute heights, and the canopy openness calculation is now correctly implements the standard deviation
```

#### r5 — score 0.479

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 3. ATL08 - atl08x
- **category:** `user_guide`
- **matched_tokens:** ['canopy', 'height']

**Full text:**

```
at) land_segments/terrain/h_te_uncertainty h_te_median Median height of the terrain meters (float) land_segments/terrain/h_te_median h_canopy 98 percentile height of canopy photons meters (float) land_segments/canopy/h_canopy (or land_segments/canopy/h_canopy_abs if use_abs_h is true) h_canopy_uncertainty Vertical uncertainty of canopy height meters (float) land_segments/canopy/h_canopy_uncertainty segment_cover Average percentage value of the valid Copernicus fractional cover product scalar land_segments/canopy/segment_cover n_ca_photons Number of canopy photons land_segments/canopy/n_ca_photons h_max_canopy Maximum canopy height meters (float) land_segments/canopy/h_max_canopy (or land_segments/canopy/h_max_canopy_abs if use_abs_h is true) h_min_canopy Minimum canopy height meters (float) land_segments/canopy/h_min_canopy (or land_segments/canopy/h_min_canopy_abs if use_abs_h is true) h_mean_canopy Mean canopy height meters (float) land_segments/canopy/h_mean_canopy (or land_segments/canopy/h_mean_canopy_abs if use_abs_h is true) canopy_openness Standard Deviation of all canopy photons meters (float) land_segments/canopy/canopy_openness canopy_h_metrics Cumulative distribution of relative canopy heights calculated at the following percentiles: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 meters (float) land_segments/canopy/canopy_h_metrics (or land_segments/canopy/canopy_h_metrics_abs if use_abs_h is true) spot ATLAS detector field of view 1-6 Inde
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.687

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 23
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 23
- **matched_tokens:** ['canopy', 'forest', 'height', 'lidar']

**Full text:**

```
T. (2002). Lidar remote
sensing of above-ground biomass in three biomes. Global Ecology and Biogeography, 11(5),
393–399. Lefsky, M. A., Harding, D. J., Keller, M., Cohen, W. B., Carabajal, C. C., Del Bom Espirito-Santo, F., et al.
(2005). Estimates of forest canopy height and aboveground biomass using ICESat: ICESAT
ESTIMATES OF CANOPY HEIGHT. Geophysical Research Letters, 32(22), n/a-n/a.
https://doi.org/10.1029/2005GL023971
23
```

#### r2 — score 0.616

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 22
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 22
- **matched_tokens:** ['forest', 'height', 'lidar', 'space']

**Full text:**

```
Hancock, S., Armston, J., Hofton, M., Sun, X., Tang, H., Duncanson, L. I., et al. (2019). The GEDI Simulator:
A Large-Footprint Waveform Lidar Simulator for Calibration and Validation of Spaceborne
Missions. Earth and Space Science, 6(2), 294–310. https://doi.org/10.1029/2018EA000506
Hansen, E. H., Gobakken, T., Bollandsås, O. M., Zahabu, E., & Næsset, E. (2015). Modeling Aboveground
Biomass in Dense Tropical Submontane Rainforest Using Airborne Laser Scanner Data. Remote
Sensing, 7(1), 788–807. https://doi.org/10.3390/rs70100788
Hansen, M. C., Stehman, S. V., & Potapov, P. V. (2010). Quantification of global gross forest cover loss. Proceedings of the National Academy of Sciences of the United States of America, 107(19),
8650–8655. https://doi.org/10.1073/pnas.0912668107
Healey, S. P., Yang, Z., Gorelick, N., & Ilyushchenko, S. (2020). Highly Local Model Calibration with a New
GEDI LiDAR Asset on Google Earth Engine Reduces Landsat Forest Height Signal Saturation. Remote Sensing, 12(17), 2840. https://doi.org/10.3390/rs12172840
Healey, S. P., Patterson, P. L., & Armston, J. (2022). Algorithm Theoretical Basis Document (ATBD) for
GEDI Level-4B Gridded Aboveground Biomass Density. Heath, L. S., Hansen, M., Smith, J. E., & Miles, P. D. (2009). Investigation into calculating tree biomass
and carbon in the FIADB using a biomass expansion factor approach. In: McWilliams, Will;
Moisen, Gretchen; Czaplewski, Ray, Comps.
```

#### r3 — score 0.587

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 11
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 11
- **matched_tokens:** ['forest', 'height', 'lidar', 'measure']

**Full text:**

```
using complete data records. If no height measurements were available, we used the published
height-diameter allometry of Muukkonen (2007) in Europe, and the models of Feldpausch et al.
(2011) elsewhere except the United States. In the United States, we developed a local height-
diameter allometry using United States Department of Agriculture Forest Inventory and
Analysis (FIA) data within the same county and used this locally developed model to predict
tree height.
4.2. Scientific assumptions
Allometric models are assumed to generate unbiased estimates of 𝑀𝑖 when applied to
non-harvested trees. Whether this assumption is true has been debated. Harvested trees used
to develop allometric scaling relationships are usually not randomly sampled (Clark and Kellner,
2012), and validation studies that directly measure tree mass have demonstrated that
allometric models systematically underestimate 𝑀𝑖 for large trees (e.g., Gonzalez de Tanago et
al., 2018). An important area for future research is the development of improved allometric
scaling models or no-allometry methods based on terrestrial laser scanning or drone lidar
(Calders et al., 2020; Disney et al., 2020; Kellner et al., 2019). GEDI04_A models treat footprints as circular areas with a radius of 12.5 m. In model
training, 𝑀𝑖 is assigned to the footprint using stem positions or the mean AGBD associated with
a given subplot that contains a simulated GEDI waveform.
```

#### r4 — score 0.678

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 19
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 19
- **matched_tokens:** ['canopy', 'forest', 'lidar']

**Full text:**

```
Coops, N. C., Hilker, T., Wulder, M. A., St-Onge, B., Newnham, G., Siggins, A., & Trofymow, J. A. (Tony).
(2007). Estimating canopy structure of Douglas-fir forest stands from discrete-return LiDAR. Trees, 21(3), 295–310. https://doi.org/10.1007/s00468-006-0119-6
Disney, M., Burt, A., Calders, K., Schaaf, C., & Stovall, A. (2019). Innovations in Ground and Airborne
Technologies as Reference and for Training and Validation: Terrestrial Laser Scanning (TLS). Surveys in Geophysics, 40(4), 937–958. https://doi.org/10.1007/s10712-019-09527-x
Disney, Mathias, Burt, A., Wilkes, P., Armston, J., & Duncanson, L. (2020). New 3D measurements of
large redwood trees for biomass and structure. Scientific Reports, 10(1), 16721.
https://doi.org/10.1038/s41598-020-73733-6
Drake, J., Dubayah, R., Clark, D. B., Knox, R. G., Hofton, M. A., Chazdon, R. L., et al. (2002). Estimation of
tropical forest structural characteristics using large-footprint lidar.
https://doi.org/10.1016/S0034-4257(01)00281-4
Dubayah, R., Blair, J. B., Goetz, S., Fatoyinbo, L., Hansen, M., Healey, S., et al. (2020). The Global
Ecosystem Dynamics Investigation: High-resolution laser ranging of the Earth’s forests and
topography. Science of Remote Sensing, 1, 100002. https://doi.org/10.1016/j.srs.2020.100002
Dubayah, R. O., Sheldon, S. L., Clark, D. B., Hofton, M. A., Blair, J. B., Hurtt, G. C., & Chazdon, R. L. (2010).
```

#### r5 — score 0.630

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl08_atbd_v007.pdf
- **title:** ATL08 v007 atbd
- **section:** Page 138
- **category:** `atbd`
- **source_product:** `ATL08` · **page:** 138
- **matched_tokens:** ['canopy', 'forest', 'height', 'lidar']

**Full text:**

```
Canopy height <2 m temperate forest, < 3 m tropical
forest
Canopy cover n/a
2917
2918 Terrain and canopy heights will be validated by computing the residuals between the
2919 ATL08 terrain and canopy height value, respectively, for a given 100 m segment and
2920 the terrain height (or canopy height) of the validation data for that same
2921 representative distance. Canopy cover on the ATL08 data product shall be validated
2922 by computing the relative canopy cover (cc = canopy returns/total returns) for the
2923 same representative distance in the airborne lidar data.
2924 It is recommended that the validation process include the use of ancillary data sets
2925 (i.e. Landsat-derived annual forest change maps) to ensure that the validation results
2926 are not errantly biased due to non-equivalent content between the data sets.
2927 Using a synergistic approach, we present two options for acquiring the required
2928 validation airborne lidar data sets.
2929
2930 Option 1:
2931 We will identify and utilize freely available, open source airborne lidar data as the
2932 validation data. Potential repositories of this data include OpenTopo (a NSF
2933 repository or airborne lidar data), NEON (a NSF repository of ecological monitoring
2934 in the United States), and NASA GSFC (repository of G-LiHT data). In addition to
2935 small-footprint lidar data sets, NASA Mission data (i.e.
```

---

