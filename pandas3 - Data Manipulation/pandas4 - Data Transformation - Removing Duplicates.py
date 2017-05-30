# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:44:32 2017

@author: azkei
This is the second stage of Data Manipulation: Data Transformation
"""
# 1. Removing Duplicates
# DataFrame with duplicate values
dframe = pd.DataFrame({'color':['white','white','red','red','white'],
                       'value':[2,1,3,3,2]})
dframe
# Returns a Series of True or False
dframe.duplicated()
# If we want to return a the duplicate rows
dframe[dframe.duplicated()]
# Generally, all duplcated rows are to be deleted from the DataFrame,
# Pandas provides drop_duplicates() function, which returns the DataFrame
# without duplicate rows
dframe.drop_duplicates()
