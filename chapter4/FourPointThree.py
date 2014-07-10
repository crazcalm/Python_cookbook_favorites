"""
            Creating New Iteration Patterns with Generators
            -----------------------------------------------

Problem:
--------

  You want to implement a custom iteration pattern that's different than
usual built-in functions (e.g., range(), reverse(), etc).

Solution:
---------

  If you want to implement a new kind of iteration pattern, define it using a
generator function. Here's a generator that produces a range of floating-point
numbers:
"""

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

"""
  To use such a function, you iterate over it using a for loop or use it with
some other function that consumes an iterable (e.g., sum(), list(), etc).
For example:
"""

for n in frange(0, 4, 0.5):
    print(n)

print("\n")
print(list(frange(0, 1, 0.125)))

"""
Discussion:
-----------

  The mere presence of the yield statement in a function turns it into a
generator. Unlike a normal function, a generator only runs in response to
iteration.
"""

