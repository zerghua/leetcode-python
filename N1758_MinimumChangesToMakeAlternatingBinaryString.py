#
# Create by Hua on 3/24/22.
#

"""
You are given a string s consisting only of the characters '0' and '1'. In one
operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.



Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".



Constraints:
    1 <= s.length <= 104
    s[i] is either '0' or '1'.
"""


class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int

        thought: It will either be 0101... or 1010...
        03/24/2022 12:24	Accepted	49 ms	13.8 MB	python
        easy 5 min.
        can also go through s and check alternating digit.
        """
        n = len(s)
        if n <= 1:
            return 0

        x = "10" * (n/2)
        y = "01" * (n/2)
        if n%2 == 1:
            x += "1"
            y += "0"

        x_c = 0
        y_c = 0
        for i in range(n):
            if x[i] != s[i]:
                x_c += 1
            if y[i] != s[i]:
                y_c += 1

        return min(x_c, y_c)
