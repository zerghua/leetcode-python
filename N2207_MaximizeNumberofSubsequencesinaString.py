#
# Create by Hua on 7/21/22
#

"""
You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.

You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.

Return the maximum number of times pattern can occur as a subsequence of the modified text.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



Example 1:

Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
Example 2:

Input: text = "aabb", pattern = "ab"
Output: 6
Explanation:
Some of the strings which can be obtained from text and have 6 subsequences "ab" are "aaabb", "aaabb", and "aabbb".


Constraints:

1 <= text.length <= 105
pattern.length == 2
text and pattern consist only of lowercase English letters.

"""


class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int

        thought: 2 ways to add pattern to text:
        1. put pattern[0] at the beginning of text, get a countA,
        2. put pattern[1] at the end of text, get a countB,
        return max(countA, countB)

        corner case 1, what if there is no pattern[0] and pattern[1] in text?
        if both pattern[0] and pattern[1] not exist in text, return 0
        if one of pattern[0] and pattern[1] not exist in text, return count of the pattern[0] or pattern[1]

        corner case 2, what if a == b?

        07/21/2022 10:37	Accepted	495 ms	17.8 MB	python
        medium 20-30min. quite a few corner cases, but I have figured out myself.

        a much simpler code:
        https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/discuss/1863900/JavaC%2B%2BPython-Straight-Forward-Solution
            def maximumSubsequenceCount(self, text, pattern):
                res = cnt1 = cnt2 = 0
                for c in text:
                    if c == pattern[1]:  # the sequence can't be reversed, not can't handle pattern[0] ==pattern[1]
                        res += cnt1
                        cnt2 += 1
                    if c == pattern[0]:
                        cnt1 += 1
                return res + max(cnt1, cnt2)

        """
        def get_count(str, a, b):
            # o(n^2) to find subsequence will TLE.
            # find number of a before b to get the total count
            a_size = 0
            ret = 0
            for i in range(len(str)):
                if str[i] == a:
                    a_size += 1
                elif str[i] == b:
                    ret += a_size
            return ret

        a,b = pattern[0], pattern[1]
        a_count, b_count = text.count(a), text.count(b)
        if a == b:
            t = a_count + 1
            return t*(t-1)/2

        if a_count == 0 and b_count == 0:
            return 0
        if a_count == 0:
            return b_count
        if b_count == 0:
            return a_count

        # now both count are not 0
        return max(get_count(a+text, a, b), get_count(text+b, a, b))




