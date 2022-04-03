#
# Create by Hua on 4/3/22.
#

"""
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.



Example 1:

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 15 + 3 + 1 = 19.



Constraints:

    1 <= numBottles <= 100
    2 <= numExchange <= 100


"""


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int

        thought: math, pay attention to remain needs to be added.
        10 bottles, 3 exchange
        10 bottles to drink -> 10 empty bottles
        3 bottles to drink + 1 empty bottle -> 4 empty bottles
        1 bottle + 1 empty -> 2 empty

        04/03/2022 15:07	Accepted	17 ms	13.4 MB	python
        easy 5-10 min. throw out example to help with logic.
        """
        ret = numBottles
        empty = numBottles
        while empty >= numExchange:
            ret += empty / numExchange
            empty = empty / numExchange + empty % numExchange

        return ret
