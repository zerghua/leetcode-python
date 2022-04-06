#
# Create by Hua on 4/6/22.
#

"""
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.



Example 1:

Input: nums = [4,3,10,9,8]
Output: [10,9]
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements.

Example 2:

Input: nums = [4,4,7,6,7]
Output: [7,7,6]
Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to returned in non-decreasing order.

Example 3:

Input: nums = [6]
Output: [6]



Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 100

"""


class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        thought: sort and pick largest nums from list and compare with rest
        04/06/2022 14:08	Accepted	56 ms	13.4 MB	python
        easy 5 min. sort
        """

        total = sum(nums)
        s = sorted(nums, reverse=True)
        cur = 0
        ret = list()
        for n in s:
            cur += n
            total -= n
            ret.append(n)
            if cur > total:
                break

        return ret
