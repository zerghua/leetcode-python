#
# Create by Hua on 3/23/22.
#

"""
A pangram is a sentence where every letter of the English alphabet
appears at least once.

Given a string sentence containing only lowercase English letters, return
true if sentence is a pangram, or false otherwise.



Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false



Constraints:
    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.
"""


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool

        thought: put each char into a set to check if len of set is 26.
        03/23/2022 13:10	Accepted	32 ms	13.6 MB	python
        easy 1 min. set.
        """

        st = set()
        for c in sentence:
            st.add(c)

        return len(st) == 26

