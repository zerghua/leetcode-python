#
# Create by Hua on 7/31/22
#

"""
You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.

The ith day is a good day to rob the bank if:

There are at least time days before and after the ith day,
The number of guards at the bank for the time days before i are non-increasing, and
The number of guards at the bank for the time days after i are non-decreasing.
More formally, this means day i is a good day to rob the bank if and only if security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter.



Example 1:

Input: security = [5,3,3,3,5,6,2], time = 2
Output: [2,3]
Explanation:
On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
Example 2:

Input: security = [1,1,1,1,1], time = 0
Output: [0,1,2,3,4]
Explanation:
Since time equals 0, every day is a good day to rob the bank, so return every day.
Example 3:

Input: security = [1,2,3,4,5,6], time = 2
Output: []
Explanation:
No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.


Constraints:

1 <= security.length <= 105
0 <= security[i], time <= 105

"""


class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]

        thought: got from hints, store the non-increasing before i and non-decreasing after i.
        both left to right and right to left

        07/31/2022 15:02	Accepted	1184 ms	33.6 MB	python
        medium
        10-20min.
        prefix sum
        """
        n = len(security)
        before, after = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                before[i] = before[i-1] + 1
            else:
                before[i] = 0

        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                after[i] = after[i+1] + 1
            else:
                after[i] = 0

        ret = list()
        for i in range(n):
            if before[i] >= time and after[i] >= time:
                ret.append(i)
        return ret