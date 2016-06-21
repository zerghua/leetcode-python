# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    # sliding window, 2 pointers, o(n)
    # 112 ms
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        ret = 0; i=-1
        for j in range(len(s)):
            if s[j] in hashmap:
                i = max(i, hashmap[s[j]])
            ret = max(ret, j-i)
            hashmap[s[j]] = j

        return ret

