#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
In a CLASS, we do not always need pass external arguments,
we can also set the default in the class
"""

class Person:
    def __init__(self, name, height='175', weight='200', email='f@jp'):
        """this is an initial"""
        self.name = name
        self.height = height
        self.weight = weight
        self.email = email
        print(self)
        print(type(self))

fang_san = Person('Fang')  # The first instance in this script
yang_san = Person('Yang', height='150', weight='110', email='hello@jp')  # The second instance here

print('fang_san.email is %s and yang_san.email is %s' % (fang_san.email, yang_san.email))

print('fang_san.weight is %s' % (fang_san.weight))

