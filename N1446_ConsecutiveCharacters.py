#
# Create by Hua on 4/5/22.
#

"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.



Constraints:

    1 <= s.length <= 500
    s consists of only lowercase English letters.


"""


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        thought: 2 loops check consecutive equal chars.
        04/05/2022 11:44	Accepted	57 ms	13.6 MB	python
        easy 5 min. 2 pointers.
        """

        n = len(s)
        i = 0
        ret = 1
        while i<n:
            j = i+1
            while j<n:
                if s[j] == s[i]:
                    j+=1
                else:
                    break
            ret = max(ret, j-i)
            i = j
        return ret
