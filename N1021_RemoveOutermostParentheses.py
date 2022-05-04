#
# Create by Hua on 5/4/22.
#

"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".



Constraints:

    1 <= s.length <= 105
    s[i] is either '(' or ')'.
    s is a valid parentheses string.


"""


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str

        thought: find the primitive decomposition(by using a counter),
        and remove its outer parentheses of each part and return.
        (())
        0123

        05/04/2022 10:29	Accepted	35 ms	13.8 MB	python
        easy 5 - 10min. need to understand the problem
        """

        i, j = 0,0
        counter = 0
        ret = list()
        for j in range(len(s)):
            if s[j] == "(":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                ret.append(s[i+1:j]) # remove outer parentheses
                i = j+1
        return "".join(ret)


