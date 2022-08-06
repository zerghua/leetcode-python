#
# Create by Hua on 8/6/22
#

"""
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.



Example 1:

ex-1
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:

ex-2
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.


Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length

"""


class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]

        thought: binary search + prefix sum
        1. put all candles index into a list;
        2. prefix sum all the plates before the candles.
        3. find the most left and right candles index, (find index >= left and <= right)
        4. use prefix sum subtraction between step 3. if right < left then return 0
        e.g

        idx = [2, 5, 9]
        left = bisect.bisect_left(l)  # bisect_left will always on the left of i, which includes i
        if l in [0,2], return 0
        if l in [3,5], return 1

        right = bisect.bisect(r)      # bisect similar to bisect, except will not include i
        if r in [0,1], return 0
        if r in [2,4], return 1
        if r in [5,8], return 2
        if r in [9], return 3


        idx[right] - idx[left] + 1 is total substring length
        right-left+1 is the number of plates inside the substring

        08/06/2022 16:10	Accepted	2544 ms	57.3 MB	python
        medium
        30-60min.
        binary search. had a hard time to figure out the formula which one to use: bisect and bisect_left, bisect_right
        """
        import bisect
        idx = []
        for i in range(len(s)):
            if s[i] == '|': idx.append(i)

        ret = []
        for l,r in queries:
            left = bisect.bisect_left(idx, l)
            right = bisect.bisect(idx, r) - 1
            ret.append(idx[right] - idx[left] - (right-left) if right > left else 0)
        return ret
