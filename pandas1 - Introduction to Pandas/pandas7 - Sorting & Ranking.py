# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:55:32 2017

@author: azkei
Sorting and Ranking indexes
"""
# 1. Sorting items in a Series
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
ser
# Sorting row indexes based alphabetical order in ascending order
ser.sort_index()
# Sorting descending order
ser.sort_index(ascending=False)

# Sorting based on rows and column labels
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index = ['red','blue','yellow','white'],
                     columns = ['ball','pen','pencil','paper'])
frame
# Row Sort
frame.sort_index()
# Column Sort
frame.sort_index(axis = 1)

# Sorting values in the Series
ser.order()

# Specify the name of the column which to sort
frame.sort_index(by='pen')

# If the criteria of sorting will be based on two or more columns
# You can assign an array containing the names of the columns to the by option
frame.sort_index(by=['pen','pencil'])

# Ranking - consists of assigning a rank(value 0 - ascending) to each elemnt of the series.
ser.rank()
# In this case the lowest value got the lowest rank and the highest value got the highest
# The rank can be assigned in the order in which the data is already okaced
ser.rank(method = 'first')

# Reverse the criterion - the largest value is the lowest rank, vice versa
ser.rank(ascending = False)