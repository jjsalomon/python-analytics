# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:56:33 2017

@author: azkei

Another alternative way of conducting selective extraction of elements
in an array is to use the conditions and boolean operators

"""

# Suppose you want to select all the values in an array 
# whose elements are less than 0.5

A = np.random.random((4,4))

# Extract out features and do boolean check
A < 0.5

# Extract out elements and place into B
B = A[A < 0.5]

