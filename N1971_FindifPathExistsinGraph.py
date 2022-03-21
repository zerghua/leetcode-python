#
# Create by Hua on 3/21/22.
#

"""
There is a bi-directional graph with n vertices, where each vertex is
labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
bi-directional edge between vertex ui and vertex vi. Every vertex pair is
connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex
source to vertex destination.

Given edges and the integers n, source, and destination, return true if
there is a valid path from source to destination, or false otherwise.



Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.



Constraints:

    1 <= n <= 2 * 105
    0 <= edges.length <= 2 * 105
    edges[i].length == 2
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= source, destination <= n - 1
    There are no duplicate edges.
    There are no self edges.


"""


class Solution(object):
    def bfs(self, graph, source, destination, n):
        visit = [0]*n
        q = list()
        q.append(source)
        while q:
            e = q.pop()
            visit[e] = 1
            if e == destination:
                return True

            for adj in graph[e]:
                if visit[adj] ==0:
                    q.append(adj)
        return False

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool

        easy-medium, 20 - 30 mins, long code, easy to have syntax bugs.

        thought: BFS? push all adjacent of source edge into stack, and
        go through them, if encounter dest then return true, else false.

        a bit long code, need to construct a graph edges and then do BFS.

        defaultdict provides a default value for a list of disctionary.

        03/21/2022 15:14	Accepted	2851 ms	115.3 MB	python

        """

        # construct graph
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        return self.bfs(graph,source, destination,n)

