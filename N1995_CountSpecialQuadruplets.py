#
# Create by Hua on 2/1/22.
#

"""
Given a 0-indexed integer array nums, return the number of distinct
quadruplets (a, b, c, d) such that:

    nums[a] + nums[b] + nums[c] == nums[d], and
    a < b < c < d


Example 1:
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement
is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

Example 2:
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].

Example 3:
Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

Constraints:
    4 <= nums.length <= 50
    1 <= nums[i] <= 100
"""


class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        easy 5 min.
        thought: o(n^4), check all possible situations.
        02/01/2022 17:39	Accepted	1640 ms	13.4 MB	python
        """

        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ret += 1

        return ret