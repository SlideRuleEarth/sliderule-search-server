# Row 90 results: docsearch / paraphrased

> Auto-generated. Open this file alongside `90-get-lake-water-levels-from-satellite-altimetry-review.md` —
> verdicts go there, this side is read-only.

**Query:** `get lake water levels from satellite altimetry`
**Panel signature:** `1e318d8f4a01`

## Auto-labeled (current ground truth)

- **corpus:** `docsearch`
- **expected_urls:**
  - https://docs.slideruleearth.io/user_guide/icesat2.html
- **expected_sections:**
  - `4. atl13`
  - `4.1 inland lake`
- **expected_pages:** (none)
- **notes:** atl13x without ATL13 terminology

---

## 📚 docsearch results (top 5)

#### r1 — score 0.566

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4.1 Inland Lake Parameters
- **category:** `user_guide`
- **matched_tokens:** ['lake', 'water']

**Full text:**

```
Inland lake data can be queried using the following parameters under the atl13 key: atl13 : refid : ATL13 reference id name : lake (or body of water) name coord : latitude and longitude coordinates contained within the desired body of water|object {âlatâ: \(lat, "lon": \) lon}
```

#### r2 — score 0.510

- **url:** https://docs.slideruleearth.io/user_guide/icesat2.html
- **title:** ICESat-2 Module
- **section:** 4. ATL13 - atl13x
- **category:** `user_guide`
- **matched_tokens:** ['from', 'lake', 'water']

**Full text:**

```
The SlideRule atl13x endpoint provides a service for ATL13 subsetting and custom processing. This endpoint queries ATL13 input granules for segment inland lake statistics based on geographic and temporal ranges. These statistics are typically directly returned to the client, but may be passed to downstream algorithms and custom processing steps like raster sampling. This endpoint is called via: sliderule . run ( 'atl13x' , parms ) The default resulting DataFrame from this API contains the following columns: Field Description Units Notes time_ns Unix Time nanoseconds index column of DataFrame latitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 longitude segment coordinate (replaced by geometry column when GeoDataFrame) degrees (double) EPSG:7912 ht_ortho Orthometric height of the water surface meters (float) EGM08 ht_water_surf Ellipsoidal height of the water surface meters (float) WGS84 stdev_water_surf Derived standard deviation of water surface meters (float) water_depth Depth from the mean water surface to detected bottom meters (float) spot ATLAS detector field of view 1-6 Independent of spacecraft orientation cycle ATLAS orbit cycle number rgt Reference Ground Track gt Beam âgt1lâ, âgt1râ, âgt2lâ, âgt2râ, âgt3lâ, âgt3râ Dependent on spacecraft orientation
```

#### r3 — score 0.398

- **url:** https://docs.slideruleearth.io/user_guide/articles/250530_arbitrary_code_execution.html
- **title:** 2025-05-30: Arbitrary Code Execution
- **section:** Example Use Case - ATL13 Lake ID Mapping
- **category:** `user_guide`
- **matched_tokens:** ['lake', 'water']

**Full text:**

```
The ATL13 inland lake data product contains along-track water surface characteristics for inland bodies of water. Each measurement (i.e. variable) in the product is tagged with a reference ID which can be used as an index into an internal ATL13 global database of inland water bodies. This database contains a geometry for each body of water and is used in the ATL13 processing to produce the ATL13 data product only over those bodies of water. Researchers requested the ability to retrieve the exact set of ATL13 data generated for a given body of water when supplying one of three pieces of information: (1) the ATL13 reference ID, (2) the name of the body of water, (3) a coordinate contained within a body of water. The ATL13 global database contains the reference ID, name, and geometry of each body of water, but does not contain a list of ATL13 granules that intersect (and therefore have data for) thoes bodies of water. We needed some way to know which granules contained data for each body of water; and we came up with two possibilities: Given a user query, use the global database to pull out the geometry. Use the geometry to query CMR for a list of granules that intersect. Build a reverse lookup table of reference IDs and granules by reading every ATL13 granule and pulling out which reference IDs are contained there in.
```

#### r4 — score 0.458

- **url:** https://docs.slideruleearth.io/background/ICESat-2.html
- **title:** ICESat-2
- **section:** Mission
- **category:** `background`
- **matched_tokens:** ['from', 'satellite']

**Full text:**

```
The Ice Cloud and land Elevation Satellite-2 (ICESat-2) is NASAâs latest satellite laser altimeter. The satellite was launched September 15, 2018 from Vandenberg Air Force Base in California onboard a ULA Delta II rocket . ICESat-2 has 1387 unique orbits that are repeated in an orbital cycle every 91 days. The primary instrumentation onboard the ICESat-2 observatory is the Advanced Topographic Laser Altimeter System (ATLAS, a photon-counting laser altimeter). ATLAS sends and receives data for 6 individual beams that are separated into three beam pairs. The two paired beams are separated on the ground by 90 meters and the three beam pairs are separated by 3 kilometers. Each beam pair consists of a weak beam and a strong beam, with the strong beam approximately four times brighter than weak. The six beam setup was designed to allow the determination of both along-track and across-track slope simultaneously everywhere on the globe. Each laser beam from the ATLAS instrument illuminates a spot on the ground. The spots illuminated from strong beams are numbered 1, 3, and 5, and the spots illuminated from weak beams are numbered 2, 4, and 6. The ICESat-2 observatory can be oriented in one of two positions with respect to the direction of travel. In the forward orientation, the weak beams lead the strong beams and a weak beam is on the left edge of the beam pattern (gt1l).
```

#### r5 — score 0.531

- **url:** https://docs.slideruleearth.io/getting_started/Examples.html
- **title:** Examples
- **section:** Examples
- **category:** `getting_started`
- **matched_tokens:** ['lake']

**Full text:**

```
ATL13 ( download ) Demonstrates different ways to access the ATL13 inland lake data: by reference ID, by name, and by contained coordinate. ATL24 ( download ) Subsets ATL24 near-shore bathymetry data using different methods and parameters. Previous Next © Copyright 2020â2026, University of Washington. Build v5.4.2 . Built with Sphinx using a theme provided by Read the Docs .
```

---

## 📘 nsidc results (top 5)

#### r1 — score 0.595

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 2.3.3 The Multiple Altimeter Beam Experimental Lidar (MABEL)
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 44
- **matched_tokens:** ['altimetry', 'from', 'lake', 'satellite', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
The feasibility of ICESat-2/ATLAS retrievals of inland water have been established in numerous
airborne lidar engineering and science studies and the ICESat/GLAS mission, including lakes. The ICESat/GLAS instrument was a single beam analog sensor with an approximately 70 m
footprint and along track spacing of about 180m. Inland water observations were successfully
explored with accuracies in the cm to decimeter range, and its height products were used in a
number of research and operational programs. The data were utilized in both lake and river
studies (e.g. Harding and Jasinski, 2004, Birkett et al., 2010, Calmant et al., 2008, Zhang et al.,
2011) that require both height and surface water slope. ICESat heights were also used to validate
radar altimetry measurements from ENVISAT and OSTM in the absence of in situ gauge data. Barton and Jasinski (2011) developed a formulation using CALIOP lidar to retrieve subsurface
backscatter as the residual term in the total water backscatter equation. They incorporated the Hu
et al (2008) surface specular reflectance that is wind and view angle dependent. The depth-
integrated attenuated backscatter (at wavelength λ, in nm) from the water surface viewed by the
satellite was represented as a linear sum of surface and subsurface scattering.
```

#### r2 — score 0.594

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.9.2.1 External Products Available for Monitoring ATL13 Data
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 86
- **matched_tokens:** ['altimetry', 'from', 'lake', 'satellite', 'water']

**Full text:**

```
Time series can be
evaluated with respect to mean water surface segment heights, variances, slopes, significant
wave height, subsurface attenuation, presence of ice, and identifiable bottom location, as a
function of water body type, location, water clarity and prevailing meteorological conditions. For
the Inland Water Data Product, monitoring occurs principally by leveraging off existing
databases supported by numerous organizations in the US and internationally, including radar
altimetry missions. Principal sources include:
a) Reservoir and lake elevations based on satellite radar altimetry from Jason 3, Sentinel 3A and
3B sensors and compiled at online archives. Example online data bases include:
i) Center for Topographic Studies of the Ocean and Hydrosphere (CTOH) data
http://ctoh.legos.obs-mip.fr/data
ii) HYDROWEB (Theia, LEGOS, other international)
https://www.theia-land.fr/en/hydroweb/
iii) Global Reservoir and Dam Database (GWSP)
https://www.globaldamwatch.org/grand/
iv) G-REALM (USDA)
https://ipad.fas.usda.gov/cropexplorer/global_reservoir
v) Global River Database
http://gaia.geosci.unc.edu/rivers/
vi) River and Lakes (ESA) (historical data)
http://altimetry.esa.int/riverlake/shared/main.html
vii) Database for Hydrological Time Series of Inland Waters (DAHITI)
https://dahiti.dgfi.tum.de/en/
viii) Global Water Monitor
63
Release 007, January 31, 2025
```

#### r3 — score 0.552

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.9.2.2 Assessment and Validation Activities
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 89
- **matched_tokens:** ['lake', 'levels', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Figure 4-10 Examples of potential collaborative calibration/validation sites (red circles) in Alaska.
c) Mid-Latitude Lakes and Reservoirs
Assessment sites include collaboration a several sites with various groups including the Great
Lakes (JALBTCX, Illinois State geological Survey), Lakes Mead (US Bureau of Reclamation),
Lake Fort Peck (USACE), Lake Tahoe and Western Lake Erie (Kent State). For the Great
Lakes, ATL13 is collaborating with efforts to measure Great Lakes surface water conditions at
the locations shown below.
Figure 4-11 Lake level gauge and monitoring stations on the Great Lakes.
https://www.glerl.noaa.gov/data/wlevels/levels.html#monitoringNetwork
d) Transitional Water Bodies (Estuaries, Bays, Near Shore Coasts)
Principal areas would include the Chesapeake Bay, and the estuaries of the
Mississippi/Atchafalaya River deltas, Everglades, Mackenzie River, and Yukon River, together
66
Release 007, January 31, 2025
```

#### r4 — score 0.544

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 7.0 REFERENCES
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 180
- **matched_tokens:** ['altimetry', 'from', 'lake', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
Birkett, C.M. and I.M. Mason, A new Global Lakes Database for a remote sensing programme
studying climatically sensitive large lakes, J. Great Lakes Research, 21, No.3, pp.307-318., 1995. Birkett, C.M., C. Reynolds, B. Beckley, and B. Doorn, From Research to Operations: The USDA
Global Reservoir and Lake Monitor, Chapter 2 in ‘Coastal Altimetry’, Springer Publications,
eds. S. Vignudelli, A.G. Kostianoy, P. Cipollini and J. Benveniste, Springer Publications, ISBN
978-3-642-12795-3, 2010. Breon, F. M., and Henriot, N., Spaceborne observations of ocean glint reflectance and modeling
of wave slope distributions, J. Geophys. Res., 111, C06005, doi: 10.1029/2005JC003343, 2006. Bricaud, A. and A. Morel (1986). Light attenuation and scattering by phytoplanktonic cells: a
theoretical modeling, Applied Optics, 25, 571-580. Buchheim, Oceanography, http://www.marinebiology.org/oceanography.htm. Bufton, J. L., F. E. Hoge, and R. N. Swift (1983), Airborne measurements of laser backscatter
from the ocean surface, Appl. Opt., 22, 2603–2618. Bukata R P, Jerome J H , Kondratyev K Y and Pozdnyakov D V 1995 Optical properties and
remote sensing of inland and coastal waters. CRC Press, 384pp. Callaghan, A., G. de Leeuw, L. Cohen, and C. D. O’Dowd (2008), Relationship of oceanic
whitecap coverage to wind speed and wind history, Geophys. Res. Lett., 35, L23609,
doi:10.1029/2008GL036165.
```

#### r5 — score 0.547

- **url:** https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl13_atbd_v007.pdf
- **title:** Table of Contents
- **section:** 4.9.2.2 Assessment and Validation Activities
- **category:** `atbd`
- **source_product:** `ATL13` · **page:** 87
- **matched_tokens:** ['lake', 'levels', 'water']

**Full text:**

```
ICESat-2 Algorithm Theoretical Basis Document for Along Track Inland Surface Water Data
ATL13 Release 7
https://blueice.gsfc.nasa.gov/gwm/lake/Index
b) In situ water level gauges primarily at reservoirs, lakes, and other water bodies monitored by
the: i) US Geological Survey (USGS), ii) National Oceanic and Atmospheric Administration
(NOAA), iii) Bureau of Land Management (BLM), and iv) US Army Corps of Engineers
(USACE). Although there are hundreds of available sites, the principal water bodies being
considered include Lake Fort Peck, MT; Lake Mead, NV; all Great Lakes; Lake Tahoe, CA;
Chesapeake Bay; Lake Teshekpuk and Toolik Lake, AK; Lake Issyk-Kul, Kyrgyzstan; water
bodies within the Mississippi, Connecticut, and Yukon River basins. All these water bodies are
well gaged by the USGS, NSF, or other US agencies with accessible online data. Analyses can
include evaluation mainly of root mean square error, bias, and mean absolute error. Databases
include:
i) NOAA Great Lakes Environmental Research laboratory
https://www.glerl.noaa.gov/data/wlevels/levels.html#observations
ii) Lake Levels (GWSP)
http://www.lakelevels.info
iii) Lakes Online
http://www.lakesonline.com/
iv) USGS National Water Information System
https://waterdata.usgs.gov/nwis
4.9.2.2 Assessment and Validation Activities
Assessment refers to a single post-launch evaluation of ICESat-2 data-product accuracy and/or
precision, generally against in situ data.
```

---

