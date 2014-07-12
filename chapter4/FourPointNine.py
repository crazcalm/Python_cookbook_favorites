"""
            Iterating Over All Possible Combinations or Permutations
            --------------------------------------------------------

Problem:
--------

  You want to iterate over all of the possible combinations of a collection
of items.

Solution:
---------

  The itertools module provides three functions for this task. The first of
these--itertools.permutations()-- takes a collection of items and produces a
sequence of tuples that rearranges all of the items into all possible
combinations (i.e., it shuffles them into all possible configurations). For
example:
"""

items = ["a", "b", "c"]
from itertools import permutations
for p in permutations(items):
    print(p)

"""
  If you want all permutations of a smaller length, you can give an optional
length arguement. For example:
"""

for p in permutations(items, 2):
    print(p)

"""
  Use itertools.combinations() to produce a sequence of combinations of items
taken from the input. For example:
"""

from itertools import combinations
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)

"""
  For combinations(), the actual order of the elements is not considered. That
is, the combinations ('a', 'b') is considered to be the same as ('b', 'a')
(which is not produced).

  When producing combinations, chosen items are removed from the collection
of possible candidates (i.e., if 'a' has already been chosen, then it is
removed from consideration). The itertools.combinations_with_replacement()
relaxes this and allows the same item to be chosen more than once. For
example:
"""

from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
