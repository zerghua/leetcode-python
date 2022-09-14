#
# Create by Hua on 9/14/22
#

"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.


Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.


Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105

"""


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        thought: 2d dp. each dp contains the max value picked so far, return the max of last row.
        time: BF solution is o(m*n*n), which will TLE, given m*n == 10^5
        for each point, it will check n times; and there are m*n points.

        the hard part is how to optimize it from o(m*n*n) to o(m*n)

        the optimization idea is to check both left and right elements.

        similar problem, check out 1014 and 931.

        09/14/2022 15:50	Accepted	3721 ms	50.1 MB	python
        medium - hard(if must optimize the solution to o(m*n), not very intuitive)
        google.
        dp.

        """
        m,n = len(points), len(points[0])
        dp = [0]* n
        for i in range(m):
            for j in range(n):      # means choose the item directly above
                dp[j] += points[i][j]

            for j in range(n-2, -1,-1):   # choose item from its right
                dp[j] = max(dp[j], dp[j+1] -1)

            for j in range(1,n):         # choose item from its left
                dp[j] = max(dp[j], dp[j-1] - 1)

        return max(dp)  # return cur will be error if only one row

class Solution_easy_understand(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        thought: 2d dp. each dp contains the max value picked so far, return the max of last row.
        time: BF solution is o(m*n*n), which will TLE, given m*n == 10^5
        for each point, it will check n times; and there are m*n points.

        the hard part is how to optimize it from o(m*n*n) to o(m*n)

        the optimization idea is to check both left and right elements.

        So for each element in a row, instead of traversing prev whole row
        what we can do is that keep left and right vectors to get max from 0 to i-1th in left side, and i+1th to n-1 in right side

        left[i] = max(point[i], left[i-1] - 1)
        now why this?

        Now for each cell max is one of when same col, from left side, from right side

        using left we will get max from left side, using right vector we will get max from right side
        and at each step we will also compare them with same col val

        so for left[0] = prev[0], because there is no element in left side
        for left[1] = max(prev[1], left[0] - 1), this -1 is the difference in cols (0 - 1)

        Now next step is important
        for left[2] = max(prev[2], left[1]-1)

        at this step, if left[1] had value of just above then we had only subtracted 1 from it, and only 1 should be subtracted only
        but if left[1] had left[0]-1 in it, then left[2] = left[0] - 2, now we can see it automatically subtracted 2 if 0th was max


        similar problem, check out 1014 and 931.
        https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344888/C%2B%2B-dp-from-O(m-*-n-*-n)-to-O(m-*-n)

        09/14/2022 15:40	Accepted	3367 ms	50.1 MB	python
        medium - hard(if must optimize the solution to o(m*n), not very intuitive)
        """
        m,n = len(points), len(points[0])
        left, right, pre,cur = [0]*n, [0]*n,[0]*n,[0]*n

        # init pre
        for i in range(n):
            pre[i] = points[0][i]

        for i in range(1, m):
            # right to left
            right[n-1] = pre[n-1]
            for j in range(n-2,-1,-1):
                right[j] = max(pre[j], right[j+1] - 1)

            # left to right
            left[0] = pre[0]
            for j in range(1,n):
                left[j] = max(pre[j], left[j-1] - 1)

            # combine
            for j in range(n):
                cur[j] = points[i][j] + max(left[j], right[j])

            pre = cur
        return max(pre)  # return cur will be error if only one row


