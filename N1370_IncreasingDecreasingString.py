#
# Create by Hua on 4/7/22.
#

"""
You are given a string s. Reorder the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.



Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.



Constraints:

    1 <= s.length <= 500
    s consists of only lowercase English letters.


"""


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str

        thought: 26 buckets dictionary with count of frequency.
        04/07/2022 11:34	Accepted	94 ms	13.6 MB	python
        easy 5-10 min.
        """

        a = [0] * 26
        n = len(s)
        for c in s:
            a[ord(c) - ord('a')] += 1

        ret = list()
        is_to_right = True
        while len(ret) !=n:
            if is_to_right:
                is_to_right = False
                for i in range(len(a)):
                    if a[i] != 0:
                        ret.append(chr(ord('a') + i))
                        a[i] -= 1
            else:
                is_to_right = True
                for i in range(len(a)-1, -1, -1):
                    if a[i] != 0:
                        ret.append(chr(ord('a') + i))
                        a[i] -= 1

        return "".join(ret)
