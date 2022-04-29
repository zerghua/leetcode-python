#
# Create by Hua on 4/29/22.
#

"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"



Constraints:

    The given dates are valid dates between the years 1971 and 2100.


"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str

        04/29/2022 13:37	Accepted	15 ms	13.7 MB	python
        easy, call functions.
        or
        return date(year, month, day).strftime("%A")
        """
        import datetime
        import calendar
        my_date = datetime.datetime(year,month,day)
        return calendar.day_name[my_date.weekday()]
