# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:30:10 2017

@author: azkei
"""
# 1. Concatenating
# Array Concatenation
array1 = np.arange(9).reshape((3,3))
array1
array2 = np.arange(9).reshape((3,3))+6
array2
# X-axis concatenate
np.concatenate([array1,array2],axis=1)
# Y-axis concatentate
np.concatenate([array1,array2],axis=0)

# Series Concatenation
ser1 = pd.Series(np.random.rand(4),index=[1,2,3,4])
ser1
ser2 = pd.Series(np.random.rand(4),index=[5,6,7,8])
ser2
pd.concat([ser1,ser2])
# By default, the concat() function works on axis=0
# If you set axis = 1, it will return a DataFrame
pd.concat([ser1,ser2],axis=1)
# As we can see, there is no overlap - we just did an outer join
# this can be changed by setting the join option to 'inner'
pd.concat([ser1,ser2],axis=0,join='inner')
# A problem is that concatenated parts are not identifiable
# this can be fixed by adding keys
pd.concat([ser1,ser2],keys=[1,2])
# Keys will give an heriarchical index
# In the case of combinations between series along the axis = 1,
# The keys becomethe column headers of the DataFrame
pd.concat([ser1,ser2],axis=1,keys=[1,2])

# DataFrame Concatenation
frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3),
                      index=[1,2,3], columns=['A','B','C'])
frame1
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3),
                      index=[4,5,6], columns=['A','B','C'])
frame2
pd.concat([frame1,frame2],axis=1)

# 2. Combining
# Useful for when you want indexes to overlap entirely or partially
ser1 = pd.Series(np.random.rand(5),index=[1,2,3,4,5])
ser1
ser2 = pd.Series(np.random.rand(4),index=[2,4,5,6])
ser2
ser1.combine_first(ser2)
ser2.combine_first(ser1)
