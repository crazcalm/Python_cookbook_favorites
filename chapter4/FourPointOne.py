"""
            Manually Consuming an Iterator
            ------------------------------

Problem:
--------

  You need to process items in an iterable, but for whatever reason, you can't
or don't want to use a loop.

Solution:
---------

  To manually consume an iterable, use the next() function and write your code
to catch the StopIteration exception. For example, this example manually reads
lines from a file:
"""

with open('etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line)
