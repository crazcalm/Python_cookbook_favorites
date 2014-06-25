"""
Problem:
--------

  You want to make a dictionary that maps keys to more than one value (a
so-called "multi-dict").

Solution:
---------

  A dictionary is a mapping where each key is mapped to a single value. If you
want to map keys to multiple values, you need to store the multiple values to
another container such as a list or set. For example, you might make
dictionaries like this:
"""

d = {
     "a" : [1,2,3],
     "b" : [4,5]
}

e = {
     "a" : {1,2,3},
     "b" : {4,5}
}

"""
  The choice of whether or not to use lists ot sets depends on intended use.
Use a list if you want to perserve the insertion order of the items. Use a set
if you want to eliminate duplicates (and don't care about the order).

  To easily construct such dictionaries, you can use defaultdict in the
collections module. A feature of defaultdict is that it automatically
initializes the first value so you can simply focus on adding items. For
Example:
"""

from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)
