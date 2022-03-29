#
# Create by Hua on 3/29/22.
#

"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.



Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]



Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100


"""


class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        03/29/2022 15:30	Accepted	44 ms	13.6 MB	python
        easy 5 min. custom sort.

        # concise solution.
        https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/1065249/Python-3-solution-with-process-of-thinking-and-improvement
        class Solution:
            def frequencySort(self, nums: List[int]) -> List[int]:
                r = Counter(nums)
                return sorted(nums, key=lambda x: (r[x], -x))

        """
        dt = dict()
        for n in nums:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1

        # sort value first, then key decreasingly
        ret = list()
        r = sorted(dt.items(), key=lambda x: (x[1], -x[0]))
        for k,v in r:
            ret.extend([k] * v)
        print(ret)
        return ret

