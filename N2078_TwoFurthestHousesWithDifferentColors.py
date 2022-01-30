#
#  Create by Hua on 1/30/2022
#

"""
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed
integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.



Example 1:
Input: colors = [1,1,1,6,1,1,1]
Output: 3
Explanation: In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.

Example 2:
Input: colors = [1,8,3,8,3]
Output: 4
Explanation: In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.

Example 3:
Input: colors = [0,1]
Output: 1
Explanation: The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.



Constraints:
    n == colors.length
    2 <= n <= 100
    0 <= colors[i] <= 100
    Test data are generated such that at least two houses have different colors.

"""


class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int

        easy 5 min, need to think a bit to find out the optimal solution o(n)

        thought: brute force (o^2), check every pair and find max. optimal, the max distance will always come from
        either leftmost or rightmost with another in between.(2*o(n))

        01/30/2022 14:09	Accepted	26 ms	13.2 MB	python
        """

        # rightmost
        ret = 0
        n = len(colors)
        for i in range(n):
            if colors[i] != colors[n-1]:
                ret = max(ret, n - 1 - i)

        # leftmost
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                ret = max(ret, i - 0)

        return ret