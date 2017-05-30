# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:21:08 2017

@author: azkei
String Manipulation using Python and Regular Expressions
"""
# 1. Built in Methods for MAnipulation of Strings
# split() function allows us to separate parts of a text, taking a reference point
# as a seperator
text = '16 Bolton Avenue, Boston'
text.split(',')
# As we can see the string has a space character at the end.
# To overcome this problem, we have to use split() along with strip() function
# This takes care of trimming whitespaces including new lines
tokens = [s.strip() for s in text.split(',')]
tokens
# The result is an array of Strings.
# If the number of elements is small and always the same, a very interesting
# way of making assignments is this.
address,city =[s.strip() for s in text.split(',')]
address
city
# The most intuitive and simple way is to concatenate the various parts of
# the text with the operator '+'
address + ',' + city
# This can be useful when you have only two or three strings to be concatenated.
# If the parts to be concatenated are much more, a more practical approach
# is to use the join() function assigned to the separator character
strings = ['A+','A','A-','B','BB','BBB','C+']
';'.join(strings)
# Detecting substrings in strings
'Boston' in text
# 2 other functions to serve this purpose: index() & find()
text.index('Boston')
text.find('Boston')
# The difference is the return value when a substring is not found
text.index('Dublin')
text.find('Dublin')
# The count() function provides you a count of occurences in a string
text.count('e')
text.count('Avenue')
# Another operation on strings is the replacement or elimination of a substring.
# In both cases we will use the replace() function.
# Replace
text.replace('Avenue','Street')
# Eliminate
text.replace('1','')

# 2. Regular Expressions
# The regular expressions provide a flexible way to search and match string
# patterns within a text. A single expression, generically called regex,
# is a string formed according to the regular expression language.
# There is a built in module called re, which is responsible for operation of regex
import re
# The re module provides a set of functions that can be divided into 3 categories
#   1. Pattern Matching
#   2. Substitution
#   3. Splitting
# E.g. The regex for expressing a sequence of one or more whitespace characters
# is \s+
text = "This is   an\t odd  \n text!"
re.split('\s+',text)
# Mechanism of re module - when re,split() is called
# The regular expression is first compiled with re.compile() function
# Then a split() function is called
regex = re.compile('\s+')
regex.split(text)
# With regards to pattern matching, we can use findall() function
# For example, if we want to find in a string all the words starting with "A"
# or "a" regardless uppercase or lowercase.
text = 'This is my address: 16 Bolton Avenue, Boston'
# Uppercase find
re.findall('A\w+',text)
# Any case
re.findall('[A,a]\w+',text)
# search() function only returns a first match,
# furthermore the object returned is an object
re.search('[A,a]\w+',text)
# It returns back the start and end position of the string
search = re.search('[A,a]\w+',text)
search.start()
search.end()
# The match function performs the matching only at the beginning of the string
# If there is no match with the first character. it goes no further.
# If it cant find a match then it will not return any objects
re.match('[A,a]\w+',text)
# If a match has a response
re.match('T\w+',text)
match = re.match('T\w+',text)
text[match.start():match.end()]  
