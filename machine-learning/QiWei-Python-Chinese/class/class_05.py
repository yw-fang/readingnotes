#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
multiple inheritance
"""

class Person:
    def eye(self):
        print('balck eyes')

    def height(self, n):
        print('height is', n)


class Girl:
    age = 30
    def skincolor(self):
        print('skin color is white')

class HotGirl(Person, Girl):
    """
    Inherit the class Person and Girl
    """
    pass


if __name__ == "__main__":
    kong = HotGirl()
    kong.eye()
    kong.height(200)
    kong.skincolor()
    print(kong.age)


