#
# Create by Hua on 7/26/22
#

"""
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.



Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""


class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: come up with solution after reading the hint:
        1. we know the final length of subarray
        2. we can check each subarray to find out how many 0 inside, which is the swap we need. (sliding window)
        3. to solve the circular array, we can double the array.
        1010
        10101010

        07/26/2022 11:42	Accepted	1267 ms	17.7 MB	python
        medium
        20-30min.
        sliding window.
        """
        window = nums.count(1)     # sliding window size
        nums = nums * 2            # double the array
        zero_count = nums[:window].count(0)  # count of 0, which is the swap we need
        ret = len(nums)
        i = 0
        while i + window < len(nums):
            if nums[i] == 0:
                zero_count -= 1
            if nums[i+window] == 0:
                zero_count += 1
            i += 1
            ret = min(ret, zero_count)
            if ret == 0: return 0
        return ret





