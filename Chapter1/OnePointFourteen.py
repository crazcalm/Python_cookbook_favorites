"""
Problem:
--------

  You want to sort objects of the same class, but they don't natively support
comparison operations.

Solution:
---------

  The built-in sorted() function takes a key argument that can pass a callable
that will return some value in the object that sorted will use to compare the
objects.
"""

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)

users = [User(23), User(3), User(99)]

sort1 = sorted(users, key=lambda u: u.user_id)
print("Sorting (lambda version): \n")
for user in sort1:
    print(user)

"""
  Instead of using lambda, an alternative approach is to use
operator.attrgetter()
"""
from operator import attrgetter

sort2 = sorted(users, key=attrgetter("user_id"))
print("\nSorting (operator.attrgetter() version): \n")

for user in sort2:
    print(user)
