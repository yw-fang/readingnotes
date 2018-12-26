#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
Namespaces in Python

- Built-in namespaces: those in the built-in functions of python

- Global namespaces: those in each module

- Local namespaces: those in the function or class located in the modules

Python will first checks the built in namespaces, then check the global, and lastly local namespaces.
"""

def foo(number, type):
    name = 'hello-kitty'
    print(locals())

foo(300, 'animal')

print(globals())

