#
# Created by Hua on 9/6/2016
#

"""
Implement pow(x, n).
"""


# iterative solution
# 35 ms  300 / 300 test cases passed.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        abs_n = abs(n)
        ret = 1
        while abs_n > 0:
            if (abs_n & 1) == 1: ret *= x
            abs_n >>= 1
            x *= x
        return ret if n > 0 else 1 / ret


# recursive
# 42 ms  300 / 300 test cases passed.
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        ret = self.myPow(x, n / 2)
        return ret * ret if n % 2 == 0 else ret * ret * x
