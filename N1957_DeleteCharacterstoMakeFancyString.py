#
# Create by Hua on 3/21/22.
#

"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s
to make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.



Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".



Constraints:
    1 <= s.length <= 105
    s consists only of lowercase English letters.

"""


class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str

        thought: go through the string, and construct a new string, when
        encounter a third duplidate and skip it. need extra storage to check
        duplicate and count.

        03/21/2022 15:47	Accepted	648 ms	16.5 MB	python

        easy, 5min, however, wasted some time on the large test string,
        so changed the direct "+" strings to append c to list and then join
        them.

        interesting solution from discussion:
        class Solution:
            def makeFancyString(self, s: str) -> str:
                s = list(s)
                for i in range(1,len(s)-1):
                    if (s[i-1] == s[i]) and (s[i+1] == s[i]):
                        s[i-1] = ""
                return "".join(s)
        """

        last = ""
        count = 0
        ret = list()
        for c in s:
            if c == last:
                count +=1
                if count < 2:
                    ret.append(c)
            else:
                ret.append(c)
                last = c
                count = 0

        return "".join(ret)

