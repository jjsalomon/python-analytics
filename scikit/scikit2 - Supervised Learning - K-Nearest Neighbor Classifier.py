# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 01:44:40 2017

@author: azkei
Now we will perform a classification using K-Nearest Neighbors classifier
Given a new measurement of an iris flower, the task of the classifier is to figure
out to which of the three species it belongs to.
The simplest possible classifier is the nearest neighbor..

A very important concept to consider is:
    training set and testing set.
If you have a single dataset, it is important not to use the same data for both
training and testing.
"""
# Proceeding further we need to divide our Iris Dataset.
# It is wise to randomly mix the array elements and then make the division
# as the dataset might have been ordered in some way using numpy random.permutation()
# The first 140 data will be used for training
# The last 10 data will be used for testing
import numpy as np
from sklearn import datasets
np.random.seed(0)
iris = datasets.load_iris()
x = iris.data
y = iris.target
i = np.random.permutation(len(iris.data))

x_train = x[i[:-10]]
y_train = y[i[:-10]]
x_test = x[i[-10:]]
y_test = y[i[-10:]]

# Now we can apply the K-Nearest Neighbor algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
# Now that we have built a model, we can use the test data
knn.predict(x_test)
y_test

# As you can see we have a 10% error
# Now we visualize this using a decision boundary space represented by the 2D
# scatterplot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
x = iris.data[:,:2] # X-Axis - Sepal Length-width
y = iris.target # Y-Axis - Species

x_min = x[:,0].min() - .5
x_max = x[:,0].max() + .5
y_min = x[:,1].min() - .5
y_max = x[:,0].max() + .5

# Mesh

h = .02
xx,yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
knn = KNeighborsClassifier()
knn.fit(x,y)
Z = knn.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

# Plot the training points
plt.scatter(x[:,0],x[:,1],c=y)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())

# We can do the same considering the size of the petals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
x = iris.data[:,2:4]    # X-Axis - Petals Length - Width
y = iris.target         #Y-Axis - Species

x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5
y_min, y_max = x[:,1].min() - .5, x[:,1].max() + .5

# Mesh
cmap_light = ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h = .02
xx, yy = np.meshgrid(np.arange(x_min,x_max,h), np.arange(y_min,y_max,h))
knn = KNeighborsClassifier()
knn.fit(x,y)
Z = knn.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

# Plot Training points
plt.scatter(x[:,0],x[:,1],c=y)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())



