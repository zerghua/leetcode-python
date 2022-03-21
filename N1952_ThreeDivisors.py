#
# Create by Hua on 3/21/22.
#

"""
Given an integer n, return true if n has exactly three positive divisors.
Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.



Example 1:
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.



Constraints:

    1 <= n <= 10^4

"""


class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool

        thought: brute force, did not use significant math solution.
        easy 5min, but have some corner cases.
        03/21/2022 16:47	Accepted	16 ms	13.5 MB	python


        """
        count = 2
        for i in range(2, 1 + n/2):
            if n % i == 0:
                count += 1
            if count > 3: return False
        return count == 3


