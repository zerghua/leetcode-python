#
# Create by Hua on 3/21/22.
#

"""
Given a string s and an array of strings words, determine whether s is a
prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the
first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.



Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    1 <= s.length <= 1000
    words[i] and s consist of only lowercase English letters.


"""


class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool

        thought: try to concatenate the first k string in array, continue until
        the length of the string >= s, and do a compare.

        easy 5min, just need to understand the problem.

        03/21/2022 15:29	Accepted	27 ms	13.6 MB	python
        """

        ret = ""
        for w in words:
            ret += w
            if len(ret) >= len(s):
                break

        return ret == s