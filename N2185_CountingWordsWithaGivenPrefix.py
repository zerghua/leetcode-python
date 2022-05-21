#
# Create by Hua on 5/21/22.
#

"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.



Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] and pref consist of lowercase English letters.


"""


class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int

        thought: startwith() function
        05/21/2022 10:42	Accepted	41 ms	13.6 MB	python
        easy 2 min.
        """

        ret = 0
        for word in words:
            if word.startswith(pref):
                ret += 1
        return ret
