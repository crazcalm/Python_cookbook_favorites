"""
            Writing a Regular Expression for Multiline Patterns
            ---------------------------------------------------

Problem:
--------

  You're trying to match a block of text using a regular expression, but you
need the match to span multiple lines.

Solution:
---------

  This problem typically arises in patterns that use the dot (.) to match any
character but forget to account for the fact that is doesn't match newlines.
For example, suppose you are trying to match C-style comments:
"""

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
                multiline comment*/'''

example1 = comment.findall(text1)
print("example1:", example1, "\n\n")

example2 = comment.findall(text2)
print("Does not capture multiline comments:", example2, "\n\n")

"""
  To fix the problem, you can add support for newlines. For example:
"""

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
example2_fixed = comment.findall(text2)
print("Captures multiline comments:", example2_fixed)

"""
  In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines
a group for the purposes of matching, but the group is not captured separately
or numbered).
"""
