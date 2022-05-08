#
# Create by Hua on 5/8/22.
#

"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.


"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool

        thought: hashmap and compare each word
        05/08/2022 16:10	Accepted	47 ms	13.7 MB	python
        easy - medium 10-20 min, a bit tricky code.

        """
        def is_bigger(w1, w2, dt):
            m, n = len(w1), len(w2)
            i = 0
            while i < m and i < n:
                if w1[i] != w2[i]:                  # tricky here.
                    return dt[w1[i]] > dt[w2[i]]
                i += 1
            return m > n

        dt = dict()
        for i in range(len(order)):
            dt[order[i]] = i

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            if is_bigger(w1, w2, dt):
                return False
        return True
