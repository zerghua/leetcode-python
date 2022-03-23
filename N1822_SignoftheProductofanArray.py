#
# Create by Hua on 3/23/22.
#

"""
There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of
all values in the array nums.

Return signFunc(product).



Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1



Constraints:
    1 <= nums.length <= 1000
    -100 <= nums[i] <= 100
"""


class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: calculate the number of negative numbers, if there is zero,
        then zero.

        03/23/2022 13:23	Accepted	53 ms	13.4 MB	python
        easy 1 min. pure math.
        """
        count = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                count += 1

        if count % 2 == 0:
            return 1
        else:
            return -1
