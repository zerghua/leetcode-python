#
# Create by Hua on 3/23/22.
#

"""
You are given coordinates, a string that represents the coordinates of a
square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate
will always have the letter first, and the number second.



Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false



Constraints:
    coordinates.length == 2
    'a' <= coordinates[0] <= 'h'
    '1' <= coordinates[1] <= '8'
"""


class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool

        Convert the coordinates to (x, y) - that is, "a1" is (1, 1), "d7" is (4, 7).
        Try add the numbers together and look for a pattern.
        even is black, odd is white
        03/23/2022 13:39	Accepted	15 ms	13.5 MB	python
        easy 5 mins. need to figure out the pattern.
        """

        a = ord(coordinates[0]) - ord('a') + 1
        b = int(coordinates[1])
        if (a + b) % 2 == 1:
            return True
        return False
