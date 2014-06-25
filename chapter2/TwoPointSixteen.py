"""
            Reformatting Text to a Fixed Number of Columns
            ----------------------------------------------

Problem:
--------

  You have long strings that you want to reformat so that they fill a
user-specified number of columns.

Solution:
---------

  Use the textwrap module to reformat text for output. For example, suppose
you had the following long string:
"""

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

"""
  Here's how you can use the textwrap module to reformat it in various ways:
"""

import textwrap
example1 = textwrap.fill(s, 70)
example2 = textwrap.fill(s, 40)
example3 = textwrap.fill(s, 40, initial_indent='    ')
example4 = textwrap.fill(s, 40, subsequent_indent='    ')

print("\n%s\n\n%s\n\n%s\n\n%s" % (example1, example2, example3, example4))

"""
Discussion:
-----------

  The textwrap module is a straightforward way to clean up text for printing--
expecially if you want the output to fit nicely on the termainal. On the subject
of terminal size, you can obtain it using os.get_terminal_size(). For example:
"""

import os
terminal_size = os.get_terminal_size().columns
print("\n\nterminal size: %s" % terminal_size)

"""
  The fill() method has a few additional options that control how it handles
tabs, sentence endings, and so on. Look at the documentation for the
textwrap.TextWrapper class for further details.
"""
