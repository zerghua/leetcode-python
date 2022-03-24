#
# Create by Hua on 3/24/22.
#

"""
You are given an integer array nums. The unique elements of an array are the
elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.



Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.



Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100


"""


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: use dictionary to count occurences of each number
        03/24/2022 14:43	Accepted	29 ms	13.3 MB	python
        easy 5 min. dictionary.
        """

        dt = dict()
        for n in nums:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1

        ret = 0
        for key in dt.keys():
            if dt[key] == 1:
                ret += key
        return ret
