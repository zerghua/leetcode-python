#
# Create by Hua on 5/30/22.
#

"""
You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

    Horizontal movement means moving in either the left or right direction.
    Vertical movement means moving in either the up or down direction.



Example 1:

Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.

Example 2:

Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
Output: 0
Explanation: The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 105
    1 <= m * n <= 105
    1 <= grid[i][j] <= 1000


"""


class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        thought: to have trailing 0s of a product, need at least a number
        can be divided by 10 (like 10,20) or have n PAIR number can be divided
        by 5 (like 5,15) and an even number (like 2,4).

        hint:
        First, instead of multiplication, we just need to sum factors of
        2 and 5. Each pair of those factors produce one trailing zero.

        https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/discuss/1955607/Python-Explanation-with-pictures-prefix-sum.

        # adapted from
        https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/discuss/1955515/Prefix-Sum-of-Factors-2-and-5

        hard to code due to the multiple dimensions, and choose the
        appropriate data structure.

        05/30/2022 13:24	Accepted	7584 ms	109.5 MB	python
        medium - hard  2-3h
        use zip and sum like below:
            ret= max(ret, min([sum(x) for x in zip(row_left, col_top)]))
        will result TLE,

        """
        def factors(num, div):
            ret = 0
            while num != 0 and num % div == 0:
                ret += 1
                num /= div
            return ret

        m,n = len(grid), len(grid[0])

        # init 2d array contains a list with extra 1 length to simplify code
        row = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]
        col = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]

        # prefix of row and col for both 2 and 5
        for i in range(m):
            for j in range(n):
                v2 = factors(grid[i][j], 2)
                v5 = factors(grid[i][j], 5)
                row[i + 1][j][0] = row[i][j][0] + v2
                row[i + 1][j][1] = row[i][j][1] + v5
                col[i][j+1][0] = col[i][j][0] + v2
                col[i][j+1][1] = col[i][j][1] + v5

        ret = 0
        for i in range(m):
            for j in range(n):
                row_left = row[i+1][j]  # include point(i,j)
                row_right = row[m][j][0] - row[i][j][0], row[m][j][1] - row[i][j][1]  # include point(i,j)
                col_top = col[i][j]   # not include point(i,j)
                col_down = col[i][n][0] - col[i][j+1][0], col[i][n][1] - col[i][j+1][1]  # not include point(i,j)

                for x1,y1 in (row_left, row_right):
                    for x2,y2 in (col_top, col_down):
                        ret = max(ret, min(x1+x2, y1+y2))
        return ret
