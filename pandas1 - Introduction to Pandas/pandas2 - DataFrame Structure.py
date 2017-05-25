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

# Generating numbers into DataFrames, assigning the index and columns
frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                                index = ['red','blue','yellow','white'],
                                columns = ['ball','pen','pencil','paper'])
frame3

# 2. Selecting Elements
# If we want to know the names of the columns
frame.columns

# If we want to get the indexes
frame.index

# Regarding the values contained within the data structure,
# we can get the entire set of data using the values attribute
frame.values

# If we want to select the values in the column
frame['price']

# As you can see, the return value is a Series object.
# Another way is to use the column name as an attribute of the instance of the
# DataFrame
frame.price

# If we want to extract the rows of the dataframe, 
# pass in the index in ix() function
frame.ix[2]

# To select multiple rows - specify more index values
frame.ix[[2,4,1,3]]

# Extracting a portion from a DataFrame
frame[0:1]
frame[1:3]

# Achieving a single value in a DataFrame - use name of column and index of row
frame['object'][3]

# 3. Assigning Values
# Giving the index a name
# Giving the columns names an index name
frame.index.name = 'id'; frame.columns.name = 'item'
frame

# Adding new column in the DataFrame
frame['new'] = 12
frame

# Updating the new column contents
frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]
frame

# Adding a Series of random numbers as a column into a DataFrame
# Generating Series
ser = pd.Series(np.arange(5))
ser
# Adding the Series into the frame column
frame['new'] = ser
frame

# Changing single value, select item and assign new value
frame['price'][2] = 3.3

# 4. Membership of a Value
# Check if these values are in the DataFrame
# True/False
frame.isin([1.5,'pen'])
# Nan
frame[frame.isin([1.0,'pen'])]

# 5. Deleting a Column
del frame['new']
frame

# 5. Filtering
# Return values less than 12
frame[frame < 12]

# 6. DataFrame from Nested Dict
nestdict = {'red':{ 2012: 22, 2013: 33},
            'white':{2011: 13, 2012: 22, 2013:16},
            'blue':{2011:17, 2012:27, 2013:18}}