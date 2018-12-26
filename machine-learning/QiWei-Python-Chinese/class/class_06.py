#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
This scripts is used for explaining the sequence of
multiple inheritance.

If a class APPLE inherits two parent classes which have some same
methods, then which method will the class APPLE use?
"""

class K1:
    def foo(self):
        print('K1-foo')

class K2:
    def foo(self):
        print('K2-foo')
    def bar(self):
        print('K2-bar')

class J1(K1,K2):
    pass

class J2(K1,K2):
    def bar(self):
        print('J2-bar')

class C(J1, J2):
    pass

if __name__ == '__main__':
    print(C.__mro__)  # print the inheritance relations
    m = C()
    m.foo()  # firstly check J1, and J2, and K1, find 'K1-foo'
    m.bar()  # firstly check J1, and J2, find 'J2-bar'
