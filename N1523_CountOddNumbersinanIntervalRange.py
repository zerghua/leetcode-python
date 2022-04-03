#
# Create by Hua on 4/3/22.
#

"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].



Constraints:

    0 <= low <= high <= 10^9

"""


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int

        thought: it's a math problem with several conditions.
        04/03/2022 14:34	Accepted	24 ms	13.5 MB	python
        easy 5 min. math
        """

        if (high - low + 1) % 2 == 0:  # even
            return (high - low + 1) / 2
        else:
            extra = 0
            if low % 2 == 1:
                extra = 1
            return (high - low + 1) / 2 + extra



