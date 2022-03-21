#
# Create by Hua on 3/21/22.
#

"""
There is a malfunctioning keyboard where some letter keys do not work.
All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or
trailing spaces) and a string brokenLetters of all distinct letter keys that
are broken, return the number of words in text you can fully type
using this keyboard.



Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.



Constraints:
    1 <= text.length <= 104
    0 <= brokenLetters.length <= 26
    text consists of words separated by a single space without any leading or trailing spaces.
    Each word only consists of lowercase English letters.
    brokenLetters consists of distinct lowercase English letters.
"""


class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int

        thought: brute force to check each string for chars.

        03/21/2022 17:16	Accepted	44 ms	13.6 MB	python

        easy 5 min.
        """

        ret = 0
        for word in text.split():
            is_ok = True
            for c in brokenLetters:
                if c in word:
                    is_ok = False
                    break

            if is_ok:
                ret += 1

        return ret
