# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:57:10 2017

@author: azkei
The last stage is Data Aggregation.

Introduction:
For Data Aggregation, you generally mean a transofmration that produces a single
integer from an array. In fact you have already made many operations of
Data Aggregation, for example, when we calculated the sum(), mean() and count().
These functions operate on a set of Data and perform a calculation with a
consistent result consisting of a single value.
However a more formal manner and the one with more control in data aggregation is that
which involves the categorization of a set.

The categorization of a set data carried out for grouping is often a critical stage.
In the process of data analysis, it is a process of transformation after the 
division into diferent groups, you apply a function that converts or transforms the data
in some way depending on the group they belong to.
Very often the two phases of grouping and apaplication of a function are performed
in a single step.

Also for this part of the data analysis, pandas provides a tool very flexible
and high performance: GroupBy

Generally it refers to its internal mechanism as a process called
Split-Apply-Combine with three operations
    1. Splitting: Division into groups of data sets
    2. Applying: Application of a function on each group
    3. Combining: Combination of all the results obtained by different groups
"""
# 1. A practical example
# First generate data
frame = pd.DataFrame({'color':['white','red','green','red','green'],
                      'object':['pen','pencil','pencil','ashtray','pen'],
                      'price1':[5.56,4.20,1.30,0.56,2.75],
                      'price2':[4.75,4.12,1.60,0.75,3.15]})
frame
# Suppose we want to calculate the average price1 column using group labels
# listed in the column color.
group = frame['price1'].groupby(frame['color'])
# The result is a GroupBy object - the operation was not calculation, it was just
# to collect all the information needed to calculate to be executed.
# This process is called grouping - which all rows having the same value of color
# are grouped into a single item.
# To analyze this more..
group.groups
# Each group is specified into where it starts and ends on the rows
# Now its sufficient to apply the operation on the group to obtain results
# for each group
# Mean
group.mean()
# Sum
group.sum()

# 2. Hierarchical Grouping
# We have seen how to group the data according to the values of a column
# as a key choice. The same thing can be extended to multiple columns
# i.e. make a grouping of multiple keys hierarchical 
ggroup = frame['price1'].groupby([frame['color'],frame['object']])
ggroup
ggroup.sum()

# So far we have applied the grouping to a single column of data, but in reality
# it can be extended to multiple columns or the entire DataFrame.
# We do not need to reuse the object GroupBy serveral times,
# it is convenient to combine in a single passing all of the grouping and calculation
# to be done, without any intermediate variable
frame[['price1','price2']].groupby(frame['color']).mean()
frame.groupby(frame['color']).mean()