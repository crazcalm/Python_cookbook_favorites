"""
            Defining Generator Function with Extra State
            --------------------------------------------

Problem:
--------

  You would like to define a generator function, but it involves extra state
that you would like to expose to the user somehow.

Solution:
---------

  If you want a generator to expose extra state to the user, don't forget that
you can easily implement it as a class, putting the generator function code in
the __iter__() method. For example:
"""

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

"""
  To use this class, you would like to treat it like a normal generator function.
However, since it creates an instance, you can access internal attributes, such
as the history attribute or the clear() method. For example:
"""

if __name__ == "__main__":
    with open("CodeLikeAPythonista.txt") as f:
        lines = linehistory(f)
        for line in lines:
            if "python" in line.lower():
                for lineno, hline in lines.history:
                    print("{}:{}".format(lineno, hline), end="")
