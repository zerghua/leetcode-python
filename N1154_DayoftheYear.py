#
# Create by Hua on 4/30/22.
#

"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:

Input: date = "2019-02-10"
Output: 41



Constraints:

    date.length == 10
    date[4] == date[7] == '-', and all other date[i]'s are digits
    date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.


"""


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int

        thought: map month to days, if it's leap year, feb + 1,
        then convert to days.

        04/30/2022 11:18	Accepted	60 ms	13.5 MB	python
        easy 5-10 min.
        """

        def is_leap(year):
            return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

        year, month, day = [int(x) for x in date.split("-")]
        m = [31,28,31,30,31,30,31,31,30,31,30,31]
        if is_leap(year):
            m[1] += 1

        return sum(m[:month-1]) + day

