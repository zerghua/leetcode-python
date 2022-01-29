#
#  Create by Hua on 1/29/2022
#

"""
Given two string arrays words1 and words2, return the number of strings that appear
exactly once in each of the two arrays.


Example 1:
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.

Example 3:
Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".


Constraints:
    1 <= words1.length, words2.length <= 1000
    1 <= words1[i].length, words2[j].length <= 30
    words1[i] and words2[j] consists only of lowercase English letters.

"""


class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int

        easy 5 min, used list.count() function.

        thought: use python list.count() function to count number of specified items. it should not exist more than
        once in both list, maintain a checked list to speed up checking.

        01/29/2022 15:14	Accepted	331 ms	13.8 MB	python
        """

        checked_list = list()
        ret = 0

        # TODO small optimization to choose the smaller size of word1 and word2
        for word in words1:
            if word not in checked_list:
                checked_list.append(word)
                if words1.count(word) == 1 and words2.count(word) == 1:
                    ret += 1

        return ret

