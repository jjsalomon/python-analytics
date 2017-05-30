# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:20:39 2017

@author: azkei
Discretization is transforming data into Discrete Categories
e.g. Divide the range of values into smaller categories and count the number
of occurences in that category
"""
# Discretization
results = [12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87]
results
# Lets say the results have a range of 0 - 100,
# We can uniformly divide these into 4 equal parts i.e. bins
# 0-25, 26-50, 5-75, 76-100
bins = [0,25,50,75,100]
bins
# There is a special function called cut() and apply it to the array of results
# passing the bins also
cat = pd.cut(results,bins)
cat
# The object returned by the cut() function is a special object of Categorical Type
# We can consider it as an array of Strings indicating the name of the bin
# Internally it contains a levels array indicating the names of the different
# internal categories and a labels array that contains a list of numbers
# equal to the elements of the results(i.e, the array subject to binning).
# The number corresponds to the bin to which the corresponding element of results
# is assigned.
# levels deprecated - use categories instead
cat.categories
# labels deprecated - use codes instead
cat.codes
# Finally to know the occurences for each bin, i.e. the number of occurences
# in each category, use value_counts() function
pd.value_counts(cat)
# We can give names to various bins by calling them in an array of strings
# Then assigning them to label options inside the cut() function we have used
# to create the Categorical object
bin_names =['unlikely','less likely','likely','highly likely']
cat2 = pd.cut(results,bins,labels=bin_names)
pd.value_counts(cat2)
# If the cut() function is passed as an argument to an integer instead of
# explicating the bin edges, this will divide the range of values of the array
# in many intervals as specified by the number
# The limits of the inveral will be taken by the minimum and maximum of the sample data
pd.cut(results,5)
# In addition to cut(), pandas provides another method for binning: qcut().
# This function divides the sample into quintiles.
# Depending on the distribution of the data sample, using cut() rightly
# you will have a different number of occurences for each bin.
# Instead qcut() will ensure that the number of occurences for each bin is equal
# but the edges of the bin to vary
quintiles = pd.qcut(results,5)
quintiles
pd.value_counts(quintiles)