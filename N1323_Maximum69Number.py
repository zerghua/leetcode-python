#
# Create by Hua on 4/16/22.
#

"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.



Constraints:

    1 <= num <= 104
    num consists of only 6 and 9 digits.


"""


class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int

        thought: scan from left to right, find the first 6 and change it
        to 9, and return.
        04/16/2022 10:14	Accepted	19 ms	13.5 MB	python
        easy 1 min. string replace
        """
        return str(num).replace("6", "9", 1)

