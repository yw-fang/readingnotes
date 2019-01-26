#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Jan. 26, 2018'

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        # long_name = self.year + ' ' + self.make + ' ' + self.model
        # note that  unsupported operand type(s) for +: 'int' and 'str'
        # hence we must use str(self.year)
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return(long_name.title())  # str.title

    def get_descriptive_name_1(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return(long_name)

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.get_descriptive_name_1())