#
# Create by Hua on 5/10/22.
#

"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104


"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        thought: find largest num/index in arr first, and check its left
        and right should be strictly increasing and decreasing

        05/10/2022 09:52	Accepted	236 ms	14.5 MB	python
        easy 10 min. some corner cases.
        """
        n = len(arr)
        if n < 3: return False

        peak = arr.index(max(arr))
        if peak == 0 or peak == n-1: return False

        for i in range(1, peak+1):  # check strictly increasing
            if arr[i] <= arr[i-1]:
                return False

        for i in range(peak+1, n):  # check strictly decreasing
            if arr[i] >= arr[i-1]:
                return False

        return True