 # -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:01:58 2017

@author: azkei
Correlation & Co-Variance
Two important statistical calculations are correlation and covariance
Expressed as corr() and cov()
These calculations normally involves two Series
"""
# 1. Series
# Generating two sequences
seq2 = pd.Series([3,4,3,4,5,4,3,2],
                 ['2006','2007','2008','2009','2010','2011','2012','2013'])
seq2

seq = pd.Series([1,2,3,4,4,3,2,1],
                ['2006','2007','2008','2009','2010','2011','2012','2013'])
seq
# Correlation
seq.corr(seq2)
# Covariance
seq.cov(seq2)

# 2. DataFrames
# Applying correlation & covariance to DataFrames
frame2 = pd.DataFrame([[1,4,3,6],
                    [4,5,6,1],
                    [3,3,1,5],
                    [4,1,6,4]],
                    index = ['red','blue','yellow','white'],
                    columns=['ball','pen','pencil','paper'])
# DF Correlation
frame2.corr()
# DF Covariance
frame2.cov()

# Using corrwith(), you can calculate the pairwise correlations
# between the columns or rows of a dataframe with a SEries or another DataFrame
ser = pd.Series([0,1,2,3,9],['red','blue','yellow','white','green'])
ser

frame2.corrwith(ser)
frame2.corrwith(frame)