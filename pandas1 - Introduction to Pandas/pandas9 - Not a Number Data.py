# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:46:59 2017

@author: azkei
"""

# 1. Assigning a NaN value
# Just in case you need to assign a NaN - np.NaN
ser = pd.Series([0,1,2,np.NaN,9],
                index=['red','blue','yellow','white','green'])
ser

# 2. Filtering Out NaN Values - Series
# Elemination of NaN values, element by element is tedious and risky
# so we use dropna()
ser.dropna()
# Another way is use notnull()
ser[ser.notnull()]

# DataFrame
frame3 = pd.DataFrame([[6,np.NaN,6],
                      [np.NaN,np.NaN,np.NaN],
                      [2,np.NaN,5]],
                        index = ['blue','green','red'],
                        columns = ['ball','mug','pen'])
frame3

# To avoid having entire rows and columns disappear
# We need to specify how to filter it using dropna()
frame3.dropna(how='all')

# 3. Filling in NaN Occurences
# Rather than filter NaN values within Data Structures.
# You run the risk of discarding relevant values
# Replacing them is a better option
# fillna() takes in 1 argument
frame3.fillna(0)
# Or you can replace NaN's with different values depending on the column
# Specifying the indexes and the associated value
frame3.fillna({'ball':1,'mug':0,'pen':99})