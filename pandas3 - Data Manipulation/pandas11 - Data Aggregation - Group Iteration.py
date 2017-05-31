# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:08:46 2017

@author: azkei
The GroupBy object supports the operation of an interation for generating
a sequence of 2-tuples containign the name of the group together
with the data portion.
"""
for name, group in frame.groupby('color'):
    print (name)
    print (group)
    
# 1. Chain of Transformations
# From these examples we have seen that for each grouping, when subjected to some
# function calculation or other operations in general, regardless of how it was obtained
# and the selection criteria, the result will be a data structure Series or DataFrame
# which then retains the index system and the name of the columns.
result1 = frame['price1'].groupby(frame['color']).mean()
type(result1)
result2 = frame.groupby(frame['color']).mean()
type(result2)
# So it is possible to select a single column at any point in the various phases
# of this process.Here are some examples
frame['price1'].groupby(frame['color']).mean()
(frame.groupby(frame['color']).mean())['price1']
# Adding a prefix to chain of transformations
means = frame.groupby('color').mean().add_prefix('mean_')
means

# 2. Functions on Groups
# Many methods have not been implemented specifically for groupby, they work
# correctly with data structures like Series. We saw how easy it is to get a esries
# through a groupby object, specifying the name of column, then applying the method
# to make the calculation. e.g. Use the calculation of quantiles with quantiles()
group = frame.groupby('color')
group['price1'].quantile(0.6)

# We can also define our own aggregation functions
# Define them separately then pass as an argument to the mark() function.
# e.g. Calculate the range of values of each group.
def range(series):
    return series.max() - series.min()
# Perform an aggregate function on a DataFrame
frame.groupby('color').agg({'price1':range})
frame.groupby('color').agg(range)
frame.groupby('color').agg(['mean','std',range])
group['price1'].agg(['mean','std',range])