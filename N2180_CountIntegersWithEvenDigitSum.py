#
# Create by Hua on 5/21/22.
#

"""
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.



Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.

Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.



Constraints:

    1 <= num <= 1000


"""


class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int

        thought: check each number's digit sum
        05/21/2022 11:04	Accepted	58 ms	13.6 MB	python
        easy 2 min.
        """
        ret = 0
        for i in range(2, num+1):
            total = sum([int(x) for x in str(i)])
            if total % 2 == 0:
                ret += 1
        return ret

