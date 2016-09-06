#
#  Create by Hua on 9/6/2016
#


"""
 Given an array of strings, group anagrams together.

 For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
 Return:

 [
     ["ate", "eat","tea"],
     ["nat","tan"],
     ["bat"]
 ]

 Note: All inputs will be in lower-case.

"""

# 228 ms  100 / 100 test cases passed.
# sort + dictionary
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in ret:
                ret[key].append(string)
            else:
                ret[key] = [string]

        return [ret[x] for x in ret]

