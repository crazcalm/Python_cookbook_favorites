"""
                Searching and Replacing Text
                ----------------------------

Problem:
--------

  You want to search for and replace a text pattern in a string

Solution:
---------

  For simple literal patterns, use the str.replace a text pattern in a string.
For example:
"""

text = 'yeah, but no, but yeah, but no, but yeah'

print("str.replace() :", text.replace('yeah', 'yep'))

"""
  For more complicated patterns, use the sub() functions/methods in the re
module. To illustrate, suppose you want to rewrite dates of the form
'11/27/2012' as '2012-11-27.' Here is a sample of how to do it:
"""

text = 'Today is 11/27/2012. Pycon starts 3/13/2013'
import re
example = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

print("re.sub() :", example, "\n\n")

"""
  The first argument to sub() is the pattern to match and the second argument
is the replacement pattern. Backslashed digits such as \3 refer to capture
group numbers in the pattern.

  If you're going to perform repeated substitutions of the same pattern,
consider compiling it first for better performance.
"""
