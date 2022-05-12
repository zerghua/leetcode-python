#
# Create by Hua on 5/12/22
#


"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]


Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.

"""


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]

        thought: use python lib,
        s.symmetric_difference(t)  s ^ t  new set with elements in either s or t but not both
        https://docs.python.org/2/library/sets.html
        this does not satisfy requirement

        2 hashmap to check
        05/12/2022 15:10	Accepted	29 ms	13.6 MB	python
        easy 5min.

        better solution, leveraging problem given:
        No matter how many sentences, uncommon word = words that appears only once
        will only need one hashmap and return key with count == 1
        """
        import collections
        ret = list()
        a, b = collections.Counter(s1.split()), collections.Counter(s2.split())
        for k, v in a.items():
            if v == 1 and k not in b:
                ret.append(k)

        for k, v in b.items():
            if v == 1 and k not in a:
                ret.append(k)

        return ret


