#
# Create by Hua on 5/4/22.
#

"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4



Constraints:

    3 <= arr.length <= 5 * 104
    -104 <= arr[i] <= 104


"""


class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        hint: If we have three parts with the same sum, what is the sum of
        each? If you can find the first part, can you find the second part?

        thought: get total sum, and calculate the 1/3 of total sum,
        try to find first and second part with 1/3 of total sum and return true.

        05/04/2022 10:44	Accepted	266 ms	19.2 MB	python
        easy-medium. 5-10 min. need to figure out the algorithm.
        """
        total = sum(arr)
        if total % 3 != 0:
            return False
        s = total / 3
        counter = 0
        p = 0
        for n in arr:
            p += n
            if p == s:
                counter += 1
                p = 0
        return counter >= 3
