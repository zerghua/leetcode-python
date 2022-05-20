#
# Create by Hua on 5/20/22
#


"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.



Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105

"""


class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: check each num
        a corner case; store distance separate from ret, due to negative number
        05/20/2022 10:18	Accepted	266 ms	13.6 MB	python
        easy 5 min.
        """
        distance = 10**6
        ret = 0
        for n in nums:
            if abs(n) < distance or (abs(n) == distance and n > ret):
                distance = abs(n)
                ret = n
        return ret