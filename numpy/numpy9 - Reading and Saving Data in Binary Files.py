# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:36:29 2017

@author: azkei
Reading and Writing Array Data to Files
"""
# 1. Loading and Saving Data in Binary Files
# Regarding saving and the nlater retrieving the data stored in binary format
# NumPy provides a pair of functions called save() and load()

# Generate Data
data = np.random.random((4,3))

# Save Data
np.save('saved_data',data)

# When you need to recover the data stored in the .npy file
loaded_data = np.load('saved_data.npy')
loaded_data

# 2. Reading File with Tabular Data
data = np.genfromtxt('data.csv',delimiter = ',',names = True)

# As a result, we get a structure array which the column headings have 
# become the names of the field

# The function performs two loops:
#   1. Reads a line at a time
#   2. Seperates and converts the values contained in it,
#       inserting the consecutive elements created specifically.

# One positive aspect of this feature is that if the file contains missing data
# the function knows how to handle it
data2 = np.genfromtxt('data2.csv',delimiter=',',names = True)
data2

# We can see that the function replaces the blanks with nan values

# We can use the headers to extract the column values
data2['id']

# We can use numerical indexes to extract row values
data[0]