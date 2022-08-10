#
# Create by Hua on 8/10/22
#

"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0

"""


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int

        company: google high frequency
        thought: bfs with pruning. (x,y,r), r is remaining obstacles we can remove.
        08/10/2022 10:40	Accepted	912 ms	22.3 MB	python
        hard - medium
        BFS.
        40-60 min.

        """

        m,n = len(grid), len(grid[0])
        lt = [(0,0,k)]
        visited = set()
        ret = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while(lt):
            tmp = set()
            for x,y,r in lt:
                visited.add((x,y,r))
                if x == m-1 and y == n-1:
                    return ret
                for a,b in dirs:
                    nx, ny = x+a, y+b
                    if 0 <= nx < m and 0<= ny < n:
                        if grid[nx][ny] == 0 and (nx,ny,r) not in visited:
                            tmp.add((nx,ny,r))
                        elif grid[nx][ny] == 1 and r > 0 and (nx,ny,r-1) not in visited:
                            tmp.add((nx,ny,r-1))
            ret += 1
            lt = list(tmp)
        return -1

