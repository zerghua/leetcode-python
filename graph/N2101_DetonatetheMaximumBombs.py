#
# Create by Hua on 7/31/22
#

"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.



Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.


Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105

"""


class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int

        thought: build directed graph, and then do BFS or DFS.
        there is no need to create graph class, just create a list of lists to represent graph.
        Euclidean distance: a^2 + b^2 == c^2

        defaultdict(<type 'list'>,
        {
        0: [1, 3, 7, 11],
        1: [0, 3, 5, 7, 8, 11],
        2: [4, 8],
        3: [0, 1, 5, 12],
        4: [2, 8],
        6: [9, 11],
        7: [0, 1],
        8: [2, 4],
        11: [0]
        })

        0,1,3,5,7, 8,11,12, 2,4, 6, 9

        07/31/2022 11:43	Accepted	1925 ms	13.4 MB	python
        medium
        30-40min. need to build a list of lists for graph, then do BFS or DFS.

        """
        # build graph
        import collections
        graph = collections.defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i].append(j)

        # BFS, need a fresh visit from every node

        ret = 0
        for i in range(n):
            visited = set()
            cur_max = 0
            lt = [i]  # bug is here, cant' set "lt = graph[i]" graph[i] has been modified when do a soft link.
            while lt:
                node_id = lt.pop()
                if node_id in visited: continue
                cur_max += 1
                visited.add(node_id)
                lt.extend(graph[node_id])
            ret = max(ret, cur_max)
        return ret


