#
# Create by Hua on 4/2/22.
#

"""
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.



Example 1:

Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.

Example 2:

Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.

Example 3:

Input: arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.



Constraints:

    2 <= arr.length <= 100
    1 <= arr[i] <= 100
    1 <= m <= 100
    2 <= k <= 100


"""


class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool

        thought: brute force, check all possibilities.
        for a length m string, check all following string
        are consecutively repeated k times.

        04/02/2022 10:50	Accepted	30 ms	13.5 MB	python
        easy - medium 10-20min
        some corner cases.
        """
        n = len(arr)
        for i in range(n-m): #TODO micro-optimization,
            pattern = arr[i:i+m]
            start = i+m
            match_times = 1
            for j in range(k):
                if start < n:
                    s = arr[start:start+m]
                    start +=m
                    if s == pattern:
                        match_times +=1
                    else:
                        break
            if match_times == k:
                return True

        return False

