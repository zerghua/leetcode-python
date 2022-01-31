#
# Create by Hua on 1/31/22.
#

"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth
distinct string present in arr. If there are fewer than k distinct strings,
return an empty string "".

Note that the strings are considered in the order in which
they appear in the array.



Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.

Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings,
we return an empty string "".



Constraints:
    1 <= k <= arr.length <= 1000
    1 <= arr[i].length <= 5
    arr[i] consists of lowercase English letters.
"""


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str

        easy 5 min. hashtable

        thought: use dictionary to store the count of each str, loop through
        the list and find the kth str with only 1 count in the dictionary.
        o(n) solution.

        01/31/2022 11:57	Accepted	58 ms	14 MB	python
        """

        dic = dict()
        for str in arr:
            if str in dic: dic[str] += 1
            else: dic[str] = 1

        for str in arr:
            if dic[str] == 1:
                k -= 1

            if k == 0:
                return str

        return ""
