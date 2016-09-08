#
# Created by Hua on 9/7/2016
#

"""
 The set [1,2,3,...,n] contains a total of n! unique permutations.

 By listing and labeling all of the permutations in order,
 We get the following sequence (ie, for n = 3):

 "123"
 "132"
 "213"
 "231"
 "312"
 "321"

 Given n and k, return the kth permutation sequence.

 Note: Given n will be between 1 and 9 inclusive.

 https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n
"""

# 65 ms 200 / 200 test cases passed.
# math, k / (n-1)! for current number,  k%(n-1)! for next iteration.
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list("123456789")
        factorial = 1
        for i in range(1, n+1):
            factorial *= i

        ret = ""
        k -= 1
        for i in range(n, 0, -1):
            factorial /= i
            ret += numbers.pop(k/factorial)  ## pop is for index, remove is for value
            k %= factorial
        return ret

