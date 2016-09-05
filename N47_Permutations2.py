#
# Create by Hua on 9/5/16.
#

"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

 For example,
 [1,1,2] have the following unique permutations:

 [
     [1,1,2],
     [1,2,1],
     [2,1,1]
 ]
"""

# 145 ms  30 / 30 test cases passed.
# DFS + backtracking used boolean array to store visited node.
# can also use binary search to skip duplicate
class Solution(object):
    def dfs(self, ret, nums, cur_list, used):
        if len(nums) == len(cur_list):
            ret.append(list(cur_list))
            return

        for i in range(len(nums)):
            if used[i]: continue
            if i>0 and nums[i-1] == nums[i] and not used[i-1]: continue  # skip duplicate
            used[i] = True
            cur_list.append(nums[i])
            self.dfs(ret, nums, cur_list, used)
            used[i] = False
            cur_list.pop()


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums is None or len(nums) == 0: return ret
        list.sort(nums)
        self.dfs(ret, nums, [], [False]*len(nums))
        return ret