# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:25:36 2017

@author: azkei
We Briefly covered operations between two data structures last file.
We will cover how arithmetic operators apply between two or more structured here
using Flexible Arithmetic Methods such as
add(), sub(),div(),mul()
"""
# 1. Flexible Arithmetic Methods
# Addition
frame1.add(frame2)
# Subtraction
frame1.sub(frame2)
# Division
frame1.div(frame2)
# Multiplication
frame1.mul(frame2)
# As you can see there is NaN's on values that have not be operated on.

# 2. Operations between DataFrame and Series
# Generate a 4x4 DF with range 0-15
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
# Generate Series, values 0-4
ser = pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
ser
# Subtract Series in DataFrame
# The frame will subtract based on the common indexes the two Structures have
frame - ser
# If the index is not present, the result will have elements with NaN
ser['mug'] = 9
frame - ser