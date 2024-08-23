import os

a, b, = 1, 2

a = 1
b = 2

a, b = b, b + a  # a, b = 2, 2 + 1 ==>  a, b = 2, 3

c = None
c = b
b = b + a
a = c
