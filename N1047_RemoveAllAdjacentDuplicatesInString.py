#
# Create by Hua on 5/1/22.
#

"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"



Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.


"""


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str

        thought: use stack or recursion.
        05/01/2022 13:22	Accepted	65 ms	14.5 MB	python
        easy 5-10min. stack.
        """

        ls = list()
        for c in s:
            if not ls:
                ls.append(c)
            else:
                if ls[-1] == c:
                    ls.pop()
                else:
                    ls.append(c)

        return "".join(ls)