#
# Created by Hua on 9/6/2016
#

"""
 You are given an n x n 2D matrix representing an image.

 Rotate the image by 90 degrees (clockwise).

 Follow up:
 Could you do this in-place?

 this one needs analyze and code.
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
"""


# in place, 4-way rotation
# 72 ms  20 / 20 test cases passed.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n / 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]   # the the first row == the second col
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp


# 55ms  20 / 20 test cases passed.
# first reverse up and down, and then transpose it.
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]