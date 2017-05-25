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
