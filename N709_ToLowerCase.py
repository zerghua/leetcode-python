#
# Create by Hua on 5/18/22
#


"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.

"""


class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        thought: I don't think it's worth the time to do the math here of manual converting.
        05/18/2022 09:57	Accepted	20 ms	13.5 MB	python

        """
        return s.lower()
