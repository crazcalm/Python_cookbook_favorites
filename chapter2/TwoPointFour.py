"""
                Matching and Searching for Text Patterns
                ----------------------------------------

Problem:
--------

  You want to match or search text for a specific patter.

Solution:
----------

  If the text you're trying to match is a simple literal, you can often just use
basic string methods, such as str.find(), str.endswith(), str.startswith(), or
similar. For example:
"""

text = 'yeah, but no, but yea, but no, but yeah'

# Exact match
text == 'yeah' # false

# Match at start or end
text.startswith('yeah') # True

text.endswith("no") # False

"""
  For more complicated matching, use regular expressions and the re module. to
illustrate the basic mechanics of using regular expressions, suppose you want to match
dates specified as digits, such as '11/27/2012.' Here is a sample of how you would do it:
"""

text1 = "11/27/2012"
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print("Yes, a match was found!\n\n")
else:
    print("No matches were found.\n\n")

"""
  if you're going to perform a lot of matches using the same pattern, it
usually pays to precompile the regular expression pattern into a pattern
object first. For example:
"""

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('Yes, a match was found!\n\n')
else:
    print("No matches found.\n\n")

"""
  Match() always tries to find the match at the start of the string. If you
want to search for all occurences of a pattern, use the findall() method
instead. For example:
"""

text = "Today is 11/27/2012. Pycon starts 3/13/2013"
example = datepat.findall(text)
print("re.findall() :", example, "\n\n")

"""
  Capture groups often simplify subsequent processing of the matched text
because the contents of each group can be extracted individually. For example:
"""

datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

# Exact the contents of each group
print("re.group() example:\n\n")
print(m.group(0))
"""
Note:
-----

  Not working in python3.4...
The strange part is tha the group stuff worked in TwoPointFive.py

print(m.group(1))
print(m.group(2))
print(m.group(3))
"""
print(m.groups())

"""
  The findall() method searchs the text and finds all matches, returning them
as a list. If you want to find matches iteratively, use the finditer() method
instead.
"""
