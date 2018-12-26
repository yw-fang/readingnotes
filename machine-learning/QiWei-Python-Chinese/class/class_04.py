#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
single inheritance
"""

class Person:
    """
    define a CLASS Person with three methods

    """
    def speak(self):
        print('How are you?')

    def listheight(self):
        print('Height is 170 cm')

    def listweight(self, n):
        print('weight is', n)


class Girl(Person):
    """
    class Girl inherits the attributes and methods
    in the class Person

    """
    def listheight(self):
        """
        overwrite the methods listheight
        """
        print('HEIGHT is 165 cm')


if __name__ == '__main__':
    cang = Girl()
    cang.listheight()
    cang.speak()
    cang.listweight(80)
