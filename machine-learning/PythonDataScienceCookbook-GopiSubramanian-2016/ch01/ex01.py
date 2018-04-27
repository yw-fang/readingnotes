# This correspodns to Page 21 for Chinese version
# This is a simple code based on a example from the book
# Written by Y.-W. Fang
__date__ = "April 27, 2018"


def process(x):
    if isinstance(x, str):
        return x.lower()
    elif isinstance(x, int):
        return x*x
    else:
        return -9


a = (1, 2, -1, -2, 'D', 3, 4, -3, 'A')
b = (process(x) for x in a)
print(a)
print(b)
