#
# Create by Hua on 5/2/22.
#

"""
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.



Example 1:

Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (0, 0) to other cells are: [0,1]

Example 2:

Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

Example 3:

Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].



Constraints:

    1 <= rows, cols <= 100
    0 <= rCenter < rows
    0 <= cCenter < cols


"""


class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]

        thought: sort value in dictionary
        05/02/2022 10:10	Accepted	263 ms	17.8 MB	python
        easy 5 - 10 min

        another sort:
        def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
            def dist(point):
                pi, pj = point
                return abs(pi - r0) + abs(pj - c0)

            points = [(i, j) for i in range(R) for j in range(C)]
            return sorted(points, key=dist)
        """
        dt = dict()
        for i in range(rows):
            for j in range(cols):
                d = abs(i - rCenter) + abs(j - cCenter)
                dt[(i,j)] = d

        r = sorted(dt.items(), key=lambda x: x[1]) # r is a 2d list
        return [x[0] for x in r]  # print first column of list

