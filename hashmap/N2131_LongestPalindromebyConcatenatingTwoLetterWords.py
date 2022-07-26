#
# Create by Hua on 7/26/22
#

"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.

"""


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int

        thought: 1 hashmap to store different word and same word count.

        corner case, when dup's count is even it can be used in addition to the largest count.
        07/26/2022 15:15	Accepted	1600 ms	38.8 MB	python
        medium - easy .
        10-20min.
        hashmap.
        """

        import collections
        dt = collections.defaultdict(int)
        ret = 0
        for w in words:
            # w[0] and w[1] are different
            reverse = w[1] + w[0]
            if dt[reverse] > 0:
                dt[reverse] -= 1
                ret += 4
            else:  # reverse not exist
                dt[w] += 1

        for key in dt.keys():
            if dt[key] > 0 and key[0] == key[1]:
                return ret + 2
        return ret
