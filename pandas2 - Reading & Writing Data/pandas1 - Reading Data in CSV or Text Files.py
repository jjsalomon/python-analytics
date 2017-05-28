# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:17:03 2017

@author: azkei
Reading Data in CSV or Text Files
"""
# 1. Reading Data in CSV or Text Files
# Since its comma delimeted, you can just use read_csv()
# to read its content and convert it as a DataFrame object
csvframe = pd.read_csv('myCSV_01.csv')
csvframe
# Since CSV files are considered text files,
# You can also use the read_table() function, but specifying the delimeter
pd.read_table('myCSV_01.csv',sep=',')
# Remove headers, use pandas default names to columns
pd.read_csv('myCSV_02.csv',header=None)
# Specify the names directly assigning a list of labels to the names option
pd.read_csv('myCSV_02.csv',
            names =['white','red','blue','green','animal'])
# Assigning index columns in the data for Heirachical Data
pd.read_csv('myCSV_03.csv',
            index_col=['color','status'])

# 2. Using RegExp for Parsing TXT Files
# Parse whitespace characters
pd.read_table('myTXT_01.txt',
              sep='\s*')
# Parse non-digit characters
pd.read_table('myTXT_02.txt',
              sep='\D*',header=None)
# Excluding lines from parsing by using skiprows
pd.read_table('myTXT_03.txt',
           sep=',',
           skiprows=[0,1,3,6])

# 3. Reading TXT Files into Parts or Partially
# Only take 3 rows and skip 2nd index rows
pd.read_csv('myCSV_02.csv',
            skiprows=[2],nrows=3,
            header=None)
# Add values of a column every 3 rows of the file
# Insert these sums into a series
out = pd.Series()
i = 0
pieces = pd.read_csv('myCSV_01.csv',chunksize=3)
for piece in pieces:
    out.set_value(i,piece['white'].sum())
    i=i+1
    
# 4. Writing Data in CSV
# to_csv() function
frame2
frame2.to_csv('outCSV_01.csv')
# By Default, the index and headers are marked on the file

# Removing header and index
frame2.to_csv('outCSV_01.csv',index=False,header=False)

# NaN values show up as empty fields on the file
frame3
frame3.to_csv('outCSV_02.csv')

# We can replace the empty fields with any value like NaN
frame3.to_csv('outCSV_02.csv',na_rep='NaN')