"""
Problem:
--------

  You have N-element tuple or sequence that you would like to unpack into a
collection of N variables

Solution:
---------

  Any sequence (or iterable) can be unpacked into variables using a simple
operation. The only requirement is that the number of variables and structure
match the sequence.
"""

p = (4, 5)
x, y = p

print("x: %s\ny: %s" % (x, y))

data = ["ACME", 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data

print("name: %s" % name)

