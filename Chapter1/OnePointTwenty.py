"""
                    Combining Mulitple Mappings into a Single
                    -----------------------------------------

Problem:
--------

  You have multiple dictionataries or mappings that you want to logically
combine into a single mapping to perform certain operations, such as looking
up values or checking for the existence of keys.

Solution:
---------

  Suppose you have two dictionaries:
"""

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

"""
  Now suppose you want to perform lookups where you have to check both
dictionaries (e.g., first checking in a then in b if not found). An easy
way to do this is to use the ChainMap class crom the collections module.
For example:
"""

from collections import ChainMap

c = ChainMap(a, b)

print("Using ChainMap\n\n")
print(c['x'])       # Output 1 (from a)
print(c['y'])       # Output 2 (from b)
print(c['z'])       # Output 3 (from a)


"""
Note:
-----

  Python 3.3 or greater is needed. Python 3.2 does not have ChainMap
"""

"""
Discussion:
-----------

  A Chainmap takes multiple mappings and makes them logically appear
as one. However, the mappings are not literally merged together. Instead,
a ChainMap simply keeps a list of the underlying mappings and redefines common
dictionary operations to scan the list. Most operations will work. For example:
"""

print("\n\nlen(c): ", len(c))
print("\n\nlist(c.keys()): ", list(c.keys()))
print("\n\nlist(c.values()): ", list(c.values()))

"""
  If there are duplicate keys, the values from the first mapping get
used. Thus, the entry c['z'] in the example would always refer to the
value in dictionary a, not the value in dictionary b.

  Operations that mutuate the mapping always affect the first mapping
listed.
"""

"""
  As an alternative to ChainMap, you might consider merging dictionaries
together using the update() method. For example:
"""

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}

merged = dict(b)
merged.update(a)

print("Merged dictionaries: ", merged)
