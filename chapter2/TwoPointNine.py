"""
            Normalizing Unicode Text to a Standard Representation
            -----------------------------------------------------

Problem:
--------

  You're working with Unicode strings, but need to make sure that all of
the strings have the same underlying representation.

Solution:
---------

  In Unicode, certain character can be represented by more than one valid
sequence of code points. To illustrate, consider the following example:
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print("Note: the unicode is different.\n")
print("s1: %s\ns2: %s" % (s1, s2))

print("s1 == s2: ", s1==s2, "\n")
print("len(s1):", len(s1), "\n")
print("len(s2):", len(s2), "\n")

"""
  Here, the text "Spicy Jalapeno" has been presented in two forms. The first
uses the fully composed "\u11f10" (U + 00F1) character. The second uses the Latin
letter "\u03030" followed by a "~" combining character (U +0303).

  Having multiple representations is a problem for programs that compare strings.
In order to fix this, you should first normalize the text into a standard
representation using the unicodedata module:
"""

import unicodedata
t1 = unicodedata.normalize("NFC", s1)
t2 = unicodedata.normalize("NFC", s2)
print("The words have been normalized!\n")
print("t1: %s\nt2: %s\n" % (t1, t2))

print("t1 == t2:", t1==t2)

print("t1:", ascii(t1))
print("t2:", ascii(t2))
