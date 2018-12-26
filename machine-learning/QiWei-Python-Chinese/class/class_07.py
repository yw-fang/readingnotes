#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
super function can be used to gain access to inherited methods – from a parent or sibling class

class_07.py introduce a problem and doesnot use the super function

The super function will be introduce in class_08.py
"""

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print('{} is about{}'.format(name, self.height))

class Girl(Person):
    def __init__(self):
        self.eyecolor = 'blue'

    def about(self, name):
        print("{} is a hot girl, she is about {}, and her eyecolor is {}".format(name, self.height, self.eyecolor))

if __name__ == '__main__':
    cang = Girl()
    cang.about('Yuri-chan')


"""
Run this script, and you will get errors:
AttributeError: 'Girl' object has no attribute 'height'

Comparing the two calsses Person and Girl, we found both __init__ and about methods were both defined in
the two classes.

In the CLASS Girl, __init__ was rewritten, and its height wasnot defined.
"""






