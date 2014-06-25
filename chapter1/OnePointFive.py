"""
Problem:
--------

  You want to implement a queue that sorts items by a given priority and always
returns the item with the highest priority.

Solution:
---------

  The following class uses the heapq module to implement a simple priority
queue:
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item(%s)" % self.name

if __name__ == "__main__":
    q = PriorityQueue()
    test = [("foo", 1), ("bar", 5), ("spam", 4), ("grok", 1)]
    for item, priority in test:
        q.push(Item(item), priority)

    for index in range(len(test)):
        print(q.pop())