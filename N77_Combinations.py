#
#  Create by Hua on 9/6/2016
#


"""
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

 For example,
 If n = 4 and k = 2, a solution is:

 [
     [2,4],
     [3,4],
     [2,3],
     [1,2],
     [1,3],
     [1,4],
 ]


"""

# 895 ms   27 / 27 test cases passed.
# DFS + backtracking. similar to permutation and subset problem.
class Solution(object):
    def dfs(self, ret, n, k, cur_list, start):
        if len(cur_list) == k:
            ret.append(list(cur_list))
            return

        for i in range(start, n+1):
            cur_list.append(i)
            self.dfs(ret, n, k, cur_list, i+1)
            cur_list.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(ret, n, k, [], 1)
        return ret


# 185 ms 27 / 27 test cases passed.
# use lib
from itertools import combinations
class Solution2(object):
    def combine(self, n, k):
        return list(combinations(range(1,n+1), k))
