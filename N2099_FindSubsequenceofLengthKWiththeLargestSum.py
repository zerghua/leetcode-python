#
#  Create by Hua on 1/29/2022
#

"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that
has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing
the order of the remaining elements.



Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].



Constraints:
    1 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5
    1 <= k <= nums.length

"""


class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        easy 5 min, used a list lookup and remove.

        thought: sort list, find the largest k items and store them in a list. loop through original list,
        match each num in the list, if there is a match, move it to the result list.

        01/29/2022 13:55	Accepted	79 ms	13.5 MB	python
        """

        sorted_list = sorted(nums,reverse=True)[0:k]
        ret = list()
        for i in nums:
            if len(sorted_list) == 0: break
            if i in sorted_list:
                ret.append(i)
                sorted_list.remove(i)

        return ret

