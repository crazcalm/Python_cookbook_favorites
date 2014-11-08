"""
Problem:
--------

  You have a nested sequence that you want to flatten into a single list
of values

Solution:
---------

  This is easily solved by writing a recursive generator function involving
a yield from statement. For example:
"""

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)

"""
  In the code, the isinstance(x, Iterable) simple checks to see if an item
is iterable. If so, yield from is used to emit all of its values as a
kind of a subroutine. The end result is a single sequence of output with no
nesting.
"""
