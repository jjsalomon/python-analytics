# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:58:26 2017

@author: azkei
The DataFrame is a tabular data structure similar to the spreadsheet.
This data structure is designed to extend the case of the Series to multiple dimensions.
The DataFrame consists of an ordered collection of columns each of which can
contain value of diferent types (numeric,string,boolean,etc) and an index
"""
# 1. Defining a DataFrame
# Here we are defining the column and the values on the column
data = {'color':['blue','green','yellow','red','white'],
        'object':['ball','pen','pencil','paper','mug'],
        'price':['1.2','1.3','1.4','1.5','1.6']}
frame = pd.DataFrame(data)
frame

# If the data contains more data than we are interested, we can make a selection
frame2 = pd.DataFrame(data, columns = ['object','price'])
frame2

# Specifying the index on the DataFrame - or else it will be numerical type
frame2 = pd.DataFrame(data,index=['one','two','three','four','five'])
frame2

# Generating numbers into DataFrames
frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                                index = ['red','blue','yellow','white'],
                                columns = ['ball','pen','pencil','paper'])
frame3

