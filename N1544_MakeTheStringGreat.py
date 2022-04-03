#
# Create by Hua on 4/3/22.
#

"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.



Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

Input: s = "s"
Output: "s"



Constraints:

    1 <= s.length <= 100
    s contains only lower and upper case English letters.


"""


class Solution(object):
    def makeGood2(self, s):
        """
        :type s: str
        :rtype: str

        thought: keep removing adjacent 2 chars until the length does not
        change.

        easy - medium  20 - 30 min. corner case of how to handle the last char.
        04/03/2022 11:41	Accepted	46 ms	13.6 MB	python

        use stack is much easier code.
        """

        ret = list(s)
        while 1:
            n = len(ret)
            tmp = list()
            i = 0
            is_last_removed = False
            while i < n - 1:
                if ret[i] == ret[i+1].swapcase():
                    i += 2
                    if i == n:
                        is_last_removed = True
                else:
                    tmp.append(ret[i])
                    i += 1
            if len(ret) >= 1 and not is_last_removed:  # special case for last char
                tmp.append(ret[-1])
            ret = tmp[:]
            if len(ret) == n:
                break

        return "".join(ret)

    def makeGood(self, s):
        """
        :type s: str
        :rtype: str

        use stack is much easier code.
        04/03/2022 11:46	Accepted	29 ms	13.3 MB	python
        """
        ret = list()
        for c in s:
            if not ret:
                ret.append(c)
            elif ret[-1] == c.swapcase():
                ret.pop()
            else:
                ret.append(c)
        return "".join(ret)


