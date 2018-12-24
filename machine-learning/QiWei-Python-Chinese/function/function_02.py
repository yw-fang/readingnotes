#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This example shows the functionality
of positional arguments and keyword ONLY arguments.

The positional arguments correspond to tuple,
the keyword ONLY arguments correspond to dict.
"""

def add_function_01(x, *args):  # you can use any other proper names instead of using args
    """ positional arguments"""
    print('x is', x)
    for i in args:
        print(i),


def add_function_02(x, *args, **kwargs):  # you can use any other proper names instead of using args
    """ positional arguments and keyword specific arguments """
    print('x is', x)
    print(args)
    print('the type of args is', type(args))
    print(kwargs.values())
    print(kwargs.keys())
    print('the type or kwargs is', type(kwargs))

if __name__ == "__main__":
    add_function_01(1,2,3,45)
    print("*************")
    add_function_02(3, 1, 2, 3, 45, c=3, d=4)
    print("*************")
