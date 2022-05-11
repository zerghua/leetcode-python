#
# Create by Hua on 5/11/22
#


"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.



Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]


Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000


Follow Up: Could you solve it in-place?


"""


class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        thought: in-place solution, 2 points, 1 point odd index, 1 point even index,
        and switch them when necessary

        05/11/2022 10:32	Accepted	316 ms	15.3 MB	python
        easy 5-10 min. in-place 2 pointers.
        """
        i, j = 0, 1
        n = len(nums)
        while i < n and j<n:
            while i<n and nums[i] % 2 == 0:  # skip if even
                i += 2
            while j<n and nums[j] % 2 == 1:  # skip if odd
                j += 2

            if i < n:
                nums[i], nums[j] = nums[j], nums[i]  # switch
            i += 2
            j += 2
        return nums


class Solution2(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        thought: in-place solution, 2 points, 1 point odd index, 1 point even index,
        and switch them when necessary

        05/11/2022 10:35	Accepted	219 ms	15.3 MB	python
        easy 5-10 min. in-place 2 pointers.
        simplified code
        """
        i, j = 0, 1
        n = len(nums)
        while i < n and j<n:
            if nums[i] % 2 == 0:  # even in-place
                i += 2
            elif nums[j] % 2 == 1:  # odd in-place
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]  # switch when both misplaced
                i += 2
                j += 2
        return nums
