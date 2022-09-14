#
# Create by Hua on 9/14/22
#

"""
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.



Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2


Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000

"""


class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int

        thought: BF is o(n^2) solution, check every pair.
        o(n) solution is to use dp and a formula. values[i] + i + values[j] - j

        09/14/2022 16:31	Accepted	716 ms	17.9 MB	python
        medium
        google
        dp, not easy to figure out the formula
        https://leetcode.com/problems/best-sightseeing-pair/discuss/260909/JavaPython-Descriptive-solution.O(N)-Time-or-O(1)-Space.-Very-similar-to-Kadence-Algo!
        """

        cur_max, ret = values[0], 0
        for i in range(1, len(values)):
            ret = max(ret, cur_max + values[i] - i)
            cur_max = max(cur_max, values[i] + i)
        return ret


