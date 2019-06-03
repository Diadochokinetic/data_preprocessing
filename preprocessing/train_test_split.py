import numpy as np 
import pandas as pd 

def train_test_split(X, y=None, train_test_ratio = 0.8):

    threshold = int(train_test_ratio*X.shape[0])
    X['random_column'] = np.random.uniform(0,1,X.shape[0])
    X.sort_values('random_column', inplace=True)
    X.drop(['random_column'], axis=1, inplace=True)
    x_train = X.iloc[0:threshold,:]
    x_test = X.iloc[threshold:,:]
    y_train = y.loc[x_train.index]
    y_test = y.loc[x_test.index]

    return x_train, x_test, y_train, y_test