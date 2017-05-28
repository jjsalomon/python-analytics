# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:22:47 2017

@author: azkei
pandas.io.sql module providesa unified interface independent of the DB,
called sqlalchemy. This interface simplifies the connection mode, since
regargless of the DB, the commands will always be the same.
For making a connection we use hte create_engine() function
"""
# 1. Introduction
from sqlalchemy import create_engine
# Here is the list of examples for the various types of databases
# PostgreSQL
engine = create_engine('postgresql://jelo:salomon@localhost:2222/mydatabase)
# MySQL
engine = create_engine('mysql+mysqldb://jelo:salomon@localhost:2222/mydatabase)
# Oracle
engine = create_engine('oracle://jelo:salomon@localhost:2222/mydatabase)
# MSSQL
engine = create_engine('mssql+pyodbc://mydsn)
# SQLite
engine = create_engine('sqlite://foo.db)

# 2. Loading and Writing Data with SQLite3
# Create DataFrame
frame = pd.DataFrame(np.arange(20).reshape(4,5),
                     columns=['white','red','blue','black','green'])
frame
# Implement a connection to a SQLite3 database
engine = create_engine('sqlite:///foo.db')
# Convert the frame in a table within the database
frame.to_sql('colors',engine)
# Read in database
pd.read_sql('colors',engine)

# Now lets try the same operation without using the pandas i/o api
import sqlite3
query="""
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

# Now we can enter data through SQL INSERT statements
data=[('white','up',1,3),
      ('black','down',2,8),
      ('green','up',4,4),
      ('red','down',5,5)]
stmt="INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()

# Query the Database we just recorded
cursor = con.execute('SELECT * FROM test')
cursor
rows = cursor.fetchall()
rows

# Get the name of columns
cursor.description
pd.DataFrame(rows,columns=list(zip(*cursor.description))[0])

# 3. Loading and Writing Data with PostgreSQL.
# Checking version
pd.__version__
# ZZZZ- finish this some other time.