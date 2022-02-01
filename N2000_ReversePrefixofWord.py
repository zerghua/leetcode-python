#
# Create by Hua on 2/1/22.
#

"""
Given a 0-indexed string word and a character ch, reverse the segment of word
that starts at index 0 and ends at the index of the first occurrence of
ch (inclusive). If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", then you should reverse
    the segment that starts at 0 and ends at 3 (inclusive).
    The resulting string will be "dcbaefd".

Return the resulting string.



Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".



Constraints:
    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.
"""


class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str

        easy 5min, convert string to list of char using list(string)
        thought: find an item and reverse part of the string.

        02/01/2022 16:29	Accepted	18 ms	13.7 MB	python
        """

        end = word.find(ch)
        if end == -1: return word

        i = 0
        ret = list(word)
        while i < end: #
            tmp = ret[i]
            ret[i] = ret[end]
            ret[end] = tmp
            i += 1
            end -=1

        return "".join(ret)


