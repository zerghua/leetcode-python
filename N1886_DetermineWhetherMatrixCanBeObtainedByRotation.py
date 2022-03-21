#
# Create by Hua on 3/21/22.
#

"""
Given two n x n binary matrices mat and target, return true if it is possible
to make mat equal to target by rotating mat in 90-degree increments,
or false otherwise.


Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.


Constraints:
    n == mat.length == target.length
    n == mat[i].length == target[i].length
    1 <= n <= 10
    mat[i][j] and target[i][j] are either 0 or 1.

    0 0 0                   1 0 0
    0 1 0                   1 1 0
    1 1 1                   1 0 0
    (0,0) (0,1) (0,2)       (2,0) (1,0) (0,0)
    (1,0) (1,1) (1,2)       (2,1) (1,1) (0,1)
    (2,0) (2,1) (2,2)       (2,2) (1,2) (0,2)
"""


class Solution(object):
    # rotate 90 degree, core, takes time to figure this out.
    def rotate(self, mat):
        ret = list()
        n = len(mat)
        for i in range(n):
            lis = list()
            for j in range(n-1, -1, -1):
                lis.append(mat[j][i])
            ret.append(lis)
        return ret

    def is_same_list(self, m1, m2):
        n = len(m1)
        for i in range(n):
            for j in range(n):
                if m1[i][j] != m2[i][j]:
                    return False
        return True


    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool

        thought: at most rotate 3 times, create a function to rotate matrix
        and check with target

        medium 30-40 min, need to find out the formula to rotate matrix

        medium, long code, corner cases.

        03/21/2022 19:55	Accepted	31 ms	13.6 MB	python
        """

        if self.is_same_list(mat, target):
            return True

        for i in range(3):
            mat = self.rotate(mat)
            if self.is_same_list(mat, target):
                return True
        return False





