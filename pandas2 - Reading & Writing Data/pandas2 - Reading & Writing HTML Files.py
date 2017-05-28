# -*- coding: utf-8 -*-
"""
Created on Fri May 26 17:52:10 2017

@author: azkei
Pandas provides the corresponding pair of I/O API functions for HTML.

read_html()
to_html()

"""
# 1. Writing Data in HTML
# Generate Data
frame = pd.DataFrame(np.arange(4).reshape(2,2))
# Using to_html()
print(frame.to_html())
# The Data Structure was formed to HTML table according to the DataFrame

frame = pd.DataFrame(np.random.random((4,4)),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
frame
# Writing a html page through generation of a string.
# First we create a string that contains the code of the HTML page.
s=['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html=''.join(s)
# Once all the listings contained within the HTML varliabl,
# You can write directly to the file
html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()

# 2. Reading Data from an HTML File.
# The read_html() function returns a list of DataFrame even if there is only
# one table.
# If there is more than one table in the html, just change the index.
web_frames = pd.read_html('myFrame.html')
web_frames[0]
# Reading a table from a URL link.
ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanissmo-complesso-sit-2/classifica-punteggio/')
ranking[0]