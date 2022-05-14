#
# Create by Hua on 5/14/22.
#

"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.



Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]



Constraints:

    1 <= s.length <= 104
    s[i] and c are lowercase English letters.
    It is guaranteed that c occurs at least once in s.


"""


class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]

        thought: 2 pass from left to right and right to left.


        easy is to check all possible distance for each i, worst case
        will be o(n^2)

        05/14/2022 11:17	Accepted	35 ms	13.5 MB	python
        easy - medium, not easy to figure out the 2 pass solution. o(n)
        30-40 min.

        """
        n = len(s)
        ret = [0] * n
        pos = -n
        for i in range(n):  # left to right
            if s[i] == c: pos = i
            ret[i] = i - pos

        for i in range(pos-1,-1,-1):  # right to left, attention, pos-1, not n-1
            if s[i] == c: pos = i
            ret[i] = min(ret[i], pos - i)
        return ret

