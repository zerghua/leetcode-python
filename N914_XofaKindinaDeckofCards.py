#
# Create by Hua on 5/11/22
#


"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.


Constraints:

1 <= deck.length <= 104
0 <= deck[i] < 104

"""


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool

        thought: hashmap, counter. to check all the counters has a common divisor >= 2

        corner case:
        1, [1,1,2,2,2,2], True
        2. [1,1,1,1,2,2,2,2,2,2], True

        05/11/2022 14:44	Accepted	110 ms	13.6 MB	python
        easy-medium, 10-20min. a couple wrong answer leads to find the logic of the problem.
        """
        if len(deck) < 2: return False
        import collections
        dt = collections.Counter(deck)
        a = dt.values()
        for i in range(2, min(a)+1):
            count = 0
            for e in a:
                if e % i == 0:
                    count += 1
            if count == len(a):
                return True
        return False
