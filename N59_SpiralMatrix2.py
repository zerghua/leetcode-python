#
# Created by Hua on 9/7/2016
#

"""
Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

# 38 ms  21 / 21 test cases passed.
# very similar to Spiral Matrix 54, 4 sides of 4 loops.
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0] * n for i in range(n)]
        if n<1: return ret
        num = 1
        top = left = 0
        right = bottom = n-1
        while num<= n*n:
            # top
            for i in range(left, right+1):
                ret[top][i] = num
                num += 1
            top += 1

            # right
            for i in range(top, bottom+1):
                ret[i][right] = num
                num += 1
            right -= 1

            # bottom
            for i in range(right, left-1, -1):
                ret[bottom][i] = num
                num += 1
            bottom -= 1

            # left
            for i in range(bottom, top-1, -1):
                ret[i][left] = num
                num += 1
            left += 1

        return ret
