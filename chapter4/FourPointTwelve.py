"""
Problem:
--------

  You need to perform the same operation on many objects, but the objects
are contained in different containers, and you'd like to avoid nested loops
without losing the readability of your code.

Solution:
---------

  The itertools.chain() method can be used to simplify this task. It takes
a list of iterables as input, and returns an iterator that effectively masks
the fact that you are really acting on multiple containers. To illustrate,
consider this example:
"""

from itertools import chain

a = [1,2,3,4]
b = ["x", "y", "z"]

for x in chain(a,b):
    print(x)

"""
  A common use of chain() is in programs where you would like to perform certain
operations on all the items at once but the items are pooled into different
working sets. For example:
"""

# Various working sets of items
active_items = set([1,2,3,4])
inactive_items = set(["x", "y", "z"])

# Iterate over all items
for item in chain(active_items, inactive_items):
    print(item)

"""
  This solution is much more elegant than using two seperate loops.
"""

"""
Discussion:
-----------

  itertools.chain() accepts one or more iterables as arguments. It then works
by creating an iterator that successively consumes and returns the items
produced by each of the supplied iterables you provided. It's a subtle
distinction, but chain() is more effecient than first combining the
sequences and iterating.
"""
