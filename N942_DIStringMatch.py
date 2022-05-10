#
# Create by Hua on 5/10/22.
#

"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

    s[i] == 'I' if perm[i] < perm[i + 1], and
    s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.



Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: s = "III"
Output: [0,1,2,3]

Example 3:

Input: s = "DDI"
Output: [3,2,0,1]



Constraints:

    1 <= s.length <= 105
    s[i] is either 'I' or 'D'.


"""


class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]

        thought: greedy? if "I" choose smallest, if "D" choose largest
        05/10/2022 09:39	Accepted	118 ms	14.7 MB	python
        easy 10 min. figure out the greedy method.

        """
        lt = range(len(s)+1)
        ret = list()
        for c in s:
            if c == 'I':
                ret.append(lt.pop(0))  # smallest
            else:
                ret.append(lt.pop(-1))  # largest
        ret.append(lt.pop())
        return ret