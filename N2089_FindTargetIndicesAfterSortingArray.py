#
#  Create by Hua on 1/29/2022
#

"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target
indices, return an empty list. The returned list must be sorted in increasing order.



Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.


Constraints:

    1 <= nums.length <= 100
    1 <= nums[i], target <= 100

"""


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        easy: 1 min

        thought: sort array and loop through list, compare value with target, and return the matched index in a list,
        can break once value > target

        01/29/2022 15:03	Accepted	54 ms	13.3 MB	python
        """

        sorted_num = sorted(nums)
        ret = list()
        for i in range(len(nums)):
            if sorted_num[i] == target:
                ret.append(i)
            elif sorted_num[i] > target:
                break

        return ret
