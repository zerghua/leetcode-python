#
# Create by Hua on 5/16/22
#


"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0


Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.

"""


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int

        thought: set or map to check existence
        05/16/2022 11:17	Accepted	25 ms	13.5 MB	python
        easy 1 min.
        """

        dt = set(list(jewels))
        ret = 0
        for s in stones:
            if s in dt:
                ret += 1
        return ret

