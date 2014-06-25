"""
                Matching String Using Shell Wildcard Patterns
                ---------------------------------------------

Problem:
--------

  You want to match text using the same wildcard patterns as are commonly used
when working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc).

Solution:
---------

  The fmatch module provides two functions--fmatch() and fmatchcase()--that
can be used to perform such matching. The usage is simple:
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))  # True
print(fnmatch('foo.txt','?oo.txt')) # True

"""
  Normally, fmatch() matches patterns using the same case-sensitivity rules
as the system's underlying filesystem (which varies based in operating system).

  If this distinction matters, use fmatchcase() instead. It matches exactly
based on the lower- and uppercase conventions that you supply.
"""
