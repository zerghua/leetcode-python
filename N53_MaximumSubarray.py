#
# Created by Hua on 9/7/2016
#

"""
 Find the contiguous subarray within an array (containing at least one number)
 which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

"""

# 49 ms  201 / 201 test cases passed.
# o(n) time, array operation. condition on if local_sum>0
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, local_max = -2**31, 0
        for a_number in nums:
            local_max += a_number
            ret = max(local_max, ret)
            local_max = max(local_max, 0)
        return ret