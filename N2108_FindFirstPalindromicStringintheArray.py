#
#  Create by Hua on 1/29/2022
#

"""
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.



Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.



Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.

"""


class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str

        easy 5 min

        thought: loop through all the strings in the list, do a palindrome check on each string, return the first
        palindrome one, if none found return ""

        01/29/2022 11:19	Accepted	137 ms	13.9 MB	python
        """
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]: return False
                i+=1
                j-=1
            return True

        for s in words:
            if isPalindrome(s): return s
        return ""

