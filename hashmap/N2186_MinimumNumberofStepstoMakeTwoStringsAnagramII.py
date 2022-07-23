#
# Create by Hua on 7/23/22
#

"""
You are given two strings s and t. In one step, you can append any character to either s or t.

Return the minimum number of steps to make s and t anagrams of each other.

An anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "leetcode", t = "coats"
Output: 7
Explanation:
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
Example 2:

Input: s = "night", t = "thing"
Output: 0
Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.


Constraints:

1 <= s.length, t.length <= 2 * 105
s and t consist of lowercase English letters.

"""


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        thought: hashmap to store count of each char, ret += abs(s - t) for each char count
        07/23/2022 08:56	Accepted	1375 ms	18 MB	python
        medium - easy
        5-10 min.
        hashmap.
        """
        import collections
        a, b = collections.Counter(s), collections.Counter(t)

        ret = 0
        import string
        for c in string.ascii_lowercase:
            ret += abs(a[c] - b[c])
        return ret

