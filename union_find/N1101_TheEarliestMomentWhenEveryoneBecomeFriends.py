#
# Create by Hua on 9/15/22
#

"""
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.



Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation:
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
Example 2:

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3


Constraints:

2 <= n <= 100
1 <= logs.length <= 104
logs[i].length == 3
0 <= timestampi <= 109
0 <= xi, yi <= n - 1
xi != yi
All the values timestampi are unique.
All the pairs (xi, yi) occur at most one time in the input.

"""

class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int

        thought: typical union find problem. union find is a type of graph.

        first need to sort by timestamp, and go through the relationship one by one.

        solution 2. use a dictionary to map people to it's direct relationship. it's a one-one mapping.
        use find to find the top parent who is map to itself. each merge will add only one friend to
        the whole group.

        09/15/2022 15:55	Accepted	179 ms	13.8 MB	python
        union find.
        """
        dt = {}
        self.group = n

        def merge(x,y):
            x,y = find(x), find(y)
            if x != y:
                self.group -= 1
                dt[x] = y

        def find(x):
            if dt[x] != x:
                dt[x] = find(dt[x])
            return dt[x]

        for i in range(n):  # init dict to map to itself
            dt[i] = i

        for t, a, b in sorted(logs):
            merge(a,b)
            if self.group == 1:
                return t
        return -1


class Solution_set(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int

        thought: typical union find problem. union find is a type of graph.

        first need to sort by timestamp, and go through the relationship one by one.

        solution 1. use a dictionary contains a set for each people, update each people's friend to full set.
        so when the len of any people reached to everyone, we return. use set union to combine people's friend.
        since each people contains the all the relationship, the space is pretty large.

        max space is o(n^2), might not be true, since each people's dictionary is a pointer to each other.

        09/15/2022 14:13	Accepted	217 ms	13.9 MB	python
        """

        logs.sort(key=lambda x:x[0])
        dt = {}
        for i in range(n):  # init set each people include itself
            dt[i] = {i}

        for t, a,b in logs:
            dt[a] = dt[a].union(dt[b])  # key for this solution
            if len(dt[a]) == n:  # we find now everyone is friend
                return t
            # update for each one in a
            for x in dt[a]:
                dt[x] = dt[a]

        return -1