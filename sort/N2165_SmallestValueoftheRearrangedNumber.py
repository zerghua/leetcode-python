#
# Create by Hua on 7/25/22
#

"""
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.



Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310.
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.


Constraints:

-10^15 <= num <= 10^15

"""


class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int

        thought: sort the num.
        07/25/2022 09:40	Accepted	19 ms	13.3 MB	python
        medium - easy
        10 min.
        sort and coding.

        better solution, just swap:
        https://leetcode.com/problems/smallest-value-of-the-rearranged-number/discuss/1748511/Sort-and-Swap
        We convert num to a string and then:
            If negative: sort descending, excluding the sign.
            If positive: sort ascending
            Find first non-zero number (e.g. 000237)
            Swap it with the first number (e.g. 200037)
        """
        if num < 0:
            a = list(str(-num))
            return int("".join(sorted(a, reverse=True))) * -1

        if num < 10:
            return num

        # now num >= 10
        a = list(str(num))
        zeros = a.count("0")
        a.sort()
        ret = list(a[zeros])
        ret.extend(["0"] * zeros)
        ret.extend(a[zeros+1:])
        return int("".join(ret))



