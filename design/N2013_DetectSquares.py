#
# Create by Hua on 9/13/22
#

"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.


Example 1:


Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points


Constraints:

point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.

"""

import collections
class DetectSquares(object):

    def __init__(self):
        self.dt = collections.Counter()


    def add(self, point):
        """
        :type point: List[int]
        :rtype: None

        thought: first need to communicate with interviewer about constraints. how many points, what are their sizes.
        find each query point p1, find its diagonal point p3,
        to form a valid square, the p3 needs to be abs(p1.x - p3.x) == abs(p1.y - p3.y) and p1 != p3
        then we find the count of p2(p1.x, p3.y) and p4(p3.x, p1.y) in the map.

        or we can compute p2 and find p3 and p4.

        https://leetcode.com/problems/detect-squares/discuss/1471958/C%2B%2BJavaPython-2-approaches-using-HashMap-with-Picture-Clean-and-Concise

        hashmap, hard part is figure out how to calculate the point.
        medium
        30-60 min
        google.
        """
        x,y = point
        self.dt[(x, y)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x1,y1= point
        ret = 0
        for (x3,y3), count in self.dt.items():
            if abs(x1-x3) == abs(y1-y3) and (x1,y1) != (x3,y3):
                ret += self.dt[(x1,y3)] * self.dt[(x3,y1)]*count
        return ret


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)