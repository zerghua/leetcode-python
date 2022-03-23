#
# Create by Hua on 3/23/22.
#

"""
Given an integer n (in base 10) and a base k, return the sum of the digits
of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number,
and the sum should be returned in base 10.



Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

Example 2:
Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.



Constraints:
    1 <= n <= 100
    2 <= k <= 10
"""


class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int

        thought: to convert number N base 10 to other base x, just get
        remainder of N/x, and add them from right to left until remainder
        becomes 0

        03/23/2022 11:44	Accepted	16 ms	13.5 MB	python
        easy, 5min, pure math.
        """
        ret = 0
        while n != 0:
            ret += n%k
            n = n/k
        return ret
