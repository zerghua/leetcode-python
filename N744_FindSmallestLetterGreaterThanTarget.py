#
# Create by Hua on 5/17/22
#


"""
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.

"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str

        thought: if no letter is larger than target, then return the smallest letters[0].
        binary search
        05/17/2022 10:27	Accepted	163 ms	15.6 MB	python
        easy 10-20 min.
        """
        import bisect
        i = bisect.bisect_right(letters, target)
        if i == len(letters):
            return letters[0]
        return letters[i]

