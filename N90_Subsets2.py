#
#  Create by Hua on 9/6/2016
#


"""
 Given a collection of integers that might contain duplicates, nums, return all possible subsets.

 Note: The solution set must not contain duplicate subsets.

 For example,
 If nums = [1,2,2], a solution is:

 [
     [2],
     [1],
     [1,2,2],
     [2,2],
     [1,2],
     []
 ]

"""

# 69 ms  19 / 19 test cases passed.
# DFS + backtracking. skip duplicate when i>start && nums[i-1] == nums[i]
class Solution(object):
    def dfs(self, ret, nums, cur_list, start):
        for i in range(start, len(nums)):
            if i>start and nums[i-1] == nums[i]: continue   # skip duplicate
            cur_list.append(nums[i])
            ret.append(list(cur_list))
            self.dfs(ret, nums, cur_list, i+1)
            cur_list.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        if nums is None or len(nums) ==0: return ret
        list.sort(nums)
        self.dfs(ret, nums, [], 0)
        return ret