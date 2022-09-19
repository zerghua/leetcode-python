#
# Create by Hua on 9/19/22
#

"""
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.



Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".


Constraints:

1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.

"""

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int

        thought:  binary search on inverted index of string.
        Example with source = "abcab", target = "aabbaac"
        The inverted index data structure for this example would be:
        inverted_index = {
        a: [0, 3] # 'a' appears at index 0, 3 in source
        b: [1, 4], # 'b' appears at index 1, 4 in source
        c: [2], # 'c' appears at index 2 in source
        }

        Initialize i = -1 (i represents the smallest valid next offset) and loop_cnt = 1 (number of passes through source).
        Iterate through the target string "aabbaac"
        a => get the offsets of character 'a' which is [0, 3]. Set i to 1.
        a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
        b => get the offsets of character 'b' which is [1, 4]. Set i to 5.
        b => get the offsets of character 'b' which is [1, 4]. Increment loop_cnt to 2, and Set i to 2.
        a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
        a => get the offsets of character 'a' which is [0, 3]. Increment loop_cnt to 3, and Set i to 1.
        c => get the offsets of character 'c' which is [2]. Set i to 3.
        We're done iterating through target so return the number of loops (3).

        https://leetcode.com/problems/shortest-way-to-form-string/discuss/304662/Python-O(M-%2B-N*logM)-using-inverted-index-%2B-binary-search-(Similar-to-LC-792)

        09/19/2022 10:36	Accepted	94 ms	13.6 MB	python
        medium. BF can pass. time o(m*n), m is the size of source, and n is the size of target
        google phone interview
        similar to 792. Number of Matching Subsequences

        binary search improvement, put index of each char in source into a map, then binary search it's index
        so imporve the o(m * n) to o(logm * n)

        09/19/2022 11:25	Accepted	44 ms	13.5 MB	python
        medium - hard.

        google phone interview. will require this binary search on inverted index solution.

        """

        # build inverted index
        import collections, bisect
        dt = collections.defaultdict(list)
        for i in range(len(source)):
            dt[source[i]].append(i)

        i, ret = -1, 1
        for c in target:
            if c not in dt:
                return -1

            lt = dt[c]
            j = bisect.bisect_left(lt, i)  # there is no dup in lt.
            if j == len(lt):  # this pass finished
                ret += 1
                i = lt[0] + 1
            else:
                i = lt[j] + 1

        return ret





        return ret

class Solution_BF(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int

        thought: BF solution, 2 pointers to go through the both strings and eliminate same one and repeat.

        corner cases:
        1   "aa"      "aaa"  2
        2.  "adbsc"   "ad d d d d d d d d d d ds bc"  13

        09/19/2022 10:36	Accepted	94 ms	13.6 MB	python
        medium. BF can pass. time o(m*n), m is the size of source, and n is the size of target
        google phone interview
        similar to 792. Number of Matching Subsequences

        binary search improvement, put index of each char in source into a map, then binary search it's index
        so imporve the o(m * n) to o(logm * n)
        a: 1,3,5
        b: 2, 8
        c: ..
        """

        if len(set(target) - set(source)) != 0:
            return -1

        ret = i = j = 0
        n = len(source)
        while i < len(target):
            while j < n:
                if source[j] == target[i]:
                    j += 1
                    i += 1
                    break
                j += 1
            if j == n:  # after this step, the current c might not have a match
                ret += 1
                j = 0
        if j != 0: ret += 1  # corner case for aa, aaa
        return ret
