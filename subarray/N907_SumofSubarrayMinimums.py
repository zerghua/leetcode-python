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

        formula is (i - j) * (j - k) * a[j].
        simulate process:
        add -inf to both end of a
          -inf, 3, 1, 2, 5, 4, -inf
    index   0,  1, 2, 3, 4, 5, 6

        stack = [0,2,3,5,6]  # store index and value of its index are increasing

        index 0, val -inf
        stack: [0]
        -------

        index 1, val 3
        stack: [0, 1]
        -------

        index 2, val 1
        A[j] = 3,  total=3, i=2, j=1, k=0
        stack: [0, 2]
        -------

        index 3, val 2
        stack: [0, 2, 3]
        -------

        index 4, val 5
        stack: [0, 2, 3, 4]
        -------

        index 5, val 4
        A[j] = 5,  total=5, i=5, j=4, k=3
        stack: [0, 2, 3, 5]
        -------

        index 6, val -inf
        A[j] = 4,  total=8, i=6, j=5, k=3
        A[j] = 2,  total=6, i=6, j=3, k=2
        A[j] = 1,  total=8, i=6, j=2, k=0
        stack: [0, 6]
        -------


        A[j] = 5,  count=5
        A[j] = 4,  count=8
        A[j] = 2,  count=6
        A[j] = 1,  count=8
        A[j] = 3,  count=3
        total can also be calculated as 3*1 + 1*8 + 2*3 + 4*2 + 5*1 = 30

        07/28/2022 16:35	Accepted	397 ms	16.9 MB	python
        medium - hard
        2-3h to fully understand this solution.
        """

        inf = float('inf')
        a = [-inf] + arr + [-inf]  # add edge
        stack = []
        ret = 0
        mod = 10**9 + 7
        for i in range(len(a)):
            while stack and a[stack[-1]] > a[i]:
                j = stack.pop()
                pre_j = stack[-1]
                ret += a[j] * (i-j) * (j-pre_j)  # (i-j) is right count, (j-pre_j) is left count
            stack.append(i)
        return ret % mod


    def sumSubarrayMins2(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: BF solution is to check record cur min and check every subarray from index i,
        it's o(n^2) solution which will pass the OJ.
        however, there is a o(n) solution which use a non-decreasing stack to maintain the index
        for each minimal value, there is a formula to calculate the value.

        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
        Together these two observations give us formula result[i] = result[j] + A[i]*(i-j)

        this is a dp

        07/28/2022 11:28	Accepted	384 ms	17.5 MB	python
        medium - hard (if require o(n) solution)


        [3,1,2,5,4]
        subarray ending with i
        [3],
        [3,1], [1]
        [3,1,2], [1,2], [2]
        [3,1,2,5], [1,2,5],[2,5],[5]
        [3,1,2,5,4], [1,2,5,4],[2,5,4],[5,4],[4]
        sum of 1..n = n(n+1)/2, when n = 5, total is 5*6/2 = 15
        min of above
        3
        1, 1
        1, 1, 2
        1, 1, 2, 5
        1, 1, 2, 4, 4
        total = 3 + 2 + 4 + 9 + 12 = 30
        from above we can see there are
        for min == 3, there are 1 subarray
        for min == 1, there are 8 subarrays
        for min == 2, there are 3 subarrays
        for min == 4, there are 2 subarrays
        for min == 5, there are 1 subarray
        total can also be calculated as 3*1 + 1*8 + 2*3 + 4*2 + 5*1 = 30
        so the optimized solution is to find how many subarrays for a given n

        for a given n,
        find the size of numbers strictly bigger than n on its left
        find the size of numbers bigger than n on its right (until a smaller)
        (j-k) is the number on the left
        (i-j) is the number on the right,
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


