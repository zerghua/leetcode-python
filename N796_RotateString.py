#
# Create by Hua on 5/14/22.
#

"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.



Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false



Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.


"""


class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool

        thought: double s and check if goal is in doubled s
        05/14/2022 16:26	Accepted	13 ms	13.5 MB	python
        easy 1 min.
        """

        return len(s) == len(goal) and goal in s*2
