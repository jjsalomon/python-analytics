# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:48:11 2017

This script is for learning about numpy library for Data Science Projects

@author: azkei
"""
# importing NumPy module withing Python session
import numpy as np

# Using ndarray - the heart of the library

a = np.array([1,2,3])

# Checking the newly created object thats an ndarray
type(a)

# Checking the associated data type of the ndarray
a.dtype
# Checking the axis of the ndarray
a.ndim
# Checking the array length
a.size
# Checking the shape attribute of the array
a.shape


# More Examples
b = np.array([0.234,0.1234,0.1234])

c = np.array([[0.2, 0.4, 0.3],[0.2,0.5,0.1]])

d = np.array([[3.212,5.123512,32.12351, 22.3244522,2.2345,233331,233],
              [988.2331,3231.34422334,22334.2221,233.21123],
              [23.3333,2124.2333,2123321.23333,22.2]])

# defines the size of each bytes of item in the array
d.itemsize
# Buffer containing the aactual elements of the array.
d.data

# Numpy arrays can contain a wide variety of data types
# e.g. String

stringArray = np.array([['a','b'],['c','d']],dtype = '|S1')
stringArray.dtype
stringArray.dtype.name

# The Array function does not just accept a single argument.
# You can use the dtype option to define an array with  complex values

f = np.array([[1,2,3],[4,5,6]],dtype = complex)

# Intrinsic creation of an Array
# The NumPy library provides a set of functions that generate the ndarrays with an initial content
# with values depending on the function

# Generate a 3x3 ndarry with 0 values
np.zeros((3,3))

# Generate a 3x3 ndarray with 1 values
np.ones((3,3))

# It's also possible to generate a sequence of values with precise intervals
np.arange(0,12,3)

# The third argument can even be a float
np.arange(0,6,0.3)

# So far you've only generated one dimensional arrays
# You can add reshape() to add extra dimensions
np.arange(0,6,0.5).reshape(3,4)

# Another function similar to arange() is linspace()
# This function still takes the first 2 arguments as the range
# However the third argument defines the number of elements we want to split
np.linspace(0,6,5)

# Lastly another way to fill an array with values is with numpy.random
np.random(3)

# Add extra dimensions
np.random.random((3,3))
