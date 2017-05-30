# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:00:02 2017

@author: azkei
Pandas provides a set of functions for mapping.
Mapping is the creation of a list of matches between two differnet values,
with the ability to bind a value to a particular label or string.

To define a mapping there is no better object than dict objects
map = {
       'label' : 'value1',
       'label2' : 'value2',
       }

The functions we will see perform specific operation but all of them are united
from accepting a dict object with matches as an argument
    1. replace(): replaces values
    2. map(): creates a new columns
    3. rename(): replaces index values
"""
# 1. Replacing Values via Mapping
# We create a DataFrame with a language thats different
# We want to change these values to correct language
frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','rosso','verde','black','yellow'],
                      'price':[5.56,4.20,1.30,0.56,2.75]})
frame
# Create a dict that maps values
newcolors={
        'rosso':'red',
        'verde':'green'
        }
newcolors
# Replace the older with newer
frame.replace(newcolors)

# A common case is to replace NaN values with another value, for example 0
ser = pd.Series([1,3,np.nan,4,6,np.nan,3])
ser
ser.replace(np.nan,0)
ser

# 2. Adding Values via Mapping
frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow']})
frame
# Lets suppose we want to add a column to indicate the price of the item shown
# in the DataFrame, it is assumed we have a list of price available somewhere.
# Define a dict object that contains the list of prices for each type of item
price={
       'ball':5.56,
       'mug':4.20,
       'bottle':1.30,
       'scissors':3.41,
       'pen':1.30,
       'pencil':0.56,
       'ashtray':2.75
       }
price
# The map() function applied to a Series or to a column of a DataFrame
# accepts a function or an object containing a dict with mapping.
# Here we apply the mapping of prices on the column item making sure to add a column
# to the price DataFrame
frame['price'] = frame['item'].map(price)
frame

# 3. Rename the indexes of the Axes
# The axis label can be transformed using mapping.
# To replace the label indexes, pandas provides the rename() function,
# which takes the mapping argument.
frame
# Index map
reindex={
        0:'first',
        1:'second',
        2:'third',
        3:'fourth',
        4:'fifth'
        }
reindex
# Index transformation using mapping
frame.rename(reindex)
# As we can see the indexes are renamed.
# If we want to rename the columns, we use the columns option
recolumn = {
        'item':'object',
        'price':'value'
        }
recolumn
frame.rename(index=reindex, columns=recolumn)
# If we want to replace a single value
frame.rename(index={1:'first'}, columns={'item':'object'})
# The rename() function returns a new DataFrame with changes,
# leaving the old unchanged.
# If we want to changes to take effect, we set inplace = True
frame.rename(columns={'item':'object'}, inplace=True)
frame
