#
# Create by Hua on 5/11/22
#


"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        thought: 2 pointers to do in-place, left and right,
        05/11/2022 15:08	Accepted	92 ms	14.1 MB	python
        easy, 5min.
        """

        n = len(nums)
        i,j = 0, n-1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j -= 1
            else:  # swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums

