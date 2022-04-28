#
# Create by Hua on 4/28/22.
#

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false



Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.

"""
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool

        thought: math, calculate the (y1-y0)/(x1-x0) ratio,
        check if they are equal.

        corner cases, points in x or y-axis

        https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/JavaPython-3-check-slopes-short-code-w-explanation-and-analysis.
        better math, 3 points in a line: (y1-y)/(x1-x) = (y0-y)/(x0-x)
        to avoid div 0 error, convert above formula to ->
        (x0-x)*(y1-y) = (y0-y)*(x1-x)

        04/28/2022 12:01	Accepted	43 ms	14.1 MB	python
        easy-medium 10-20min. not very easy to come up with the correct
        formula
        """

        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates:
            if (x0-x)*(y1-y) != (y0-y)*(x1-x):
                return False
        return True

