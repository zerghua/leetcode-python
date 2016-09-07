#
# Created by Hua on 9/7/2016
#

"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
"""

# 52 ms 22 / 22 test cases passed.
# 4 sides(top, bottom, left and right). ++ or --
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if matrix is None or len(matrix) == 0: return ret
        top = left =0
        bottom = len(matrix)-1
        right = len(matrix[0])-1

        while left<=right or top <=bottom:
            # top side
            if top<= bottom:
                for i in range(left, right+1):
                    ret.append(matrix[top][i])
                top += 1

            # right side
            if left<=right:
                for i in range(top, bottom+1):
                    ret.append(matrix[i][right])
                right -= 1

            # bottom side
            if top <= bottom:
                for i in range(right, left-1, -1):
                    ret.append(matrix[bottom][i])
                bottom -= 1

            # left side
            if left<=right:
                for i in range(bottom, top-1, -1):
                    ret.append(matrix[i][left])
                left += 1

        return ret