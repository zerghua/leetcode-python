#
# Create by Hua on 5/16/22
#


"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.



Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99


Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?

"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool

        hint: Check whether each value is equal to the value of it's top-left neighbor.
        if a[i][j] == a[i-1][j-1] if i-1 and j-1 are valid

        05/16/2022 11:21	Accepted	161 ms	13.6 MB	python
        easy 5-10min

        for follow up question, dynamically replacing the used to new element of the next row.
        """
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i-1 >=0 and j-1 >=0:
                    if matrix[i][j] != matrix[i-1][j-1]: return False

        return True
