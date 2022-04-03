#
# Create by Hua on 4/3/22.
#

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.



Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length


"""


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int

        thought: iterate 1-3000, build missing array, and return the kth
        04/03/2022 14:04	Accepted	112 ms	13.6 MB	python
        easy 5 min.
        can do binary search.
        https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC%2B%2BPython-O(logN)
        """

        rt = list()
        for i in range(1, 3001):
            if i not in arr:
                rt.append(i)
            if len(rt) == k:
                return rt[-1]

        return -1
