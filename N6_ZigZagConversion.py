#
# Created by Hua on 8/16/2016
#

"""
 The string "PAYPALISHIRING" is written in a zigzag pattern
 on a given number of rows like this: (you may want to display
 this pattern in a fixed font for better legibility)

 P   A   H   N
 A P L S I I G
 Y   I   R

 And then read line by line: "PAHNAPLSIIGYIR"

 Write the code that will take a string and make this conversion given a number of rows:

 string convert(string text, int nRows);

 convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

class Solution(object):
    # 128 ms
    # use offset to update position
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows <= 1): return s;
        wordList = [""]*numRows    # list of arrays
        index=0; offset = 1
        for c in s:
            wordList[index] += c
            if index == 0: offset = 1
            elif index == numRows-1: offset = -1
            index += offset
        return "".join(wordList)