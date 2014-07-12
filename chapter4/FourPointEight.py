"""
            Skipping the First Part of an interable
            ---------------------------------------

Problem:
--------

  You want to iterate over items in an iterable, but the first few items aren't
of interest and you just want to discard them.

Solution:
---------

  The itertools module has a few functions that can be used to address this task.
The first is the itertools.dropwhile() function. To use it, you supply a
function and an iterable. The returned iterator discards the first times in the
sequence as long as the supplied returns True. Afterward, the entirety of the
sequence is produced.

  To illustrate, suppose you are reading a file that starts with a series of
comment lines. For exmaple:
"""

with open("crontab") as f:
    for line in f:
        print(line, end='')

"""
  If you want to skip all of the initial comment lines, here's one way to do it:
"""

from itertools import dropwhile
with open("crontab") as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end="")

"""
  This example is based on skipping the first items according to a test function.
If you happen to know the exact number of items you want to skip, then you can
use itertools.islice() instead. For example:
"""

from itertools import islice

items = ["a", "b", "c", 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

"""
  In this example, the last None argument to islice() is required to indicate
that you want everything beyond the first three items as opposed to only the
first three items (e.g., a slice of [3:] as opposed to [:3]).
"""
