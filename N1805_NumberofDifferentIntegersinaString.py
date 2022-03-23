#
# Create by Hua on 3/23/22.
#

"""
You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example,
"a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with
some integers that are separated by at least one space: "123", "34", "8", and "34".

Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without
any leading zeros are different.



Example 1:
Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

Example 2:
Input: word = "leet1234code234"
Output: 2

Example 3:
Input: word = "a1b01c001"
Output: 1
Explanation: The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.



Constraints:
    1 <= word.length <= 1000
    word consists of digits and lowercase English letters.
"""


class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int

        thought: replace chars to space, and split remaining into numbers,
        and put them into set. pay attention to leading zeros.

        03/23/2022 14:44	Accepted	27 ms	13.8 MB	python
        easy 10min, string replace function and ascii lowercase set.
        """

        import string
        for c in string.ascii_lowercase:
            word = word.replace(c, " ")

        st = set()
        for s in word.split():
            st.add(int(s))

        return len(st)
