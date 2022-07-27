#
# Create by Hua on 7/27/22
#

"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.



Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0].
Changing s[0] to either '(' or ')' will not make s valid.


Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.

"""


class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool

        thought: if we encounter ")" and it's locked, there should be a locked "("  or unlocked exist.
        if length is odd, it's always false.
        fail to work out this one.

        https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646594/Left-to-right-and-right-to-left
        A useful trick (when doing any parentheses validation) is to greedily check balance left-to-right, and then right-to-left.

        Left-to-right check ensures that we do not have orphan ')' parentheses.
        Right-to-left checks for orphan '(' parentheses.

        https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646582/Python3-Java-C%2B%2B-Counting-Brackets-O(n)

        should check both side
        "))(("
        "0011"

        ()
        11

        07/27/2022 11:44	Accepted	373 ms	18.3 MB	python
        medium.
        didn't come up with the correct solution.

        """
        if len(s) % 2 == 1: return False
        total = left = right = 0
        for i in range(len(s)):
            if locked[i] == '0':  total += 1
            elif s[i] == '(': left += 1
            elif s[i] == ')': right += 1
            if total + left - right < 0: return False

        total = left = right = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':  total += 1
            elif s[i] == '(': left += 1
            elif s[i] == ')': right += 1
            if total - left + right < 0: return False
        return True
