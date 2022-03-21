#
# Create by Hua on 3/21/22.
#

"""
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number
of occurrences (i.e., the same frequency).



Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'.
All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.



Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""


class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool

        thought: hashtable(dictionary) to check count of each key

        03/21/2022 17:08	Accepted	39 ms	13.4 MB	python

        easy, 5 min, hashtable

        solution from discussion:
        class Solution:
            def areOccurrencesEqual(self, s: str) -> bool:
                return len(set([s.count(i) for i in s])) == 1
        """

        dic = dict()
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        count = dic[s[0]]
        for key in dic.keys():
            if count != dic[key]:
                return False
        return True
