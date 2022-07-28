#
# Create by Hua on 7/28/22
#

"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.


Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109


Follow-up: Could you find a solution with O(n) time complexity?


"""


class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: this is very similar to N907. return sum(max) - sum(min)  for o(n) solution
        07/28/2022 16:39	Accepted	69 ms	13.7 MB	python
        medium, if understand N907.

        """
        inf = float('inf')
        a = [-inf] + nums + [-inf]  # add edge
        stack = []
        ret = 0
        # get all min
        for i in range(len(a)):
            while stack and a[stack[-1]] > a[i]:
                j = stack.pop()
                pre_j = stack[-1]
                ret -= a[j] * (i-j) * (j-pre_j)  # (i-j) is right count, (j-pre_j) is left count
            stack.append(i)

        # get all max
        a[0] = a[-1] = inf
        stack = []
        for i in range(len(a)):
            while stack and a[stack[-1]] < a[i]:
                j = stack.pop()
                pre_j = stack[-1]
                ret += a[j] * (i-j) * (j-pre_j)  # (i-j) is right count, (j-pre_j) is left count
            stack.append(i)

        return ret

    def subArrayRanges_BF(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: this is very similar to N907. return sum(max) - sum(min)  for o(n) solution
        BF will be o(n^2) to check each subarray.
        07/28/2022 13:18	Accepted	4541 ms	13.5 MB	python
        medium - easy (if BF)
        10 min
        """
        n = len(nums)
        ret = 0
        for i in range(n):
            a = b = nums[i]
            for j in range(i+1, n):
                a = max(a, nums[j])
                b = min(b, nums[j])
                ret += a-b
        return ret



