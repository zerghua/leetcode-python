#
# Create by Hua on 4/30/22.
#

"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 9


"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        04/30/2022 13:52	Accepted	67 ms	13.9 MB	python
        easy 5 - 10 min. extra space.
        """

        n = len(arr)
        ret = list()
        for i in arr:
            if i == 0:
                ret.extend([0,0])
            else:
                ret.append(i)
            if len(ret) > n:
                break
        for i in range(n):
            arr[i] = ret[i]
