#
# Create by Hua on 5/14/22.
#

"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.



Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".



Constraints:

    1 <= s.length <= 1000
    s contains lowercase English letters only.


"""


class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]

        thought: 2 pointers.
        05/14/2022 10:15	Accepted	31 ms	13.6 MB	python
        easy 5 min. a corner case
        """
        i, n = 0, len(s)
        ret = list()
        while i < n-1:
            j = i
            while j+1 < n and s[i] == s[j+1]:  # corner case, j+1 < n
                j += 1
            # at this point, j points the last same char of s[i]
            if j - i >= 2:
                ret.append([i,j])
            i = j+1
        return ret