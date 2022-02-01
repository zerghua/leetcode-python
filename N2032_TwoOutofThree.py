#
# Create by Hua on 2/1/22.
#

"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array
containing all the values that are present in at least two out of the three
arrays. You may return the values in any order.



Example 1:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

Example 2:
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

Example 3:
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.



Constraints:
    1 <= nums1.length, nums2.length, nums3.length <= 100
    1 <= nums1[i], nums2[j], nums3[k] <= 100
"""


class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]

        easy 5 min, set.intersection(another_set), set.update(another_set)

        thought: set intersection.

        02/01/2022 12:40	Accepted	74 ms	13.4 MB	python
        """

        a = set(nums1)
        b = set(nums2)
        c = set(nums3)

        ret = set()
        ret.update(a.intersection(b))
        ret.update(a.intersection(c))
        ret.update(b.intersection(c))

        return list(ret)

