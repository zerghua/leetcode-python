#
# Create by Hua on 4/7/22.
#

"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15



Constraints:

    The given dates are valid dates between the years 1971 and 2100.


"""


class Solution(object):
    def is_leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def to_days(self, date):
        # yyyy-mm-dd
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        ret = 0
        d = date.split("-")
        year = int(d[0])
        m = int(d[1])
        day = int(d[2])
        for i in range(1971, year):
            ret += 365
            if self.is_leap(i):
                ret += 1
        ret += sum(month[:m-1])
        ret += day
        if self.is_leap(year) and m > 2:
            ret += 1

        return ret

    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int

        thought: convert date to days between date to 1971-01-01
        四年一闰，百年不闰，四百年再闰
        04/07/2022 14:26	Accepted	26 ms	13.4 MB	python
        easy - medium 20-30 min.
        """

        return abs(self.to_days(date1) - self.to_days(date2))

