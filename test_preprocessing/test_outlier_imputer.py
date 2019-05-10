import pandas as pd
import sys
sys.path.append('')
from preprocessing import outlier_imputer

"""no NaN values"""
print(
"""
=============
no NaN values
=============
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':['a','b','c']})
print('\nbefore imputing \n',df)
oi = outlier_imputer.outlier_imputer()
oi.fit(df)
print('\nafter imputing \n',oi.transform(df))


"""NaN values in numeric column"""
print(
"""
============================
NaN values in numeric column
============================
"""
)
df = pd.DataFrame({'a':[1,2,float('nan')],'b':[1,2,3], 'c':['a','b','c']})
print('\nbefore imputing \n',df)
oi = outlier_imputer.outlier_imputer()
oi.fit(df)
print('\nafter imputing \n',oi.transform(df))


"""NaN values in numeric and string column"""
print(
"""
=======================================
NaN values in numeric and string column
=======================================
"""
)
df = pd.DataFrame({'a':[1,2,float('nan')],'b':[1,2,3], 'c':['a','b',float('nan')]})
print('\nbefore imputing \n',df)
oi = outlier_imputer.outlier_imputer()
oi.fit(df)
print('\nafter imputing \n',oi.transform(df))

