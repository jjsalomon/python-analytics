# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:05:13 2017

@author: azkei
Arithmetic Operations using NumPy
"""
# Generate an array
a = np.arange(4)
# Sum
a+4
# Multiplication
a*2

b = np.arange(4,8)
# Add 2 arrays together
a+b
# Minus
a-b
# Multiply
a*b

# Multiple array with the sine or square root of the elements
# Sine
a * np.sin(b)
# Square Root
a * np.sqrt(b)

# Moving to a multi-dimensional case
A = np.arange(0,9).reshape(3,3)
B = np.ones((3,3))


