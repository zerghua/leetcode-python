#
#  Create by Hua on 1/29/2022
#

"""
You are given a string title consisting of one or more words separated by a single space, where each word consists
of English letters. Capitalize the string by changing the capitalization of each word such that:

    If the length of the word is 1 or 2 letters, change all letters to lowercase.
    Otherwise, change the first letter to uppercase and the remaining letters to lowercase.

Return the capitalized title.



Example 1:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"
Explanation:
Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.

Example 2:
Input: title = "First leTTeR of EACH Word"
Output: "First Letter of Each Word"
Explanation:
The word "of" has length 2, so it is all lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.

Example 3:
Input: title = "i lOve leetcode"
Output: "i Love Leetcode"
Explanation:
The word "i" has length 1, so it is lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.



Constraints:
    1 <= title.length <= 100
    title consists of words separated by a single space without any leading or trailing spaces.
    Each word consists of uppercase and lowercase English letters and is non-empty.

"""


class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str

        easy: 5 min

        thought: 1. convert all chars to lower case; 2. split the string into list of strings; 3. for each string
        count the length, if length > 2, then capitalize the first letter, else do nothing; 4. concatenate the list
        of strings

        01/29/2022 10:23	Accepted	27 ms	13.4 MB	python
        """
        ret = list()
        t_list = title.lower().split(" ")
        for s in t_list:
            if len(s) > 2:
                ret.append(s[0].upper() + s[1:])
            else:
                ret.append(s)
        return " ".join(ret)