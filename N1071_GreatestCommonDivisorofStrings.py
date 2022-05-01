#
# Create by Hua on 5/1/22.
#

"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""



Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.


"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        abc
        012
        thought: BF to try all prefix of the small string
        05/01/2022 12:02	Accepted	26 ms	13.5 MB	python
        easy - medium 5-10 min.
        1 corner case.
        """


        if len(str2) > len(str2):
            str1, str2 = str2, str1

        m, n = len(str1), len(str2)
        for i in range(m, 0, -1):
            if m % i == 0 and n % i == 0:
                x = str1[:i]
                if x * (m/i) == str1 and x * (n/i) == str2:
                    return x
        if str1[0] * m == str1 and str1[0] * n == str2: # corner case, single char
            return str1[0]

        return ""