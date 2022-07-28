#
# Create by Hua on 7/28/22
#

"""
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.



Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]


Constraints:

1 <= prices.length <= 105
1 <= prices[i] <= 105

"""


class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        thought: find multiple longest continuous subarray(size is k) satisfy the requirement, and calculate the sum.
        for each subarray, the sum == k*(k-1)/2 , also add each element to final answer
        2 or more pointers.

        07/28/2022 09:24	Accepted	1771 ms	24.3 MB	python
        medium - easy
        10-20min
        """
        n = len(prices)
        ret, i = n, 0
        while i < n:
            if i+1 < n and prices[i] - prices[i+1] == 1:  # let's find the longest subarray
                j = i + 1
                while j + 1 < n:
                    if prices[j] - prices[j+1] == 1: j += 1
                    else: break
                k = (j - i + 1)
                ret += k*(k-1)/2
                i = j
            else: i+=1
        return ret



