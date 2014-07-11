"""
            Calculating with Large Numerical Arrays
            ---------------------------------------

Problem:
--------

  You need to perform calculations on a large numerical datasets, such as
arrays or grids.

Solution:
---------

  For any heavy computation involving arrays, use the NumPy library. The major
feature of NumPy is that it gives Python an array object that is much more
efficient and better suited for mathematical calulations than standard Python
list. Here is a short example illustrating important behavioral differences
between lists and NumPy arrays:
"""

import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print("ax:", ax)
print("ay:", ay)
print("\n")
print("ax * 2:", ax * 2)
print("ax + 10:", ax + 10)
print("ax + ay:", ay + ax)

"""
  As you can see, basic mathematical operations involving arrays behave
differently. Specifically, scalar operations apply the operation on an element-
by-element basis. In addition, performing math operations with both operands are
arrays applies the operation to all elements and produces a new array.

  The fact that math operations apply to all of the elements simultaneously
makes it very easy and fast to compute functions across an entire array.
For example, if you want to compute the value of a polynomial.
"""

def f(x):
    return 3*x**2 - 2*x + 7

print("Polynomial equation:", f(ax))

"""
  NumPy provides a collection of "universal functions" that also allow for
array operations. These are replacements for similiar functions normally
found in the math module. For example:
"""

print("np.sqrt(ax):", np.sqrt(ax))
print("np.cos(ax):", np.cos(ax))

"""
  Using universal functions can be hundreds of times faster than looping
over the array elements one at a time and performing calculations using functions
in the math module. Thus, you should perfer their use whenever posible.

  Under the covers, NumPy arrays are allocated in the same manner as in C or
Fortran. Namely, they are large, contiguous memory regions consisting of a
homogenous data type. Because of this, it's possible to make arrays much larger
than anything you would normally put into a Python list. For example, if you
want to make a two-dimensional grid of 10,000 by 10,000 floats, it's not an
issue:
"""

grid = np.zeros(shape = (10000, 10000), dtype=float)
print("grid:", grid)

grid += 10
print("grid + 10", grid)

print("np.sin(grid):", np.sin(grid))

"""
  One extremely notable aspect of NumPy is the manner in which it extends
Python's list indexing functionality--especially with multidimensional arrays.
To illustrate, make a simple two-dimensial array and try some experiments:
"""

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Selecting row 1
print("Selecting row 1:", a[1])

# Selecting column 1
print("Selecting a column:", a[:, 1])

# Selecting a subregion and change it
print("Selecting a subregion and change it:", a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows

print("Broadcast a row vector across an operation on all rows:"
        , a + [100, 101, 102, 103])

# Conditional assignment on a array
print("Conditional assignment on a array:", np.where(a < 10, a, 10))
