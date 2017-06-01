# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:47:58 2017

@author: azkei
Description
Examples of Supervised Learning:
    Classification:
        K-Nearest Neoughbors Classifier
        Support Vector Machines
    Regression:
        Linear Regression
        Support Vector Machines
        
Supervised learning consists of learning possible patterns between two or more features
reading values from a training set; the learning is possible because the training
set contains known results(target or labels).
All models in scikit-learn are referred to as supervised estimators, using the fit(x,y)
function that makes their training.
x comprises the features observed, while y indicates the target.
Once the estimator has carried out the training it will be able to predict the value
of y for any new observation x not labeled.
This operation will make it through the predict(x) function
"""
# import dataset
from sklearn import datasets
iris = datasets.load_iris()
# In order to see the values in the dataset
iris.data
# To know what kind of flower belongs to each item
iris.target
# 150 items with 3 possible integer results : 0,1,2
# which correspond to 3 species of iris
iris.target_names

# To better understand this data, we use matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data[:,0] # X-Axis - sepal length
y = iris.data[:,1] # Y-Axis - sepal length
species = iris.target # Species

x_min = x.min() - .5
x_max = x.max() + .5

y_min = y.min() - .5
y_max = y.max() + .5

# Scatterplot
plt.figure()
plt.title('Iris Dataset - Classification by Sepal Sizes')
plt.scatter(x,y, c=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# Blue - Iris Setosa
# Green - Iris Versicolor
# Red - Iris Virginica

# We can see that Iris Setosa differ from the other two
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data[:,2] # X-Axis - petal length
y = iris.data[:,3] # Y-Axis - petal length
species = iris.target # Species

x_min = x.min() - .5
x_max = x.max() + .5

y_min = y.min() - .5
y_max = y.max() + .5

# Scatterplot
plt.figure()
plt.title('Iris Dataset - Classification by Petal Sizes', size = 14)
plt.scatter(x,y, c=species)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# 2. PCA Decomposition - Principal Component Analysis
# This technique allows you to reduce the number of dimensions and then plot the results
# within a 3D Graph
# Scikits allows use to do dimension reduction, using fit_transform which belongs
# to the PCA object which has a constructor of n_components which in this case is 3
from sklearn.decomposition import PCA
x_reduced = PCA(n_components=3).fit_transform(iris.data)

import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
x = iris.data[:,1]  # X - Axis - Petal Length
y = iris.data[:,2]  # Y - Axis - Petal Length
species = iris.target # Species
x_reduces = PCA(n_components = 3).fit_transform(iris.data)

# Scatterplot 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Iris Dataset by PCA', size = 14)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel('First Eigenvector')
ax.set_ylabel('Second Eigenvector')
ax.set_zlabel('Third Eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())

# Division of three species is much more evident


