#
# Create by Hua on 3/24/22.
#

"""
A string s is nice if, for every letter of the alphabet that s contains,
it appears both in uppercase and lowercase. For example, "abABB" is nice
because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not
because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are
multiple, return the substring of the earliest occurrence. If there are none,
return an empty string.



Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the
alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear.
The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.



Constraints:
    1 <= s.length <= 100
    s consists of uppercase and lowercase English letters.
"""


class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str

        medium: divide and conquer, or brute force
        https://leetcode.com/problems/longest-nice-substring/discuss/1074589/JavaStraightforward-Divide-and-Conquer

        03/24/2022 14:10	Accepted	29 ms	13.5 MB	python
        20-30min, medium. brute force list all subsets or divide and conquer.
        """
        if not s: return ""
        n = len(s)
        ss = set(s)
        for i in range(n):
            if s[i].swapcase() not in ss:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return max(s1,s2, key=len)
        return s
