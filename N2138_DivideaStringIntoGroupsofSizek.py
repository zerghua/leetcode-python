#
#  Create by Hua on 1/28/2022
#

"""
A string s can be partitioned into groups of size k using the following procedure:

    1. The first group consists of the first k characters of the string, the second group consists of the next k
    characters of the string, and so on. Each character can be a part of exactly one group.

    2. For the last group, if the string does not have k characters remaining, a character fill is
    used to complete the group.

Note that the partition is done so that after removing the fill character from the last group (if it exists)
and concatenating all the groups in order, the resultant string should be s.

Given the string s, the size of each group k and the character fill, return a string array denoting the composition
of every group s has been divided into, using the above procedure.



Example 1:
Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]
Explanation:
The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".

Example 2:
Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]
Explanation:
Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".



Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters only.
    1 <= k <= 100
    fill is a lowercase English letter.

"""


class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]

        easy: 10 min.

        thoughts: split string into chars(a quick solution can use split() function), construct string for every
        k chars, fill the last group with fill char(len(last_group)-k)

        01/28/2022 14:13	Accepted	45 ms	13.6 MB	python
        """

        ret=list()
        count = 0
        tmp = ""
        for c in s:
            if count == k:
                ret.append(tmp)
                tmp = ""
                count = 0
            tmp += c
            count += 1

        # handle last group
        if len(tmp) != 0:
            for i in range(k - len(tmp)):
                tmp += fill
        ret.append(tmp)

        return ret