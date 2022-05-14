#
# Create by Hua on 5/14/22.
#

"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.



Example 1:

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.

Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000



Constraints:

    3 <= points.length <= 50
    -50 <= xi, yi <= 50
    All the given points are unique.


"""


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float

        check out the solution here
        https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove

        easy-medium, need to figure out the formula.
        05/14/2022 16:00	Accepted	92 ms	13.6 MB	python
        30-40 min.
        """
        import itertools
        return max(0.5 * abs(
            i[0] * j[1] + j[0] * k[1] + k[0] * i[1] -
            j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
                   for i, j, k in itertools.combinations(points, 3))
