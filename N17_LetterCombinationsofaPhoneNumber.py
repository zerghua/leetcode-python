#
# Created by Hua on 8/30/2016
#

"""
 Given a digit string, return all possible letter combinations that the number could represent.

 A mapping of digit to letters (just like on the telephone buttons) is given below.

 Input:Digit string "23"
 Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

 Note:
 Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

# 48 ms
class Solution(object):
    def dfs(self, digits, map, ret, start, cur_str):
        if len(digits) == len(cur_str):
            ret.append(cur_str)
            return

        strs = map[int(digits[start])]
        for i in range(len(strs)):
            self.dfs(digits,map,ret,start+1, cur_str+strs[i])


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if digits == None or len(digits) == 0: return ret

        map = ["", "*", "abc",
               "def", "ghi", "jkl",
               "mno", "pqrs", "tuv","wxyz"]

        self.dfs(digits, map, ret, 0, "")
        return ret