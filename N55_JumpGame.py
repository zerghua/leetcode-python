#
# Created by Hua on 9/7/2016
#

"""
 Given an array of non-negative integers, you are initially positioned
 at the first index of the array.

 Each element in the array represents your maximum jump length at that position.

 Determine if you are able to reach the last index.

 For example:
 A = [2,3,1,1,4], return true.

 A = [3,2,1,0,4], return false.
"""


# 48 ms  72 / 72 test cases passed.
# array operation. o(n), scan each item and exit early if possible.
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) <= 1: return True
        max_jump_index = 0
        last_index = len(nums) -1
        for i in range(last_index):
            if i> max_jump_index: break  #prunnig
            max_jump_index =  max(max_jump_index, i+nums[i])
            if max_jump_index >= last_index: return True
        return False


