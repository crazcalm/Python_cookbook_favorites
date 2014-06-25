"""
            Converting Strings into Datetimes
            ---------------------------------

Problem:
--------

  Your application receives temporal data in string format, but you want to
convert those strings into datetime objects in order to perform nonstring
operations on them.

Solution:
---------

  Python's standard datetime module is typically the easy solution for this.
For example:
"""

from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, "%Y-%m-%d")
z = datetime.now()
diff = z-y

print(y)
print(z)
print(diff)

"""
Discussion:
-----------

  The datetime.strptime() methos supports a host of formatting codes, like
%Y for the four-digit year %m for the two-digit month. It's also worth noting
that the formating placeholders also work in reverse, in case you need to
represent a datetime object in string output and make it look nice.

  For example, let's say you had some code that generates a datetime object, but
you need to format a nice, human-readable date to put in the header of an
auto-generated letter or report:
"""

# Type error
#nice_z = datetime.strptime(z, "%A %B %d, %Y")
#print(nice_z)
