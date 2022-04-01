#
# Create by Hua on 4/1/22.
#

"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:

Input: arr = [10,11,12]
Output: 66



Constraints:

    1 <= arr.length <= 100
    1 <= arr[i] <= 1000


"""


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        thought: math. simulate the statement.
        04/01/2022 15:38	Accepted	75 ms	13.5 MB	python
        04/01/2022 15:41	Accepted	61 ms	13.4 MB	python
        easy, 5-10 min. need to work out the math.
        """

        ret = 0
        n = len(arr)
        for g in range(1, n+1, 2):
            for i in range(n):
                if i+g > n:
                    break
                ret += sum(arr[i:i+g])
        return ret
