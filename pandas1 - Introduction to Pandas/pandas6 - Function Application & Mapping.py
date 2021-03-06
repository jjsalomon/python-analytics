# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:28:59 2017

@author: azkei
This section covers pandas library functions.
Pandas library is built on the foundations of NumPy, these extends many of its
features adapting them to new data structures such as Series and DataFrames
"""
# 1. Functions by Element
# Universal Functions - ufunc
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index = ['red','blue','yellow','white'],
                     columns =['ball','pen','pencil','paper'])
frame
# Calculating the square root of each value
np.sqrt(frame)

# 2. Functions by Row or Column
# Define a lambda that calculates the range covered by the elements
f = lambda x: x.max() - x.min()
# OR
def f(x):
    return x.max() - x.min()
# Using apply() - you can aply the function defined on the DataFrame
frame.apply(f)
# The result is only one value column
# Apply by row instead
frame.apply(f,axis = 1)

# More useful case - extending the application to many functions
def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])

frame.apply(f)

# 2. Statistic Functions
# Summing values in columns
frame.sum()
# Mean of values in columns
frame.mean()
# Summary Statistic of Data
frame.describe()