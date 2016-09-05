#
# Create by Hua on 9/5/16.
#

"""
 Given a collection of numbers, return all possible permutations.

 For example,
 [1,2,3] have the following permutations:
 [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""


# 63 ms  25 / 25 test cases passed.
# DFS + backtracking, use boolean array to store visited node.
class Solution(object):
    def dfs(self, ret, nums, cur_list, used):
        if len(cur_list) == len(nums):
            ret.append(list(cur_list))
            return

        for i in range(len(nums)):
            if used[i]: continue

            used[i] = True
            cur_list.append(nums[i])
            self.dfs(ret, nums, cur_list, used)
            used[i] = False
            cur_list.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums is None or len(nums) == 0: return ret
        self.dfs(ret, nums, [], [False]*len(nums))
        return ret
