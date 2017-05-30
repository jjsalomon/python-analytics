# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:20:06 2017

@author: azkei
In addition to assembling the data to unify the values collected from different sources,
Another fairly common operation is Pivoting.
Arranging values by row or by column is not always suited to your goals.
Sometimes you would like to rearrange the data carrying column values
on rows or vice versa.
"""
# 1. Pivoting with Hierarchical Indexing.
# We have already seen that a DataFrame can support hierarchical indexing.
# This feature can be exploited to rearrange the data in a DataFrame.
# In the context of 2 operations
#   1. Stacking
#   2. Unstacking
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
frame1
# Using the stack() function, we will get the pivoting of a column in rows
# thus producing a series
ser5 = frame1.stack()
ser5
# Vice versa - Hierarchical Series to a DataFrame using unstack() function
ser5.unstack()
# We can also unstack on a different level,
#specifying the number of levels sor its name as an argument of the function
ser5.unstack(1)

# 2. Pivoting from "Long" to "Wide" Format
longframe = pd.DataFrame({'color':['white','white','white',
                                   'red','red','red',
                                   'black','black','black'],
                            'item':['ball','pen','mug',
                                    'ball','pen','mug',
                                    'ball','pen','mug'],
                            'value':np.random.rand(9)})
longframe
# Changing this longframe into a wide frame
wideframe = longframe.pivot('color','item')
wideframe
# As we can see the data is more compact and the data contained in it is more readable

# 3. Removing
# The last stage of Data Preparation is the removal of columns and rows.
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
frame1
# To remove a column, use del command
del frame1['ball']
frame1
# To remove an unwanted row, use the drop() function with the label of the index
# as the argument
frame1.drop('white')
frame1