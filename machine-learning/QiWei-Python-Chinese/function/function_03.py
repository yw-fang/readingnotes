#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
This example shows how to gently 
make use of functions
"""

def add(x, y):
    return(x+y)

"""
In general, we use this function by this way
"""
sum_01 = add(2, 3)

"""
Gently, we can pass a tuple directly to the function
"""
tuple_value = (3, 4)
sum_02 = add(*tuple_value)

"""or we can dict to pass the parameters"""
values = {"x":3, "y":5}
sum_03 = add(**values)

if __name__ == '__main__':
    print('sum_01 is', sum_01)
    print('sum_02 is', sum_02)
    print('sum_03 is', sum_03)


