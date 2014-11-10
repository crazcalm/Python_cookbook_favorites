"""
Problem:
--------

  You want a function to only accept certain arguements by keyword

Solution:
---------

  This feature is easy to implement if you place the keyword argument
after a * argument or a single unnamed *. For example:
"""

def recv(maxsize, *, block):
    'Receives a message'
    pass

#recv(1024, True) Type Error
recv(1024, block=True) # okay

"""
  This technique can also be used to specify keyword arguments for functions
that accept a varying number of positional arguments. For example:
"""

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(mininum(1,5,-5,10)) # Returns -5
print(mininum(1,5,2,-5,10, clip=0)) # Returns 0

"""
Discussion:
-----------

  Keyword-onlu arguments are often a good way to enforce greater code
clarity when specifying optional function arguments.
"""


