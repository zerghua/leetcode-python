#
# Create by Hua on 4/16/22.
#

"""
Given an array nums of integers, return how many of them contain an even number of digits.



Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.



Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 105


"""


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: convert to string. or do math.
        04/16/2022 15:27	Accepted	38 ms	13.6 MB	python
        easy 5 min.
        """
        ret = 0
        for n in nums:
            if len(str(n)) % 2 == 0 :
                ret += 1
        return ret
