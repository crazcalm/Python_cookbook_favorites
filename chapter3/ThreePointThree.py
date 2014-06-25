"""
            Formatting Numbers for Output
            -----------------------------

Problem:
--------

  You need to format a number for outpur, controlling the number of digits,
alignment, inclusion of a thousands seperator, and other details.

Solution:
---------

  To format a single number for output, use the built-in format() function.
For example:
"""

x = 1234.5678

print("Formating %f:\n\n" % x)

# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified
print(format(x, '<10.1f'))

# Centered
print(format(x, '^10.1f'))

# Inclusion of thousands seperator
print(format(x, ','))
print(format(x, '0,.1f'))

"""
  If you want to use exponentional notation, change the f to an e or E,
depending on the case you want used for the exponential specifier. For example:
"""

print("Exponential formatting:\n\n")

print(format(x, 'e'))
print(format(x, '0.2E'))

"""
  The general form of the width and precision in both cases is
'[<>^]?width[,](.digits)?' where width and digits are integers and ? signifies
optional parts. The same format codes are also used in the .format() method
for strings. For example:
"""

print("The value is {:0.2f}".format(x))
