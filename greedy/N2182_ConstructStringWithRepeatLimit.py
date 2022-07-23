#
# Create by Hua on 7/23/22
#

"""
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.



Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa".
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.


Constraints:

1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.

"""


class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str

        thought: greedy?

        test cases:
        ccbbcbaa, 2
        "ccbcbbaa"  should be returned

        ccbbcbbb, 2
        "ccbcbb" should be returned, rather than "ccbbcbb", (OJ is expecting "ccbcbb")

        so after some test case experiment, the logic should be, append the largest char as much as possible(meet
        the repeatlimit requirement), even we can't use all the chars.

        07/23/2022 10:23	Accepted	1541 ms	15.8 MB	python
        medium, tricky long code.
        30-40min.

        use a max heap
        heap solution: https://leetcode.com/problems/construct-string-with-repeat-limit/discuss/1784749/Python-short-solution-using-heap
        The idea is simple, keep a max heap of all the characters and their available counts.
        If the max character element at the top of the heap is already exceeding the limit in terms of count,
        then pop the next one and add to heap. Also add back the unused max character element to the heap.

        """

        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        ret = list()
        while 1:
            tmp = ""
            for i in range(25, -1, -1):
                if count[i] == 0: continue
                c = chr(ord("a") + i)
                if len(ret) > 0 and ret[-1][-1] == c:  # add one smaller
                    for j in range(i - 1, -1, -1):
                        if count[j] > 0:
                            tmp = chr(ord("a") + j)
                            count[j] -= 1
                            break
                    if len(tmp) > 0: break

                else:
                    size = min(count[i], repeatLimit)
                    tmp = c * size
                    count[i] -= size
                    break

            if len(tmp) == 0: break
            ret.append(tmp)

        return "".join(ret)