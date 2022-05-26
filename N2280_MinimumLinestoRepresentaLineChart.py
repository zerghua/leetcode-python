#
# Create by Hua on 5/26/22
#


"""
You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:


Return the minimum number of lines needed to represent the line chart.



Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.


Constraints:

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
All dayi are distinct.

"""


class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int

        thought: sort stock prices by day first. calculate the slope of all adjacent points, compare it with it's
        previous adjacent points slope, if not equal, ret += 1, else continue
        no corner case on y-axis line, since all dayi are distinct.
        (x,y)  (x1,y1)  (x2,y2)
        (y1 - y) / (x1 - x) == (y2-y)/(x2-x)  ->
        (y1-y)*(x2-x) == (y2-y)*(x1-x)

        corner case:
        1. use float rather than int.
        2.

        05/26/2022 10:37	Accepted	1304 ms	61.6 MB	python
        medium 20-30 min. math. convert division to multiplication
        """
        n = len(stockPrices)
        if n == 1: return 0
        ret = 1
        s = sorted(stockPrices, key = lambda x: x[0])
        for i in range(2,n):
            (x,y) = s[i-2][0], s[i-2][1]
            (x1, y1) = s[i-1][0], s[i-1][1]
            (x2, y2) = s[i][0], s[i][1]
            if (y1-y)*(x2-x) != (y2-y)*(x1-x):
                ret += 1

        return ret


