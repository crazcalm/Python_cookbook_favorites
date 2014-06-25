"""
Problem:
--------

  You want to perform various calculations (e.g., minimum value, maximum value,
sorting, etc.) on a dictionary.

Solution:
---------

  Consider a dictionary that maps stock names to prices
"""

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75
}

"""
  In order to perform useful calculaions on the dictionary contents, it is
often useful to invert the keys and values of the dictionary using zip(). For
example, here is how to find the minimum and maximum and stock name:
"""

# Taking a look at zip()
#for x in zip(prices.values(),prices.keys()):
#    print(x)

min_price = min(zip(prices.values(), prices.keys()))
print("Min:", min_price)

max_price = max(zip(prices.values(), prices.keys()))
print("\n\nMax:", max_price)

# Similarly, to rank the data, use zip() with sorted(), as in the following
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print("\n\nSorted:", prices_sorted)