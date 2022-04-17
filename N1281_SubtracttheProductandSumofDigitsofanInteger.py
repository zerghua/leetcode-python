#
# Create by Hua on 4/16/22.
#

"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.



Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21



Constraints:

    1 <= n <= 10^5


"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int

        thought: convert number to list of digit.
        04/16/2022 15:55	Accepted	13 ms	13.3 MB	python
        easy 1 min.
        """
        p = 1
        s = 0
        for d in str(n):
            s += int(d)
            p = p * int(d)

        return p - s

