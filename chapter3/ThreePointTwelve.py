"""
        Converting Days to Seconds, and Other Basic Time Conversions
        ------------------------------------------------------------

Problem:
--------

  You have code that needs to perform simple time converstions, like
days to seconds, hours to minutes, and so on.

Solution:
---------

  To Perform conversions and arithmetic involving different units of time,
use the datetime module. For example, to represent an interval of time, create
a timedelta instance like this:
"""

from datetime import datetime, timedelta

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012,12,21)
d = b - a
print(d.days)


now = datetime.today()
print(now)

print(now + timedelta(minutes=10))

"""
  When making calculations, it should be noted that datetime is aware of leap
year.
"""

"""
Discussion:
-----------

  For most basic date and time manipulation problems, the datetime module will
suffice. If you need to perform more complex date manipulations, such as dealing
with time zones, fuzzy time ranges, calculating the dates of holidays, and so
forth, look at the dateutil module.
"""
