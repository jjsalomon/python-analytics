# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:17:25 2017

@author: azkei
Detecting and Filtering Outliers
"""
# Create a DataFrame with 3 columns from 1000 random values
randframe = pd.DataFrame(np.random.rand(1000,3))
randframe
# Check the statistics for each column
randframe.describe()
# For example, we might consider outliers those that have a value greater than
# three times the standard deviation of each column of the DataFrame
# use std() function
randframe.std()
# Now we apply the filtering of all the values of the DataFrame,
# applying the corresponding standard deviation for each column.
# Using the any() function, we can apply the filter on each column
randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]
