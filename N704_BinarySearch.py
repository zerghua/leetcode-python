#
# Create by Hua on 5/18/22
#


"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        thought: bisect, return the insert index.
        05/18/2022 10:07	Accepted	353 ms	14.6 MB	python
        easy 5-10 min. binary search
        """
        import bisect
        i = bisect.bisect_left(nums, target)  # will return the insert pos
        if i == len(nums) or nums[i] != target: return -1
        return i