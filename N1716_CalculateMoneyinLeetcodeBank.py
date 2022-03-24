#
# Create by Hua on 3/24/22.
#

"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.



Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.



Constraints:

    1 <= n <= 1000


"""


class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        thought: every 7 days, it's increasing 7 times,
        1,2,3,4,5,6,7  (28)     n/7 = 0
        2,3,4,5,6,7,8  (28+1*7) n/7 = 1
        3,4,5,6,7,8,9  (28+2*7) n/7 = 2
        4,5,6,7,8,9,10 (28+3*7) n/7 = 3

        03/24/2022 17:15	Accepted	28 ms	13.4 MB	python
        easy-medium, 20-30 min.  math.

        """

        d = n / 7
        ret = 0
        if d >=1:
            ret = 28*d + 7*sum(range(d-1))
        r = n % 7
        ret += sum(range(d+1,d+r+1))
        return ret




