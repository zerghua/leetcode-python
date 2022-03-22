#
# Create by Hua on 3/22/22.
#

"""
The letter value of a letter is its position in the alphabet starting
from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the
concatenation of the letter values of each letter in s, which is then
converted into an integer.

    For example, if s = "acb", we concatenate each letter's letter value,
    resulting in "021". After converting it, we get 21.

You are given three strings firstWord, secondWord, and targetWord, each
consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and
secondWord equals the numerical value of targetWord, or false otherwise.



Example 1:

Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation:
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation:
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.



Constraints:
    1 <= firstWord.length, secondWord.length, targetWord.length <= 8
    firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.
"""


class Solution(object):
    def convertToInt(self, str):
        times = 0
        ret = 0
        for s in str[::-1]:  # iterate through right to left
            i = int(ord(s) - ord('a')) * (10**times)
            times += 1
            ret += i
        return ret


    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool

        thought: only 0-9 digits given(a-j), convert string to int, and check
        03/22/2022 09:48	Accepted	32 ms	13.3 MB	python
        easy 5 min.
        """
        return self.convertToInt(firstWord) + self.convertToInt(secondWord) == self.convertToInt(targetWord)

