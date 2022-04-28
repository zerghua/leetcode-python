#
# Create by Hua on 4/28/22.
#

"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".



Constraints:

    1 <= s.length <= 1000
    s[i] is either 'L' or 'R'.
    s is a balanced string.


"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int

        thought: maintain a counter, encounter L, then ++, encounter R
        then --, ret++ when count == 0

        04/28/2022 12:09	Accepted	22 ms	13.5 MB	python
        easy 5min.
        """
        counter = 0
        ret = 0
        for c in s:
            if c == 'L':
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                ret += 1

        return ret