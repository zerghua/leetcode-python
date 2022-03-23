#
# Create by Hua on 3/23/22.
#

"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive
range [birthi, deathi - 1]. Note that the person is not counted in the year
that they die.

Return the earliest year with the maximum population.



Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.


Constraints:
    1 <= logs.length <= 100
    1950 <= birthi < deathi <= 2050

"""


class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int

        thought: for each year, check how many people in are born but not dead.
        meaning, birth_i <= year_i < death_i. return the earlist.

        optimization, iterate between the min and max year of given list.

        03/23/2022 10:58	Accepted	48 ms	13.3 MB	python
        easy, 5-10 min, need to understand the problem and transform to math.
        """

        max_p = 0
        ret = 0
        for i in range(1950, 2051):
            count = 0
            for y in logs:
                if y[0] <= i and i < y[1]:
                    count += 1
            if count > max_p:
                max_p = count
                ret = i
        return ret
