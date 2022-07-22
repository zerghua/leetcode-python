#
# Create by Hua on 7/22/22
#

"""
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.



Example 1:

Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum.
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 108

"""


class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        thought:
        math
        initialize sum(1,k), - sum(nums in [1,k]) + sum(k+1, .. k+1+size)
        use set to store nums, and adjust final answer

        tricky code
        07/22/2022 10:11	Accepted	897 ms	31.1 MB	python
        medium. math
        20-30 min.

        """

        ret = k*(k+1)/2
        cur_max = k + 1
        st = set(nums)
        for n in st:
            if n <= k:   # important
                while cur_max in st:
                    cur_max += 1
                ret = ret + cur_max - n
                cur_max += 1
        return ret



