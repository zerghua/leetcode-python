#
# Create by Hua on 7/23/22
#

"""
You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.



Example 1:

Input: finalSum = 12
Output: [2,4,6]
Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.
Example 2:

Input: finalSum = 7
Output: []
Explanation: There are no valid splits for the given finalSum.
Thus, we return an empty array.
Example 3:

Input: finalSum = 28
Output: [6,8,2,12]
Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24).
(6 + 8 + 2 + 12) has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.


Constraints:

1 <= finalSum <= 1010

"""


class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]

        thought: math.greedy. don't have the math proof why this solution works.
        lets do it for 24,
        28-----> [2]
        26----->[2,4]
        22----->[2,4,6]
        16----->[2,4,6,8] here if we add 8 we will be left with 16-8=8 but our next number in sequence is 10, we cannot accommodate 10, so instead of adding 8+10=18 just add 16. are you getting? answer will be [2,4,6,16]

        lets do it for 48,
        48----->[2]
        46----->[2,4]
        42----->[2,4,6,8]
        34------>[2,4,6,8,10]
        24------>[2,4,6,8,10,12]
        12------> but we cant accommodate 14 ,so remove 12 and add 18 so answer will be [2,4,6,8,10,18]

        basically if sum - cur < cur +2(the next smallest number),  then we can't divide remain anymore.
        https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1783317/JavaPython-3-Greedy-w-brief-explanation-and-analysis.

        07/23/2022 14:15	Accepted	604 ms	25.9 MB	python
        medium. 30-40mins
        math, greedy
        don't have the math proof.
        """
        if finalSum % 2 == 1: return []

        ret = list()
        i, remain =2, finalSum
        while i <= remain:
            ret.append(i)
            remain -= i
            i += 2
        ret[-1] += remain  # the last part is repeating
        return ret
