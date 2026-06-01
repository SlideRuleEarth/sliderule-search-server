# Row 81 results: docsearch / example

> Auto-generated. Open this file alongside `81-export-results-to-geoparquet-for-gis-review.md` —
> verdicts go there, this side is read-only.

**Query:** `export results to GeoParquet for GIS`
**Panel signature:** `7a1e5adc0e9a`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/arrow_output.html
  - https://docs.slideruleearth.io/user_guide/articles/230224_geoparquet.html
- **expected_sections:** (none)
- **expected_pages:** (none)
- **notes:** GeoParquet/arrow output

---

## 📚 docsearch results (top 5)

#### r1 — score 0.604

- **url:** https://docs.slideruleearth.io/user_guide/arrow_output.html
- **title:** Arrow Output
- **section:** Parameters
- **category:** `user_guide`
- **matched_tokens:** ['geoparquet', 'results']

**Full text:**

```
To control writing the data to an Arrow supported format, the output parameter is used. output : settings to control how SlideRule outputs results path : the full path and filename of the file to be constructed by the client, NOTE - the path MUST BE less than 128 characters format : the format of the file constructed by the servers and sent to the client (currently, only GeoParquet is supported, specified as âparquetâ) open_on_complete : boolean; if true then the client is to open the file as a DataFrame once it is finished receiving it and writing it out; if false then the client returns the name of the file that was written as_geo : if the parquet format is specified, write the data compliant with the GeoParquet specification with_checksum : include a checksum of the returned file in the response with_validation : run the Apache Arrow validation routine on the resulting file before returning it to the user endpoint : AWS endpoint (i.e. region) when the output path is an S3 bucket (e.g. âs3.us-west-2.amazonaws.comâ) asset : the name of the SlideRule asset from which to get credentials for the optionally supplied S3 bucket specified in the output path credentials : the AWS credentials for the optionally supplied S3 bucket specified in the output path aws_access_key_id : AWS access key id aws_secret_access_key : AWS secret access key aws_session_token : AWS session token fields : the list of fields to include in the file output, trimming anything not found in this list
```

#### r2 — score 0.593

- **url:** https://docs.slideruleearth.io/user_guide/articles/230224_geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** 2023-02-24: GeoParquet
- **category:** `user_guide`
- **matched_tokens:** ['geoparquet', 'results']

**Full text:**

```
Warning SlideRule now supports returning results back to data users as GeoParquet files. The functionality described in this article has been improved with broad support for returning data via Apache Arrow based formats.
```

#### r3 — score 0.489

- **url:** https://docs.slideruleearth.io/developer_guide/design/SlideRuleWebClient.html
- **title:** SlideRule Web Client
- **section:** SRWC-3.6: Result Display
- **category:** `developer_guide`
- **matched_tokens:** ['geoparquet', 'results']

**Full text:**

```
When the results of a processing request are returned to the client, those results should immediately be displayed on the map view if applicable. In other words, if the request parameters are such that the data is streamed back to the client as it becomes available (e.g. the GeoParquet option is NOT selected), then the map should display the data points immediately upon receipt and not wait for the entire processing request to finish before displaying the data points.
```

#### r4 — score 0.573

- **url:** https://docs.slideruleearth.io/user_guide/articles/230224_geoparquet.html
- **title:** 2023-02-24: GeoParquet
- **section:** Overview
- **category:** `user_guide`
- **matched_tokens:** ['geoparquet', 'results']

**Full text:**

```
SlideRule currently supports returning results back to data users as GeoParquet files. These files are built on the server and either streamed back directly to the user, or uploaded to a user-specified S3 bucket for later access. To specify the GeoParquet option, the request must include the output parameter with the output.format field set to âparquetâ . See the section on output parameters in Arrow Output for more details.
```

#### r5 — score 0.478

- **url:** https://docs.slideruleearth.io/developer_guide/release_notes/release-v02-00-00.html
- **title:** Release v2.0.x
- **section:** New Features
- **category:** `release_notes`
- **matched_tokens:** ['geoparquet', 'results']

**Full text:**

```
Ancillary Fields : Additional ATL03 subgroup datasets can now be included in the results of the calls to atl03sp and atl06p . When requested, they appear as additional columns in the GeoDataFrame. This feature was added to support bathymetry and other science use cases that used additional data provided in the ATL03 data that isnât provided as a part of the standard ATL06-SR processing. GeoParquet : SlideRule can now return results as a GeoParquet file which is built entirely on the servers and streamed directly back to the client. Intelligent Load Balancing : The underlying architecture of the cluster of processing nodes was reworked so that each processing node is allocated a fixed number of computational credits. When a request is made to a cluster, the processing is routed to the nodes with the most available credits. If there are no nodes with available credits, the request is held while the system polls for available nodes until a user-supplied timeout is reached, at which point the client is informed that the request could not be processed.
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.185

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 15
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 15
- **matched_tokens:** ['results']

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

#### r2 — score 0.153

- **url:** https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4A_AGB_Density_GW/comp/GEDI_ATBD_L4A_v1.0.pdf
- **title:** Microsoft Word - GEDI_ATBD_L4A_20210811.docx
- **section:** Page 18
- **category:** `atbd`
- **source_product:** `GEDI_L4A` · **page:** 18
- **matched_tokens:** ['results']

**Full text:**

```
Repeating this process for many individual trees results in data that are used to estimate the
parameters of equation (3). For every tree-record in the FSBD we used an allometric model appropriate to the given
PFT and world region to predict 𝑀!. When there was more than one model that could be used for
a given tree, we favored locally developed models over regional ones, as long as locally-
developed models were not site-specific. We also favored models with finer taxonomic
resolution. In Australia we use eight allometric models developed by Paul et al. (2016) and
Roxburgh et al. (2019). In New Zealand we use the model developed by Moore (2010) for Pinus
radiata, and the model of Beets et al. (2011) for all other species. In North America we use the
models of Jenkins et al. (2003) in the continental United States and the models of Ung et al.
(2008) in Canada. In Europe we use the allometric models of Forrester et al. (2017). Throughout
the tropics of South America, Africa and Asia we use the model of Chave et al. (2014). In some situations there was more than one candidate model to predict 𝑀! that met
GEDI04_A requirements. For example, the models of Brown (1997) and Chave et al. (2014)
have been used to predict 𝑀! in Central American evergreen broadleaf forests. The models of
Muukkonen (2007) and Forrester et al. (2017) have been used in deciduous broadleaf and
evergreen needleleaf forests of Europe.
```

#### r3 — score 0.221

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 4
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 4

**Full text:**

```
The
FSBD is the most geographically comprehensive data available for the development of AGBD
models using remote sensing, but important regions are under-represented. Underrepresented
locations include the forests of continental Asia, the evergreen broadleaf forests throughout
the islands of Southeast Asia and north of Australia, and the worldwide distribution of savannas
and deciduous tropical forests (Table 1). The approach to model development considered candidates whose performance was
evaluated outside the geographic extent of training data. Candidate models were evaluated
within sets of 5-degree grid cells that contain simulated GEDI waveforms with coincident field
data. The approach set aside data from one grid cell for testing and trained the model using
data within the remaining grid cells. The trained model was used to predict AGBD within the
held-out grid cell, and the process was repeated for all grid cells and all models under
consideration (Fig. 1).
3.1. Stratification of GEDI04_A models
Building globally representative GEDI04_A models requires stratification (Duncanson et
al., 2022). The models are stratified by world region and PFT (Fig. 2, Table 1). World regions are
the geologically defined continents of Africa and Europe in addition to other continents and
locations. The South America world region is the continent of South America, Central America
and the Caribbean islands, and geological North America south of southern Mexico.
```

#### r4 — score 0.235

- **url:** https://daac.ornl.gov/GEDI/guides/GEDI_L4A_AGB_Density_V2_1.html
- **title:** GEDI_L4A v2.1 user guide
- **section:** Page 32
- **category:** `user_guide`
- **source_product:** `GEDI_L4A` · **page:** 32

**Full text:**

```
Table 2. Associations between 14 models and 32 prediction strata in the GEDI domain. These associations refer to the release 1
and release 2 GEDI04_A data product.
Model name Prediction strata
DBT DBT × North Asia, EBT North Asia
EBT DBT × South Asia, EBT × South Asia
DNT × North Asia, DNT × South Asia, ENT × Africa, ENT × North Asia, ENT × South America, ENT ×
ENT
South Asia
GSW × Africa, GSW × Europe, GSW × North America, GSW × North Asia, GSW × South America,
GSW
GSW × South Asia
DBT × Africa DBT × Africa
DBT × Europe DBT × Europe, EBT × Europe
DBT × North America DBT × North America, EBT × North America
EBT × Africa EBT × Africa
EBT × Australia DBT × Australia, EBT × Australia
EBT × South America DBT × South America, EBT × South America
ENT × Australia DNT × Australia, ENT × Australia
ENT × Europe DNT × Europe, ENT × Europe
ENT × North America DNT × North America, ENT × North America
GSW × Australia and Oceania GSW × Australia and Oceania
32
```

#### r5 — score 0.197

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl24_atbd_v001.pdf
- **title:** ATL24 v001 atbd
- **section:** Page 6
- **category:** `atbd`
- **source_product:** `ATL24` · **page:** 6
- **matched_tokens:** ['results']

**Full text:**

```
List of Tables
1 History of changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
2 ATL24 input variables and processing details within each stage of the product
production . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 ATL24 component input for processing pipeline . . . . . . . . . . . . . . . . 12
4 ATL24 output variables for each stage of the product production . . . . . . . 12
5 ATL24 naming convention . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 Sea Surface cross validation results from 180 labeled datasets. . . . . . . . . 39
7 Bathymetry cross validation results from 180 labeled datasets. . . . . . . . . 39
8 Cross validation results from 180 labeled datasets. . . . . . . . . . . . . . . . 39
9 Known issues, reasons and possible solutions to ATL24 classification accuracy 48
vi
```

---

