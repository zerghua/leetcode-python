#
# Create by Hua on 5/17/22
#


"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]

        thought: typical BFS, store visited node.
        05/17/2022 11:37	Accepted	102 ms	13.6 MB	python
        easy - medium 20-30min. long BFS code

        DFS code:
            r, c = len(image), len(image[0])
            color = image[sr][sc]
            def dfs(i, j):
                if i < 0 or i>=r or j < 0 or j >= c:
                    return
                if image[i][j] == newColor or image[i][j] != color:
                    return
                image[i][j] = newColor
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i,j+1)
                dfs(i, j-1)
            dfs(sr, sc)
            return image
        }
        """
        m,n = len(image), len(image[0])
        visited = []
        for i in range(m):
            visited.append([0]*n)

        lt = [[sr,sc]]
        visited[sr][sc] = 1
        val = image[sr][sc]
        image[sr][sc] = newColor
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while lt:
            tmp = list()
            for p in lt:
                for d in directions:
                    r, c = p[0] + d[0], p[1] + d[1]
                    if 0 <= r < m and 0 <= c < n:
                        print(r)
                        print(c)
                        if not visited[r][c] and image[r][c] == val:
                            image[r][c] = newColor
                            tmp.append([r,c])
                        visited[r][c] = 1
            lt = tmp
        return image