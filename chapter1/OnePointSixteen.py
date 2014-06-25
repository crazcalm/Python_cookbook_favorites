"""
                        Filtering Sequence Elements:
                        ----------------------------

Problem:
--------

  You have data inside a sequence, and need to extract values
or reduce the sequence using some criteria.

Solution:
---------

  The easiest way to filter sequence data is often to use a
list comprehension. For example:
"""

myList = [1, 4, -5, 10, -7, 2, 3, -1]

listComprehension = [n for n in myList if n > 0]
print("List comprehesion: ", listComprehension, "\n\n")

"""
  One potential downside if using a list comprehension is that
it might produce a large result if the original input is large.
If this is a concern, you an use generator expressions to produce
the filtered values iteratively. For example:
"""

# this creates a generator!
pos = (n for n in myList if n > 0)
print("pos: ", pos, "\n\n")

for x in pos:
    print(x)

"""
  Sometimes, the filtering criteria cannot be easily expressed in
a list comprehension or generator expression. For example, suppose
that the filtering process involves exception handling or some
other complicated detail. For this, put the filtering code into
its own function and use the built-in filter() function. For example:
"""

values = ["1", "2", "-3", "-", "4", "N/A", "5"]

def is_int(val):
    try:
        x = int(val)
        return True

    except ValueError:
        return False

ivals = list(filter(is_int, values))
print("\nUsing the built-in filter() function: \n\n", ivals)

"""
  filter() creates an iterator, so if you want to create a list
of results, makes sure you also use list() as shown
"""


"""
Discussion:
----------

  List comprehensions and generator expressions are often the easiest
and most straightforward ways to filter simple data. They also have the
added power to transform the data at the same time. For example:
"""

# myList is defined above
import math
example = [math.sqrt(n) for n in myList if n > 0]
print("Using math.sqrt() in a list comprehension: ", example, "\n\n")

"""
  One variation on filtering involves replacing the values that don't
meet the criteria with a new value instead of discarding them. For
example, perhaps instead of just finding positive values, you want to
also clip bad values to fit within a specific range. This is often easily
accomplished by moving the filter criterion into a conditional expression
like this:
"""

clip_neg = [n if n > 0 else 0 for n in myList]

print("List Comprehension with if/else statement: ", clip_neg)

"""
  Another notable filtering tool is itertools.compress(), which takes
an iterable and an accompanying Boolean selector sequence as input. As
output, it gives you all of the items in the iterable where the corresponding
elements in the selector is True.

  This can be useful if you are trying to apply results of filtering one
sequence to another sequence. For example, suppose you have the following
two columns of data:
"""

address = [
    '5412 N CLARK',
    '5148 n CLARK',
    '5800 e 58TH',
    '2122 n CLARK',
    '5645 N RAVENWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

count = [0, 3, 10, 4, 1, 7, 6, 1]

"""
  Now suppose you want to make a list of all addresses where the
corresponding count value was greater than 5. Here's how you could do it:
"""

from itertools import compress

# You create a Boolean?
more5 = [n > 5 for n in count]
print("Boolean comprehensions?! ", more5, "\n\n")

example2 = list(compress(address, more5))
print("Using itertools.compress(): ", example2)

"""
  The key here is to first create a list of Booleans that indicates which
elements satisfy the desired condition. The compress() function then
picks out the items corresponding to True values.

  Like filter(), compress() normally returns an iterator. Thus, you need
to use list() to turn the result into a list into a list if desired.
"""
