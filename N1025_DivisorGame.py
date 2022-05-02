#
# Create by Hua on 5/2/22.
#

"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < n and n % x == 0.
    Replacing the number n on the chalkboard with n - x.

Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.



Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.



Constraints:

    1 <= n <= 1000


"""


class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        https://leetcode.com/problems/divisor-game/discuss/274606/JavaC%2B%2BPython-return-N-2-0
        math. even wins.
        medium, if can't figure out, can never solve it.
        05/02/2022 10:28	Accepted	19 ms	13.4 MB	python
        A: even -> odd  (even - 1) is odd
        B: odd -> even
        ...
        whoever got 1 will lose


        """
        return n % 2 == 0