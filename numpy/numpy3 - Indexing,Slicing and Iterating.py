# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:19:03 2017

@author: azkei
This script  will show how to manipulate objects that we have created before
"""
# 1. Indexing - when an array is created an index is automatically created
# Check element on 4th index of array
a = np.arange(10,16)
a[2]

# Numpy accepts negative indexes, -1,-2,-3
# -1 being the largest index
a[-1]

# Selecting multiple indexes
a[[1,2,3]]

newArray = np.arange(10,19).reshape((3,3))
# index of 2nd level 3rd element
newArray[1,2]

# 2. Slicing - the operation of extracting portions of an array to generate a new one
# Generate new array and take first to 5th index
a[1:5]

# Take every end number in the splice
a[1:5:2]

# Others
a[::2]
a[:5:2]
a[:5:]

# Slicing multi-dimensional arrays
A = np.arange(10,19).reshape((3,3))
# Extracting first row
A[0,:]
# Extracting first column
A[:,0]
# Extracting smaller matrix
A[0:2, 0:2]
# Extracting using indexes
A[[0,2],0:2]

# 3. Iterating an Array
# Simple array iteration
for i in a:
    print (i)
    
# Iteration through multi-dimensional array
for row in A:
    print (row)
    
# Iterating element by element in a multi-dimensional array
for item in A.flat:
    print (item)
    
# apply_along_axis() - 3 arguments
# 1. the aggregate function 
# 2. the axis to apply iteration
# 3. the array
# If axis = 0 -> Row
# If axis = 1 -> Col
np.apply_along_axis(np.mean,axis=0, arr = A)
np.apply_along_axis(np.mean,axis=1, arr = A)

# Self defined function
def foo(x):
    return x/2

np.apply_along_axis(foo,axis=1,arr=A)

    
