import pandas as pd

def columns_to_string(df = pd.DataFrame({}), columns_to_string = []):
    
    """
    ==================================================================
    converts specific columns of a pandas DataFrame into string format

    Input:
        Pandas DataFrame 
        list of columns to convert into string

    Output:
        Pandas DataFrame
    ==================================================================
    """

    if not columns_to_string:
        print("\n no columns_to_string passed \n")

    """check which columns_to_string exist in the input DataFrame"""
    columns_to_convert = []
    for x in range(0,len(columns_to_string)):
        if columns_to_string[x] in df.columns:
            columns_to_convert.append(columns_to_string[x])

    """convert columns to string"""
    df[columns_to_convert] = df[columns_to_convert].astype(str)
    print("\n converted columns: {} \n".format(len(columns_to_convert)))

    return df