#
# Create by Hua on 4/6/22.
#

"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.



Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.



Constraints:

    1 <= arr.length <= 500
    1 <= arr[i] <= 500


"""
import collections


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: hashmap to check k = v
        04/06/2022 15:08	Accepted	70 ms	13.8 MB	python
        easy 5 - 10 min.
        """
        dt = dict()
        for n in arr:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1

        ret = -1
        for k,v in dt.items():
            if k == v:
                ret = max(ret, k)

        return ret


    def findLucky2(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: hashmap to check k = v
        04/06/2022 15:10	Accepted	56 ms	13.4 MB	python
        easy 5 - 10 min.
        """
        dt = collections.Counter(arr)

        ret = -1
        for k,v in dt.items():
            if k == v:
                ret = max(ret, k)

        return ret