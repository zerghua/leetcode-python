#
#  Create by Hua on 1/28/2022
#

"""
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
Example 1:

Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.

Example 2:

Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.



Constraints:

    1 <= nums.length <= 100
    -105 <= nums[i] <= 105

"""


class Solution(object):
    def countElements(self, nums):
        """
            easy, about 5 min.
            solution: o(n) one loop to find largest and smallest in the array, another o(n) loop to compare each
            num with max and mix, if in between count++, return count.
            01/28/2022 11:07	Accepted	63 ms	13.7 MB	python
        """
        import sys
        max_n = -sys.maxint
        min_n = sys.maxint

        for n in nums:
            max_n = max(n, max_n)
            min_n = min(n, min_n)

        count = 0
        for n in nums:
            if min_n < n < max_n:
                count += 1
        return count
