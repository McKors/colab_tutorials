# Enzy(ML)e - machine learning prediction regarding enzymatic degradation of polymers

In this project, we use machine learning models for the prediction of the crystallinity xc of a polymer dependent on the time of incubation and enzyme used. We provide the time of incubation, the poylmer and enzyme as an input. The output of the models is the respective crystallinity xc of the polymer at a certain time of incubation and enzyme.


## Objective
Predict crystallinity xc of polymers dependent on the enzyme and time of incubation.


## Data

The data has to be synthetically generated with Python.


### Format

| time of incubation | polymer        | enzyme    | crystallinity  Xc | 
| ------------------ | -------------- | ----------|-------------------| 
| 0 h                | [*]CC([*])C    | PETase    | 40.1              | 
| 8 h                | [*]CC([*])C    | PETase    | 42.0              |
| 16 h               | [*]CC([*])C    | PETase    | 42.4              |

## Rough plan

1. Synthetically generate data set
3. Fingerprinting polymer and enzyme 
4. Normalize fingerprints
5. Data splitting into train and test set
5. Train ML model
6. Deploy 

