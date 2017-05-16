# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:12:02 2017

@author: azkei
The Series constitutes the data structure designed to accomodate a sequence of
one-dimensional data, while the Data Frame, a more complex data structure,
is designed to contain cases of multi-dimensions
"""
#importing pandas & numpy
import pandas as pd
import numpy as np

# The Series Data Structure is a simple structure containing 2 arrays
# one main array containing values and paired with an array of indexes

# 1. Declaring a Series
s = pd.Series([12,-4,7,9])
s
# If you do not specify the index, pandas will automatically assign numerical values

# Specifying our own index
s = pd.Series([12,-4,7,9], index =['a','b','c','d'])
s

# Individually calling the two arrays that make up the Series
s.values
s.index

# 2. Selecting the Internal Elements
# For concerning individual elements on the Series
s[2]

# or labels/index
s['a']

# Selecting multiple items
s[0:2]

# Selecting a list of labels/index
s[['b','c']]

# 3. Assigning Values to the Elements
# numerical index
s[1] = 0
s
# label
s['b'] = 0

# 4. Defining Series from NumPy Arrays and Other Series
# You can define new Series starting with NumPy arrays or existing Series
arr = np.array([1,2,3,4])
s3 = pd.Series(arr)

s4 = pd.Series(s)
s4

# Keep in mind that the values contained within the NumPy array or original series
# are not copied but are passed as a reference
s3
arr[2] = -2
s3

# 5. Filtering Values
# Return values greater than 8 in the Series.
s[s > 8]

# 6. Operations and Mathematical Functions
s / 2

# Regarding NumPy mathematical functions you can pass down the series
np.log(s)

# 7. Evaluating 
# Often there may be duplicate values in a Series and you may have to gather information
# on the samples contained

# Declaring a series with duplicates
serd = pd.Series([1,0,2,1,2,3],
                 index = ['white','white','blue',
                          'green','green','yellow'])
serd

# To know all the values contained without the duplicates
serd.unique()

# Return unique values and its occurences
serd.value_counts()

# isin() function checks if values exist within the Series or Data Frame
# Checking if 0,3 exists in serd
serd.isin([0,3])

# Returns back the corresponding values and index
serd[serd.isin([0,3])]

# 8. NaN Values
s2 = pd.Series([5,-3,np.NaN,14])
s2

# The isnull() and notnull() functions are very useful to identify the indexes
# without a value
s2.isnull()
s2.notnull()

# These two functions are useful to be placed inside a filtering to make a condition
# Returns not null values
s2[s2.notnull()]
# Returns null value
s2[s2.isnull()]

# 9. Series as Dictionaries
# Another good way to think about Series is an object dictionary
# You can create a series from a dict previously defined.

# Define a dict
mydict = {'red': 2000, 'blue' : 1000, ' yellow' : 500, 'orange' : 1000}
mydict
# Assign dict into Series
myseries2 = pd.Series(mydict)
myseries2

# You can also define the indexes separately
# In the case of mismatch, pandas will assign a NaN automatically
colors = ['red','yellow','orange','blue','green']
myseries = pd.Series(mydict, index = colors)

# 10. Operations between Series
# Series can align daa differently between them by identifying
# their corresponding label
# In this example you sum two Series having only some elements in common with label
mydict2 = {'red':400, 'blue':100,'yellow':1000,'black':700}
myseries2 = pd.Series(mydict2)
myseries + myseries2

# We get a new object Series in which only the items with the same label are added.
# All other label present in one of the two series are still added to the result
# but have a NaN value