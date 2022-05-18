#
# Create by Hua on 5/18/22
#


"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30

"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int

        thought: dp?
        a[n] = a[n-1] + a[n-2]
        05/18/2022 13:41	Accepted	32 ms	13.4 MB	python
        easy 1 min.
        """
        if n == 0: return 0
        a = [0] * (n+1)
        a[1] = 1
        for i in range(2, n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]
