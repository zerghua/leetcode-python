#
# Create by Hua on 1/31/22.
#

"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and
has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"



Constraints:

    1 <= word.length <= 100
    word consists of lowercase English letters only.
"""


class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int

        easy 30 min, stuck on thought1. Take away, do not always go to the optimal solution, go for brute force
        first, optimal later.

        thought 1: not very easy, need 2 pointers, to point the fast and slow of a substring, also maintain
        a count of each vowel, when find a non-vowel char, need to move the slow to fast one by one until
        not-all vowel in the record, then reset the count to 0 and move both fast and slow to the next vowel.
        o(n) solution. But it will be quite challenge to write the correct code, might have some bugs.

        thought 2: scratch thought1, this is a worst o(n^2) problem, check all substring in 2 loops. some optimal
        technique, start with a vowel.

        01/31/2022 11:12	Accepted	68 ms	13.4 MB	python
        """

        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        ret = 0
        for i in range(n):
            if word[i] not in vowels: continue

            dic = dict()
            dic[word[i]] = 1
            for j in range(i+1, n):
                c = word[j]
                if c not in vowels: break
                if c not in dic: dic[c] = 1
                else: dic[c] += 1

                if len(dic) == 5:
                    ret += 1

        return ret