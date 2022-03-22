#
# Create by Hua on 3/22/22.
#

"""
Given a binary string s, return true if the longest contiguous segment of 1's
is strictly longer than the longest contiguous segment of 0's in s,
or return false otherwise.

    For example, in s = "110100010" the longest continuous segment of 1s has
    length 2, and the longest continuous segment of 0s has length 3.

Note that if there are no 0's, then the longest continuous segment of 0's is
considered to have a length 0. The same applies if there is no 1's.



Example 1:
Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Example 2:
Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.

Example 3:
Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.



Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.
"""


class Solution(object):
    def count(self, s, c):
        ret = 0
        count = 0
        for e in s:
            if e == c:
                count += 1
                ret = max(ret, count)
            else:
                count = 0
        return ret

    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool

        thought: go through the string and count.
        03/22/2022 10:48	Accepted	37 ms	13.6 MB	python
        easy 10 - 20min, take some time to come up with correct solution,
        need to have some sample data to work it through.
        """
        return self.count(s, '1') > self.count(s,'0')


