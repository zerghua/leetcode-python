#
# Create by Hua on 3/27/22.
#

"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.



Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.



Constraints:

    1 <= words.length <= 104
    1 <= allowed.length <= 26
    1 <= words[i].length <= 10
    The characters in allowed are distinct.
    words[i] and allowed contain only lowercase English letters.


"""


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int

        thought: put allowed chars into a set, go through words,
        if a char is not in the set, this word is not allowed.
        03/27/2022 11:26	Accepted	200 ms	16.1 MB	python
        5 min. easy. set
        """

        st = set(allowed) # put each char into a set
        ret = 0
        for word in words:
            valid = True
            for w in word:
                if w not in st:
                    valid = False
            if valid:
                ret += 1

        return ret


