#
#  Create by Hua on 8/31/2016
#


"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

# 40ms
# stack operation to match pair.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0: return True

        stack = []
        for c in s:
            if c in ['(', '{', '[']: stack.append(c)
            elif len(stack) != 0:
                if c == ')' and stack[-1] == '(': stack.pop()
                elif c == ']' and stack[-1] == '[': stack.pop()
                elif c == '}' and stack[-1] == '{': stack.pop()
                else: return False
            else: return False
        return len(stack) == 0

