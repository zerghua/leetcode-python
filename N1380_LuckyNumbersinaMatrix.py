#
# Create by Hua on 4/7/22.
#

"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.



Constraints:

    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 105.
    All elements in the matrix are distinct.


"""


class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        thought: find out the min in each row, and max in each column, and save
        them. go through the matrix to match the criteria

        04/07/2022 09:57	Accepted	128 ms	13.8 MB	python
        easy 5-10 min. corner cases on list initialization
        """

        m = len(matrix)
        n = len(matrix[0])
        row = [10**6]*m
        col = [0]*n
        for i in range(m):
            for j in range(n):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])

        ret = list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row[i] and matrix[i][j] == col[j]:
                    ret.append(matrix[i][j])

        return ret