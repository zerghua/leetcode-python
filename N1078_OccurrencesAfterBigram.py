#
# Create by Hua on 4/30/22.
#

"""
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".



Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]



Constraints:

    1 <= text.length <= 1000
    text consists of lowercase English letters and spaces.
    All the words in text a separated by a single space.
    1 <= first.length, second.length <= 10
    first and second consist of lowercase English letters.


"""


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]

        thought: check every 3 words
        04/30/2022 14:00	Accepted	17 ms	13.4 MB	python
        easy 5 min.
        """
        a = text.split()
        n = len(a)
        ret = list()
        for i in range(n-2):
            if a[i] == first and a[i+1] == second:
                ret.append(a[i+2])
        return ret

