"""
Problem:
--------

  You want to iterate over the items contained in more than one sequence
at a time.

Solution:
---------

  To iterate over more than one sequence simultaneiously, use the zip()
function. For example:
"""

xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99]
for x, y in zip(xpts, ypts):
    print(x,y)

"""
zip(a, b) works by creating an iterator that produces tuples(x, y) where x is
taken from a and y is taken from b. Iteration stops whenever one of the input
sequences is exhuasted. Thus, the length of the iteration is the same length
of the shortest input. For Example:
"""

a = [1,2,3]
b = ["w", "x", "y", "z"]
for i in zip(a,b):
    print(i)

"""
  If this behavior is not desired, use itertools.zip_longest() instead. For
Example:
"""

from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

"""
Discussion:
-----------

  zip() is commonly used whenever you need to pair data together. For example,
suppose you have a list of column headers and column values like this:
"""

headers = ["name", "share", "price"]
values = ["ACME", 100, 490.1]

"""
Using zip(), you can pair the values together to make a dictionary like this:
"""

s = dict(zip(headers, values))

"""
Alternatively, if you are trying to produce output, you can write code like
this:
"""

for name, value in zip(headers, values):
    print(name, "=", value)

"""
It's less common, but zip() can be passed more than two sequences as input.
For this case, the resulting tuples have the same number of items in them as
the number of input sequences. For Example:
"""

a = [1,2,3]
b = [10,11,12]
c = ["x", "y", "z"]

for i in zip(a,b,c):
    print(i)
