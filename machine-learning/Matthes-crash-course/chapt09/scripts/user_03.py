#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Dec. 28, 2018'

"""
9-3. Users: Make a class called User . Create two attributes called first_name and last_name, and then create
several other attributes that are typically stored in a user profile . Make a method called describe_user()
that prints a summary of the user’s information . Make another method called greet_user() that prints a
personalized greeting to the user .
Create several instances representing different users, and call both methods for each user .t mv dog.py
"""

class User:
    """
    a class for User
    """
    def __init__(self, first_name, last_name, gender, age, email='f@cn'):
       self.name = first_name + last_name
       self.gender = gender
       self.age = age
       self.email = email  # if no email is specified, the default will be used

    def describe_use(self):
        print('The profile of ' + self.name + ":")
        print('Gender: ', self.gender)
        print('Age: ', self.age)
        print('Email: ', self.email)

Tiantian_Li = User('Tiantian', 'Li', 'Male', '20', email='Li@cn')
Tiantian_Li.describe_use()


