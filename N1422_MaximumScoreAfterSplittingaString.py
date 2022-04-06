#
# Create by Hua on 4/6/22.
#

"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.



Example 1:

Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3



Constraints:

    2 <= s.length <= 500
    The string s consists of characters '0' and '1' only.


"""


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int

        thought: precompute 1's(an optimization), iterate s, record 0's on the
        left, if encounter 1, substract from 1s, if encounter, zero, add to left
        attention: non-empty substring(corner case here)
        04/06/2022 11:51	Accepted	24 ms	13.5 MB	python
        easy 5 min.
        """

        right = s.count("1")
        left = 0
        ret = 0
        for i in range(len(s)-1):
            c = s[i]
            if c == "0":
                left += 1
            else:
                right -= 1
            ret = max(ret, left + right)
        return ret