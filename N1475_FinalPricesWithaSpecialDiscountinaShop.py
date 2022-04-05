#
# Create by Hua on 4/5/22.
#

"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.



Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation:
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.

Example 3:

Input: prices = [10,1,1,6]
Output: [9,0,1,6]



Constraints:

    1 <= prices.length <= 500
    1 <= prices[i] <= 10^3


"""


class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]

        thought: brute force of 2 loops, find the first price less than a[i]
        after i
        04/05/2022 10:29	Accepted	55 ms	13.6 MB	python
        easy 5 min.
        """
        ret = list()
        n = len(prices)
        for i in range(n):
            found_discount = False
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    ret.append(prices[i] - prices[j])
                    found_discount = True
                    break
            if not found_discount:
                ret.append(prices[i])

        return ret