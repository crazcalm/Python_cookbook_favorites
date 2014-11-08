"""
Problem:
-------

  You want to iterate over a sequence, but would like to keep track of which
elements of the sequence is currently being processed.

Solution:
---------

  The built-in enumerate() function handles this quite nicely:
"""

my_list = ["a", "b", "c"]
for idx, val in enumerate(my_list):
    print(idx, val)

"""
  For printing output with canonical line numbers (Where you typically start
the numbering at 1 instead of 0), you can pass in a start argument:
"""

my_list = ["a", "b", "c"]
for idx, val in enumerate(my_list, 1):
    print(idx, val)

"""
  This case is especially useful for tracking line numbers in files should
you want to use line numbers in an error message:
"""

def parse_data(filename):
    with open(filename, "rt") as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(field[1])
            except ValueError as e:
                print("Line {}: Parse error: {}".format(lineno, e))

"""
  enumerate() can be handy for keeping track of the offset into a list for 
occurences of certain values, for example. So, if you want to map words in a
file to the lines in which they occur, it can easily be accomplished using
enumerate() to map each word to the line offset in the file where it was found.
"""
from collections import defaultdict

word_summary =defaultdict(list)

with open("NightAndDayByVirginiaWoolf.txt", "r") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Creates a list of words i current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

for key, item in word_summary.items():
    print(key, item)
    print("\n\n")
    input()
"""
  If you print word_summary after processing the file, it'll be a dictionary
(a default dict to be precise), and it'll have a key for each word. The
value for each word-key will be list of line numbers that word occurred on.
If the word occurred twice on a single line, that line number will be listed
twice, making it possible to identify various simple metrics about the text.
"""
