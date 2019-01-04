#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Jan. 3, 2019'

"""
"""

class HaveFun():
    @staticmethod
    def helloworld():
        print('my name is Li Lei')

    @classmethod
    def hellomars(cls):
        print('This is class method hellomars()')
        print("hellomars() is part of class: ", cls.__name__)


class Action(HaveFun):
    def __init__(self):
        print("Hello, 2019")


AA = Action()
AA.hellomars()
print(dir(AA))
AA.helloworld()