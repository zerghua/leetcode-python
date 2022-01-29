#
#  Create by Hua on 1/29/2022
#

"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before
every 'b' in the string. Otherwise, return false.


Example 1:
Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

Example 2:
Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

Example 3:
Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.



Constraints:

    1 <= s.length <= 100
    s[i] is either 'a' or 'b'.

"""


class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool

        easy: 2 min

        thought: go through the string, record found_b, if found a and found_b is true, return false, else return true.

        01/29/2022 10:44	Accepted	14 ms	13.3 MB	python
        """

        is_found_b=False
        for c in s:
            if c == 'b': is_found_b = True
            elif c == 'a':
                if is_found_b: return False
        return True
