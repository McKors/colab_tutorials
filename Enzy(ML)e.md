# Enzy(ML)e - machine learning prediction regarding enzymatic degradation of polymers

In this project, we use machine learning models for the prediction of mechanical polymer properties dependent on the degree of enzymatic degradation. We provide the time of degradation and the respective degree of degradation together with some degradation-relevant polymer properties like molecular weight, crystallinity, Tg, mechanical properties (tensile strength, strain at break, E modulus etc.) as an input. The output of the models is the respective mechanical property of the polymer at a certain degree of degradation.


## Objective
Predict mechanical properties (e.g. E modulus, tensile strength etc.) of polymers based on their degree of degradation.


## Data

The data has to be synthetically generated.


### Format

| time of incubation | degree of degradation | molecular weight | yield strength | fingerprint |
| ------------------ | --------------------- | -----------------|----------------| [0,1,0,0,1] |
| 4 h                | 2 %                   | 50.000           | 3              | [1,0,0,0,1] |
| 8 h                | 5 %                   | 45.000           | 3.5            | [1,1,0,0,1] |
| 16 h               | 10 %                  | 40.000           | 4.0            | [1,1,0,0,0] |

## Rough plan

1. Curate and clean data 
2. Use clustering for outlier detection
3. Fingerprint
4. Normalize fingerprints
5. Data splitting into train and test set
5. Train ML model
6. Deploy 