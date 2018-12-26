#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
super function is introduced to remove the error in class_07.py
"""

class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print('{} is about {}'.format(name, self.height))

class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        # the __init__ method of parent class Person will be inherited
        # in super function, the first one is the name of class, here is Girl; the second is
        # self, the third is method, here, it's __init__
        self.eyecolor = 'blue'

    def about(self, name):
        print("{} is a hot girl, she is about {}, and her eyecolor is {}".format(name, self.height, self.eyecolor))
        super(Girl, self).about(name)  # the about method of parent class Person will be inherited

if __name__ == '__main__':
    cang = Girl()
    cang.about('Yuri-chan')
