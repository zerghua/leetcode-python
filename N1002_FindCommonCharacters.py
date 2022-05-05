#
# Create by Hua on 5/5/22.
#

"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.


"""


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]

        thought: for each char in words[0], check its existence in other words
        corner case: how to handle duplicate? see example 2.

        then need to hashmap all words and check their count
        05/05/2022 10:22	Accepted	100 ms	14 MB	python
        05/05/2022 10:25	Accepted	88 ms	13.7 MB	python
        easy 10-20 min. use of  data structure.
        """
        import collections

        # get intersection of all counters
        dt = collections.Counter(words[0])
        for w in words:
            dt = dt & collections.Counter(w)
        return dt.elements()
