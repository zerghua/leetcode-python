#
# Create by Hua on 3/21/22.
#

"""
You are given a string num, representing a large integer. Return the
largest-valued odd integer (as a string) that is a non-empty substring of num,
or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.



Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52".
"5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.



Constraints:
    1 <= num.length <= 10^5
    num only consists of digits and does not contain any leading zeros.

"""


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str

        thought: scan from right to left and found the first odd number,
        then return [0:i]

        03/21/2022 18:31	Accepted	97 ms	18.6 MB	python

        easy 5 min, some corner cases.
        """
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]

        return ""