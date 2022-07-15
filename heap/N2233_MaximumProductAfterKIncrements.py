#
# Create by Hua on 7/15/22
#

"""
You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo.



Example 1:

Input: nums = [0,4], k = 5
Output: 20
Explanation: Increment the first number 5 times.
Now nums = [5, 4], with a product of 5 * 4 = 20.
It can be shown that 20 is maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.
Example 2:

Input: nums = [6,3,3,2], k = 2
Output: 216
Explanation: Increment the second number 1 time and increment the fourth number 1 time.
Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is maximum product possible, so we return 216.
Note that there may be other ways to increment nums to have the maximum product.


Constraints:

1 <= nums.length, k <= 105
0 <= nums[i] <= 106

"""


class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        thought: use min heap to store the data and increase 1 to the top of heap
        07/15/2022 15:30	Accepted	6596 ms	23.1 MB	python
        medium - easy heap.
        5-10 min.
        """
        import heapq
        heapq.heapify(nums)

        while k > 0:
            v = heapq.heappop(nums)
            heapq.heappush(nums, v+1)
            k -= 1

        ret = 1
        mod = 10**9 + 7
        for n in nums:
            ret = ret * n % mod
        return ret
