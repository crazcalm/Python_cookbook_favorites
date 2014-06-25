"""
Problem:
--------

  You have a sequence of items, and you'd like to determine the most frequently
occuring items in the sequence.

Solution:
---------

  The collections.Counter class is designed for just such a problem. It even
comes with a handy most_common() method that will give you the answer.

  To illustrate, let's say you have a list of words and you want to find out
which words occur most often. Here's how you would do it:
"""

words = [
    "look", "into", "my", "eyes", "look", "into", "my", "eyes", "the", "eyes",
    "the", "eyes", "the", "eyes", "the", "eyes", "not", "look", "around", "the",
    "eyes", "look", "into","my", "eyes", "you're", "under"
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print("The top three words are: ", top_three)

"""
Discussion:
-----------

  As input, Counter objects can be fed any sequence of hashable input items.
Under the covers, a Counter is a dictionary that maps the items to the number
of occurrences. For example:
"""

print("\n\nThe word 'not' appears:",word_counts["not"], "times.")
print("\nThe word 'eyes' appears", word_counts["eyes"], "times.")

"""
If you want to increment the count manually, simply use addition:
"""

morewords = ["why", "are", "you", "not", "looking", "in", "my", "eyes"]
for word in morewords:
    word_counts[word] += 1

print("After adding more words, the word 'eyes' now appears", word_counts["eyes"], "times.")