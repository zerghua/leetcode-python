#
# Create by Hua on 4/29/22.
#

"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0



Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.


"""


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int

        thought: count the frequency of "balloon" in string, return the min
        of the count. special handle for l and o

        corner case1: when string is less than "balloon", like "lloo"
        corner case2: "l" does not exist in string

        04/29/2022 10:20	Accepted	27 ms	13.5 MB	python
        easy 5-10 min. 2 bugs.

        cleaner code is to
            def maxNumberOfBalloons(self, text: str) -> int:
                record = {'b':1,'a':1,'l':2,'o':2,'n':1}
                h= {'b':0,'a':0,'l':0,'o':0,'n':0}
                for i in text:
                    if i in h:
                        h[i] += 1
                return min(h[i]//record[i] for i in h)

        """
        dt = dict()
        for n in text:
            if n in "balloon":
                if n in dt:
                    dt[n] += 1
                else:
                    dt[n] = 1
        if "l" in dt:
            dt["l"] = dt["l"] / 2

        if "o" in dt:
            dt["o"] = dt["o"] / 2

        if len(dt) >= 5:
            return min(dt.values())

        return 0
