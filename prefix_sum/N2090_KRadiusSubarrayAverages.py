#
# Create by Hua on 8/1/22
#

"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.


Example 1:


Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
Example 2:

Input: nums = [100000], k = 0
Output: [100000]
Explanation:
- The sum of the subarray centered at index 0 with radius 0 is: 100000.
  avg[0] = 100000 / 1 = 100000.
Example 3:

Input: nums = [8], k = 100000
Output: [-1]
Explanation:
- avg[0] is -1 because there are less than k elements before and after index 0.


Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105

"""


class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        thought: prefix sum.
        if k == 0, return nums
        else:
        if: len(nums) < 2*k + 1
            return [-1] * len(nums)
        else:
            total = sum(nums[:2*k+1])  # the sliding window should be 2k+1

        k = 1, n = 5,  right: n - 1 - k(inclusive)
        window = 2*k+1 = 3
        0,1,2,3,4
        -1    -1
        [0,1,2], remove (i), add(i+window), remove(0), add(3)
         [1,2,3], remove(1), remove (4)
          [2,3,4] i + window < n

        08/01/2022 17:50	Accepted	2274 ms	32.9 MB	python
        medium
        20-30min.
        the code is a bit tricky, took me some time to figure out need to skip the last increment or will be
        out of index.
        """

        if k == 0: return nums
        n = len(nums)
        window = 2 * k + 1
        if n < window:
            return [-1] * n

        total = sum(nums[:window])
        ret = [-1] * k

        for i in range(0, n - window+1):  # n =5, window = 3,   [0,2]
            ret.append(total / window)
            total -= nums[i]   # prepapre for the next round
            if i+window < n:  total += nums[i+window]  # to avoid out of index

        ret += [-1] * k
        return ret

