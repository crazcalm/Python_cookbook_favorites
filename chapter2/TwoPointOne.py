"""
                Splitting Strings on Any of Multiple Delimiters
                -----------------------------------------------

Problem:
--------

  You need to splite a string into fields, but the delimiters (and spacing
around them) aren't consistent throughout the string.

Solution:
---------

  The split() methos of string object is really meant for very simple case,
and does not allow for multiple delimiters or account for possible whitespace
around the delimiters. In cases when you need a bit more flexibility, use the
re.split() method:
"""

line = "asdf fjdk, fjek, fjek,asdf,        foo"
import re

example = re.split(r'[;,\s]\s*', line)
print("Using re.split(): ", example, "\n\n")

"""
Discussion:
-----------

  The re.split() function is useful because you cam specify multiple patterns
for separator. For example, as shown in the solution, the separator is either a
comma (,), semicolon (;), or whitespace followed by anu amount of extra
whitespace.Whenever that pattern is found, the entire match becomes the
delimiter between whatever fields lie on either side of the match. The result
is a list of fields, just as with str.split()

  When using re.split(), you need to be a bit careful should the regular
expression pattern involve a capture group enclosed in parentheses. If capture
groups are used, then the matched text is also include in the result. For
example, watch what happens here:
"""

fields = re.split(r'(;|,|\s)\s*', line)
print("THe wrong way: ", fields, "\n\n")

"""
  Getting the split characters might be useful in certain contexts. For example,
maybe you need the split characters later on the reform an output string:
"""

values = fields[::2]
delimiters = fields[1::2] + ['']
print("values: ", values, "\n\n")
print('delimiters: ', delimiters)
