#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Jan. 21, 2019'

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = 'Luffy'
        self.__name = 'Vivi'

    def __python(self):
        print("I love navigating")

    def code(self):
        print("which hobby do you like?")
        self.__python()


if __name__ == "__main__":
    p = ProtectMe()
    print(p.me)
    print(p.__name)


"""
The output of this python script is
#############
Luffy
Traceback (most recent call last):
  File "class_12.py", line 28, in <module>
    print(p.__name)
AttributeError: 'ProtectMe' object has no attribute '__name'
#############

This is because __name was hidden for external use.
However, it can be use internally.

"""

