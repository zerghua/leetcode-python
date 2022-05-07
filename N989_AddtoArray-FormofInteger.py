#
# Create by Hua on 5/7/22.
#

"""
The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.



Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021



Constraints:

    1 <= num.length <= 104
    0 <= num[i] <= 9
    num does not contain any leading zeros except for the zero itself.
    1 <= k <= 104


"""


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]

        thought: convert num list to number and add to k, and make the final
        number back into a list. math or string

        it will not overflow

        05/07/2022 12:09	Accepted	8506 ms	13.9 MB	python
        easy 5-10min.
        """

        r = 0
        ret = 0
        for n in num[::-1]:  # from right to left
            ret += n * (10**r)
            r += 1

        ret += k

        return list(str(ret))



