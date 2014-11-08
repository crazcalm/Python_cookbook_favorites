"""
Problem:
--------

  You want to write a function that accepts any number of input arguments.

Solution:
---------

  To write a function that accepts any number of positional arguments, use a 
* argument. For example:
"""

def avg(first, *rest):
    return (first + sum(rest)/ (1 + len(rest)))

"""
  In this example, rest is a tuple of all the extra positional arguments passed.
The code treats it as a sequence in performing subsequent calculations.
"""

"""
  To accept any number of keyword arguments, use an argument that starts with
**. For example:
"""

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = "".join(keyvals)
    element = '<{name}{attrs}> <{value}></{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))

    return element

"""
  With this function, all of the posistional arguments are placed into a
tuple args, and all of the keyword arguments are placed into a dictionary
kwargs
"""

def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    print(avg(1,2))
    print(avg(1,2,3,4))
    test = make_element("item", "Albatross", size="6", quantity=6)
    print(test)
    anyargs(1,2,3,4,3,4, test=True, name="Marcus", age=26)

