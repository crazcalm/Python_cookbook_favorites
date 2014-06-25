"""
                        Mapping Names to Sequence Elements

Problem:
--------

  You have code that accesses a list or tuple by position, but this makes the
code somewhat difficult to read at times. You'd also like to be less dependent
on position in the structure, by accessing the elements by name.

Solution:
---------

  collections.namedtuple() provides these benefits, while adding minimal
overhead over using a normal tuple object. collections.namedtuple() is actually
a factory method that a subclass of the standard Python tuple type. You feed
it a type name, and the fields you've defined, and so on. For example:
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ["addr", 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print("Named tuple: ", sub, "\n")
print("sub.addr: ", sub.addr, "\n")
print('sub.joined: ', sub.joined, "\n\n")

"""
  Although an instance of a namedtuple looks like a normal class instance, it
is interchangeable with a tuple and supports all of the usual tuple operations
such as indexing and unpacking.
"""

"""
  A major use case for named tuples is decoupling your code from the position
of the elements it manipulates. So, if you get back a large list of tuples from
a database call, then manipulate them by accessig the positional elements, your
code could break if, say, you add a new column to your table. Not so if you
cast the return tuples to named tuples
"""

"""
Discussion:
-----------

  One possible use of a namedtuple is as a replacement for a dictionary, which
requires more space to store. Thus, if you are building large data structures
involving dictionaries, use of a namedtuple will be more than efficient.
However, be aware the unlike a dictionary, a namedtuple is immutable.

  IF you need to change any of the attributes, it can be done using _replace()
method of a namedtuple instance, which makes an entirely new namedtuple with
specified values replaced.
"""
