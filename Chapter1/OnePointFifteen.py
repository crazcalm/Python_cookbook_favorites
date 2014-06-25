"""
Problem:
--------

  You have a sequence of dictionaries or instances and you want to iterate
over the data in groups based on the value of a particular field, such as date.

Soluton:
--------

  The itertools.groupby() function is particularly useful for grouping data
together like this. To illustrate, suppose you have the following list of
dictionaries:
"""

rows = [
    {"address": "5412 N CLARK", "date": "07/01/2012"},
    {"address": "5148 N CLARK", "date": "07/04/2012"},
    {"address": "5800 E 58TH", "date": "07/02/2012"},
    {"address": "2122 N CLARK", "date": "07/03/2012"},
    {"address": "5645 N RAVENWOOD", "date": "07/02/2012"},
    {"address": "1060 W ADDISON", "date": "07/02/2012"},
    {"address": "4801 N BROADWAY", "date": "07/01/2012"},
    {"address": "1039 W GRANVILLE", "date": "07/04/2012"}
]

"""
  Now suppose you want to iterate over data in chunks grouped by date. To do
it, first sort by the desired field (in this case, date) and then use
itertools.groupby():
"""
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter("date"))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print("     ", i)

"""
Discussion:
-----------

  The groupby() function works by scanning a sequence and finding
sequencial "runs" of identical values (or values returned by the
given key function). One each iteration, it returns the value along
with an iterator that produces all of the items in a group with
the same value.

  An important preliminary step is sorting the data according to
the field of interest. Since groupby() only examines consecutive
items, failing to sort first won't group the records as you want.
"""

"""
Extra:
------

  If your goal is to simply group the data together by dates into
a large data structure that allows random access, you may have
better luck using defualtdict() to build a multidict, as described
in Recipe 1.6. For example:
"""

print("\n\nDefaultdict use case:\n\n")

from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row["date"]].append(row)

"""
  This allows the records for each date to be accessed
easily like this:
"""

for r in rows_by_date["07/01/2012"]:
    print(r)

print("\n\nrows_by_date:\n", rows_by_date)

"""
Note:
-----

 This is the python answer to that ruby quiz I had to do!
"""
