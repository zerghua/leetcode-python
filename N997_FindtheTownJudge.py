#
# Create by Hua on 5/5/22.
#

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1



Constraints:

    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n


"""


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int

        thought: seems like a graph problem, return the one has only inward
        direction, else return -1

        so the judge should have n-1 votes, and other people might vote
        multiple people, but it should contain the judge vote

        corner cases: many
        4
        [[1,3],[1,4],[2,3]]
        Expected: -1

        4
        [[1,3],[1,4],[2,3],[2,4],[4,3]]
        Expected: 3

        05/05/2022 11:21	Accepted	712 ms	18.7 MB	python
        easy - medium. 10-20 min.
        """

        vote = [0] * (n+1)
        for i, j in trust:
            vote[i] -= 1
            vote[j] += 1

        for i in range(1, len(vote)):
            if vote[i] == n - 1:
                return i

        return -1
