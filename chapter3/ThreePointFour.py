"""
            Working with Binary, Octal, and Hexadecimal
            -------------------------------------------

Problem:
--------

  You need to convert or output itegers represented by binary, octal, or
hexadecimal digits.

Solution:
--------

  To convert an integer into a binary, octal, or hexadecimal text string, use
bin(), oct(), or hex() functions, respectively:
"""

print("Using bin(), oct(), and hex():\n\n")

x = 1234
print("number:", x)
print("bin():", bin(x))
print("oct():", oct(x))
print('hex():', hex(x))

"""
  Alternatively, you can use the format() function if you don't want the 0b,
0o, or 0x prefixes to appear. For example:
"""

print("\n\nUsing format(): \n\n")

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

"""
  To convert integer strings in different bases, simply use the int() function
with an appropriate base. For example:
"""

print("\n\nConversions using int():\n\n")
print(int('4d2', 16))
print(int('10011010010', 2))

