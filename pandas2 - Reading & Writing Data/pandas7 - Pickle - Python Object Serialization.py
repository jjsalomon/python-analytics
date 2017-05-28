# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:57:12 2017

@author: azkei
The pickle module implements a powerful algorithm for serialization and de-serialiation
of a data structure implemented in Python. Pickling is the rocess in which the
heirarchy of an object is converted into a stream of bytes.
This allows an object to be transmitted, store and then rebuilt by the receiver itself
retaining all the original features.
We're going to be using cPickle module to do this, as it was written in C and heavily
optimized.
"""
# 1. Serialize a Python Object with cPickle
# Import cPickle, now called _pickle
import _pickle as pickle
# Create sufficient data
data = {'color':['white','red'],'value':[5,7]}
# Perform serialization of Data through dumps() function
pickled_data = pickle.dumps(data)
print(pickled_data)
# Once Data has been Serialized, they can be written on a file, or sent over a socket etc. 
# Once it has been transmitted, it is possible to reconstruct the serialized object
# using loads() function
nframe = pickle.loads(pickled_data)
nframe

# 2. Pickling with pandas.
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['up','down','left','right'])
frame.to_pickle('frame.pkl')
# To open the pkl file
pd.read_pickle('frame.pkl')
# NOTE: Make sure that the data doesnt have any malicious data in it, as pickle
# was not designed to be safe.