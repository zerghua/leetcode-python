#
# Create by Hua on 3/24/22.
#

"""
You are given two strings s1 and s2 of equal length. A string swap is an
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.



Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.



Constraints:
    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.
"""


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        thought: check the non-equal positions, should be 0 or 2. further the
        non-equal position should have the same chars(use set to check).
        03/24/2022 10:57	Accepted	20 ms	13.5 MB	python
        easy 10-20 min. missed on corner cases. do not initiate 2 lists like
        lt1 = lt2 = list(), they will have the same content.
        """

        lt1 = list()
        lt2 = list()
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                lt1.append(s1[i])
                lt2.append(s2[i])

        if len(lt1) == 0 or len(lt1) == 2:
            return set(lt1) == set(lt2)

        return False