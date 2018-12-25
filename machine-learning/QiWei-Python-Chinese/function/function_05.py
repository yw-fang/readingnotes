#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
filter function in python  3.
Note that the filter function in python 2 and python 3 are
very different, here I only use python 3.
"""

xlist = [i for i in range(10)]
filtered = list(filter(lambda x: x<=2, xlist))
print(filtered)