#
# Created by Hua on 9/7/2016
#

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""

#  62 ms  59 / 59 test cases passed.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0: return 0
        ret = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                ret += 1
            else:
                if ret != 0: break
        return ret