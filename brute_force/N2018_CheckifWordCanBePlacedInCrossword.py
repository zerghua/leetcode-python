#
# Create by Hua on 10/2/22
#

"""
You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.



Example 1:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).
Example 2:


Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
Example 3:


Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left).


Constraints:

m == board.length
n == board[i].length
1 <= m * n <= 2 * 105
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.

"""


class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        thought: try every left to right and top to bottom when find an empty cell iff
        the left/top of the current cell is '#', find empty cell until encounter '#' or wall.
        then check if the word can match the find spaces.
        (left to right and right to left/ top to bottom and bottom to top)

        10/02/2022 15:50	Accepted	2611 ms	79.9 MB	python
        google
        BF. 
        """

        def check_match(lt, word):
            # should check both ways, left to right and right to left
            n = len(word)
            if len(lt) != n:
                return False

            # forward
            i = 0
            while i < n :
                if lt[i] == ' ' or lt[i] == word[i]:
                    i += 1
                else:
                    break
            if i == n:
                return True

            # backward
            lt = lt[::-1]
            i = 0
            while i < n :
                if lt[i] == ' ' or lt[i] == word[i]:
                    i += 1
                else:
                    break
            if i == n:
                return True

            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != '#':
                    # check left of cur cell
                    if j == 0 or board[i][j-1] == '#':
                        # find from left to right until '#' or wall
                        k = j
                        while k < n and board[i][k] != '#':
                            k += 1
                        if check_match(board[i][j:k], word):
                            return True

                    # check top of cur cell
                    if i == 0 or board[i-1][j] == '#':
                        k = i
                        tmp = []
                        while k < m and board[k][j] != '#':
                            tmp.append(board[k][j])
                            k += 1
                        if check_match(tmp, word):
                            return True
        return False


