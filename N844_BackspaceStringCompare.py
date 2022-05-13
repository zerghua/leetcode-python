#
# Create by Hua on 5/13/22
#


"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?


"""


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        thought: stack solution is o(n) space and o(n) time
        for follow up question, require o(1) space, are we looking for multiple pointers solution?
        turns out, we need to scan from right to left, store # and skip char if we have num(#) > 0
        until we end at left

        05/13/2022 14:14	Accepted	24 ms	13.3 MB	python
        medium 20-30 min.
        """

        m, n = len(s), len(t)
        i, j = m-1, n-1
        count_s = count_t = 0
        while 1:
            while i >= 0 and (count_s != 0 or s[i] == '#'):
                if s[i] == '#':
                    count_s += 1
                else:
                    count_s -= 1
                i -= 1

            while j >= 0 and (count_t != 0 or t[j] == '#'):
                if t[j] == '#':
                    count_t += 1
                else:
                    count_t -= 1
                j -= 1

            if i>=0 and j>=0 and s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break
        return i == -1 and j == -1


class Solution2(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        thought: stack solution is o(n) space and o(n) time
        05/13/2022 14:17	Accepted	19 ms	13.5 MB	python
        easy 5 min.
        """
        a,b = list(), list()
        for c in s:
            if c == '#':
                if a: a.pop()
            else:
                a.append(c)

        for c in t:
            if c == '#':
                if b: b.pop()
            else:
                b.append(c)

        return a == b