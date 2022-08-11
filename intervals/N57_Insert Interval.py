#
# Create by Hua on 8/11/22
#

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        thought: we can put the extra new interval into the list of sorted intervals(by nlogn sort or binary search
        insert)
        then it's a problem of N56 merge intervals.

        08/11/2022 11:15	Accepted	131 ms	17 MB	python   # binary search insert
        08/11/2022 11:18	Accepted	89 ms	16.9 MB	python   # add new interval and sort whole list

        """
        # new of this problem
        #import bisect
        #a = [p[0] for p in intervals]
        #i = bisect.bisect(a, newInterval[0])
        #intervals.insert(i, newInterval)

        # add and sort whole list
        intervals.append(newInterval)
        intervals.sort()

        # solution from N56
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            pre_start, pre_end = ret[-1][0], ret[-1][1]
            if start <= pre_end:  # start in pre range, after sort, start will always >= pre_start
                ret.pop(-1)
                ret.append([pre_start, max(end, pre_end)])
            else:  # no overlap.
                ret.append(intervals[i])
        return ret



