#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 26, 2018'

"""
Here, I rewrote the example dog.py in the book
of Python Crash Couse.
This example is not exactly same to the one
in that book.
"""

class Dog():  # (1)
    """Dog class"""  # (2)

    def __init__(self, name, age):  # (3)
        """
        initialize the name and age
        :param name: the name of dog
        :param age: the age of the dog
        """
        self.name = name  # (4)
        self.age = age

    def sit(self):  # (5)
        """
        :return: dog sits
        """
        print(self.name.title() + ' is sitting now')  # title() used for capitalizing the first letter

    def roll_over(self):
        """
        :return: dog rolls over
        """
        print(self.name.title() + ' is rolling over now!')

if __name__ == "__main__":
    """
    In the first instance, I pass the string '2' to age.
    In the second instance, I pass the integer 2 to age.
    This reflects the Polymorphism of Python.
    
    In the two instances, two dogs were created.
    """
    x = Dog('Henry', '2')
    print('The name of the dog is %s' % (x.name.title()) + '.')
    print('The age of the dog is %s' % x.age + '.')
    x.roll_over()

    y = Dog('Will', 2)
    print('The name of the dog is %s' % (y.name.title()) + '.')
    print('The age of the dog is %s' % (str(y.age)) + '.' )  # convert the integer to string
    y.roll_over()
