#
# Create by Hua on 3/21/22.
#

"""
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.



Example 1:
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).



Constraints:
    1 <= n <= 250

"""


class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int

        thought: brute force with some minor optimization

        03/21/2022 17:32	Accepted	2968 ms	13.7 MB	python

        easy 5 min.

        better solution from discussion:
        class Solution:
            def countTriples(self, n: int) -> int:
                s = set()
                answer = 0

                for i in range(1, n + 1):
                    s.add(i*i)

                for i in range(1, n + 1):
                    for j in range(i+1, n + 1):
                        if  (i*i + j*j) in s:
                            answer += 2

                return answer
        """

        ret = 0
        for i in range(1, n - 1):
            for j in range(i+1, n):
                for k in range(j+1, n+1):
                    if i*i + j*j == k*k:
                        ret += 2
                    elif i*i + j*j < k*k:
                        break

        return ret

