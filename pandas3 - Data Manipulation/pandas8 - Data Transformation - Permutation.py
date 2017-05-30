# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:55:32 2017

@author: azkei
The operations of permutation(random reordering) of a Series or the rows
of a DataFrame are easy to do using the numpy.random.permutation() function
"""
# For this example, we create a DataFrame containing integers in ascending order
nframe = pd.DataFrame(np.arange(25).reshape(5,5))
nframe
# Create an array of 5 integers, from 0-4 arranged in random order with the 
# permutation() function. This will be the new order in which to set the values
# of a row of DataFrame
new_order = np.random.permutation(5)
new_order
# Apply it to the DataFrame using the take() function
nframe.take(new_order)
# The order of the rows has been changed; i.e. the indices follow the same order
# as new_order
# We can submit even a portion of the entire DataFrame to a permutation.
# It generates an array that has a sequence limited to a certain range
# e.g. in our case 2 to 4
new_order=[3,4,2]
nframe.take(new_order)

# 2. Random Sampling
# We have just seen how to extract a portion of a DataFrame determined 
# by subjecting it to permutation.
# Sometimes, when we have a huge DataFrame, we may need to sample is randomly,
# The quickest way to do this is by using np.random.randint() function
sample = np.random.randint(0,len(nframe),size=3)
sample
nframe.take(sample)
# As we can see from this random sampling, we can get the same sample even more times
