"""
                    Extracting a subset of a dictionary
                    -----------------------------------

Problem:
--------

  You want to make a dictionary that is a subset of another dictionary.

Solution:
---------

  This is easily accomplished using a dictionary comprehension. For
example:
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Makes a dictionary of all the prices over 200
p1 = { key:value for key, value in prices.items() if value > 200}
print("DIct comprehension with if statement: \n", p1, "\n\n")

# Make a dictionary of tech stocks
tech_names = ["AAPL", "IBM", "HPQ", "MSFT"]
p2 = {key:value for key, value in prices.items() if key in tech_names}
print("Dict comprehension with if statement asnd list: \n", p2)
