#
# Create by Hua on 5/7/22.
#

"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5

Example 2:

Input: nums = [1,2,1]
Output: 0



Constraints:

    3 <= nums.length <= 104
    1 <= nums[i] <= 106


"""


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: math, if sum of 2 sides > largest side, then a triangle
        can be formed. else return 0

        don't assume len(nums) == 3

        sort list, and pick 3 from the largest and do the math
        05/07/2022 12:19	Accepted	279 ms	14.5 MB	python
        easy 5-10min. missed the corner case of assuming len(nums) == 3
        """
        s = sorted(nums)
        for i in range(len(s) - 3, -1, -1):
            a,b,c = s[i], s[i+1], s[i+2]
            if a + b > c:
                return a+b+c
        return 0
