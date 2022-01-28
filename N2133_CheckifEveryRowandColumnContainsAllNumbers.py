#
#  Create by Hua on 1/28/2022
#

"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.



Example 1:

Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Example 2:

Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.



Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    1 <= matrix[i][j] <= n

"""


class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool

        easy: 10-15min, delayed on loop matrix and missing a corner case.

        thoughts 1: if n is not too big to overflow, let's sum(1,n), compare with each row and column. return true if
        all equals, else false. (it has corner case: [2,2,2],[2,2,2],[2,2,2])

        thoughts 2: for each row and col, keep them in the set, compare the set size and sum of set.

        01/28/2022 15:01	Accepted	1002 ms	13.8 MB	python(thought 2)
        """
        n = len(matrix)
        total = sum(range(n+1))

        for i in range(n):
            # check row
            lis= set()
            t = 0
            for j in range(n):
                t += matrix[i][j]
                lis.add(matrix[i][j])
            if t != total or len(lis) != n: return False

            # check col
            t = 0
            lis = set()
            for j in range(n):
                t += matrix[j][i]
                lis.add(matrix[j][i])
            if t != total or len(lis) != n: return False
        return True
