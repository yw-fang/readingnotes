#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
We have two ways to define the class.

Way 1:

class BB(object):
    pass
    
b = BB()
    
Way 2:

__metaclass__ = type
class CC:
    pass
    
c = CC()
"""

__metaclass__ = type

# define a class Person
# In general Capitalize the first letter of a each word
class Person:
    def __init__(self, name):  # __init__ is necessary for call to initialize
        self.name = name

    def getName(self):
        return(self.name)

    def color(self, color):
        print("%s is %s" % (self.name, color))

# FANG is an instantce, it has attribution and method
# we pass 'FANG' to the name in the Person class
person = Person('FANG')
print(person.name)