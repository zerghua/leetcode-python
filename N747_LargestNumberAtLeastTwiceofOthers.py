#
# Create by Hua on 5/17/22
#


"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.



Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.


Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.

"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: find largest number can compare it with all others.
        can also use 1 pass to find largest and second largest and compare
        05/17/2022 09:57	Accepted	36 ms	13.1 MB	python
        easy 5 min.
        """
        m = max(nums)
        ret = -1
        for i in range(len(nums)):
            n = nums[i]
            if n != m:
                if n != 0 and m / n < 2:
                    return -1
            else:
                ret = i
        return ret