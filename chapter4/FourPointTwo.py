"""
                Delegating Iteration:
                ---------------------

Problem:
--------

  You have built a custom container object that internally holds a list, tuple,
or some other iterable. You would like to make iteration work with your new
container.

Solution:
---------

  Typically, all you need to do is defined an __iter__() method that delegates
iteration to the internally held container. For example:
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

"""
  In this code, the __iter__() method simply forwards the iteration request to
the internally held _children attribute.
"""

"""
Discussion:
-----------

  Python's iterator protocal requires __iter__() to return a special iterator
object that implements a __next__() method to carry out the actual iteration.
If all you are doing is iterating over the contents of another container, you
don't really need to worry the underlying details of how it works. All you
need to do is to forward the iteration request along.
"""

if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)
