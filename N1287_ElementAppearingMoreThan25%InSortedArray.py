#
# Create by Hua on 4/16/22.
#

"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1



Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 105


"""


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        thought: sorted array, obviously looking for a binary search solution.
        1,1
        1,2,2
        1,2,2,3
        1,1, 2,2, 2,3, 3,4,5
        this is a math problem.
        04/16/2022 15:48	Accepted	66 ms	15.8 MB	python
        easy 5 -10min.
        might only need to check 4 positions.
        """
        dt = dict()
        for n in arr:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1

        ret = 0
        max_freq = 0
        for k, v in dt.items():
            if v > max_freq:
                ret = k
                max_freq = v
        return ret
