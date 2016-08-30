#
#  Create by Hua on 8/30/2016
#


"""
 Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container, such that the container contains the most water.

 Note: You may not slant the container.

"""

# 84 ms
# two pointers and greedy.  o(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left=0; right=len(height)-1
        ret=0
        while left<right:
            minval = min(height[left], height[right])
            ret = max(ret, minval * (right-left))
            while left<right and height[left] <= minval : left +=1
            while left<right and height[right] <= minval : right -=1

        return ret