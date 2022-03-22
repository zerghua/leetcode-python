#
# Create by Hua on 3/22/22.
#

"""
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring,
every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".



Constraints:

    1 <= s.length <= 100
    s consists of lowercase English letters.
"""


class Solution(object):
    def is_valid(self, s):
        return s[0] != s[1] and s[0] != s[2] and s[1] != s[2]

    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        thought: get all 3 chars substrings, validate before put in a list.
        03/22/2022 10:05	Accepted	28 ms	13.4 MB	python
        easy 10 min.
        """
        ret = list()
        n = len(s)
        for i in range(n-2):
            sub = s[i:i+3]
            if self.is_valid(sub):
                ret.append(sub)

        return len(ret)

