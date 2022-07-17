#
# Create by Hua on 7/17/22
#

"""
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.



Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.


Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012

"""


class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int

        thought: BF solution, set initial ret = sum(candies) / k, check if such ret satisfy, if not,
        decrease ret by 1, and repeat until 1. it will TLE due to ret can be large.

        The optimal solution is instead of decrease by 1, use binary search for the ret value. check if such ret
        satisfy or not, if not decrease by half. max of ret = 10**7

        refer: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/discuss/1908888/JavaC%2B%2BPython-Binary-Search-with-Explanation

        Tips
        Tip1. left < right Vs left <= right

        Check all my solution, I keep using left < right.
        The easy but important approach:
        follow and upvote my codes,
        try to do the same.
        you'll find all binary search is similar,
        never bother thinking it anymore.

        Tip2. mid = (left + right + 1) / 2 Vs mid = (left + right) / 2

        mid = (left + right) / 2 to find first element valid
        mid = (left + right + 1) / 2 to find last element valid

        0,1,2,3

        07/17/2022 09:49	Accepted	3082 ms	24.6 MB	python
        medium, didn't get the idea of using binary search initially.

        """

        left, right = 0, 10**7
        while left < right:
            mid = (left+right+1)/2  # candies to distribute per kid
            satisfied_kid = 0
            for c in candies:
                satisfied_kid += c / mid

            if k > satisfied_kid:
                right = mid - 1
            else:
                left = mid
        return left



