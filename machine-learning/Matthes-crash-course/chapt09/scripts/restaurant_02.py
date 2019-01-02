#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 28, 2018'

"""
Questions from chapter 09 of python crash course
9-1. Restaurant: Create a class called Restaurant . The __init__() method for Restaurant should 
store two attributes: a restaurant_name and a cuisine_type . Make a method called describe_restaurant() that prints 
these two pieces of information, and a method called open_restaurant() that prints a message indi- cating that 
the restaurant is open .
Make an instance called restaurant from your class . Print the two attri- butes individually, and then call 
both methods .
9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three different instances from the 
class, and call describe_restaurant() for each instance .

"""

class Restaurant():
    """Restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open')

my_restaurant = Restaurant(restaurant_name='Apple', cuisine_type='Western')
print('The name and the cuisine_type of my restaurant are %s and %s' % (my_restaurant.restaurant_name,
                                                                        my_restaurant.cuisine_type))
my_restaurant.describe_restaurant()

Yuki_restaurant = Restaurant(restaurant_name='Tentora', cuisine_type='Japanese')
Yuki_restaurant.describe_restaurant()


Lili_restaurant = Restaurant(restaurant_name='Sichuan', cuisine_type='Chinese')
Lili_restaurant.describe_restaurant()
