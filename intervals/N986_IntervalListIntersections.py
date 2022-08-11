#
# Create by Hua on 8/11/22
#

"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []


Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1

"""


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]


        better solution is like the merge part of merge sort, use 2 pointers.
        a trick to use, max(a2,b2) and min(a1,b2) to check if they have intersection.
        08/11/2022 12:11	Accepted	118 ms	14.2 MB	python  <
        08/11/2022 12:13	Accepted	101 ms	14.3 MB	python  <=
        o(n) solution
        https://leetcode.com/problems/interval-list-intersections/discuss/231108/O(n)-%22merge-sort%22
        """

        ret = []
        i=j=0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ret.append([lo,hi])

            # discard the smallest end
            if firstList[i][1] < secondList[j][1]:   # can be both < and <=
                i += 1
            else:
                j += 1
        return ret


    def intervalIntersection_BF(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]

        thought: just write the code o(n^2), do they have duplicate intervals?
        a    [3-5]
        b1 [2-3]        partial
        b2 [2     - 8]  a in b
        b3    [4-5]     b in a
        b4    [4  - 8]  partial
        b5 [0-1]        no overlap
        b6        [7-8] no overlap

        08/11/2022 11:50	Accepted	2480 ms	14.4 MB	python
        08/11/2022 11:53	Accepted	2511 ms	13.7 MB	python
        medium
        20-30 min.

        if there is overlap, we pick max(a1,b1) and min(a2,b2)
        this is BF solution o(n^2)

        better solution is like the merge part of merge sort, use 2 pointers.
        """

        ret = []
        for i in range(len(firstList)):
            a1, a2 = firstList[i][0], firstList[i][1]
            for j in range(len(secondList)):
                b1,b2 = secondList[j][0], secondList[j][1]
                if a1 <= b2 <= a2 or a1 <= b1 <= a2:   # b start or end in range a
                    ret.append([max(a1,b1), min(a2,b2)])
                elif b1 <= a1 and a2 <= b2:  # a in range b
                    ret.append([a1,a2])
        return ret





