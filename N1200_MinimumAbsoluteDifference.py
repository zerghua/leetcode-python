#
# Create by Hua on 4/29/22.
#

"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr



Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]



Constraints:

    2 <= arr.length <= 105
    -106 <= arr[i] <= 106


"""


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]

        thought: sort the array and find the min, it must between adjacent
        2 values in sorted array. then go through the sorted array and
        return the pair.

        04/29/2022 10:10	Accepted	341 ms	25.2 MB	python
        easy 5 min.
        """

        a = sorted(arr)
        m = 10**8
        ret = list()
        for i in range(1, len(a)):
            t = a[i] - a[i-1]
            if t < m:
                del ret[:]
                ret.append((a[i-1], a[i]))
                m = t
            elif t == m:
                ret.append((a[i-1], a[i]))

        return ret
