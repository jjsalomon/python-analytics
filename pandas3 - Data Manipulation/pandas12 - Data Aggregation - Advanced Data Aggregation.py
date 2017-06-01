# -*- coding: utf-8 -*-
"""
Created on Wed May 31 01:10:01 2017

@author: azkei
In this section we will be introduced to transform() and apply() functions
which will allow us to perform many kinds of group operations, some very complex.

Now suppose we want to bring together in the same DataFrame the following:
    1. The DataFrame of Origin - the one containing the data
    2. That obtained by the calculation of group aggregation e.g. sum
"""
frame = pd.DataFrame({'color':['white','red','green','red','green'],
                      'price1':[5.56,4.20,1.30,0.56,2.75],
                      'price2':[4.75,4.12,1.60,0.75,3.15]
                      })
frame
sums = frame.groupby('color').sum().add_prefix('tot_')
sums
pd.merge(frame,sums,left_on='color',right_index=True)
# Thanks to merge(), we managed to add the results of the aggregation in each line
# of the DataFrame to start.
# There is another way of doing this type of operation using transform().
# This function performs the calculation of aggregation as we have seen before,
# but at the same time shows the values calculated based on the key value
# on each line of the DataFrame to start
frame.groupby('color').transform(np.sum).add_prefix('tot_')
# As we can see the transform() method is a more specialized function that has very specific
# requirements: the function passed as an argument must produce a single scalar value
# to be broadcasted.
# The method to cover more general groupby is applical to apply().
# this method applies in its entirety the scheme split-apply-combine.
# In fact, this function divides the object into parts in order to be manipulated
# invokes the passage of function in each piee, then tries to chain together
# the various parts
frame = pd.DataFrame({'color':['white','black','white','white','black','black'],
                      'status':['up','up','down','down','down','up'],
                      'value1':[12.33,14.55,22.34,27.84,23.40,18.33],
                      'value2':[11.23,32.80,29.99,31.18,18.25,22.44]})
frame
frame.groupby(['color','status']).apply(lambda x: x.max())
frame.rename(index=reindex,columns=recolumn)
temp = pd.date_range('1/1/2015',periods=10,freq='H')
temp
timetable = pd.DataFrame({'date':temp,
                          'value1':np.random.rand(10),
                          'value2':np.random.rand(10)
                          })
timetable
timetable['cat'] = ['up','down','left','left','up','up','down','right','right','up']
timetable