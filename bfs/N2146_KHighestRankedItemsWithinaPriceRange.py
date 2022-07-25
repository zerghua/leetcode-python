#
# Create by Hua on 7/25/22
#

"""
You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.

You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.



Example 1:


Input: grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3
Output: [[0,1],[1,1],[2,1]]
Explanation: You start at (0,0).
With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2).
The ranks of these items are:
- (0,1) with distance 1
- (1,1) with distance 2
- (2,1) with distance 3
- (2,2) with distance 4
Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).
Example 2:


Input: grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2
Output: [[2,1],[1,2]]
Explanation: You start at (2,3).
With a price range of [2,3], we can take items from (0,1), (1,1), (1,2) and (2,1).
The ranks of these items are:
- (2,1) with distance 2, price 2
- (1,2) with distance 2, price 3
- (1,1) with distance 3
- (0,1) with distance 4
Thus, the 2 highest ranked items in the price range are (2,1) and (1,2).
Example 3:


Input: grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3
Output: [[2,1],[2,0]]
Explanation: You start at (0,0).
With a price range of [2,3], we can take items from (2,0) and (2,1).
The ranks of these items are:
- (2,1) with distance 5
- (2,0) with distance 6
Thus, the 2 highest ranked items in the price range are (2,1) and (2,0).
Note that k = 3 but there are only 2 reachable items within the price range.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= grid[i][j] <= 105
pricing.length == 2
2 <= low <= high <= 105
start.length == 2
0 <= row <= m - 1
0 <= col <= n - 1
grid[row][col] > 0
1 <= k <= m * n

"""


class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]

        thought: bfs to search each neighbour cells and can decide their distance, with in the same distance, we
        sort them by price(price has to be in the pricing range), row and col. return the first k or until we can't
        search anymore.

        bfs usually need a visited set to avoid duplicate search.

        https://stackoverflow.com/questions/20145842/python-sorting-by-multiple-criteria
        python sort by multiple criteria, just list them by order
            List the three criteria in your key:
                sorted(inputlist, key=lambda e: (len(e[0]), e[0], e[1]))

        07/25/2022 15:04	Accepted	5852 ms	69.4 MB	python
        medium, bfs and custom sort
        30-40min

        interesting solution: check out how it's sorting, used a 4 items tuples and just sort it.
        https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/discuss/1709671/Python-classical-bfs-solution-explained
        class Solution:
            def highestRankedKItems(self, G, pricing, start, k):
                m, n = len(G), len(G[0])
                row, col = start
                node = (0, G[row][col], row, col)
                visited = set()
                visited.add((row, col))
                d = deque([node])
                ans = []

                while d:
                    dist, cost, row, col = d.popleft()
                    if pricing[0] <= cost <= pricing[1]:
                        ans += [(dist, cost, row, col)]

                    for x, y in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                        if 0 <= x <= m-1 and 0 <= y <= n-1 and (x, y) not in visited and G[x][y] != 0:
                            d.append((dist + 1, G[x][y], x, y))
                            visited.add((x, y))

                ans = sorted(ans)

                return [[x, y] for _, _, x, y in ans[:k]]
        """
        visited = set()  # visited cell
        q = [(start[0], start[1])]  # store each level of search, which has the same distance
        m,n = len(grid), len(grid[0])
        ret = list()
        while q:
            tmp_ret = list()
            next_round = set()  # need to be set to avoid duplicate visit
            for cell in q:
                r,c = cell[0], cell[1]
                visited.add((r,c))
                if pricing[0] <= grid[r][c] <= pricing[1]: # add to ret
                    tmp_ret.append((r,c))

                # add neighbour for the next round
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dir in directions:
                    a, b = r + dir[0], c + dir[1]
                    if 0 <= a < m and 0 <= b < n and (a,b) not in visited and grid[a][b] != 0:
                        next_round.add((a,b))
            q = list(next_round)
            tmp_ret.sort(key=lambda x: (grid[x[0]][x[1]], x[0], x[1]))
            ret.extend(tmp_ret)
            if len(ret) >=k: break
        return ret[:k]


