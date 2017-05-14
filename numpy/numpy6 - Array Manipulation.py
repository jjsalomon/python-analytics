# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:53:57 2017

@author: azkei
OFten you will need to create an array using already created arrays
You will see how to create new arrays by joining or splitting arrays
"""

# 1. Stacking - Assembling arrays
# Generate 2d arrays
A = np.ones((3,3))
B = np.zeros((3,3))

# Vertical Stacking - Add the 2nd array as rows
np.vstack((A,B))

# Horizontal Stacking - Add the 2nd array as columns
np.hstack((A,B))

# Two other functions performing stacking between multiple arrays are
# column_stack()
# row_stack()
# These functions operate differently, stacking one dimensional arrays
# to two-dimensional arrays
a = np.array([0,1,2])
b = np.array([3,4,5])
c = np.array([6,7,8])

np.column_stack((a,b,c))
np.row_stack((a,b,c))

# 2. Splitting Arrays
# Generate new array
A = np.arange(16).reshape((4,4))

# Horizontal - Splitting the 4x4
[B,C] = np.hsplit(A,2)
B
C

# Vertical - Splitting the 4x4
[B,C] = np.vsplit(A,2)
B
C

# A more complex command is the split() function
# which allows you to split the array into non-symettrical parts
# axis = 1 -> column
[A1,A2,A3] = np.split(A,[1,3],axis=1)
A1
A2
A3

# axis = 0 -> row
[A1,A2,A3] = np.split(A,[1,3],axis=0)

