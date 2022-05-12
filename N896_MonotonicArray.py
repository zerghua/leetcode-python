#
# Create by Hua on 5/12/22
#


"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        thought: o(n), 2 times loop
        05/12/2022 10:35	Accepted	805 ms	24.8 MB	python
        easy 5min.
        """

        n = len(nums)
        find_invalid = False
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                find_invalid = True
                break
        if not find_invalid: return True

        find_invalid = False
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                find_invalid = True
                break
        if not find_invalid: return True

        return False