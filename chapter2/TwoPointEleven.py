"""
            Stripping Unwanted Characters from Strings
            ------------------------------------------

Problem:
--------

  You want to strip unwanted characters, such as whitespace, from the
beginning , end, or middle of a text string.

Solution:
---------

  The strip() method can be used to strip characters from the beginning or end
of a string. lstrip() and rstrip() perform stripping from the left or right
side, respectively. By default, these methods strip whitespace, but other
characters can be given. For example:
"""

# Whitespace stripping
s = '    hello world    \n'
print("Original string: %s" % s)
print("strip(): %s" % s.strip())
print("lstrip(): %s" % s.lstrip())
print("rstrip(): %s\n\n" % s.rstrip())

# Character stripping
t = '-----hello====='
print("Original string: %s" % t)
print("lstrip(): %s" % t.lstrip('-'))
print("strip(): %s" % t.strip('-='))

