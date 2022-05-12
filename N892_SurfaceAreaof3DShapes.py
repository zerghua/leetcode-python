#
# Create by Hua on 5/12/22
#


"""
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.



Example 1:


Input: grid = [[1,2],[3,4]]
Output: 34
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 3:


Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Constraints:

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50

"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        thought:
        https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/163414/C%2B%2BJava1-line-Python-Minus-Hidden-Area

        didn't work out the formula:
            For each tower, its surface area is 4 * v + 2
            However, 2 adjacent tower will hide the area of connected part.
            The hidden part is min(v1, v2) and we need just minus this area * 2

        05/12/2022 11:55	Accepted	104 ms	13.3 MB	python
        easy - medium. 30-40 min.
        """

        ret = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0: ret += 4*grid[i][j] + 2
                if i>0: ret -= min(grid[i][j], grid[i-1][j])*2  # top
                if j>0: ret -= min(grid[i][j], grid[i][j-1])*2  # left
        return ret