#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yue-Wen FANG'
__maintainer__ = "Yue-Wen FANG"
__email__ = 'fyuewen@gmail.com'
__license__ = 'Apache License 2.0'
__creation_date__= 'Mar. 20, 2019'

"""
Extra whitespace can be confusing in your programs. To programmers 'python' and 'python '
look pretty much the same. But to a program, they are two different strings.
"""

message = '     Python        '
message_1 = message.rstrip()  # trim left empty
message_2 = message.lstrip()  # trim right empty

print(message_1,'\n',message_2)
print(len(message_1),'\n',len(message_2))