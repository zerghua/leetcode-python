#
# Create by Hua on 8/3/22
#

"""
A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.

originalText is placed first in a top-left to bottom-right manner.


The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.

encodedText is then formed by appending all characters of the matrix in a row-wise fashion.


The characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.

For example, if originalText = "cipher" and rows = 3, then we encode it in the following manner:


The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = "ch ie pr".

Given the encoded string encodedText and number of rows rows, return the original string originalText.

Note: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one possible originalText.



Example 1:

Input: encodedText = "ch   ie   pr", rows = 3
Output: "cipher"
Explanation: This is the same example described in the problem description.
Example 2:


Input: encodedText = "iveo    eed   l te   olc", rows = 4
Output: "i love leetcode"
Explanation: The figure above denotes the matrix that was used to encode originalText.
The blue arrows show how we can find originalText from encodedText.
Example 3:


Input: encodedText = "coding", rows = 1
Output: "coding"
Explanation: Since there is only 1 row, both originalText and encodedText are the same.


Constraints:

0 <= encodedText.length <= 106
encodedText consists of lowercase English letters and ' ' only.
encodedText is a valid encoding of some originalText that does not have trailing spaces.
1 <= rows <= 1000
The testcases are generated such that there is only one possible originalText.

"""


class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str

        thought:
        for row == 3, col == 1, it can fit at most 1 = 1 chars
        0
        0
        0

        for row == 3, col == 2, it can fit at most 2+1 = 3 chars
        0 0
        0 0
        0 0

        for row == 3, col == 3, it can fit at most 3+2+1 = 6 chars
        0 0 0
        0 0 0
        0 0 0
        for row == 3, col == 4, it can fit at most 3+3+2+1 = 9 chars
        0 0 0 0
        0 0 0 0
        0 0 0 0

        for row == 3, col == 5, it can fit at most 3+3+3+2+1 = 12 chars
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

        for row == 2, col = 1, it can fit 1 chars
        0
        0

        for row == 2, col = 2, it can fit 2+1=3 chars
        0 0
        0 0

        for row == 2, col = 3, it can fit 2+2+1=5 chars
        0 0 0
        0 0 0

        so number of chars can fit formula: sum(1...col) caped by row. sum[1:row] + max(0,col-row)*row

        "i love leetcode" == 15
        for row = 4, if col ==4, sum(1:4) = 10, if col ==5, 10+4=14

        1. find col
        2. 1 row len == col, 2 row len == col - 1, n row len == col-row+1
        3. split string into row list
        4. build final string

        wow, the actual len(encodedText) == row*col, much easier than I calculated

        #  1. get col
        n = len(encodedText)
        col = rows
        t = sum(range(col+1))
        if t < n:
            col += (n - t) % rows + 1
        else:
            while t > n:  # at most 1000 times, row <=1000
                t -= col
                col -= 1
            col += 1

        08/03/2022 14:15	Accepted	791 ms	45.1 MB	python
        medium
        problem description not very clear, or it will be much easier than I thought originally
        simulation
        30-60min
        """
        if rows == 1:
            return encodedText

        # 1. get col
        n = len(encodedText)
        col = n / rows

        # 2. split encoded into list
        lt = []
        i, size = 0, col
        for _ in range(rows):
            lt.append(encodedText[i:i+size])
            i += size

        # 3. build final string
        ret = []
        for i in range(col):
            j = i
            for s in lt:
                c = s[j] if j < len(s) else ""
                ret.append(c)
                j += 1
        return "".join(ret).rstrip()

