#
# Create by Hua on 4/29/22.
#

"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true



Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000


"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        thought: count occurrence using hashmap, and use set to get unique
        count, compare it with num_of hashmap values.

        04/29/2022 09:54	Accepted	18 ms	13.6 MB	python
        easy 5 min. hashmap.
        """

        dt = dict()
        for n in arr:
            if n in dt:
                dt[n] += 1
            else:
                dt[n] = 1
        return len(dt.values()) == len(set(dt.values()))

