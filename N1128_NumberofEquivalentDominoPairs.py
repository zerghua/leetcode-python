#
# Create by Hua on 4/30/22.
#

"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].



Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3



Constraints:

    1 <= dominoes.length <= 4 * 104
    dominoes[i].length == 2
    1 <= dominoes[i][j] <= 9


"""


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int

        thought: hashmap to store visited sorted pair
        04/30/2022 11:46	Accepted	195 ms	25.4 MB	python
        easy 5 min.
        """

        dt = dict()
        ret = 0
        for p in dominoes:
            sp = tuple(sorted(p)) # list is not hashable, so convert to tuple
            if sp in dt:
                ret += dt[sp]
                dt[sp] += 1
            else:
                dt[sp] = 1

        return ret