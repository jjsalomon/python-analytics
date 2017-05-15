# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:04:42 2017

@author: azkei
In previous sections we covered monodimensional and two-dimensional arrays
NumPy provides the possibility of creating more complex arrays called Structured arrays
"""
# Structured Arrays that explicitly define the data type
structured = np.array([(1, 'First',0.5, 1+2j),(2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)],dtype=('i2,a6,f4,c8'))

structured

structured = np.array([(1, 'First',0.5, 1+2j),(2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)],dtype=('int16,a6,float32,complex64'))
structured

# Writing the appropriate reference index,
# you can obtain the corresponding row which contains the struct
structured[1]

# The names assigned automatically to each item can be considered as the names
# of the column of the structure.
# You can refer to items on the names/columns
structured['f1']

# These names are assigned automatically with f(which stands for field)
# You can specify the names with something more meaningful
# Only possible at declaration
structured = np.array([(1, 'First',0.5, 1+2j),
                       (2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)], dtype=[('id','i2'),('position','a6'),
                       ('value','f4'),('complex','c8')])

structured

# Or at a later time, redefining the tuples of names assigned to the dtype attribute
#structured.dtype.names('id','order','value','complex')

# Now you can use meaningful names for the various types of fields
structured['id']