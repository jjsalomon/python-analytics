# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:14:44 2017

@author: azkei
Here we will learn different functionalities on Indexes...
Reindexing, Dropping and Alignment
"""

# 1. Reindexing
# Indexes can be changed
ser = pd.Series([2,5,7,4], index = ['one','two','three','four'])
ser
# reindex() - creates news Series objects with the values of the previous Series
# according to new sequence of labels
ser.reindex(['three','four','five','one'])
# Interpolation of incorrect/missing indexes
ser3 = pd.Series([1,5,6,3], index=[0,3,5,6])
ser3
# filling the missing index with a range of values 0-5
ser3.reindex(range(6),method='ffill')
# If we want the indexes to be back assigned during interpolation we use bfill
ser3.reindex(range(6),method='bfill')

# Reindexing columns - if theres missing columns pandas will fill them with NaN
frame.reindex(range(5),method='ffill',columns=['color','price','new','object'])
# 2. Dropping - Deleting a Row or Column
ser = pd.Series(np.arange(4.), index = ['red','blue','yellow','white'])
ser
# Deleting an item corresponding to the label'yellow'
ser.drop('yellow')
# Drop more items
ser.drop(['yellow','blue','white'])

# Regarding DataFrames
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame
# Delete Rows in DF
frame.drop(['blue','yellow'])
# Delete Columns - specify the indexes of the columns and axis from where to delete
frame.drop(['pen','pencil'],axis = 1)

# 2. Arithmetic and Data Alignment
# Aligning indexes coming from two different sources
s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,1],['white','yellow','black','blue','brown'])
# Adding 2 series together
s1 + s2
# The values that could not be added are NaN's

# Regarding DataFrames
frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index=['blue','green','white','yellow'],
                      columns=['mug','pen','ball'])
# Same principle applied but for rows and columns


