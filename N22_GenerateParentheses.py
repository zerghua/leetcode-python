#
#  Create by Hua on 8/31/2016
#


"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 For example, given n = 3, a solution set is:

 "((()))", "(()())", "(())()", "()(())", "()()()"

"""

# 64 ms
# DFS on number of left and right parentheses
class Solution(object):
    def dfs(self, ret, cur_str, left, right):
        if left<0 or right<0 or right < left: return   # right < left, important
        if left == 0 and right ==0:
            ret.append(cur_str)
            return

        self.dfs(ret, cur_str + "(", left - 1, right)
        self.dfs(ret, cur_str + ")", left, right - 1)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.dfs(ret, "", n, n)
        return ret