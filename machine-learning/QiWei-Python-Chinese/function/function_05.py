#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
filter function
"""

xlist = [i for i in range(10)]
print(filter(lambda x: x<=2, xlist))
print(filter(x<=2, xlist))
