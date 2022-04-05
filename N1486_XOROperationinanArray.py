#
# Create by Hua on 4/5/22.
#

"""
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.



Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.



Constraints:

    1 <= n <= 1000
    0 <= start <= 1000
    n == nums.length


"""


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int

        thought: simulate
        04/05/2022 10:07	Accepted	34 ms	13.4 MB	python
        easy 5 min. xor math.
        """

        a = [0]*n
        for i in range(n):
            a[i] = start + 2*i

        ret = 0
        for x in a:
            ret ^= x
        return ret
