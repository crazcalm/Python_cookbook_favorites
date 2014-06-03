"""
Problem:
-------

  You have two dictionaries and want to find out what they have in common
(same keys, same values, etc.).

Solution:
---------

  Consider two dictionaries:
"""

a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}

"""
To find out what the two dictionaries have in common, simply perform common set
operations using the keys() or items() methods. For example:
"""

#Find Keys in Common
print("Common keys:", a.keys() & b.keys())

#Find keys in a that are not in b
print("\n\nKeys in a that are not in b:", a.keys() - b.keys())

#Find (key,value) pairs in common
print("\n\nCommon key,value pairs:", a.items() &b.items())

"""
  These kinds of operations can also be used to alter or filter dictionary
contents. For example, suppose you want to make a new dictionary with selected
keys removed. Here is some code using a dictionary comprehension.
"""

#Makes a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {"z", "w"}}
print("\n\ndict c:", c)
