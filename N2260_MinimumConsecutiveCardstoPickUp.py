#
# Create by Hua on 5/29/22.
#

"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.



Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.



Constraints:

    1 <= cards.length <= 105
    0 <= cards[i] <= 106


"""


class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int

        thought: use hashtable to store the last index of the card
        05/29/2022 11:09	Accepted	931 ms	33.6 MB	python
        meadium - easy 10 min.
        """
        dt = dict()
        ret = 10**6
        for i in range(len(cards)):
            card = cards[i]
            if card in dt:
                ret = min(ret, i - dt[card] + 1)
            dt[card] = i

        if ret == 10**6:
            return -1
        return ret



