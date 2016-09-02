#
#  Create by Hua on 9/2/2016
#


"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 --> 2
[1,3,5,6], 2 --> 1
[1,3,5,6], 7 --> 4
[1,3,5,6], 0 --> 0

"""


# return left if want insert index
# 44 ms  62 / 62 test cases passed.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left