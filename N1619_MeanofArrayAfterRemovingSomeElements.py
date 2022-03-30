#
# Create by Hua on 3/30/22.
#

"""
Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.



Example 1:

Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

Example 2:

Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000

Example 3:

Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
Output: 4.77778



Constraints:

    20 <= arr.length <= 1000
    arr.length is a multiple of 20.
    0 <= arr[i] <= 105


"""


class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float

        thought: sort array and remove first and last 5% of array
        and return mean.

        03/30/2022 10:04	Accepted	40 ms	13.7 MB	python
        easy 5 min. math
        """

        n = len(arr)
        i = int(0.05 * n)

        return float(sum(sorted(arr)[i:n-i])) / (n - 2*i)
