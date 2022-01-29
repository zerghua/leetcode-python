#
#  Create by Hua on 1/29/2022
#

"""
Reversing an integer means to reverse all its digits.

    For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.

Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if
reversed2 equals num. Otherwise return false.



Example 1:
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.


Constraints:

    0 <= num <= 10^6

"""


class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool

        easy 2 min

        thought: if 0 return true; if last digit is 0, return false, else return true

        01/29/2022 10:59	Accepted	28 ms	13.4 MB	python
        """

        if num == 0: return True
        s = str(num)
        if s[-1] == '0': return False
        return True


