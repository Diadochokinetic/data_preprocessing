# data_preprocessing

This repository contains some useful modules to preprocess data for machine learning. There is a test file for each module to verify its functions.

## table of contents

1. [columns_to_string](https://github.com/Diadochokinetic/data_preprocessing/blob/master/preprocessing/columns_to_string.py)

Machine learning often requires categorical data to be encoded into binary variables. Sometimes categorical data is represented by numeric values. Most encoders ignore numeric columns. This module converts numeric columns, storing categorical data, into dtype "string".

2. [outlier_imputer](https://github.com/Diadochokinetic/data_preprocessing/blob/master/preprocessing/outlier_imputer.py)

Machine learning often requires numeric data to be free of missing values. To avoid dropping all rows with at least one numeric value missing, those values get imputed by an outlier. 
