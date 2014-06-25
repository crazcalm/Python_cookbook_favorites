"""
                Matchin Text at the Start or End of a String
                --------------------------------------------

Problem:
--------

  You need to check the start or end of a string for specific text patterns,
such as filename extentions, URL schemes, and so on.

Solution:
---------

  A simple way to check the beginning or end of a string is to use the
str.startswith() or str.endswith() methods. For example:
"""

filename = 'spam.txt'
print("String:", filename)
print("Using str.endswith() :", filename.endswith('.txt'))
print("Using str.startswith() :", filename.startswith('file:'), "\n\n")

url = 'http://www.python.org'
print("String:", url)
print("Using str.startswith() :", url.startswith('http:'), "\n\n")

"""
  If you need to check against multiple choices, simply provide a tuple of
possiblities to startwith() or endswith():
"""

import os

filenames = os.listdir("..")
print("filenames:", filenames, "\n\n")

example = [name for name in filenames if name.endswith((".py", ".txt"))]
print("Using endswith with multiple params:", example, "\n\n")

"""
  Oddly, this is one part of Python where a tuple is actually required as
input. If you happen to have the choices specified in a list or set, just
make sure you convert them using tuple() first.
"""
