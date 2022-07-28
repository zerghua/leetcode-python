#
# Create by Hua on 7/28/22
#

"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444


Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

"""


class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: BF solution is to check record cur min and check every subarray from index i,
        it's o(n^2) solution which will pass the OJ.
        however, there is a o(n) solution which use a non-decreasing stack to maintain the index
        for each minimal value, there is a formula to calculate the value.

        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
        Together these two observations give us formula result[i] = result[j] + A[i]*(i-j)

        more of a dp

        07/28/2022 11:28	Accepted	384 ms	17.5 MB	python
        medium - hard (if require o(n) solution)
        """

        lt = [0]  # stack add 0 to make code cleaner
        a = [0] + arr   # all values are positive
        ret = [0] * len(a)
        mod = 10**9 + 7
        for i in range(len(a)):
            while a[lt[-1]] > a[i]:
                lt.pop()
            pre_index = lt[-1]
            ret[i] = ret[pre_index] + (i-pre_index)*a[i]
            lt.append(i)
        return sum(ret) % mod
