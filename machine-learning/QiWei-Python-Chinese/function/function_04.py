#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 25, 2018'

"""
This example shows 
how to use lambda, map, reduce, zip

These examples are only used for displaying the functionality of these functions.
Some of the examples are not recommended although the results are exactly same.
"""

# Question: there are two lists xlist and ylist
# Please calculate the sum = x1*y1 + x2*y2 +... + x_n*y_n
# import numpy as np
from functools import reduce
# for python 3, reduce is placed in the module of functools
# for python 2, we can directly use reduce without import it

xlist = [i for i in range(10)]
ylist = [i for i in range(10, 20)]

# basic usages

# method 1: without builtin function
def sum_product(xlist, ylist):

    product = []
    for i in range(len(xlist)):
        product.append(xlist[i] * ylist[i])
    return(sum(product))


x_y_list = (xlist, ylist)
print('sum(product)', sum_product(*x_y_list))


# method 2 : use lambda
def sum_product_lambda(xlist, ylist):
    lam = lambda x, y: x*y
    product = []
    for i in range(len(xlist)):
        product.append(lam(xlist[i], ylist[i]))
    return(sum(product))


print('sum(product) using lambda is', sum_product_lambda(xlist, ylist))


# method 3: use map, lambda
def sum_product_map(xlist, ylist):
    product = map(lambda x,y: x*y, xlist, ylist)
    return(sum(product))


print('sum(product) using map and lambda', sum_product_map(xlist, ylist))

# method 4: use map, lambda, reduce
def sum_product_reduce(xlist, ylist):
    product = map(lambda x,y: x*y, xlist, ylist)
    return(reduce(lambda m,n: m+n, product))


print('sum(product) using map and lambda and reduce', sum_product_reduce(xlist, ylist))


# method 5: use zip
def sum_product_zip(xlist, ylist):
    x_y_list = zip(xlist, ylist)
    sum_xy = sum(x*y for x,y in x_y_list)
    return(sum_xy)


print('sum(product) using zip', sum_product_zip(xlist, ylist))


# method 6: use reduce, lambda, zip
def sum_product_reducezip(xlist, ylist):
    x_y_list = zip(xlist, ylist)
    sum_xy = reduce(lambda sum, (x,y): sum+x*y, x_y_list, 0)
    return(sum_xy)


print('sum(product) using zip and reduce', sum_product_reducezip(xlist, ylist))
