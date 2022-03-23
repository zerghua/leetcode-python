#
# Create by Hua on 3/23/22.
#

"""
Given an alphanumeric string s, return the second largest numerical digit
that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase
English letters and digits.



Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.



Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.
"""


class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int

        thought: extract all the unique digits into set and convert them into
        list and sort, return the second largest. note on the corner cases.

        03/23/2022 15:56	Accepted	66 ms	13.4 MB	python
        easy 5 min. set and sort.
        """

        st = set()
        for c in s:
            if c in "0123456789":
                st.add(int(c))

        if len(st) <= 1:
            return -1
        return sorted(st, reverse=True)[1]
