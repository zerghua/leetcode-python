#
# Create by Hua on 5/30/22.
#

"""
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:

    A lattice point is a point with integer coordinates.
    Points that lie on the circumference of a circle are also considered to be inside it.



Example 1:

Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

Example 2:

Input: circles = [[2,2,2],[3,4,1]]
Output: 16
Explanation:
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle.
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).



Constraints:

    1 <= circles.length <= 200
    circles[i].length == 3
    1 <= xi, yi <= 100
    1 <= ri <= min(xi, yi)


"""


class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int

        thought:
        for r = 1, total (1*2+1)^2 = 9 points,  2*2 not inside
        for r = 2, total (2*2+1)^2 = 25 points, 4*2 + 2*2 not inside
        for r = 3, total (3*2+1)^2 = 49 points, 6*2 + 4*2 + 2*2 not inside
        the key is to find the intersect of circles.
        r max = 100, total (100*2+1)^2 ~= 40000 points
        total 200 circle, 4*10**4 * 2*10**2 = 8 * 10**6

        BF, store all valid points(as tuple) in a set
        distance between 2 points, (2,2) and (1,4)， (4,2)

        05/30/2022 10:20	Accepted	4873 ms	18.5 MB	python
        medium. 40-50 min. initially working on a wrong solution.

        """
        ret = set()
        for x,y,r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if (i-x)**2 + (j-y)**2 <= r**2:  #Pythagorean theorem
                        ret.add((i,j))
        return len(ret)