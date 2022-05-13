#
# Create by Hua on 5/13/22
#


"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.


Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.

"""


class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool

        thought: multiple corner cases. it seems you can only swap once, then try
        05/13/2022 11:44	Accepted	51 ms	14.5 MB	python
        easy. 10-20 min.
        """
        import collections
        a,b = collections.Counter(s), collections.Counter(goal)
        if a != b: return False

        n = len(s)
        diff = 0
        for i in range(n):
            if s[i] != goal[i]:
                diff += 1

        if diff == 2: return True
        if diff == 0:
            if len(set(list(s))) != len(s): return True
        return False


