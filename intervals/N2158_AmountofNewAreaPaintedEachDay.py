#
# Create by Hua on 8/10/22
#

"""
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.



Example 1:


Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1.
Example 2:


Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1.
Example 3:


Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.


Constraints:

1 <= paint.length <= 105
paint[i].length == 2
0 <= starti < endi <= 5 * 104

"""


class Solution(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]

        thought: typical segment tree problem. but can be solved using hashmap to store the next start position
        for pruning.

        https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1751389/Jump-Line
        class Solution:
        def amountPainted(self, paint: List[List[int]]) -> List[int]:
            line, res = [0] * 50001, [0] * len(paint)
            for i, (start, end) in enumerate(paint):
                while start < end:
                    jump = max(start + 1, line[start])
                    res[i] += 1 if line[start] == 0 else 0
                    line[start] = max(line[start], end)  # compression
                    start = jump
            return res


            Input: paint = [[1,4],[5,8],[4,7]]
            Output: [3,3,1]

            i = 0, start=1, end=4
            while loop start < end
            jump=max(2, 0) = 2
            res[0] = 1
            line[1] = max(0,4) = 4
            start = 2

            jump=max(3, 0) = 3
            res[0] = 2
            line[2] = max(0,4) = 4
            start = 3

            jump=max(4, 0) = 4
            res[0] = 3
            line[3] = max(0,4) = 4
            start = 4

            end loop.

            i=1, start =5, end=8
            while loop start < end
            jump=max(6, 0) = 6
            res[1] = 1
            line[5] = max(0,8) = 8
            start = 6

            jump=max(7, 0) = 7
            res[1] = 2
            line[6] = max(0,8) = 8
            start = 7

            jump=max(8, 0) = 8
            res[1] = 3
            line[7] = max(0,8) = 8
            start = 8
            end loop.

            i=2, start =4, end=9
            while loop start < end
            jump= max(5,line[4] 0) = 5
            ret[2] = 1
            line[4] = max(0, 9) = 9
            start = 5

            jump= max(6,line[5] 8) = 8
            ret[2] = 1
            line[5] = max(8, 9) = 9
            start = 8

        company: google high frequency
        08/11/2022 10:04	Accepted	2979 ms	62.5 MB	python
        hard
        more of array map, not easy to figure out the algorithm and code.

        can also do segment tree:
        https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1825122/Python-or-Segment-Tree-clean-code

        or merge intervals:
        https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1751389/Jump-Line
        """

        p, ret = [0] * (10**5 + 1), [0] * len(paint)  # p store the end of the paint.
        for i in range(len(paint)):
            start, end = paint[i][0], paint[i][1]
            while start < end:
                next_paint = max(start + 1, p[start])  # next step we either check start+1 or the end of last painted.
                ret[i] += 1 if p[start] == 0 else 0  # paint if not painted
                p[start] = max(p[start], end)    # set the current paint's end to either itself or the end of new paint
                start = next_paint
        return ret