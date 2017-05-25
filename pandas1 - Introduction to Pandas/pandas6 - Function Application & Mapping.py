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