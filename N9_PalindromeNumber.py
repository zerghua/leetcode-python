#
# Created by Hua on 8/29/2016
#

"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

"""

# 304 ms
# strip left and right integer and compare
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div=1
        while x/div >= 10:
            div *= 10

        while x !=0:
            left = x/div
            right = x%10
            if left != right:
                return False
            x = (x%div)/10
            div /= 100

        return True
