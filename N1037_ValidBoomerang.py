#
# Create by Hua on 5/2/22.
#

"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.



Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false



Constraints:

    points.length == 3
    points[i].length == 2
    0 <= xi, yi <= 100


"""


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool

        thought: math
        (y2-y0)/(x2-x0) != (y1-y0)/(x1-x0)  ->

        (y2-y0) * (x1-x0) != (y1-y0) * (x2-x0)
        05/02/2022 09:56	Accepted	25 ms	13.2 MB	python
        easy 5 min.
        """
        p2 = points[2]
        p1 = points[1]
        p0 = points[0]
        a = (p2[1] - p0[1]) * (p1[0] - p0[0])
        b = (p1[1] - p0[1]) * (p2[0] - p0[0])
        return a != b

