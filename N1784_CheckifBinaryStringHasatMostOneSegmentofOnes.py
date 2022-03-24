#
# Create by Hua on 3/24/22.
#

"""
Given a binary string s without leading zeros, return true if s contains at
most one contiguous segment of ones. Otherwise, return false.



Example 1:
Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:
Input: s = "110"
Output: true



Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.
    s[0] is '1'.
"""


class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool

        thought: should be no more 1s after 0s.
        03/24/2022 11:09	Accepted	16 ms	13.4 MB	python
        easy, 5min. logic transformation.
        """

        found_0 = False
        for c in s[1:]:
            if c == '0':
                found_0 = True
            if c == '1' and found_0:
                return False
        return True

