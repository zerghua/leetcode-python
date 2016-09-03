#
# Created by Hua on 9/3/2016
#

"""
 Given a collection of candidate numbers (C) and a target number (T),
 find all unique combinations in C where the candidate numbers sums to T.

 Each number in C may only be used once in the combination.

 Note:

 All numbers (including target) will be positive integers.
 The solution set must not contain duplicate combinations.

 For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
 A solution set is:

 [
     [1, 7],
     [1, 2, 5],
     [2, 6],
     [1, 1, 6]
 ]
"""

# 72 ms  172 / 172 test cases passed.
# DFS and backtracking. similar to N40. only diff is i vs i+1(each num use once)
class Solution(object):
    def dfs(self, candicates, target, ret, cur_list, start):
        if target == 0 :
            ret.append(list(cur_list))
            return

        for i in range(start, len(candicates)):
            if i> start and candicates[i] == candicates[i-1]: continue # skip duplicate
            if candicates[i] > target: return
            cur_list.append(candicates[i])
            self.dfs(candicates,target-candicates[i],ret, cur_list, i+1) # each num use once
            cur_list.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list.sort(candidates)
        ret = []
        self.dfs(candidates, target, ret, [], 0)
        return ret
