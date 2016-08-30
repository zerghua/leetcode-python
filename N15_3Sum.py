#
#  Create by Hua on 8/30/2016
#

"""
 Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
 Find all unique triplets in the array which gives the sum of zero.

 Note: The solution set must not contain duplicate triplets.

 For example, given array S = [-1, 0, 1, 2, -1, -4],

 A solution set is:
 [
     [-1, 0, 1],
     [-1, -1, 2]
 ]

"""

# 217 ms
# sort + two pointers to make o(n^3) brute force to o(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        if n < 3: return ret

        list.sort(nums)   # or nums.sort()  sort list
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]: continue  # skip duplicate

            left = i+1
            right = n-1
            while left<right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicate
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif sum_of_three > 0: right -=1
                else: left += 1

        return ret