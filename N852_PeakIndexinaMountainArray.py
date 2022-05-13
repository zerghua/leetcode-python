#
# Create by Hua on 5/13/22
#


"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1


Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?

"""


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: o(n) is to find the max value, and return it's index
        05/13/2022 14:19	Accepted	69 ms	14.9 MB	python
        easy 1 min.
        """
        return arr.index(max(arr))


class Solution2(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
        only binary search can do o(logn), modified binary search compare to it's right
        m = (l+r)/2 ->  (r - l)/2 + l

        1,3,5,7,6,4
        0,1,0
        0,1,2,0
        0,5,2,1,0
        05/13/2022 14:51	Accepted	65 ms	14.6 MB	python
        easy - medium, 20-30 min.

        """
        n = len(arr)
        l, r = 0, n - 1
        while l < r:
            m = (l+r)/2
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return l

