"""
Problem:
--------

  You want to keep a limited history of the last few items seen during iteration
or during some other kind of process

Solution:
---------

  Keeping a limited history is a perfect use for a collections.deque. For
example, the following code performs a simple text match on a sequence of lines
and yeilds the matching line with the previous N lines of context when found.
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


"""
Discussion:
-----------

  When writing code to search for items, it is common to use a generator
function involking yield, as shown in this recipe's solution. This decouples
the process of searching from the code that uses the result.If you are new to
generators, see Recipe 4.3.

  Using deque(maxlen=N) creates a fixed-sized queue. When new items are added
and the queue is full, the oldest items is automatically removed.
"""

if __name__ == "__main__":
    with open('NightAndDayByVirginiaWoolf.txt') as f:
        for line, prevlines in search(f, "regret", 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-" * 70)