#
# Create by Hua on 3/24/22.
#

"""
Given an array nums, return true if the array was originally sorted in
non-decreasing order, then rotated some number of positions (including zero).
Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same
length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.



Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.



Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100

"""


class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        thought: brute force, check each possible rotation.
        faster solution, check increasing order, include last to first,
        should there be only 1 deceasing.

        03/24/2022 14:38	Accepted	36 ms	13.2 MB	python
        easy 5min. math.
        """


        n = len(nums)
        count = 0
        nums.append(nums[0])
        for i in range(1, n+1):
            if nums[i] < nums[i-1]:
                count += 1

            if count > 1: return False

        return count <= 1

