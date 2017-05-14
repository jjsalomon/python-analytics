# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:18:48 2017

@author: azkei

Shape Manipulating arrays 
We've already covered how the reshape() function can convert two-dimensional
arrays into a matrix
"""
# Generate new random numbers
a = np.random.random(12)
# Reshape into a 4x3 matrix
A = a.reshape(3,4)

# The reshape() function returns a new array
# so its useful to create new objects

# However if you want to modify an object's shape,
# You have to assign a tuple containing the new dimensions directly
# to it's shape attribute
a.shape = (3,4)
a

# If you want to convert a two-dimensional array to one
a = a.ravel()
a

# Or directly use the shape attribute of the array itself
a.shape = (12)
a

# Transposition of a matrix
# Inverting the rows with the columns
A.transpose()
A