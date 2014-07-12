"""
            Taking a Slice of a iterator
            ----------------------------

Problem:
--------

  You want to take a slice of data produced by an iterator, but the normal
slicing operator doesn't work.

Solution:
---------

  The itertool.islice() function is perfectly suited for taking slices of
iterators and generators. For example:
"""
import itertools

def count(n):
    while True:
        yield n
        n +=1

c = count(0)
for x in itertools.islice(c, 10, 20):
    print(x)

"""
Discussion:
-----------

  Iterators and generators can't normally be sliced, because no information
is known about their length (and they don't implement indexing). The result
of islice() is an iterator that produces the desired slice items, but it does
this by consuming and discarding all of the items up to the starting slice
index. Further items are then produced by the islice object until the ending
index has been reached.

  It's important to emphasize that islice() will consume data on the supplied
iterator. Since iterators can't be rewound, that is something to consider. If
it's important to go back, you should probably just into a list first.
"""
