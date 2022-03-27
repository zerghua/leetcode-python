#
# Create by Hua on 3/27/22.
#

"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.



Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".



Constraints:

    1 <= sequence.length <= 100
    1 <= word.length <= 100
    sequence and word contains only lowercase English letters.


"""


class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int

        thought: build string and compare if it's substring.
        03/27/2022 14:03	Accepted	12 ms	13.7 MB	python
        easy 5 min. string.
        """

        n = len(word)
        s = word * (len(sequence) / n)
        while len(s) > 0:
            if s in sequence:
                return len(s) / n
            else:
                s = s[:len(s) - n]

        return 0