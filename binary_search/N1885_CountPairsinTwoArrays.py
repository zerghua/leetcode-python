#
# Create by Hua on 8/22/22
#

"""
Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j)
such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.



Example 1:

Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
Output: 1
Explanation: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.
Example 2:

Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
Output: 5
Explanation: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.


Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105

"""


class Solution(object):
    def countPairs(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int

        thought: BF is o(n^2) to check every pair in the array.
        optimized solution is to convert, sort and binary search, it's o(nlogn)

        convert
        nums1[i] + nums1[j] > nums2[i] + nums2[j]
        to
        nums1[i] - nums2[i] > -(nums2[j]-nums2[j])

        store the diff in an array, and sort it. find  number of diff[i] > -diff[j]. i < j.

        08/22/2022 10:51	Accepted	1803 ms	38.1 MB	python
        medium
        30-40min. need some analysis

        refer here:
        https://leetcode.com/problems/count-pairs-in-two-arrays/discuss/1467647/Python-3-or-Math-Binary-Search-or-Explanation

        Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
        Output: 5
        Explanation: The pairs satisfying the condition are:
        - (0, 1) where 1 + 10 > 1 + 4.
        - (0, 2) where 1 + 6 > 1 + 1.
        - (1, 2) where 10 + 6 > 4 + 1.
        - (1, 3) where 10 + 2 > 4 + 5.
        - (2, 3) where 6 + 2 > 1 + 5.

        diff = [0, 6,5,-3] = [-3,0,5,6]
                              0  1 2 3

        -3: 2
        0:  2
        5:  1

        example of dup diff
        diff=[-3,0,0,5,6]
              0  1 2 3 4
        -3  (5-3) = 2
        0   (5-3) = 2
        0   (5-3) = 2
        5   (5-4) = 1


        """

        import bisect
        diff = sorted(x-y for x, y in zip(nums1, nums2))
        ret, n = 0, len(diff)
        for i in range(n):
            num = diff[i]
            idx = bisect.bisect_right(diff, -num, i+1)  # bisect_right to make sure it's not counting duplicate
            ret += n - idx
        return ret