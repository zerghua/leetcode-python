#
# Create by Hua on 5/29/22.
#

"""
You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that lie on the edges of a rectangle are also considered to be contained by that rectangle.



Example 1:

Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
Output: [2,1]
Explanation:
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].

Example 2:

Input: rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
Output: [1,3]
Explanation:
The first rectangle contains only the point (1, 1).
The second rectangle contains only the point (1, 1).
The third rectangle contains the points (1, 3) and (1, 1).
The number of rectangles that contain the point (1, 3) is 1.
The number of rectangles that contain the point (1, 1) is 3.
Therefore, we return [1, 3].



Constraints:

    1 <= rectangles.length, points.length <= 5 * 104
    rectangles[i].length == points[j].length == 2
    1 <= li, xj <= 109
    1 <= hi, yj <= 100
    All the rectangles are unique.
    All the points are unique.


"""


class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]

        thought:  BF m*n check all points with each rectangle, will TLE.
        binary search.
        easy to get the logic, but not very easy to code.

        since height is between [1,100], we can use list to store
        height and length of each rectangle and sort the length of each
        height list

        1,3,5
        0 1 2

        05/29/2022 17:08	Accepted	3380 ms	37.4 MB	python
        medium 30-40 min. takes some time to code.
        """
        import bisect
        heights = [list() for i in range(101)]
        for x, y in rectangles:
            heights[y].append(x)

        for i in range(101):  # sort length at each height
            heights[i].sort()

        n = len(points)
        ret = [0] * n
        for i in range(n):
            x, y = points[i][0], points[i][1]
            count = 0
            for h in range(y, 101):
                if heights[h]:  # such height exist, simplify code, of heights[h] is empty, bisect_left will return 0, so this line can be removed.
                    idx = bisect.bisect_left(heights[h], x)
                    count += len(heights[h]) - idx
            ret[i] = count
        return ret

