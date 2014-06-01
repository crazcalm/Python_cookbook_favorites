"""
Problem:
--------

  You want to create a dictionary, and you also want to control the order of
items when iterating or serializing.

Solution:
---------

  To control the order of items in a dictionary, you can use an OrderedDict
from the collections module. It exactly preserves the original insertion order
of data when iterating. For Example:
"""

from collections import OrderedDict

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key in d:
    print(key, d[key])