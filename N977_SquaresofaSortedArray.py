#
# Create by Hua on 5/7/22.
#

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        thought: o(n) is to find the middle point(square min val) of the sorted
        array and goto left and right from there, like merging 2 list

        can first square all.

        05/07/2022 12:11	Accepted	292 ms	15.4 MB	python
        easy 5-10 min.

        https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
        2 pointers from left and right and append to end.
        def sortedSquares(self, A):
            answer = collections.deque()
            l, r = 0, len(A) - 1
            while l <= r:
                left, right = abs(A[l]), abs(A[r])
                if left > right:
                    answer.appendleft(left * left)
                    l += 1
                else:
                    answer.appendleft(right * right)
                    r -= 1
            return list(answer)

        """

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        m = nums.index(min(nums))
        ret = list()
        right = nums[m:]
        left = nums[:m]
        r = 0
        l = m - 1
        while r < len(right) and l >= 0:
            if right[r] < left[l]:
                ret.append(right[r])
                r += 1
            else:
                ret.append(left[l])
                l -= 1

        while r < len(right):
            ret.append(right[r])
            r += 1

        while l >= 0:
            ret.append(left[l])
            l -= 1

        return ret



