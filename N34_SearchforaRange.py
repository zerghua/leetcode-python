#
#  Create by Hua on 9/2/2016
#


"""
 Given a sorted array of integers, find the starting and ending position of a given target value.

 Your algorithm's runtime complexity must be in the order of O(log n).

 If the target is not found in the array, return [-1, -1].

 For example,
 Given [5, 7, 7, 8, 8, 10] and target value 8,
 return [3, 4].


 I like this problem and solution, two recursive call inside equal condition.

"""

# 42 ms  81 / 81 test cases passed.
class Solution(object):
    def bs(self, ret, nums, target, left, right):
        if left>right: return

        mid = (right + left)/2  #python won't overflow
        if nums[mid] == target:
            if ret[0] == -1 or mid < ret[0]: ret[0] = mid
            if ret[1] == -1 or mid > ret[1]: ret[1] = mid
            self.bs(ret, nums, target, left, mid-1)
            self.bs(ret, nums, target, mid+1, right)
        elif nums[mid] < target:
            self.bs(ret, nums, target, mid + 1, right)
        else:
            self.bs(ret, nums, target, left, mid - 1)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1,-1]
        if nums is None: return ret
        self.bs(ret, nums,target, 0, len(nums)-1)
        return ret
