#
# Create by Hua on 4/6/22.
#

"""
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.



Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.



Constraints:

    1 <= s.length <= 500
    s consists of only lowercase English letters and/or digits.


"""


class Solution(object):
    def reformat2(self, s):
        """
        :type s: str
        :rtype: str

        thought: put numbers and chars into 2 lists, they abs length diff
        should be <= 1, if so, assemble them
        04/06/2022 12:39	Accepted	52 ms	13.6 MB	python
        easy 5-10min. long code
        """

        a = list()
        b = list()
        for c in s:
            if c in "0123456789":
                a.append(c)
            else:
                b.append(c)

        if abs(len(a) - len(b)) > 1:
            return ""

        m = a if len(a) >= len(b) else b
        n = a if len(a) < len(b) else b
        ret = list()
        for i in range(len(n)):
            ret.append(m[i])
            ret.append(n[i])

        if len(m) != len(n):
            ret.append(m[-1])
        return "".join(ret)



    def reformat(self, s):
        """
        :type s: str
        :rtype: str

        thought: put numbers and chars into 2 lists, they abs length diff
        should be <= 1, if so, assemble them
        04/06/2022 12:44	Accepted	28 ms	13.7 MB	python
        easy 5-10min. simplified code
        """

        a = list()
        b = list()
        for c in s:
            if c in "0123456789":
                a.append(c)
            else:
                b.append(c)

        if abs(len(a) - len(b)) > 1:
            return ""

        if len(a) < len(b):
            a,b = b, a
        ret = list()
        for i in range(len(b)):
            ret.append(a[i])
            ret.append(b[i])

        if len(a) != len(b):
            ret.append(a[-1])
        return "".join(ret)