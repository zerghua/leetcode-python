#
# Create by Hua on 5/13/22
#


"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.





Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

"""


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        thought: matrix operation, get cols
        05/13/2022 10:38	Accepted	60 ms	14.5 MB	python
        easy 5 min.
        """

        m, n  = len(matrix), len(matrix[0])
        ret = list()
        for i in range(n):
            col = [r[i] for r in matrix]  # get col
            ret.append(col)
        return ret