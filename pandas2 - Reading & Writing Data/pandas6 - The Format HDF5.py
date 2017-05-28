# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:49:41 2017

@author: azkei
HDF stands for Heirarchical Data Format.
We will be using HDFStore library, PyTables to store pandas objects.
"""
# Import HDFStore
from pandas.io.pytables import HDFStore
# Generate DataFrame
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
store = HDFStore('mydata.h5')
# Store First Frame
store['obj1']=frame
# Store Second Frame
store['obj2']=frame2
# See a description of the data stored in the HDF file
store
# See DataFrame inside the HDF
store['obj1']