#
# Create by Hua on 4/6/22.
#

"""
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.



Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.



Constraints:

    1 <= nums.length <= 105
    0 <= k <= nums.length
    nums[i] is 0 or 1


"""


class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        thought: store last 1 position, and compare with current one distance
        04/06/2022 10:56	Accepted	881 ms	17.8 MB	python
        easy 5min.
        """
        last = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if last != -1:
                    if i - last - 1 < k:
                        return False
                last = i
        return True

