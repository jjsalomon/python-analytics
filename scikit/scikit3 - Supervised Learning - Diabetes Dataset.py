# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:55:10 2017

@author: azkei
"""
from sklearn import datasets
diabetes = datasets.load_diabetes()

# The dataset contains physiological data collected on 442 patients
# and as corresponding target an indicator of the diseases progression after a year.
# The physiological data occupy the first 10 columns with values that indicate respectively
#   Age, Sex, Body Mass Index, Blood Pressure, S1,-S6(Blood Serum Measurements)
# These measurements can be obtained by calling the data attribute.
# But going to check the values in the dataset we will find values very different
# from what we would expect.
# e.g. 10 values for the first patient
diabetes.data[0]

# These values have been processed, each of the ten values was mean centered and 
# subsequently scaled by the standard deviation times the number of the samples.
# We can check by
np.sum(diabetes.data[:,0]**2)
# Checking the data more
diabetes.target