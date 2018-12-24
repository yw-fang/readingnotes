#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
This example shows that documentation for the functions
you defined is important for others who read your codes.

To understand the importance of the documentation for the
function, run this script by:
python function_01.py

For the first function ''add_function', since I wrote the
documentation, its information will be printed, for the second
one, 'None' will be printed.
"""

def add_function(x,y):
    """ This function will add x to y, and return the sum"""
    z = x + y
    return(z)


def sumxy(x,y):
    z = x + y
    return(z)


if __name__ == '__main__':
    number = add_function(3, 4)
#     dir_info = dir(add_function)
#     print('number is ', number)
#     print('dir_info of function: ', dir_info)
    print('documentation information: ', add_function.__doc__)

    value = sumxy(3,4)
#     dir_info = dir(add_function)
#     print('number is ', number)
#     print('dir_info of function: ', dir_info)
    print('documentation information: ', sumxy.__doc__)
