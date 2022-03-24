#
# Create by Hua on 3/24/22.
#

"""
You are given an array items, where each items[i] = [typei, colori, namei]
describes the type, color, and name of the ith item. You are also given a rule
represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

    ruleKey == "type" and ruleValue == typei.
    ruleKey == "color" and ruleValue == colori.
    ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.



Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],
["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule,
which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],
["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are
["phone","blue","pixel"] and ["phone","gold","iphone"].
Note that the item ["computer","silver","phone"] does not match.



Constraints:
    1 <= items.length <= 104
    1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
    ruleKey is equal to either "type", "color", or "name".
    All strings consist only of lowercase letters.
"""


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int

        thought: similar to db query, find certain column with matching string.
        03/24/2022 11:37	Accepted	258 ms	21.2 MB	python
        easy 5min. db query.
        """
        ret = 0
        for i in items:
            if ruleKey == "type" and ruleValue == i[0]:
                ret += 1
            elif ruleKey == "color" and ruleValue == i[1]:
                ret += 1
            elif ruleKey == "name" and ruleValue == i[2]:
                ret += 1
        return ret

    def countMatches2(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
            simplify code
            03/24/2022 11:43	Accepted	246 ms	21.2 MB	python
        """
        ret = 0
        d = {"type":0, "color":1, "name":2}
        for i in items:
            if i[d[ruleKey]] == ruleValue:
                ret += 1
        return ret