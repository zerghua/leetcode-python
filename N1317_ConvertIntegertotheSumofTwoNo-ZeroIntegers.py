#
# Create by Hua on 4/16/22.
#

"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

    A and B are No-Zero integers.
    A + B = n

The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B do not contain any 0 in their decimal representation.

Example 2:

Input: n = 11
Output: [2,9]



Constraints:

    2 <= n <= 104


"""


class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]

        thought: after a test, find out the return num should not contain
        any zeros, like 10, is invalid
        04/16/2022 10:20	Accepted	31 ms	13.6 MB	python
        easy 5 min.
        """

        for i in range(1, n):
            j = n - i
            if str(i).find("0") == -1 and str(j).find("0") == -1:
                return [i,j]

