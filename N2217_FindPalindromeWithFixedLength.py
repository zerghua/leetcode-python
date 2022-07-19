#
# Create by Hua on 7/19/22
#

"""
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.



Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.
Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.


Constraints:

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15

"""


class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]

        thought:
        peeked hint:
        Since a palindrome reads the same forwards and backwards, consider how you can efficiently find the
        first half (ceil(intLength/2) digits) of the palindrome.

        if len = 1
        (0 - 9) 10

        if len = 2
        (11,22,...99) 9

        if len = 3, we have palindrome:
        101, 111, 121, 131, 202, 212, ... 999
        (10 - 99)

        len=4
        1001, 1111, ... 2002, ... 9999
        (10 - 99)  99-10 +1=90

        len=5
        10001, 10101,10201, ... 99999
        (100,101,...999) 999-100+1=900

        half_len = ceil(len/2)
        max_index = 10^half_len - 10^(half_len - 1)  index start from 1

        07/19/2022 14:12	Accepted	826 ms	23.6 MB	python
        medium. find pattern, quite several cases.
        20-30min.
        """

        ret = list()
        if intLength == 1:  # interesting, 0 is not palindrome according the test case.
            for n in queries:
                if n <= 9:
                    ret.append(n)
                else:
                    ret.append(-1)
        elif intLength == 2:
            for n in queries:
                if n <= 9:
                    ret.append(n*10 + n)
                else:
                    ret.append(-1)
        else:
            is_odd = True if intLength % 2 == 1 else False
            half_len = intLength / 2 if intLength % 2 == 0 else intLength / 2 + 1
            max_index = 10**(half_len) - 10**(half_len - 1)
            start = 10**(half_len - 1)
            for n in queries:
                if n <= max_index:
                    first_half = str(start + n - 1)
                    if is_odd:
                        num = int(first_half[:-1] + first_half[::-1])
                    else:
                        num = int(first_half + first_half[::-1])
                    ret.append(num)
                else:
                    ret.append(-1)
        return ret

