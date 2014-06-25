"""
            Interpolating Variables in Strings
            ----------------------------------

Problem:
--------

  You want to create a string in which embedded variable names are substituted
with a string representation of a variable's value.


Solution:
---------

  Python has no direct support for simply substituting variable values in
strings. However, this feature can be approximated using the format()
method of strings. For example:
"""

s = "{name} has {n} messages."
print(s.format(name="Guido", n= 37))

"""
  Alternatively, if the values to be substituted are truly found in variables,
you can use the combination of format_map() and vars(), as in the following:
"""

name = "Guido"
n = 37
print(s.format_map(vars()))

"""
  One downside of format() and format_map() is that they do not deal gracefully
with missing values.
"""

