#
# Create by Hua on 7/24/22
#

"""
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.



Example 1:

Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
Example 2:

Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.


Constraints:

0 <= num <= 1015

"""


class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]


        thought: math, the num needs to be dividable by 3.
        07/24/2022 09:04	Accepted	37 ms	13.2 MB	python
        medium - easy
        2 min.
        math
        """
        if num % 3 != 0:
            return []

        n = num / 3
        return [n-1, n, n+1]
