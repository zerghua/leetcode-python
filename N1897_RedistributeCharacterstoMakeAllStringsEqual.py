#
# Create by Hua on 3/21/22.
#

"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a
non-empty string, and move any character from words[i]
to any position in words[j].

Return true if you can make every string in words equal using any number
of operations, and false otherwise.



Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.



Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool

        thought: hashtable to count chars in all words, and check if they can
        be distributed into the n words evenly.

        03/21/2022 18:43	Accepted	56 ms	13.8 MB	python

        easy 5 min. hashtable
        """

        dic = dict()
        n = len(words)
        for word in words:
            for c in word:
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1

        for key in dic.keys():
            if dic[key] % n != 0:
                return False

        return True
