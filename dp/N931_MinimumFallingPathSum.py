#
# Create by Hua on 9/15/22
#

"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).



Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

"""


class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        
        thought: dp, to check top, top left and top right.

        09/15/2022 10:12	Accepted	200 ms	14.4 MB	python

        """
        
        n = len(matrix)
        pre, cur = [0] * n, [0] * n
        for i in range(n):
            for j in range(n):
                cur[j] = matrix[i][j]
                if j == 0:
                    cur[j] += min(pre[j], pre[j + 1] if j+1<n else 101)  # max of m[i][j] == 100
                elif j == n-1:
                    cur[j] += min(pre[j - 1], pre[j])
                else:
                    cur[j] += min(pre[j - 1], pre[j], pre[j + 1])
            pre = cur[:]  # copy data
        return min(pre)
