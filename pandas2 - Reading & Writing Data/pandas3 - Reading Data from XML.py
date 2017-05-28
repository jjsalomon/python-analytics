# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:51:28 2017

@author: azkei
Using lxml library to read XML data
"""

# We want to take the data structure inside the XML file and convert it into
# a DataFrame.
# For that, we need objectify.
from lxml import objectify
# Now we can do the parser of the XML file using parse()
xml = objectify.parse('books.xml')
xml
# Define a root structure
root = xml.getroot()
# Access different nodes in the root structure
root.Book.Author
# Access various elements corresponding to a node
root.Book.getchildren()
# Get the various tags in the structure
[child.tag for child in root.Book.getchildren()]
# Get the corresponding value
[child.text for child in root.Book.getchildren()]
# Converting the Tree Structure into a DataFrame
def etree2df(root):
    column_names=[]
    for i in range(0,len(root.getchildren()[0].getchildren())):
        column_names.append(root.getchildren()[0].getchildren()[i].tag)
    xmlframe = pd.DataFrame(columns=column_names)
    for j in range(0,len(root.getchildren())):
        obj = root.getchildren()[j].getchildren()
        texts = []
        for k in range(0,len(column_names)):
            texts.append(obj[k].text)
        row = dict(zip(column_names,texts))
        row_s = pd.Series(row)
        row_s.name = j
        xmlframe = xmlframe.append(row_s)
    return xmlframe
# Running the function
etree2df(root)