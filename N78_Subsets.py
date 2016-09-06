#
#  Create by Hua on 9/6/2016
#


"""
 Given a set of distinct integers, nums, return all possible subsets.

 Note: The solution set must not contain duplicate subsets.

 For example,
 If nums = [1,2,3], a solution is:

 [
     [3],
     [1],
     [2],
     [1,2,3],
     [1,3],
     [2,3],
     [1,2],
     []
 ]

"""

# 75 ms  10 / 10 test cases passed.
# DFS + backtracking.
class Solution(object):
    def dfs(self, ret, nums, cur_list, start):
        for i in range(start, len(nums)):
            cur_list.append(nums[i])
            ret.append(list(cur_list))
            self.dfs(ret, nums, cur_list, i+1)
            cur_list.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        if nums is None or len(nums)== 0: return ret
        self.dfs(ret, nums, [], 0)
        return ret
