#
# Create by Hua on 3/23/22.
#

"""
Given an integer array nums (0-indexed) and two integers target and start,
find an index i such that nums[i] == target and abs(i - start) is minimized.
Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.



Example 1:
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

Example 2:
Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

Example 3:
Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.



Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^4
    0 <= start < nums.length
    target is in nums.
"""

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int

        thought: no need to micro-optimize the solution(because it's still o(n))
        solution, go through the list find the num[i] == target and calculate
        the abs(i-start), find the min.

        03/23/2022 11:07	Accepted	84 ms	13.7 MB	python

        easy 5 min.
        """

        ret = 10**5
        for i in range(len(nums)):
            if nums[i] == target:
                ret = min(ret, abs(i-start))

        return ret
