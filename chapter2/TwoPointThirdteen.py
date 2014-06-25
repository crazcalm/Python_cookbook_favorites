"""
                Aligning Text Strings:
                ----------------------

Problem:
--------

  You need to format text with some sort of alignment applied.

Solution:
---------

  For basic alignment of strings, the ljust(), rjust(), and center() methods of
strings can be used. For example:
"""

text = "Hello World"
print("Original string: %s" % text)
print("ljust(): %s" % text.ljust(20))
print("rjust(): %s" % text.rjust(20))
print("center(): %s\n" % text.center(20))

"""
  All of these methods accept an optional &&65.180&&fill character as well.
For example:
"""

print("Adding a filler character to the methods used above.\n")
print("%s\n%s\n" % (text.rjust(20, '='), text.center(20, "*"))) 

"""
  The format() function can also be used to easily align things. All you need
to do is use the <, >, or ^ characters along with a desired witdh. For example:
"""
print("Using the format() function for the following code:\n\n")
print("%s\n%s\n%s\n" % (format(text, ">20"), format(text, ">20"), \
                        format(text, "^20")))

"""
  If you want to include a fill character other than a space, specify it before
the alignment character:
"""

print("%s\n%s\n" % (format(text, "=>20"), format(text, "*^20")))

"""
  These format codes can also be used in format() methos when formatting multiple
values. For example:
"""

print("{:>10s} {:>10s}".format("Hello", "World"))
