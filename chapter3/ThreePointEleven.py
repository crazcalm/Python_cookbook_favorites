"""
            Picking Things at Random
            ------------------------

Problem:
--------

  You want to pick random items out of a sequence or generate random numbers.

Solution:
---------

  The random module has various functions for random numbers and picking
random items. For example, to pick a random item out of a sequence, use
random.choice():
"""

import random

print("Random Module:\n\n")

values = [1,2,3,4,5,6]
for num in range(4):
    print(random.choice(values))

"""
  To take a sampling of N items where selected items are removed from further
consideration, use random.sample() instead:
"""

for num in range(4):
    print(random.sample(values, 2))

"""
  If you simply want to shuffle items in a sequence in place, use
random.shuffle():
"""

for num in range(3):
    random.shuffle(values)
    print(values)

"""
  To produce random integers, use random.randint():
"""

for num in range(10):
    print(random.randint(0, 10))

"""
  To produce uniform floating-point values in the range 0 to 1, use
random.random():
"""

for num in range(4):
    print(random.random())

"""
  To get N random-bits expressed as an integer, use random.getranbits():
"""

print(random.getrandbits(200))

"""
Discussion:
-----------

  The random module computers random numbers using the Mersenne Twister
algorithm. This is a deterministic algorithm, but you can alter the initial
seed by using the random.seed() function. For example:

random.seed()               # Seed based on system time or os.urandom
random.seed(12345)          # Seed based on integer given
random.seed(b'bytedata')    # Seed based on byte data

  In addition to the functionality shown, random() includes functions for
uniform, Gaussian, and other probability distributions. For example,
random.uniform() computes uniformly distributed numbers, ad random.gauss()
computers normally distributed numbers. Consult the documentation for
information on other supported distributions.

  Functions, in random() should not be used in programs related to
cryptography. If you need such functionality, consider using functions in the
ssl module instead. For example, ssl.RAND_bytes() can be used to generate a
cryptographically secure sequence of random bytes.
"""
