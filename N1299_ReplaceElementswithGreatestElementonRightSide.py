#
# Create by Hua on 4/16/22.
#

"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.



Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5


"""


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        thought: scan throught right to left, and keep cur max.
        04/16/2022 15:16	Accepted	195 ms	15.1 MB	python
        easy 5 - 10 min.
        """

        ret = list()
        cur_max = arr[-1]
        ret.append(-1)
        for i in range(len(arr) -2, -1, -1):
            ret.insert(0, cur_max)
            cur_max = max(cur_max, arr[i])

        return ret

