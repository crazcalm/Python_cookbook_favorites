"""
                Implementing the Iterator Protocal
                ----------------------------------

Problem:
--------

  You are building custom objects on which you would like to support
iteration, but would like and easy way to implement the iterator protocal.

Solution:
---------

  By far, the easiest way to implement iteration on an object it to use a
generator function. In Recipe 4.2, a Node class was presented for representing
tree structures. Perhaps you want to implement an iterator that traverses
nodes in a depth-first pattern. Here is how you could do it:
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

"""
  In this code, the depth_first() method is simple to read and describe. It
first yields itself and then iterates over each child yielding the items
produced by the child's depth_first() method (using yield from)
"""

"""
Discussion:
-----------

  Python's iterator protocal requires __iter__() to return a special object that
implements a __next__() operation and uses a StopIteration exception to signal
completion. However, implementing such objects can often be a messy affair. For
example, the following code shows an alternate implementation of the depth_first()
method using an associated iterator class. (It is an example of bad code. Not
writing it.)
"""
if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
