import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin

class outlier_imputer(TransformerMixin):

    """
    impute missing values of numeric variables for classification problems
    missing values in character variables remain untouched
    """

    def __init__(self):
        self.values_to_fill = {}
        self.columns_to_impute = []


    def fit(self, X):

        """
        Input: pd.DataFrame
        """

        dtypes = [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]
        self.columns_to_impute = X.select_dtypes(include=dtypes).columns

        for column in self.columns_to_impute:
            min_value = X[column].min()
            max_value = X[column].max()
            self.values_to_fill[column] = min_value-0.1*(max_value-min_value)
            #self.values_to_fill.append(min_value-0.1*(max_value-min_value))


    def transform(self, X):

        """
        Input: pd.DataFrame
        Output: pd.DataFrame
        """

        X_t = pd.DataFrame({})
        for column in X.columns:
            X_t[column] = X[column]

        X[self.columns_to_impute]=X[self.columns_to_impute].fillna(value = self.values_to_fill, inplace = False)

        #for v, c in enumerate(self.columns_to_impute):
         #   x_t = X[c].fillna(value = self.values_to_fill[v], inplace = False)
          #  print(v,'\n', X)

        return X