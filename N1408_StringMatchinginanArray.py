#
# Create by Hua on 4/6/22.
#

"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].



Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    It's guaranteed that words[i] will be unique.


"""


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]

        thought: 2 loops to check every 2 words relations
        04/06/2022 13:29	Accepted	52 ms	13.4 MB	python
        easy 5min.
        better solutin is to join words as string, and check if word exist
        in string over twice.
        """
        n = len(words)
        ret = set()
        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[i] in words[j]:
                        ret.add(words[i])
                        break
        return list(ret)

