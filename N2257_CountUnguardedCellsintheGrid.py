#
# Create by Hua on 5/29/22.
#

"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.



Example 1:

Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

Example 2:

Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.



Constraints:

    1 <= m, n <= 105
    2 <= m * n <= 105
    1 <= guards.length, walls.length <= 5 * 104
    2 <= guards.length + walls.length <= m * n
    guards[i].length == walls[j].length == 2
    0 <= rowi, rowj < m
    0 <= coli, colj < n
    All the positions in guards and walls are unique.


"""


class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int

        thought: simulate the grid, for each guard, go four directions,
        and mark them. go through the grid again, to count all
        the unguarded cells.

        0 is unguarded, 1 is guarded cell, 2 is guards and wall

        05/29/2022 12:03	Accepted	2792 ms	45.1 MB	python
        medium 30-40 min.
        had a corner case(TLE):
        need to set both wall and guards first. initial solution
        only set wall, didn't set guard, then will TLE.
        """
        '''
            grid = list()
            for i in range(m):
                grid.append([0] * n)
        '''
        grid = [[0] * n for i in range(m)]
        for i,j in walls+guards:   # set wall and guards
            grid[i][j] = 2

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i,j in guards:  # go through guards
            for x,y in directions:
                a,b = i+x, j+y
                while 0 <= a < m and 0 <= b < n and grid[a][b] != 2:
                    grid[a][b] = 1
                    a += x
                    b += y

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ret += 1
        return ret






