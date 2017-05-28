# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:28:06 2017

@author: azkei
This script uses the data.xlxs file.
The data contains 2 sheets of data.
We will be using the to_excel() and read_excel() functions
"""
# Read in sheet1 in the file
pd.read_excel('data.xlsx')
# Read in sheet2
pd.read_excel('data.xlsx','Sheet2')

# Writing a DataFrame into Excel
# Generate the frame first
frame = pd.DataFrame(np.random.random((4,4)),
                     index=['exp1','exp2','exp3','exp4'],
                     columns=['Jan2015','Feb2015','Mar2015','Apr2015'])
frame
# Write it to an excel sheet.
frame.to_excel('data2.xlsx')