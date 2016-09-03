#
# Created by Hua on 9/3/2016
#

"""
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C
 where the candidate numbers sums to T.

 The same repeated number may be chosen from C unlimited number of times.

 Note:

 All numbers (including target) will be positive integers.
 The solution set must not contain duplicate combinations.

 For example, given candidate set [2, 3, 6, 7] and target 7,
 A solution set is:

 [
     [7],
     [2, 2, 3]
 ]
"""

# 75 ms   168 / 168 test cases passed.
# DFS and backtracking.
class Solution(object):
    def dfs(self, candicates, target, ret, cur_list, start):
        if target == 0:
            ret.append(list(cur_list))
            return

        for i in range(start, len(candicates)):
            if candicates[i] > target: return
            if i>start and candicates[i] == candicates[i-1]: continue
            cur_list.append(candicates[i])
            self.dfs(candicates,target - candicates[i], ret, cur_list, i)
            cur_list.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list.sort(candidates)
        ret = []
        self.dfs(candidates, target, ret, [], 0)
        return ret

