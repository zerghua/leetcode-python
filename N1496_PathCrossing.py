#
# Create by Hua on 4/5/22.
#

"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.



Example 1:

Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.



Constraints:

    1 <= path.length <= 104
    path[i] is either 'N', 'S', 'E', or 'W'.


"""


class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool

        N(1,0), S(-1,0), E(0,1), W(0,-1)

        thought: simulate the travel, keep record on the visited point(not just
        the original point)

        04/05/2022 09:49	Accepted	33 ms	13.6 MB	python
        easy 5-10 min. only tuple can be put into set.
        tuple is also not modifiable, use list instead.
        or can do
        r = (0,0)
        r = (r[0] + r[1] + 1)

        """

        visited = set()
        r = [0, 0]
        visited.add(tuple(r))

        for p in path:
            if p == 'N':
                r[0] += 1
            elif p == 'S':
                r[0] -= 1
            elif p == 'E':
                r[1] += 1
            else:
                r[1] -= 1
            if tuple(r) in visited:
                return True
            visited.add(tuple(r))
        return False


