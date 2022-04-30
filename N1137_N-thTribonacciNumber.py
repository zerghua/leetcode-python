#
# Create by Hua on 4/30/22.
#

"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537



Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int

        thought: maintain a 38 size array

        04/30/2022 11:36	Accepted	17 ms	13.4 MB	python
        easy 5 min.
        """
        a=[0] * 38
        a[1], a[2] = 1, 1
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]

        return a[n]