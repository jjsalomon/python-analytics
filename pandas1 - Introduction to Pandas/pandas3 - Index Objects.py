# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:57:51 2017

@author: azkei
The index objects are responsible for the labels on the axes and other metadata
as the name of the axes.
We have already seen as an array containing abels is converted into an Index object
We need to specify index option within the constructor
"""
# 1. Index Objects
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
ser.index

# 2. Methods on Index
# Return the index with the lowest value
ser.idxmin()
# Return the index with the Largest value
ser.idxmax()

# 3. Index with Duplicate Labels
serd = pd.Series(range(6), index = ['white','white','blue','green','green','yellow'])
serd
# Return back values with index 'white'
serd['white']

# 4. Identifying unique/duplicate indexes
# Valuable for Big Data
# Series
serd.index.is_unique
# DataFrame
frame.index.is_unique