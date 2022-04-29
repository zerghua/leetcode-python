#
# Create by Hua on 4/29/22.
#

"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.



Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    words[i] and chars consist of lowercase English letters.


"""


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int

        thought: count occurrence for each string
        https://docs.python.org/2.7/library/collections.html

        04/29/2022 15:12	Accepted	731 ms	14 MB	python
        easy 10-20min.
        """
        import collections
        map = collections.Counter(chars)
        ret = 0
        for word in words:
            m = collections.Counter(word)
            map.subtract(m)
            if min(map.values()) >= 0:
                ret += len(word)

            map.update(m)
        return ret