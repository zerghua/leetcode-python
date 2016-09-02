#
#  Create by Hua on 9/2/2016
#


"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Wrong example:
        # 1. row = col = box = [[False]*9 for i in range(9)]
        # 2. row = [[False]*9] * 9

        row = [[False]*9 for i in range(9)]
        col = [[False]*9 for i in range(9)]
        box = [[False]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = (i/3)*3 + j/3
                    if row[i][num] or col[j][num] or box[k][num]:
                        return False
                    row[i][num] = col[j][num] = box[k][num] = True
        return True