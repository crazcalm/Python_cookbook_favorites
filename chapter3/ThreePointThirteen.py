"""
            Dertermining Last Friday's Date
            -------------------------------

Problem:
--------

  You want a general solution for finding a date for the last occurrence of
a day of the week. Last Friday, for example:

Solution:
---------

  Python's datetime module has utility functions and classes to help perform
calculations like this. A decent, generic solution to this problem looks like
this:
"""

from datetime import datetime, timedelta

weekdays = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7

    if days_ago == 0:
        days_ago = 7

    target_date = start_date - timedelta(days= days_ago)
    return target_date

"""
Discussion:
-----------

  This recipe works by mapping the start date and the target date to their
numeric position in the week (with Monday as 0). Modular arithmetic is then
used to figure out how many days ago the target date last occured. From there,
the desired date is calculated from the start date by substracting an
appropriate timedelta instance.

  If you're performing a lot of date calculations like this, you may be
better off installing the python-dateutil package insteas.

"""

if __name__ == "__main__":
    print("Today: ", datetime.today())

    # Go through all the days in the week
    for day in weekdays:
        print(get_previous_byday(day))

    print("\n\nUsing the optional start_date:\n")
    print(get_previous_byday("Sunday", datetime(2012, 12, 21)))

