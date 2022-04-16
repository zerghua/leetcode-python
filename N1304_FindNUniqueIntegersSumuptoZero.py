#
# Create by Hua on 4/16/22.
#

"""
Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]



Constraints:

    1 <= n <= 1000


"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]

        thought: math, find symmetric +x and -x, append 0 if n is odd
        04/16/2022 15:05	Accepted	24 ms	13.5 MB	python
        easy 5 min.
        """
        m = n / 2
        ret = list()
        ret.extend(list(range(1,m+1)))
        ret.extend(list(range(-m,0)))
        if n % 2 == 1:
            ret.append(0)
        return ret
