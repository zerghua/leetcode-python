#
# Create by Hua on 4/2/22.
#

"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"



Constraints:

    0 <= n <= 231 - 1


"""


class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str

        thought: add point every 3 digits from right to left.
        04/02/2022 16:34	Accepted	16 ms	13.4 MB	python
        easy 5-10 mins.
        """
        s = str(n)
        ret = list()
        for i in range(len(s)-3, -1, -3):
            ret.insert(0, s[i:i+3])
        if len(s) % 3 != 0:
            ret.insert(0, s[0: len(s)%3])

        return ".".join(ret)
