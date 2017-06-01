# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:35:03 2017

@author: azkei
Introduction to Matplotlib
"""
# Importing pylab
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()

plt.axis([0,5,0,20])
plt.title('My First Plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()

# matplotlib and NumPy
import math
t = np.arange(0,2.5,0.1)
y1 = np.sin(t)
y2 = np.sin(t+10)
y3 = np.sin(t+20)
# Blue star, Green triangle, Yellow square
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
# Blue broken line, green line, red broken line
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r--')
