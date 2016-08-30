#
#  Create by Hua on 8/30/2016
#


"""
Write a function to find the longest common prefix string amongst an array of strings.

"""

# 48 ms
# vertical scanning of each string
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs is None or len(strs) == 0: return ""

        for col in range(0,len(strs[0])):
            char = strs[0][col]
            for j in range(1,len(strs)):
                if(col >= len(strs[j]) or strs[j][col] != char):
                    return strs[0][:col]

        return strs[0]