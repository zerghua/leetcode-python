#
#  Create by Hua on 8/30/2016
#


"""
 Given an array S of n integers, find three integers in S such that the sum is closest to a given number,target.
 Return the sum of the three integers. You may assume that each input would have exactly one solution.

 For example, given array S = {-1 2 1 -4}, and target = 1.

 The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

# 312 ms
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        list.sort(nums)
        n = len(nums)
        min_diff = sys.maxint
        ret = 0

        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three == target: return target
                elif sum_of_three > target : right -= 1
                else: left += 1

                diff = abs(target - sum_of_three)
                if diff < min_diff:
                    min_diff = diff
                    ret = sum_of_three

        return ret


# 180 ms
# less code.
class Solution2(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        list.sort(nums)
        n = len(nums)
        ret = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three == target: return target
                elif sum_of_three > target : right -= 1
                else: left += 1

                ret = sum_of_three if abs(target - sum_of_three) < abs(target - ret) else ret
        return ret


# optimization with skip duplicate
# 196 ms, well it seems not really optimized, the timing actually varies different runs.
class Solution3(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        list.sort(nums)
        n = len(nums)
        ret = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three == target: return target
                elif sum_of_three > target :
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: left += 1

                ret = sum_of_three if abs(target - sum_of_three) < abs(target - ret) else ret
        return ret