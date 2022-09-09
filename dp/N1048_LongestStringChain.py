#
# Create by Hua on 9/9/22
#

"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.

"""


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int

        improvement solution using dictionary as dp(word, count)
        09/09/2022 11:29	Accepted	97 ms	14.1 MB	python
        much faster, this is more of o(n) solution
        dp + hashmap + sort.
        """

        words.sort(key=len)
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                if pre in dp:
                    dp[word] = max(dp[word], dp[pre] + 1)
        return max(dp.values())

class Solution_myself(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int

        thought: comes from hint:
        1. Instead of adding a character, try deleting a character to form a chain in reverse.
        2. For each word in order of length, for each word2 which is word with one character removed,
           length[word2] = max(length[word2], length[word] + 1).

        for word (a, b), if a is the pre of b only when len(a) + 1 = len(b) and remove one char from b == a
        use dp to record the count of current word, and check backward. o(n^2) solution

        corner case, the whole words list can be rearranged, so we can sort the word list by size
        09/09/2022 11:15	Accepted	3686 ms	14 MB	python
        medium
        20-30min
        dp + right to left + sort.
        """

        words.sort(key=lambda n: len(n))
        n = len(words)
        dp = [1] * n
        for i in range(n-2, -1, -1):
            a = words[i]
            for j in range(i+1, n):
                b = words[j]
                if len(a) + 1 == len(b):  # check every word after a, if there is a match, update the dp value.
                    for k in range(len(b)):
                        if b[:k] + b[k+1:] == a:
                            dp[i] = max(dp[i], dp[j] + 1)
                            break

        return max(dp)