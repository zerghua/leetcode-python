#
# Create by Hua on 8/11/22
#

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        thought: sort the intervals first. after sort, next start won't before pre start
        check the next start and end if they are in the pre range, if so, merge them.

        google. medium frequency
        08/11/2022 10:57	Accepted	122 ms	18.2 MB	python
        medium - easy
        sort and merge.
        10-20 min.
        """

        intervals.sort()
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


