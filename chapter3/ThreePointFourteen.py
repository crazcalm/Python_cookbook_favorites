"""
            Finding the Date Range for the Current Month
            --------------------------------------------

Problem:
--------

  You have some code that needs to loop over each date in the current month,
and want an efficient way to calculate that date range.

Solution:
---------

  Looping over the dates doesn't require building a list of all the dates
ahead of time. You can just calculate the starting and stopping date in the
range, then use datetime.timedelta object to incremet the date as you go.

  Here's a functions that takes any datetime object, and returns a tuple
cotaining the first date of the month and the starting date of the next month.
"""

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date == None:
        start_date = date.today().replace(day=1)

    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days= days_in_month)
    return (start_date, end_date)

"""
Discussion:
-----------

  This recipe works by first calculating a date correspoding to the first day
of the month. A quicke way to do this is to use the replace() method of a datetime
object to simply set the days attribute to 1. One nice thing about the replace()
method is that it creates the same kind of object that you started with. Thus,
if the input was a date instance, the result is a date.

  After that, calendar.monthrange() function is used to find out how many days
are in the month in question. Any time you need to get basic information
about caledars, the calendar module ca be useful. monthrange() is only one
such function that returns a tuple containing the day of the week alog with
the number in days in the month.

  Once the number of days in the month is known, the ending date is calculated
by adding an appropriate timedelta to the starting date. It's subtle, but an
important aspect of this recipe is that the eding date is not to be included
in the range (it is atcually the first day of the next month). 

  To loop over the date range, standard math and comparison operators are used.
For example, timedelta instance can be used to increment the date. The <
operator is used to check whether a date comes before the ending date.
"""

if __name__ == "__main__":
    a_day = timedelta(days=1)

    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day
