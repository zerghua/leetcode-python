#
# Create by Hua on 4/3/22.
#

"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.



Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.



Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000

"""


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        thought: check every 3 numbers in sequence.
        04/03/2022 10:48	Accepted	46 ms	13.4 MB	python
        easy 5 min.
        """

        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] %2 == 1:
                return True

        return False