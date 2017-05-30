# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:13:00 2017
@author: azkei
After the Data is in a DataFrame format we can start Manipulating Data.
The three phases of data manipulation are:
    1. Data Preparation
    2. Data Transformation
    3. Data Aggregation

Data preparation procedures:
    1. Loading
    2. Assembling
        a. Merging
        b. Concatenating
        c. Combining
    3. Reshaping (pivoting)
    4. Removing
"""
# Assembling can be done in different ways:
#   Merging: using pandas.merge() function
#   Concatenating: using the pandas.concat()
#   Combining: using pandas.DataFrame.combine_first()

# 1. Merging - SQL join
import numpy as np
import pandas as pd
frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'price':[12.33,11.44,33.21,13.23,33.62]})
frame1
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'color':['white','red','red','black']})
frame2
# Carry out merge function
pd.merge(frame1,frame2)
# As we can see as a result, the returned DataFrame consists of all the rows that
# have an ID in common between the DataFrame. In addition the common column
# that both have been added.

# Specifying which column to be the base for merging.
frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'color':['white','red','red','black','green'],
                       'brand':['OMG','ABC','ABC','POD','POD']})
frame1
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'brand':['OMG','POD','ABC','POD']})
frame2
# In this case we have 2 DataFrames having columns with the same name.
# So if we merge, we do not get any results
pd.merge(frame1,frame2)
# So it is necessary to explicitly define the criterion of merging using on option
pd.merge(frame1,frame2,on='id')
pd.merge(frame1,frame2,on='brand')
# The results vary considerably depending on the criteria for merging.
# A potential proble can arise where the column names you want to merge
# do not have the same name
# to fix this we use left_on, right_on
frame2 = frame2.rename(columns={'id':'sid'})
frame2
pd.merge(frame1,frame2,left_on='id',right_on='sid')
# By Default the merge() function perorms an inner join.
# The keys in the result are the result in the intersection.
# Using the how option, you can perform, left join, right join and outer joins
frame2 = frame2.rename(columns={'sid':'id'})
# Default inner join
pd.merge(frame1,frame2,on='id')
# Full outer join
pd.merge(frame1,frame2,on='id',how='outer')
# Left join
pd.merge(frame1,frame2,on='id',how='left')
# Right join
pd.merge(frame1,frame2,on='id',how='right')
# To make a merge of multiple keys, just add a list to the on option
pd.merge(frame1,frame2,on=['id','brand'],how='outer')

# 2. Merging on Index - using index as a criterion for merging
# Using right_index, left_index
pd.merge(frame1,frame2,right_index=True, left_index=True)
# DataFrame objects have a join() function when you want to do merging by index

# This wont work as the index names are the same
frame1.join(frame2)
# rename
frame2 = frame2.rename(columns={'id':'id1','brand':'brand2'})
frame1.join(frame2)
# As you can see there are some values corresponding to a frame that have NaN

