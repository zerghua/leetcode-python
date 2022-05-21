#
# Create by Hua on 5/21/22.
#

"""
You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

    If original is found in nums, multiply it by two (i.e., set original = 2 * original).
    Otherwise, stop the process.
    Repeat this process with the new number as long as you keep finding the number.

Return the final value of original.



Example 1:

Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation:
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.

Example 2:

Input: nums = [2,7,9], original = 4
Output: 4
Explanation:
- 4 is not found in nums. Thus, 4 is returned.



Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i], original <= 1000


"""


class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int

        thought: use set to check number faster
        05/21/2022 11:39	Accepted	48 ms	13.6 MB	python
        easy 2 min.

        """

        st = set(nums)
        i = original
        while 1:
            if i not in st:
                return i
            i = i*2

