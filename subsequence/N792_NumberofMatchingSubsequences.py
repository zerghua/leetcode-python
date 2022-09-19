#
# Create by Hua on 9/19/22
#

"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.

"""


class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int

        thought:  build inverted index for string and then binary search. which will improve
        the time from o(m*n) to o(logm * n), if m is sufficiently large,  the runtime will have significant
        improvement.

        09/19/2022 11:45	Accepted	1656 ms	18.9 MB	python
        medium
        google
        binary search on inverted index on string.
        similar to N1055 shortest way to form strings.
        """
        import collections, bisect
        dt = collections.defaultdict(list)

        for i in range(len(s)):  # build inverted index
            dt[s[i]].append(i)

        ret = 0
        for word in words:
            # check each word
            is_valid = True
            i = -1
            for c in word:
                lt = dt[c]
                if c not in dt:    # simple case, char not exist
                    is_valid = False
                    break

                j = bisect.bisect_left(lt, i)
                if j == len(lt):  # need more char, but not exist
                    is_valid = False
                    break
                else:
                    i = lt[j] + 1

            if is_valid:
                ret += 1
        return ret