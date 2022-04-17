#
# Create by Hua on 4/16/22.
#

"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

    Players take turns placing characters into empty squares ' '.
    The first player A always places 'X' characters, while the second player B always places 'O' characters.
    'X' and 'O' characters are always placed into empty squares, never on filled ones.
    The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.



Constraints:

    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= rowi, coli <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.


"""


class Solution(object):

    def tictactoe(self, moves):
        def is_win(p):
            n = 3
            board = [[0] * n for i in range(n)]  # init n*n array with 0
            for i,j in p:
                board[i][j] = 1


            # check rows
            for i in range(n):
                if sum(board[i]) == 3:
                    return True

            # check col
            for j in range(n):
                if sum([row[j] for row in board]) == 3:
                    return True

            # check diagonal
            diag = 0
            r_diag = 0
            for i in range(n):
                for j in range(n):
                    if i == j:
                        diag += board[i][j]
                    if i + j == n-1:
                        r_diag += board[i][j]

            if diag == 3 or r_diag == 3:
                return True

            return False


        """
        :type moves: List[List[int]]
        :rtype: str
        
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        thought: have a is_win function to check if win.
        in main function, check if A or B wins, if both not, when there
        are 9 moves, then it's a Draw, else it's Pending
        
        04/17/2022 10:32	Accepted	18 ms	13.5 MB	python
        easy - medium 10-20 min. many details.
        """

        a = moves[0::2]
        b = moves[1::2]
        if is_win(a):
            return "A"
        if is_win(b):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

