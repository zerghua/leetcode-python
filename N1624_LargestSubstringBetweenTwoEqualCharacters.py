#
# Create by Hua on 3/30/22.
#

"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.



Constraints:

    1 <= s.length <= 300
    s contains only lowercase English letters.


"""


class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int

        thought: dictionary to store index of each char,
        compare the length of first and last char for each char.
        03/30/2022 09:49	Accepted	29 ms	13.5 MB	python
        5-10min, easy. dictionary of list.
        """

        dt = defaultdict(list)
        for i in range(len(s)):
            dt[s[i]].append(i)

        ret = -1
        for k in dt.keys():
            if len(dt[k]) >= 2:
                ret = max(ret, dt[k][-1] - dt[k][0] - 1)

        return ret
