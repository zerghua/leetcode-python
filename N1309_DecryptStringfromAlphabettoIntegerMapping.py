#
# Create by Hua on 4/16/22.
#

"""
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:

Input: s = "1326#"
Output: "acz"



Constraints:

    1 <= s.length <= 1000
    s consists of digits and the '#' letter.
    s will be a valid string such that mapping is always possible.


"""


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        thought: if 3rd char is #, it's definitely over 10.
        04/16/2022 10:50	Accepted	25 ms	13.6 MB	python
        easy 5 - 10 min. char, int conversion use ord to convert char to int,
        and use chr to convert int to char.
        """
        n = len(s)
        i = 0
        ret = list()
        while i < n:
            if i+2 < n and s[i+2] == '#':
                ret.append(chr(int(s[i:i+2]) -1 + ord('a')))
                i += 3
            else:
                ret.append(chr(int(s[i]) -1 + ord('a')))
                i += 1
        return "".join(ret)