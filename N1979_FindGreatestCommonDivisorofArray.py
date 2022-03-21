#
# Create by Hua on 3/21/22.
#

"""

Given an integer array nums, return the greatest common divisor of the smallest
number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer
that evenly divides both numbers.


Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.


Constraints:

    2 <= nums.length <= 1000
    1 <= nums[i] <= 1000

"""


class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        easy, find gcd.
        5-10 min, math.
        03/21/2022 11:13	Accepted	70 ms	13.6 MB	python

        """
        #import math
        #return math.gcd(min(nums), max(nums)) # python 3.5
        # 03/21/2022 11:10	Accepted	84 ms	14 MB	python3

        low = min(nums)
        high = max(nums)
        for i in range(high, 1, -1):
            if high >= i and low>=i and high%i ==0 and low %i == 0:
                return i
        return 1


