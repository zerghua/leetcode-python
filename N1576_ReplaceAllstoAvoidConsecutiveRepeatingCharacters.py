#
# Create by Hua on 4/2/22.
#

"""
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".



Constraints:

    1 <= s.length <= 100
    s consist of lowercase English letters and '?'.


"""


class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str

        thought: check "?" left and right, replace ? with non-repeat char.
        04/02/2022 10:19	Accepted	38 ms	13.7 MB	python
        easy 5-10 min.
        """

        n = len(s)
        ret = list(s)
        for i in range(n):
            if ret[i] == "?":
                left = ""
                if i-1 >= 0:
                    left = ret[i-1]
                right = ""
                if i+1 < n:
                    right = ret[i+1]
                for c in string.ascii_lowercase:
                    if c != left and c != right:
                        ret[i] = c
                        break
        return "".join(ret)