"""
Problem:
--------

  You need to unpack N elements from an iterable, but the iterable may be
longer than N elements, causing a "too many values to unpack exception"

Solution:
---------

  Python "star expressions" can be used to address this problem. For example,
suppose you run a course and decide at the end of the semester that you're
going to drop the first and last homework grades, and only average the rest of
them.
"""

def avg(grades):
    return sum(grades)/len(grades)

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

"""
Discussion:
-----------

  Extended iterable unpacking is tailor-made for unpacking iterables of unknown
or arbitrary length. Oftentimes, these iterables have have some known component
or pattern in their construction, and star unpacking lets the developer leverage
those patterns easily instead of performing acrobatics to get at the relevant
elements in the iterable.
"""

records = [
           ("foo", 1, 2),
           ("bar", "hello"),
           ("foo", 3, 4)]

def do_foo(x,y):
    print("foo", x, y)

def do_bar(s):
    print("bar", s)

if __name__ == "__main__":
    grades = [1,2,3,4,5,6,7,8,9,10]
    average = drop_first_last(grades)
    print("grades average: %s\n\n" % average)

    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
        elif tag == "bar":
            do_bar(*args)
