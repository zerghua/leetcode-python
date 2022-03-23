#
# Create by Hua on 3/23/22.
#

"""
You are given an integer array nums (0-indexed). In one operation, you can
choose an element of the array and increment it by 1.

    For example, if nums = [1,2,3], you can choose to increment nums[1]
    to make nums = [1,3,3].

Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all
0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.



Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
Input: nums = [1,5,2,4,1]
Output: 14

Example 3:
Input: nums = [8]
Output: 0



Constraints:
    1 <= nums.length <= 5000
    1 <= nums[i] <= 104
"""


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: since it can only do increment, so it's easy.
        for each number, make sure it's one more than it's previous.

        03/23/2022 13:18	Accepted	159 ms	14.1 MB	python
        easy 5 min. figure out the formula.
        """
        n = len(nums)
        ret = 0
        if n <= 1: return 0
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                ret += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1

        return ret