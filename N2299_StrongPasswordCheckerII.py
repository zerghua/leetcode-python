#
# Create by Hua on 7/13/22
#

"""
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.



Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.


Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".

"""


class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool

        thought: do a require, lots of if.

        It has at least 8 characters.
        It contains at least one lowercase letter.
        It contains at least one uppercase letter.
        It contains at least one digit.
        It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
        It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
        Given a string password, return true if it is a strong password. Otherwise, return false.

        07/13/2022 11:49	Accepted	29 ms	13.5 MB	python
        easy 5-10 min. can return early for performance.
        """

        longer_than_8 = len(password) >= 8
        has_lower = has_upper = has_digit = has_special = False
        pre = ""
        special = "!@#$%^&*()-+"
        for c in password:
            if c.islower(): has_lower = True
            elif c.isupper(): has_upper = True

            if c.isdigit(): has_digit = True
            if c in special: has_special = True

            if c == pre: return False
            pre = c

        return longer_than_8 and has_lower and has_upper and has_digit and has_special


