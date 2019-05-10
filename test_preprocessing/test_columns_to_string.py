import pandas as pd 
import numpy as np 
import sys
sys.path.append('')
from preprocessing import columns_to_string

"""no columns_to_string passed"""
print(
"""
===========================
no columns_to_string passed
===========================
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df)
print('\ndtypes after conversion \n', df.dtypes)


"""one columns_to_string passed"""
print(
"""
============================
one columns_to_string passed
============================
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df, 'a')
print('\ndtypes after conversion \n', df.dtypes)


"""multiple columns_to_string passed"""
print(
"""
=================================
multiple columns_to_string passed
=================================
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df, ['a','b'])
print('\ndtypes after conversion \n', df.dtypes)


"""unknown columns_to_string passed"""
print(
"""
================================
unknown columns_to_string passed
================================
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df, 'd')
print('\ndtypes after conversion \n', df.dtypes)


"""multiple + unknown columns_to_string passed"""
print(
"""
===========================================
multiple + unknown columns_to_string passed
===========================================
"""
)
df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df, ['a','b','d','e'])
print('\ndtypes after conversion \n', df.dtypes)


"""string columns_to_string passed"""
print(
"""
===============================
string columns_to_string passed
===============================
"""
)
df = pd.DataFrame({'a':['a','b','c'],'b':[1,2,3], 'c':[1,2,3]})
print('\ndtypes before conversion \n', df.dtypes)
df = columns_to_string.columns_to_string(df, 'a')
print('\ndtypes after conversion \n', df.dtypes)