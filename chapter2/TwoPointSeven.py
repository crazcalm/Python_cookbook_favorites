"""
            Specifying a Regular Expression for the Shortest Match
            ------------------------------------------------------

Problem:
--------

  You're trying to match a text pattern using regular expressions, but it is
identifying the longest possible matches of the pattern. Instead, you would
like to change it to find the shortest possible match.

Solution:
---------

  This problem often arises in patterns that try to match text enclosed inside
a pair of starting and ending delimiters (e.g., a quoted string). To illustrate,
consider this example:
"""
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
example1 = str_pat.findall(text1)
print("example1: ", example1, "\n\n")

text2 = 'Computer says "no." Phone says "yes."'
example2 = str_pat.findall(text2)
print("This phrase was not quoted: ", example2, "\n\n")

"""
  In this example, the pattern r'\"(.*)\"' is attempting to match text enclosed
inside quotes. However, the * operator in a regular expression is greedy, so
matching is based on finding the longest possible match. Thus, in the second
example involving text2 incorrectly matches the two quoted strings.

  To fix this, add the ? modifier after the * operator in the pattern,
like this:
"""

str_pat = re.compile(r'\"(.*?)\"')
example2_fixed = str_pat.findall(text2)
print("Correctly finded quoted phrases: ", example2_fixed, "\n\n")

"""
  This makes the matching nongreedy, and produces the shortest match instead.
"""
