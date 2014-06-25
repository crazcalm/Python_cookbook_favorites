"""
                Transforming and Reducing Data at the Same Time
                -----------------------------------------------

Problem:
--------

  You need to execute a reduction function (e.g., sum(), min(), max()),
but first need to transfor or filter the data.

Solution:
---------

  A very elegat way to combine a data reduction and a transformation is to
use a generator-expression arguement. For example, if you want to calculate
the sum of squares, do the following:
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

print("sum() with a generator expression", s, "\n\n")

"""
  Here are a few other examples
"""

# Determine if any .py files exist in a directory
import os
files = os.listdir(".")

if any(name.endswith(".py") for name in files):
    print("There be python!\n\n")
else:
    print("Sorry, no python.\n\n")

"""
Discussion:
-----------

  The solution shows a subtle syntactic aspect of generator expressions when
supplied as the single argument to a function (i.e., you don't need repeated
parentheses). For example:
"""

s = sum((x * x for x in nums)) # Pass generator-expr as arguement
print("s (not elegant): ", s, "\n")
s = sum(x *x for x in nums)    # More elegant sytax
print("s (elegant): ", s)

"""
  Using a generator argument is often a more efficient and elegant approach
than first creating a temporary list.
""" 

"""
Notes:
------

  Learn the any() function.

"""
