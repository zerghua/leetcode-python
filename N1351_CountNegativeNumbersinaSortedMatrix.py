#
# Create by Hua on 4/7/22.
#

"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?
"""


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        +++++-
        ++++--
        ++----
        +-----

        check from left bottom
        04/07/2022 15:10	Accepted	163 ms	14.5 MB	python
        easy 5-10 min.
        """
        m = len(grid)
        n = len(grid[0])
        r = m - 1
        c = 0
        ret = 0
        while r >=0 and c < n:
            if grid[r][c] < 0:
                ret += n - c
                r -= 1
            else:
                c += 1
        return ret


