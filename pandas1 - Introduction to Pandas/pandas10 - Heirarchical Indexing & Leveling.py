# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:29:42 2017

@author: azkei
Heirarchical indexing is very important feature in pandas, as it allows you
to have multiple levels of indexes on a single axis.
Somehow it gives you a way to work with data in multiple dimensions continuing to work
in two-dimensional structure.
"""
# 1.Heirarchical indexing & Leveling
# Generate a series with two arrays of indexes
mser = pd.Series(np.random.rand(8),
                 index =[['white','white','white','blue','blue','red','red','red'],
                         ['up','down','right','up','down','up','down','left']])
mser
mser.index
# You can select values for a given value of the first index.
mser['white']
# Or you can select values for a given value of the second index.
mser[:,'up']

# If you want to specify a single value, you specify both indexes
mser['white','up']

# The heirarchical index plays a key role in reshaping data and group based operations
# such as pivot-tables, the data can be converted into a dataframe format using
# unstack() - this function converts Series with heirarchical data into a
# simple DataFrame.
mser.unstack()

# To do reverse operation i.e. convert a DataFrame into a Series.
# Use a stack() function
frame.stack()

# As regards the DataFrame, it is possible to define a hierarchical index both
# for the rows and for the columns.
# At the time of the declaration of the DataFrame, #
# you have to define an array of arrays for both the index option and column option
mframe = pd.DataFrame(np.random.rand(16).reshape(4,4),
                      index=[['white','white','red','red'],
                             ['up','down','up','down']],
                             columns=[['pen','pen','paper','paper'],
                                      [1,2,1,2]])
mframe

# 2. Reordering & Sorting Levels
# Occasionally, you could need to rearrange the order of the levels on an axis
# or do sorting for values at a specific level.
# The swaplevel() accepts as a argument the names assigned to the two levels
# you want to interchange, and returns a new object with the two levels
# interchanged between them. Leaving the data unmodified.

# Column Labels
mframe.columns.names=['objects','id']
# Row Labels
mframe.index.names=['colors','status']
mframe

# Interchange rows
mframe.swaplevel('colors','status')

# sortlevel() - orders the data considering only those of a certain level
mframe.sortlevel('colors')

# 3. Summary Statistic by Level
# Make a Summary Statistic at Row level.
mframe.sum(level='colors')
# Make a Summary statistic for a given level of column, e.g. id
# You will need to specify the axis which it lies on
mframe.sum(level='id',axis=1)