#
# Create by Hua on 9/20/22
#

"""
You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.



Example 1:


Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column
Example 2:


Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1's from grid.
Example 3:


Input: grid = [[0]]
Output: true
Explanation: There are no 1's in grid.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is either 0 or 1.

"""


class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool

        thought: not easy to come up the solution by myself, but it's pretty easy to understand once know the answer.
        the pattern for each row needs to be the same or the inverted version, or it won't be true.
        001100 and 001100  ok
        001100 and 110011  ok

        https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation

        09/20/2022 14:54	Accepted	1034 ms	15.8 MB	python
        medium
        google.
        math.
        """
        r1, r1v = grid[0], [1-v for v in grid[0]]  # r1v is the inverted version, e.g r1=010, r1v=101

        # check each row should be the same or inverted as first row
        for i in range(1, len(grid)):
            if grid[i] != r1 and grid[i] != r1v:
                return False
        return True