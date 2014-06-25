"""
            Combining and Cancatenating Strings
            -----------------------------------

Problem:
--------

  You want to combine many small strigs together into a larger string.

Solution:
---------

  If the strings you wish to combine are found in a sequence or iterable, the
fastest way to combine them is usig the join() method. For example:
"""

parts = ["Is", 'Chicago', 'Not', 'Chicago?']
print("iterable.join(): ", " ".join(parts))

"""
  At first glance, this syntax might look really, odd, but the join() operation
is specified as a method on strings. Partly this is because the objects you
want to join could come from many any number of different data sequences (e.g.,
lists, tuples, dicts, files, sets, or generators), and it would be redundant
to have join() implemented as a method on all of those objects seperately.
"""

"""
  If you're only combining a few strings, using + usually works well enough:
"""

a = "IS Chicago"
b = "Not Chicago?"
print("+ operator: ", a + " " + b)

"""
  The + operator also works fine as a substitute for more complicated
string formatting operations. For example:
"""

print("str.format(): " + '{} {}'.format(a, b))

"""
  If you're trying to combine string literals together in source code, you
can simply place them adjacent to each other with no + operator. For example:
"""

a = "Hello" "World"
print("String concatenation without + operator:", a)

"""
Discussion:
-----------

  The most important thing to know is that using the + operator to join a lot
of strings together is grossly inefficient due to the memory copies and
garbage collection that occurs.

  Also be on the lookout for unneecessary string concatenations. Sometimes
programmers get carried away with concatanation when it's really not
technically necessary. For example:
"""

print("\n\nBad code to better code:\n")

a = "Marcus"
b = "Allen"
c= "Willock"

print(a + ':' + b + ':' + c)
print(":".join([a, b, c]))
print(a, b, c, sep=":")
