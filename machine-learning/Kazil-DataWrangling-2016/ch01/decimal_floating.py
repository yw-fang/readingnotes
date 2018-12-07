"""
Donot name this file as 'decimal.py',  otherwise
you will get an error: 'getcontext' is not defined
See ref: https://stackoverflow.com/questions/42357610/why-i-cannot-import-getcontext-from-python-decimal-module
"""
from decimal import getcontext, Decimal
getcontext().prec = 1
a = 0.523
b = 0.554

c1 = a + b
print(c1)
c2 = Decimal(a) + Decimal(b)
print(c2)
