#
# Create by Hua on 5/12/22
#


"""
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.



Example 1:

Input: aliceSizes = [1,1], bobSizes = [2,2]
Output: [1,2]
Example 2:

Input: aliceSizes = [1,2], bobSizes = [2,3]
Output: [1,2]
Example 3:

Input: aliceSizes = [2], bobSizes = [1,3]
Output: [2,3]


Constraints:

1 <= aliceSizes.length, bobSizes.length <= 104
1 <= aliceSizes[i], bobSizes[j] <= 105
Alice and Bob have a different total number of candies.
There will be at least one valid answer for the given input.

"""


class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]

        thought: math, sort list to make solution o(nlogn) rather than o(n^2),
        key is to find the abs(x-y) == abs(sum(a) - sum(b))/2
        TLE, this solution is not truly o(nlogn)

        second thought: use binary search to make it real o(nlogn)
        05/12/2022 11:26	Accepted	551 ms	15.2 MB	python
        easy - medium 20-30 mins. binary search

        better code use set(below solution assumes a >= b):
        https://leetcode.com/problems/fair-candy-swap/discuss/161269/C%2B%2BJavaPython-Straight-Forward
            def fairCandySwap(self, A, B):
                dif = (sum(A) - sum(B)) / 2
                A = set(A)
                for b in set(B):
                    if dif + b in A:
                        return [dif + b, b]
        """
        import bisect

        is_alice_larger = False
        if sum(aliceSizes) >= sum(bobSizes):
            is_alice_larger = True
            aliceSizes, bobSizes = bobSizes, aliceSizes

        diff = (sum(bobSizes) - sum(aliceSizes)) / 2
        b = sorted(bobSizes)
        for i in sorted(aliceSizes):
            v = diff + i
            j = bisect.bisect_left(b, v)   # j is index
            if j != len(bobSizes) and b[j] == v:
                if is_alice_larger: return [v,i]
                return [i,v]
        return None


