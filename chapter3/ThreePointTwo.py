"""
            Performing Accurate Decimal Calculations
            ----------------------------------------

Problem:
--------

  You need to perform accurate calculations with decimal numbers, and don't
want small errors that naturally occur with floats.

Solution:
---------

  A well-known issue with floating-point numbers is that they can't accurately
represent all based-10 decimals. Moreover, even simple mathematical
calculations introduce errord. For example:
"""

a = 4.2
b = 2.1
print("float-point error: %f" % (a+b))
print("(a+b) == 6.3:",  a+b == 6.3)

"""
  If you want more accuracy (and are willing to give up some performance), you
can use the decimal module:
"""

print("Decimal class stuff: \n\n")
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print("Decimal class example: ", a+b)
print("(a+b) == Decmial('6.3'):", (a+b) == Decimal('6.3'))

"""
  A major feature of decimal is that it allows you to control different aspects
of calculations, including number of digits and rounding. To do this, you
create a local context and change its settings. For example:
"""

from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print("a/b:", a/b)

print("Using local ")

with localcontext() as ctx:
    ctx.prec = 3
    print("localcontext (3):", a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print('localcontext (50):', a/b)

"""
  The decimal module implements IBM's "General Decimal Arithmetic Specification."
Needless to say, there are a huge number of configuration options that are
beyond the scope of this book.
"""
