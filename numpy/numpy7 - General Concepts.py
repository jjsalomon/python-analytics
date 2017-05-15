# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:14:36 2017

@author: azkei
This section describes general concepts in NumPy
"""

#1. Copies or Views of Objects
a = np.array([1,2,3,4])
b = a
b

a[2] = 0
b
# As you can see array b has been assigned array a
# array b does not do a copy but only points to array a

c = a[0:2]
c

a[0] = 0
c

# If you want to generate a complete copy and distinct array
# use copy() function
a = np.array([1,2,3,4])
c = a.copy()
c

a[0] = 0
# As you can see, even changing the items in the array a
# array c remains unchanged

# 2. Vectorization - NumPy allows you to to do mathematical operations
# Without using loops.
# This makes operations more readable on a more mathematical expression
a * b


# 3. Broadcasting is the operation that allows an operator or a function
# to act on two or more arrays to operate even if these arrays do not have exactly
# the same shape.
# Simple case
A = np.arange(16).reshape(4,4)
b = np.arange(4)

A + b

# More complex case
m = np.arange(6).reshape(3,1,2)
n = np.arange(6).reshape(3,2,1)