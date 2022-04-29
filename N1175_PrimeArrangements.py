#
# Create by Hua on 4/29/22.
#

"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input: n = 100
Output: 682289015



Constraints:

    1 <= n <= 100


"""


class Solution(object):
    def numPrimeArrangements(self, n):
        def is_prime(n):
            if n == 2 or n == 3: return True
            if n == 1 or n % 2 == 0: return False
            for i in range(3, 1 + int(n**0.5), 2):
                if n % i == 0:
                    return False
            return True

        """
        :type n: int
        :rtype: int

        thought: math. get count of prime and non-prime between [1,n]
        then do product for each position. 1 is not prime
        
        04/29/2022 14:48	Accepted	25 ms	13.3 MB	python
        easy - medium. 20-30 min.
        """

        p = 0  # number of prime
        for i in range(1, n+1):
            if is_prime(i):
                p += 1

        q = n - p
        ret = 1
        m = 10**9 + 7

        for i in range(1, p+1): # prime
            ret *= i
            ret %= m

        for i in range(1, q+1): # non-prime
            ret *= i
            ret %= m

        """
        for i in range(1, n+1):
            if is_prime(i):
                ret *= p
                ret %= m
                p -= 1
            else:
                ret *= q
                ret %= m
                q -= 1
        """

        return ret
