"""
Problem:
--------

  You want to eliminate the duplicate values in a sequence, but preserve the
order of the remaining items.

Solution:
---------

  If the values in the sequence are hashable, the probem can be easily solved
using a set and a generator. For example:
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print("list:", a)
print("\nDedupe list:", list(dedupe(a)))

"""
  This only works if the items in the sequence are hashable. If you are trying
to eliminate duplicates in a sequence of unhasable types (such as dicts), you
can make a slight change to this recipe, as follows:
"""

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

"""
  Here, the purpose of the key argument is to specify a function that converts
sequence items into a hashable type for the purpose of duplicate detections.
Here's how it works:
"""

a = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]
print("\n\nList of dict objects:", a)
print("\nDedupe2: ", list(dedupe2(a, key=lambda d: (d["x"], d["y"]))))