#
# Create by Hua on 5/5/22.
#

"""
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.



Example 1:

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.

Example 2:

Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.

Example 3:

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.



Constraints:

    board.length == 8
    board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'


"""


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int

        thought: try 4 directions, stop when encounter B or p or wall
        if meet p before wall or B, then ret += 1

        first need to find R pos.
        05/05/2022 10:42	Accepted	31 ms	13.5 MB	python
        easy 5-10 min. but need to simplify code
        """

        m, n= len(board), len(board[0])
        x,y = 0,0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    x,y = i,j


        # try 4 directions
        ret = 0
        t = x
        while t >= 0:
            if board[t][y] == 'p':
                ret += 1
                break
            elif board[t][y] == 'B':
                break
            t -= 1

        t = x
        while t < m:
            if board[t][y] == 'p':
                ret += 1
                break
            elif board[t][y] == 'B':
                break
            t += 1

        t = y
        while t >= 0:
            if board[x][t] == 'p':
                ret += 1
                break
            elif board[x][t] == 'B':
                break
            t -= 1

        t = y
        while t < n:
            if board[x][t] == 'p':
                ret += 1
                break
            elif board[x][t] == 'B':
                break
            t += 1

        return ret

class Solution2(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int

        thought: try 4 directions, stop when encounter B or p or wall
        if meet p before wall or B, then ret += 1

        first need to find R pos.
        05/05/2022 10:49	Accepted	26 ms	13.7 MB	python
        """

        m, n= len(board), len(board[0])
        x,y = 0,0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    x,y = i,j


        #  try 4 directions, simplified code
        ret = 0
        for i, j in [[0,1], [0,-1], [1, 0], [-1,0]]:
            a, b = x + i, y + j
            while 0 <= a < m and 0 <= b < n:
                if board[a][b] == 'p': ret += 1
                if board[a][b] != '.': break
                a, b = a + i, b + j
        return ret