"""
            Calculating with Fractions
            --------------------------

Problem:
--------

 You have entered a time machine and suddenly find yourself working on
elementary level homewrok problems involving fractions. Or perhaps you're
writing code to make calculations involving measurements made in your wood
shop.

Solution:
---------

  The Fraction module can be used to perform mathematical calculations involving
fractions. For example:
"""

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print("Fraction1: ", a, "\nFraction2: ", b, "\n")
print(a + b)
print(a * b)

# Getting numerator.denominator
c = a * b
print("numerator:", c.numerator)
print("denominator:", c.denominator)

# Converting to a float
print("float:", float(c))

# Limiting the denominator of a value
print("Limiting the denominator:", c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print("Converting float to fraction:", y)
