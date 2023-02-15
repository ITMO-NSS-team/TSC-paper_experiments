![](doc/fedot-industrial.png)
## Time series classification experiments

The repository contains the experimental studies for "Evolutionary 
automated machine learning approach for time series classification" 
paper.

The experimental was conducted on the datasets taken from [UEA & UCR Time Series Classification Repository](http://www.timeseriesclassification.com/).

* **For binary classification** – BirdChicken, Chinatown, Computers, Coffee, DistalPhalanxOutlineCorrect
Earthquakes, ECG200, FordA, GunPointAgeSpan, GunPointMaleVersusFemale, GunPointOldVersusYoung, 
Ham, Herring, ItalyPowerDemand, Lightning2, MiddlePhalanx0utlineCorrect, MoteStrain, 
Phalanges0utlinesCorrect, PowerCons, ProximalPhalanxOutlineCorrect, ShapeletSim, SonyAIBORobotSurface1, 
SonyAIBORobotSurface2, Strawberry, ToeSegmentation2, TwoLegECG, Wafer, WormsTwoC1ass, Yoga

* **For multiclass classification** – ACSF1, Adiac, ArrowHead, Beef, Car, ChlorineConcentration, 
CricketX, CricketY, CricketZ, Crop, DistalPhalanxTW, DistalPhalanx0utlineAgeGroup, ECG5000, 
ElectricDevices, EOGVerticalSignal, EthanolLevel, FaceFour, Haptics, InlineSkate, LargeKitchenAppliances, 
Lightning7, Mallat, Meat, MiddlePhalanxOutlineAgeGroup, MiddlePhalanxTW, OliveOil, Phoneme, Plane, 
ProximalPhalanxOutlineAgeGroup, ProximalPhalanxTW, RefrigerationDevices, Rock, ScreenType, 
SwedishLeaf, SyntheticControl, Trace, UMD


FEDOT.Industrial framework is available in [main repository](https://github.com/aimclub/Fedot.Industrial).

#### Results for multiclass classification 

| Dataset                        | SOTA result | SOTA algorithm | Baseline model | FEDOT result | Feature generation algorithm                          |
| ------------------------------ | ----------- | -------------- | -------------- | ------------ | ----------------------------------------------------- |
| ACSF1                          | 0.901       | OS-CNN         | 0.733          | 0.849        | WindowQuantiIe                                        |
| Adiac                          | 0.851       | OS-CNN         | 0.011          | 0.776        | Ensemble: Quantile, Topological                       |
| ArrowHead                      | 0.876       | cBOSS          | 0.635          | 0.803        | WindowSpectraI                                        |
| Beef                           | 0.768       | OS-CNN         | 0.572          | 0.828        | Quantile                                              |
| Car                            | 0.914       | ROCKET         | 0.668          | 0.933        | Ensemble: WindowSpectral, WindowQuantile, Topological |
| ChlorineConcentration          | 0.850       | OS-CNN         | 0.522          | 0.720        | WindowQuantiIe                                        |
| CricketX                       | 0.855       | InceptionTime  | 0.469          | 0.707        | WindowQuantile                                        |
| Crickety                       | 0.863       | OS-CNN         | 0.452          | 0.653        | WindowQuantile                                        |
| CricketZ                       | 0.859       | OS-CNN         | 0.515          | 0.729        | Ensemble: WindowSpectraI, WindowQuantiIe, Topological |
| Crop                           | 0.791       | InceptionTime  | 0.647          | 0.798        | Ensemble:WindowSpectraI, WindowQuantiIe               |
| DistalPha1anxTW                | 0.863       | OS-CNN         | 0.590          | 0.660        | WindowQuantile                                        |
| DistalPhalanxOutIineAgeGroup   | 0.808       | TS-CHIEF       | 0.779          | 0.749        | Ensemble: Quantile, Spectral, WindowQuantiIe          |
| ECG5000                        | 0.945       | OS-CNN         | 0.008          | 0.933        | recurrence                                            |
| ElectricDevices                | 0.868       | ROCKET         | 0.649          | 0.725        | Ensemble: Quantile, WindowQuantile                    |
| EOGVerticalSignaI              | 0.811       | InceptionTime  | 0.373          | 0.475        | Ensemble: Quantile, WindowQuantiIe                    |
| EthanolLeveI                   | 0.875       | InceptionTime  | 0.343          | 0.792        | Ensemble: Quantile, ECM                               |
| FaceFour                       | 0.999       | TS-CHIEF       | 0.579          | 0.831        | Ensemble: Topological, Quantile                       |
| Haptics                        | 0.521       | STC            | 0.350          | 0.440        | Ensemble: Topological, Quantile                       |
| InlineSkate                    | 0.668       | WEASEL         | 0.341          | 0.378        | Ensemble: Topological, WindowQuantile, Wavelet        |
| LargeKitchenAppliances         | 0.954       | ResNet         | 0.766          | 0.816        | Ensemble: Quantile, Topological                       |
| Lightning7                     | 0.818       | InceptionTime  | 0.497          | 0.779        | Quantile                                              |
| Mallat                         | 0.976       | TS-CHIEF       | 0.739          | 0.884        | Ensemble: Wavelet, WindowQuantiIe                     |
| Meat                           | 0.994       | ResNet         | 0.770          | 0.836        | Ensemble: Topological, Spectral                       |
| MiddlePhaIanxOutIineAgeGroup   | 0.653       | ROCKET         | 0.521          | 0.606        | Ensemble: Spectral, Topological, Quantile             |
| MiddlePhalanxTW                | 0.543       | OS-CNN         | 0.442          | 0.497        | Ensemble: Spectral, WindowQuantile                    |
| OliveOi1                       | 0.897       | TS-CHIEF       | 0.640          | 0.810        | Ensemble: Topological, Spectral                       |
| Phoneme                        | 0.331       | OS-CNN         | 0.028          | 0.244        | Topological                                           |
| Plane                          | 1.0         | OS-CNN         | 1.0            | 1.0          | WindowQuantile                                        |
| ProximalPhalanxOutlineAgeGroup | 0.840       | OS-CNN         | 0.831          | 0.847        | Ensemble: Wavelet, WindowQuantile                     |
| ProximalPha1anxTW              | 0.793       | OS-CNN         | 0.725          | 0.844        | Ensemble: Wavelet, WindowQuantiIe                     |
| RefrigerationDevices           | 0.790       | HIVE-COTE v1.0 | 0.498          | 0.545        | WindowQuantile                                        |
| Rock                           | 0.848       | STC            | 0.493          | 0.880        | Ensemble: Topological, WindowQuantiIe                 |
| ScreenOpe                      | 0.755       | ResNet         | 0.420          | 0.484        | Ensemble: Topological, WindowQuantiIe, Wavelet        |
| SwedishLeaf                    | 0.971       | OS-CNN         | 0.810          | 0.904        | Ensemble: Topological, Spectral                       |
| SyntheticControI               | 0.999       | TS-CHIEF       | 0.912          | 0.999        | Ensemble: Quantile, Spectral                          |
| Trace                          | 1.0         | OS-CNN         | 1.0            | 1.0          | Spectral                                              |
| UMD                            | 0.993       | OS-CNN         | 0.892          | 1.0          | Ensemble: WindowQuantile, WindowSpectral              |
| **Average values**                 | **0.839**       |                | **0.574**          | **0.750**        |                                                       |

### Results for binary classification

| Dataset                       | SOTA result | SOTA algorithm  | Baseline model | FEDOT result | Feature generation algorithm       |
| ----------------------------- | ----------- | --------------- | -------------- | ------------ | ---------------------------------- |
| BirdChicken                   | 0.999       | TS-CHIEF        | 0.800          | 1.0          | Statistical                        |
| Chinatown                     | 0.993       | ROCKET          | 0.896          | 0.995        | WindowQuantile                     |
| Computers                     | 0.927       | InceptionTime   | 0.744          | 0.766        | Quantile                           |
| Coffee                        | 1.0         | OS-CNN          | 0.933          | 1.0          | WindowSpectral                     |
| DistalPhalanxOutlineCorrect   | 0.914       | ROCKET          | 0.769          | 0.771        | WindowQuanti1e                     |
| Earthquakes                   | 0.693       | ProximityForest | 0.509          | 0.740        | Quantile                           |
| ECG200                        | 0.957       | InceptionTime   | 0.820          | 0.894        | Ensemble: Quantile, WindowQuantile |
| FordA                         | 0.994       | WEASEL          | 0.705          | 0.970        | Spectral                           |
| GunPointAgeSpan               | 0.999       | TS-CHIEF        | 0.968          | 0.971        | Spectral                           |
| GunPointMaleVersusFemale      | 1.0         | OS-CNN          | 0.997          | 1.0          | Spectral                           |
| GunPointOldVersusYoung        | 1.0         | OS-CNN          | 1.0            | 1.0          | Spectral                           |
| Ham                           | 0.706       | OS-CNN          | 0.600          | 0.724        | WindowQuanti1e                     |
| Herring                       | 0.686       | STC             | 0.653          | 0.626        | Topological                        |
| ItalyPowerDemand              | 0.992       | TS-CHIEF        | 0.723          | 0.993        | Ensemble: WindowSpectral, ECM      |
| Lightning2                    | 0.928       | InceptionTime   | 0.629          | 0.689        | WindowSpectral                     |
| MiddlePhalanxOutlineCorrect   | 0.928       | ROCKET          | 0.708          | 0.803        | Window Quantile                    |
| MoteStrain                    | 0.984       | HIVE-COTE v1.0  | 0.804          | 0.834        | Spectral                           |
| PhalangesOutlinesCorrect      | 0.929       | InceptionTime   | 0.711          | 0.818        | Window Quantile                    |
| PowerCons                     | 1.0         | TSF             | 0.950          | 1.0          | Window Spectral                    |
| ProximalPhalanxOutlineCorrect | 0.946       | InceptionTime   | 0.709          | 0.848        | Window Quantile                    |
| ShapeletSim                   | 1.0         | HIVE-COTE v1.0  | 0.489          | 1.0          | Topological                        |
| SonyAIBORobotSurface1         | 0.998       | ResNet          | 0.849          | 0.892        | Window Quantile                    |
| SonyAIBORobotSurface2         | 0.997       | ResNet          | 0.770          | 0.824        | Window Quantile                    |
| Strawberry                    | 0.997       | ROCKET          | 0.905          | 0.924        | Spectral                           |
| ToeSegmentation2              | 0.995       | HIVE-COTE v1.0  | 0.622          | 0.869        | Spectral                           |
| TwoLeadECG                    | 1.0         | ResNet          | 0.846          | 0.919        | Quantile                           |
| Wafer                         | 1.0         | TS-CHIEF        | 0.944          | 1.0          | Quantile                           |
| WormsTwoC1ass                 | 0.904       | BOSS            | 0.652          | 0.715        | Topological                        |
| Yoga                          | 0.975       | S-BOSS          | 0.730          | 0.797        | WindowQuantile                     |
| **Average values**                | **0.946**       |                 | **0.774**          | **0.873**        |                                    |