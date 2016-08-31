#
# Created by Hua on 8/30/2016
#

"""
 Given an array S of n integers, are there elements a, b, c, and d
 in S such that a + b + c + d = target? Find all unique quadruplets
 in the array which gives the sum of target.

 Note: The solution set must not contain duplicate quadruplets.

 For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

 A solution set is:
 [
     [-1,  0, 0, 1],
     [-2, -1, 1, 2],
     [-2,  0, 0, 2]
 ]

"""

# 236 ms, has to put k==2 inside the same function, if in separate def, will TLE.
class Solution(object):
    def ksum(self, nums, target, k, cur_list, ret, left, right):
        if k == 2:
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    ret.append(cur_list + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1

                elif cur_sum > target:
                    right -= 1
                else:
                    left += 1

        for i in range(left, right):
            if target < nums[left]*k or target > nums[right]*k : break;  # optimize for a corner case.
            if i > left and nums[i] == nums[i-1]: continue
            self.ksum(nums, target-nums[i], k-1, cur_list + [nums[i]], ret, i+1, right)


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = []
        n = len(nums)
        if  n < 4: return ret
        list.sort(nums)
        self.ksum(nums, target, 4, [], ret, 0, n-1)
        return ret

