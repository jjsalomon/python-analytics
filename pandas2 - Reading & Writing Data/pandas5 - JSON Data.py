# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:37:50 2017

@author: azkei
"""
# Creating a DataFrame and writing it to JSON
# Generate DataFrame
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
# Convert it to a json file
frame.to_json('frame.json')

# Reading in JSON files
pd.read_json('frame.json')
# Generally speaking, JSON wont be in tabular form, like we have here,
# In that case we have to convert the structure dict file into tabular form.
# This process is called normalization.
# Pandas provides a function called json_normalize(), that converts a dict/list
# in a table
# First we will need to import it
from pandas.io.json import json_normalize
import json
file = open('books.json','r')
text = file.read()
text = json.loads(text)

# We might want to see the contents of all the books with books as the key.
json_normalize(text,'books')

# The above function only gives information on an internal level.
# To get more information, we put more keys into the function
json_normalize(text,'books',['writer','nationality'])
# As a result we get a DataFrame from a starting tree structure.