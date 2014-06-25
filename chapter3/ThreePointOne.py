"""
            Rounding Numerical Values
            -------------------------

Problem:
--------

  You want to round a floating-point number to a fixed number of decimal places.

Solution:
---------

  For simple roounding, use the built-in round(value, ndigits) function. For
example:
"""

print("Rounding: \n\n")

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

"""
  When a value is exactly halfway between two choices, the behavior of round
is to round to the nearest even digit. That is, values such as 1.5 2.5 both
get rounded to 2.

  The number of digits given to round() can be negative, in which case rounding
takes place for tens, hundreds, thousands, and so on. For example:
"""

print("\n\nRounding the tens, hundreds, and thousands:\n")

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))
print(round(a, -4))

"""
Discussion:
-----------

  Don't confuse rounding with formatting a value for output. If your goal is
simply to output a numerical value with a certain number of decimal places,
you don't typically need to use round(). Instead, just specify the desired
precision formatting. For example:
"""

print("\n\nFormatting numbers in output:\n")

x = 1.23456
print(format(x, '-.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))
