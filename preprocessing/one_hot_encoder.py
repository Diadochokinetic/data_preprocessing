import pandas as pd 
import numpy as np
from sklearn.base import TransformerMixin

class one_hot_encoder(TransformerMixin):

    """
    This module performs binary encoding on columns containing categorical data.
    It assumes that all non numeric columns contain categorical data.
    This module works well with the module columns_to_string.py in a pipeline.

    Input:
        pandas DataFrame containing columns with categorical data

    Output:
        pandas DataFrame with coloumns containing binary encoded categorical data

    """

    def __init__(self, number_of_top_values = 10, special_columns = {}):

        """
        Parameters:

            number_of_top_values (int, default = 10):
                in order to reduce dimensionality, only the most common values of a column get encoded
                all other values will be encoded in a 'rest' column
                columns in 'special_columns' are not affected by this

            special_columns (dict, default = {})
                sometimes reducing dimensionality by encoding only the most common values creates an information loss
                such columns can be passed in a dictionary with the number of values to be encoded manually
        """

        self.number_of_top_values = number_of_top_values
        self.top_values = {}
        self.special_columns = special_columns
        self.columns_to_encode = []
        self.columns_to_keep = []


    def fit(self, df):

        numerics = [np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]

        """identify numeric and non numeric columns"""
        for column in df.columns:
            if df[column].dtype not in numerics:
                self.columns_to_encode.append(column)
            else:
                self.columns_to_keep.append(column)

        """
        create a dicitionary with all columns_to_encode as key and all values to be binary encoded
        different handling of columns in the special_columns dicitionary
        """
        for column in self.columns_to_encode:
            if column in self.special_columns:
                self.top_values[column] = df[column].value_counts().sort_values(ascending=False).index[0:self.special_columns[column]]
            else:
                self.top_values[column] = df[column].value_counts().sort_values(ascending=False).index[0:self.number_of_top_values]


    def transform(self, df):

        """create DataFrame with all numeric columns and initialize empty DataFrame for binary encoded data"""
        df_numeric = df[self.columns_to_keep]
        df_non_numeric = pd.DataFrame({})

        """fill the empty DataFrame with binary encoded data"""
        for column in self.columns_to_encode:
            for value in self.top_values[column]:
                df_non_numeric[column+'_OH_'+value] = df[column].apply(lambda x: 1 if x == value else 0)

            df_non_numeric[column+'_OHE_REST'] = df[column].apply(lambda x: 1 if x not in self.top_values[column] else 0)

        """merge numeric and non numeric DataFrame"""
        df = df_numeric.merge(df_non_numeric, how='inner', left_index=True, right_index=True)

        return df


    def fit_transform(self, df):

        """execute fit & transform"""

        self.fit(df)
        df = self.transform(df)

        return df

        
