#
#  Create by Hua on 9/6/2016
#


"""
 Given a string s, partition s such that every substring of the partition is a palindrome.

 Return all possible palindrome partitioning of s.

 For example, given s = "aab",
 Return

 [
     ["aa","b"],
     ["a","a","b"]
 ]


"""

# 102 ms  22 / 22 test cases passed.
# DFS + backtracking + DP. see the classic way to pre-check palindrome of all sub strings.
class Solution(object):
    def dfs(self, ret, s, isPal, cur_list, start):
        n = len(s)
        if start == n:
            ret.append(list(cur_list))
            return

        for i in range(start, n):
            if isPal[start][i]:
                cur_list.append(s[start:i+1])
                self.dfs(ret, s, isPal, cur_list, i+1)
                cur_list.pop()


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # pre-check palindrome for all substrings.
        n = len(s)
        isPal = [[False]*n for i in range(n)]
        for j in range(n):
            for i in range(0,j+1):
                if s[i] == s[j] and (j-i<=1 or isPal[i+1][j-1]): isPal[i][j] = True

        ret = []
        self.dfs(ret, s, isPal, [], 0)
        return ret